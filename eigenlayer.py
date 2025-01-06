import os
import pickle
import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import io
from googleapiclient.http import MediaIoBaseDownload
import google.generativeai as genai

# Define the scopes required for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Define folder paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

# Create directories if they don't exist
os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def authenticate_google_drive():
    creds = None
    token_path = os.path.join(CONFIG_DIR, 'token.pickle')
    credentials_path = os.path.join(CONFIG_DIR, 'credentials.json')

    # Check if the token.pickle file exists, which stores the user's access and refresh tokens
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    # If no valid credentials are available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Drive API service
    service = build('drive', 'v3', credentials=creds)
    return service

def list_files_in_folder(service, folder_id):
    # List all files in the folder
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query).execute()
    return results.get('files', [])

def download_file(service, file_id, file_name):
    # Save file in specified download directory
    file_path = os.path.join(DOWNLOAD_DIR, file_name)
    
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {file_name} {int(status.progress() * 100)}%.")
    fh.close()
    return file_path

def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def wait_for_files_active(files):
    """Waits for the given files to be active."""
    print("Waiting for file processing...")
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")
    print("...all files ready")
    print()

# Authenticate with Google Drive API
service = authenticate_google_drive()

# Folder ID extracted from the URL you provided
folder_id = '1C7dt1zGEYPXk3Baxyhu4mekuxKCy_OGU'

# List and download files from the Google Drive folder
files_in_folder = list_files_in_folder(service, folder_id)

downloaded_files = []

# Check if file already exists locally, only download new files
for file in files_in_folder:
    file_name = file['name']
    file_id = file['id']
    
    # Check if file already exists locally
    if os.path.exists(os.path.join(DOWNLOAD_DIR, file_name)):
        print(f"File {file_name} already exists, skipping download.")
    else:
        print(f"Downloading new file: {file_name}")
        download_file(service, file_id, file_name)
        downloaded_files.append(os.path.join(DOWNLOAD_DIR, file_name))

# If no new files, use previously downloaded ones
if not downloaded_files:
    downloaded_files = [os.path.join(DOWNLOAD_DIR, file['name']) for file in files_in_folder]

# Upload the files to Gemini and start the session
if downloaded_files:
    # Configure the Gemini API
    genai.configure(api_key=os.environ["API_KEY"])

    # Upload the downloaded files to Gemini
    uploaded_files = [upload_to_gemini(file, mime_type="text/plain") for file in downloaded_files]

    # Wait for the uploaded files to be processed
    wait_for_files_active(uploaded_files)

    # Initialize the model
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 512,
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-002",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    {"text": "I have uploaded several files related to restaking in EigenLayer. Can you teach me more about how restaking works in EigenLayer?"}
                ],
            },
        ]
    )

    while True:
        user_input = input("Ask a question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting chat.")
            break
        
        response = chat_session.send_message(user_input)
        print("\nGemini: ", response.text)

else:
    print("No new files to download or upload.")
