[\[Goerli Testnet] Incident Update: 
 EigenDA Blobs Not Retrieving](/status/goerli-eigenda-retrieving-outatge-feb-2024)
-----------------------------------------------------------------------------------------------------------------------

February 19, 2024 · 2 min read### Resolved \[Feb 19, 2024 \- 15:00 PT][​](#resolved-feb-19-2024---1500-pt "Direct link to Resolved [Feb 19, 2024 - 15:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues relating to EigenDA blob retrieval, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-eigenda channel.


### Monitoring \[Feb 19, 2024 \- 15:00 PT][​](#monitoring-feb-19-2024---1500-pt "Direct link to Monitoring [Feb 19, 2024 - 15:00 PT]")


* **Actions:** We identified the root cause of the issue as a race condition in the disperser that caused blobs to be encoded twice, resulting in the blob's dispersal metadata changing between one call to GetBlobStatus() and the next. We have successfully deployed [a fix](https://github.com/Layr-Labs/eigenda/pull/262) to testnet, and we are continuing to monitor the service. We don’t expect rollup operators to face any further issues relating to this, but testnet rollup operators may need to redeploy their Goerli chains with a new genesis in order to continue producing blocks.


### Investigating \[Feb 16, 2024 \- 15:00 PT][​](#investigating-feb-16-2024---1500-pt "Direct link to Investigating [Feb 16, 2024 - 15:00 PT]")


* **Incident Context:** We became aware that the Goerli EigenDA network was reporting blobs as confirmed and then later failing to retrieve these blobs. The error messages on retrieval include the string "there is no metadata for batch".
* **Impact:** Testnet rollup sequencers and nodes experience chain halts and are unable to recover without DA backup.
* **Actions:** Our team has declared this as an operational incident internally, and is initiating a thorough investigation to understand the cause of this issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[\[Goerli Testnet] Incident Update: 
 EigenDA Operator Opt\-In Churner function impacted on Goerli testnet](/status/goerli-eigenda-churner-outage-feb-2024)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

February 16, 2024 · 2 min read### Resolved \[Feb 16, 2024 \- 18:15 PT][​](#resolved-feb-16-2024---1815-pt "Direct link to Resolved [Feb 16, 2024 - 18:15 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with opting\-in into EigenDA, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Monitoring \[Feb 16, 2024 \- 15:30 PT][​](#monitoring-feb-16-2024---1530-pt "Direct link to Monitoring [Feb 16, 2024 - 15:30 PT]")


* **Actions:** We identified the root cause that resulted in this incident with the Churner service. We have successfully deployed the fixes, and are continuing to monitor the service. We don’t expect operators to face any further issues related to opting\-in of EigenDA, and can resume normal operations on Goerli testnet.
* **Additional Support:** If you (EigenLayer operators) are still encountering issues with the EigenDA opt\-in functionality, please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Investigating \[Feb 15, 2024 \- 15:00 PT][​](#investigating-feb-15-2024---1500-pt "Direct link to Investigating [Feb 15, 2024 - 15:00 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the EigenDA Churner that is not available. This incident is confined to the Goerli testnet.
* **Impact:** EigenLayer operators are unable to opt\-in to EigenDA on Goerli testnet. Request to the Churner service are failing with a 404 error response. Existing nodes are not impacted.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[\[Goerli Testnet] Incident Update: 
 Native Restaking Withdrawals Impacted on Goerli testnet](/status/goerli-native-restaking-withdrawal-outage-feb-2024)
----------------------------------------------------------------------------------------------------------------------------------------------------------

February 1, 2024 · 2 min read### Resolved \[Feb 13, 2024 \- 16:30 PT][​](#resolved-feb-13-2024---1630-pt "Direct link to Resolved [Feb 13, 2024 - 16:30 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with EigenPod withdrawals (partial or full), please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.


### Monitoring \[Feb 07, 2024 \- 16:30 PT][​](#monitoring-feb-07-2024---1630-pt "Direct link to Monitoring [Feb 07, 2024 - 16:30 PT]")


* **Actions:** We identified some scalability bottlenecks that led to this incident. We deployed fixes this week, restored normal opertation, and are continuing to monitor our service. We don’t expect users to face any further issues, and can resume normal operations of partial and full withdrawals from EigenPods on Goerli testnet.
* **Additional Support:** If you are still encountering issues with EigenPod withdrawals (partial or full), please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.


### Investigating \[Feb 01, 2024 \- 11:50 PT][​](#investigating-feb-01-2024---1150-pt "Direct link to Investigating [Feb 01, 2024 - 11:50 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to withdrawal proof generation that supports native ETH restaking functionality. This incident was confined to the testnet, with no impact on our mainnet operations.
* **Impact:** Staking users are not able to initiate EigenPod partial and full withdrawal on Goerli testnet.
* **Safety of User Assets:** While we work on a fix, we assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
[\[Goerli Testnet] Incident Update: 
 EigenPod Withdrawals Impacted due to Goerli Hard Fork](/status/goerli-hardfork-eigenpods-outage-jan-2024)
-----------------------------------------------------------------------------------------------------------------------------------------------

January 24, 2024 · 5 min read### Resolved \[Jan 26, 2024 \- 13:00 PT][​](#resolved-jan-26-2024---1300-pt "Direct link to Resolved [Jan 26, 2024 - 13:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with EigenPod withdrawals (partial or full), please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.




---


### Monitoring \[Jan 25, 2024 \- 12:00 PT][​](#monitoring-jan-25-2024---1200-pt "Direct link to Monitoring [Jan 25, 2024 - 12:00 PT]")


* **Actions:** We successfully deployed the fixes yesterday, and are continuing to monitor the results for an additional day. We don’t expect users to face any further issues, and can resume normal operations for partial and full withdrawals from EigenPods on Goerli testnet.
* **Additional Support:** If you are still encountering issues with EigenPod withdrawals (partial or full), please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Next Update:** Jan 26, 2024 \- 11:00 PT




---


### Monitoring \[Jan 24, 2024 \- 16:30 PT][​](#monitoring-jan-24-2024---1630-pt "Direct link to Monitoring [Jan 24, 2024 - 16:30 PT]")


* **Restoration of EigenPod Functionalities on Goerli:** We identified and deployed a number of changes needed to the EigenPod contracts (see [PR: Layr\-Labs/eigenlayer\-contracts/pull/395](https://github.com/Layr-Labs/eigenlayer-contracts/pull/395)), and to the proof generation implementation ([tip of this branch](https://github.com/Layr-Labs/eigenpod-proofs-generation/pull/22)). At around 13:05 PT, we verified that this successfully restored both partial and full withdrawal functionalities on the Goerli network (successful Deneb withdrawal on Deneb state \- [Etherscan transaction](https://goerli.etherscan.io/tx/0x2ffe8814abc94439e5049ab24889cf4b5542230f8cc6e57095d0b5beb462d819) (timestamp of the withdrawal at validatorIndex:668660, timestamp:1705595700, post deneb). We re\-enabled the native staking (EigenPod) functionality on the Goerli web application at 13:30 PT.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Actions:** We have successfully deployed the fixes, and are monitoring the results. We don’t expect users to face any further issues, and can resume normal operations for partial and full withdrawals from EigenPods on Goerli testnet.
* **Next Update**: Jan 25, 2024 \- 12:00 PT




---


### Identified \[Jan 19, 2024 \- 10:40 PT][​](#identified-jan-19-2024---1040-pt "Direct link to Identified [Jan 19, 2024 - 10:40 PT]")


* **Summary:** The issue was identified as being triggered by the [Goerli hard fork event](https://cryptopotato.com/ethereums-dencun-upgrade-is-live-on-goerli-testnet-but-there-is-a-catch/) on 01/17/2024 (geth release v1\.13\.9 block height 1705473120\) wherein the consensus layer upgraded from Capella to Deneb consensus client specifications.
* **Root cause:** For context, the [Deneb consensus specs](https://github.com/ethereum/consensus-specs/blob/dev/specs/deneb/beacon-chain.md#executionpayload) (subsequent to the fork) for *ExecutionPayload* container contains 17 fields compared to that for [Capella consensus specs](https://github.com/ethereum/consensus-specs/blob/dev/specs/capella/beacon-chain.md#executionpayload) (prior to the fork) which contains 15 fields. The addition of these two new fields changes the Merkle tree height from 4 to 5 as the number of fields goes over the next power of two of (2^4 \= 16 fields). We found that our implementation of the [proofgen library](https://github.com/Layr-Labs/eigenpod-proofs-generation) was not compatible with the new set of consensus layer client specifications included as part of the Deneb fork due to the **additional 2 fields.**


More specifically, the proofgen library assumed a hard\-coded Merkle tree height of 4 for the ExecutionPayload container, meaning that it expected Merkle proofs of fields within the container to be of precisely length 4\. However, the Deneb fork changed the specification in a way that modified these proofs to be of length 5, but only for epochs after the fork (i.e., proofs against old state still had to be of length 4\). It is still necessary for some proofs to be made against the state in these past epochs, which occurred prior to this change. Due to this nuance, we were unable to resolve the issue by simply changing the hard\-coded “4” to a hard\-coded “5”. Fully resolving the issue ultimately required modifying the code to be more flexible, as it was necessary for it to be capable of flexibly handling both cases.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Actions:** We disabled native ETH restaking functions on the [Goerli testnet web application](https://goerli.eigenlayer.xyz/) to avoid further inconvenience to users. We are identifying the fixes necessary to restore the system, and will share an update once those changes are ready for implementation.




---


### Investigating \[Jan 18, 2024 \- 16:25 PT][​](#investigating-jan-18-2024---1625-pt "Direct link to Investigating [Jan 18, 2024 - 16:25 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the proof generation that supports native ETH restaking functionality. This incident was confined to the testnet, with no impact on our mainnet operations.
* **Impact:** Staking users are not able to initiate EigenPod partial and full withdrawal on Goerli testnet.
* **Safety of User Assets:** While we work on a fix, we assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)


\[Goerli Testnet] Incident Update: 
 EigenDA Operator Opt\-In Churner function impacted on Goerli testnet
=========================================================================================================

February 16, 2024 · 2 min read### Resolved \[Feb 16, 2024 \- 18:15 PT][​](#resolved-feb-16-2024---1815-pt "Direct link to Resolved [Feb 16, 2024 - 18:15 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with opting\-in into EigenDA, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Monitoring \[Feb 16, 2024 \- 15:30 PT][​](#monitoring-feb-16-2024---1530-pt "Direct link to Monitoring [Feb 16, 2024 - 15:30 PT]")


* **Actions:** We identified the root cause that resulted in this incident with the Churner service. We have successfully deployed the fixes, and are continuing to monitor the service. We don’t expect operators to face any further issues related to opting\-in of EigenDA, and can resume normal operations on Goerli testnet.
* **Additional Support:** If you (EigenLayer operators) are still encountering issues with the EigenDA opt\-in functionality, please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Investigating \[Feb 15, 2024 \- 15:00 PT][​](#investigating-feb-15-2024---1500-pt "Direct link to Investigating [Feb 15, 2024 - 15:00 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the EigenDA Churner that is not available. This incident is confined to the Goerli testnet.
* **Impact:** EigenLayer operators are unable to opt\-in to EigenDA on Goerli testnet. Request to the Churner service are failing with a 404 error response. Existing nodes are not impacted.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[Newer Post\[Goerli Testnet] Incident Update: 
 EigenDA Blobs Not Retrieving](/status/goerli-eigenda-retrieving-outatge-feb-2024)[Older Post\[Goerli Testnet] Incident Update: 
 Native Restaking Withdrawals Impacted on Goerli testnet](/status/goerli-native-restaking-withdrawal-outage-feb-2024)

\[Goerli Testnet] Incident Update: 
 EigenDA Blobs Not Retrieving
=================================================================

February 19, 2024 · 2 min read### Resolved \[Feb 19, 2024 \- 15:00 PT][​](#resolved-feb-19-2024---1500-pt "Direct link to Resolved [Feb 19, 2024 - 15:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues relating to EigenDA blob retrieval, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-eigenda channel.


### Monitoring \[Feb 19, 2024 \- 15:00 PT][​](#monitoring-feb-19-2024---1500-pt "Direct link to Monitoring [Feb 19, 2024 - 15:00 PT]")


* **Actions:** We identified the root cause of the issue as a race condition in the disperser that caused blobs to be encoded twice, resulting in the blob's dispersal metadata changing between one call to GetBlobStatus() and the next. We have successfully deployed [a fix](https://github.com/Layr-Labs/eigenda/pull/262) to testnet, and we are continuing to monitor the service. We don’t expect rollup operators to face any further issues relating to this, but testnet rollup operators may need to redeploy their Goerli chains with a new genesis in order to continue producing blocks.


### Investigating \[Feb 16, 2024 \- 15:00 PT][​](#investigating-feb-16-2024---1500-pt "Direct link to Investigating [Feb 16, 2024 - 15:00 PT]")


* **Incident Context:** We became aware that the Goerli EigenDA network was reporting blobs as confirmed and then later failing to retrieve these blobs. The error messages on retrieval include the string "there is no metadata for batch".
* **Impact:** Testnet rollup sequencers and nodes experience chain halts and are unable to recover without DA backup.
* **Actions:** Our team has declared this as an operational incident internally, and is initiating a thorough investigation to understand the cause of this issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[Older Post\[Goerli Testnet] Incident Update: 
 EigenDA Operator Opt\-In Churner function impacted on Goerli testnet](/status/goerli-eigenda-churner-outage-feb-2024)

\[Goerli Testnet] Incident Update: 
 EigenPod Withdrawals Impacted due to Goerli Hard Fork
==========================================================================================

January 24, 2024 · 5 min read### Resolved \[Jan 26, 2024 \- 13:00 PT][​](#resolved-jan-26-2024---1300-pt "Direct link to Resolved [Jan 26, 2024 - 13:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with EigenPod withdrawals (partial or full), please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.




---


### Monitoring \[Jan 25, 2024 \- 12:00 PT][​](#monitoring-jan-25-2024---1200-pt "Direct link to Monitoring [Jan 25, 2024 - 12:00 PT]")


* **Actions:** We successfully deployed the fixes yesterday, and are continuing to monitor the results for an additional day. We don’t expect users to face any further issues, and can resume normal operations for partial and full withdrawals from EigenPods on Goerli testnet.
* **Additional Support:** If you are still encountering issues with EigenPod withdrawals (partial or full), please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Next Update:** Jan 26, 2024 \- 11:00 PT




---


### Monitoring \[Jan 24, 2024 \- 16:30 PT][​](#monitoring-jan-24-2024---1630-pt "Direct link to Monitoring [Jan 24, 2024 - 16:30 PT]")


* **Restoration of EigenPod Functionalities on Goerli:** We identified and deployed a number of changes needed to the EigenPod contracts (see [PR: Layr\-Labs/eigenlayer\-contracts/pull/395](https://github.com/Layr-Labs/eigenlayer-contracts/pull/395)), and to the proof generation implementation ([tip of this branch](https://github.com/Layr-Labs/eigenpod-proofs-generation/pull/22)). At around 13:05 PT, we verified that this successfully restored both partial and full withdrawal functionalities on the Goerli network (successful Deneb withdrawal on Deneb state \- [Etherscan transaction](https://goerli.etherscan.io/tx/0x2ffe8814abc94439e5049ab24889cf4b5542230f8cc6e57095d0b5beb462d819) (timestamp of the withdrawal at validatorIndex:668660, timestamp:1705595700, post deneb). We re\-enabled the native staking (EigenPod) functionality on the Goerli web application at 13:30 PT.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Actions:** We have successfully deployed the fixes, and are monitoring the results. We don’t expect users to face any further issues, and can resume normal operations for partial and full withdrawals from EigenPods on Goerli testnet.
* **Next Update**: Jan 25, 2024 \- 12:00 PT




---


### Identified \[Jan 19, 2024 \- 10:40 PT][​](#identified-jan-19-2024---1040-pt "Direct link to Identified [Jan 19, 2024 - 10:40 PT]")


* **Summary:** The issue was identified as being triggered by the [Goerli hard fork event](https://cryptopotato.com/ethereums-dencun-upgrade-is-live-on-goerli-testnet-but-there-is-a-catch/) on 01/17/2024 (geth release v1\.13\.9 block height 1705473120\) wherein the consensus layer upgraded from Capella to Deneb consensus client specifications.
* **Root cause:** For context, the [Deneb consensus specs](https://github.com/ethereum/consensus-specs/blob/dev/specs/deneb/beacon-chain.md#executionpayload) (subsequent to the fork) for *ExecutionPayload* container contains 17 fields compared to that for [Capella consensus specs](https://github.com/ethereum/consensus-specs/blob/dev/specs/capella/beacon-chain.md#executionpayload) (prior to the fork) which contains 15 fields. The addition of these two new fields changes the Merkle tree height from 4 to 5 as the number of fields goes over the next power of two of (2^4 \= 16 fields). We found that our implementation of the [proofgen library](https://github.com/Layr-Labs/eigenpod-proofs-generation) was not compatible with the new set of consensus layer client specifications included as part of the Deneb fork due to the **additional 2 fields.**


More specifically, the proofgen library assumed a hard\-coded Merkle tree height of 4 for the ExecutionPayload container, meaning that it expected Merkle proofs of fields within the container to be of precisely length 4\. However, the Deneb fork changed the specification in a way that modified these proofs to be of length 5, but only for epochs after the fork (i.e., proofs against old state still had to be of length 4\). It is still necessary for some proofs to be made against the state in these past epochs, which occurred prior to this change. Due to this nuance, we were unable to resolve the issue by simply changing the hard\-coded “4” to a hard\-coded “5”. Fully resolving the issue ultimately required modifying the code to be more flexible, as it was necessary for it to be capable of flexibly handling both cases.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Actions:** We disabled native ETH restaking functions on the [Goerli testnet web application](https://goerli.eigenlayer.xyz/) to avoid further inconvenience to users. We are identifying the fixes necessary to restore the system, and will share an update once those changes are ready for implementation.




---


### Investigating \[Jan 18, 2024 \- 16:25 PT][​](#investigating-jan-18-2024---1625-pt "Direct link to Investigating [Jan 18, 2024 - 16:25 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the proof generation that supports native ETH restaking functionality. This incident was confined to the testnet, with no impact on our mainnet operations.
* **Impact:** Staking users are not able to initiate EigenPod partial and full withdrawal on Goerli testnet.
* **Safety of User Assets:** While we work on a fix, we assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
[Newer Post\[Goerli Testnet] Incident Update: 
 Native Restaking Withdrawals Impacted on Goerli testnet](/status/goerli-native-restaking-withdrawal-outage-feb-2024)

\[Goerli Testnet] Incident Update: 
 Native Restaking Withdrawals Impacted on Goerli testnet
============================================================================================

February 1, 2024 · 2 min read### Resolved \[Feb 13, 2024 \- 16:30 PT][​](#resolved-feb-13-2024---1630-pt "Direct link to Resolved [Feb 13, 2024 - 16:30 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with EigenPod withdrawals (partial or full), please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.


### Monitoring \[Feb 07, 2024 \- 16:30 PT][​](#monitoring-feb-07-2024---1630-pt "Direct link to Monitoring [Feb 07, 2024 - 16:30 PT]")


* **Actions:** We identified some scalability bottlenecks that led to this incident. We deployed fixes this week, restored normal opertation, and are continuing to monitor our service. We don’t expect users to face any further issues, and can resume normal operations of partial and full withdrawals from EigenPods on Goerli testnet.
* **Additional Support:** If you are still encountering issues with EigenPod withdrawals (partial or full), please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.


### Investigating \[Feb 01, 2024 \- 11:50 PT][​](#investigating-feb-01-2024---1150-pt "Direct link to Investigating [Feb 01, 2024 - 11:50 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to withdrawal proof generation that supports native ETH restaking functionality. This incident was confined to the testnet, with no impact on our mainnet operations.
* **Impact:** Staking users are not able to initiate EigenPod partial and full withdrawal on Goerli testnet.
* **Safety of User Assets:** While we work on a fix, we assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
[Newer Post\[Goerli Testnet] Incident Update: 
 EigenDA Operator Opt\-In Churner function impacted on Goerli testnet](/status/goerli-eigenda-churner-outage-feb-2024)[Older Post\[Goerli Testnet] Incident Update: 
 EigenPod Withdrawals Impacted due to Goerli Hard Fork](/status/goerli-hardfork-eigenpods-outage-jan-2024)

2 posts tagged with "eigenda"
=============================

[View All Tags](/status/tags)[\[Goerli Testnet] Incident Update: 
 EigenDA Blobs Not Retrieving](/status/goerli-eigenda-retrieving-outatge-feb-2024)
-----------------------------------------------------------------------------------------------------------------------

February 19, 2024 · 2 min read### Resolved \[Feb 19, 2024 \- 15:00 PT][​](#resolved-feb-19-2024---1500-pt "Direct link to Resolved [Feb 19, 2024 - 15:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues relating to EigenDA blob retrieval, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-eigenda channel.


### Monitoring \[Feb 19, 2024 \- 15:00 PT][​](#monitoring-feb-19-2024---1500-pt "Direct link to Monitoring [Feb 19, 2024 - 15:00 PT]")


* **Actions:** We identified the root cause of the issue as a race condition in the disperser that caused blobs to be encoded twice, resulting in the blob's dispersal metadata changing between one call to GetBlobStatus() and the next. We have successfully deployed [a fix](https://github.com/Layr-Labs/eigenda/pull/262) to testnet, and we are continuing to monitor the service. We don’t expect rollup operators to face any further issues relating to this, but testnet rollup operators may need to redeploy their Goerli chains with a new genesis in order to continue producing blocks.


### Investigating \[Feb 16, 2024 \- 15:00 PT][​](#investigating-feb-16-2024---1500-pt "Direct link to Investigating [Feb 16, 2024 - 15:00 PT]")


* **Incident Context:** We became aware that the Goerli EigenDA network was reporting blobs as confirmed and then later failing to retrieve these blobs. The error messages on retrieval include the string "there is no metadata for batch".
* **Impact:** Testnet rollup sequencers and nodes experience chain halts and are unable to recover without DA backup.
* **Actions:** Our team has declared this as an operational incident internally, and is initiating a thorough investigation to understand the cause of this issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[\[Goerli Testnet] Incident Update: 
 EigenDA Operator Opt\-In Churner function impacted on Goerli testnet](/status/goerli-eigenda-churner-outage-feb-2024)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

February 16, 2024 · 2 min read### Resolved \[Feb 16, 2024 \- 18:15 PT][​](#resolved-feb-16-2024---1815-pt "Direct link to Resolved [Feb 16, 2024 - 18:15 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with opting\-in into EigenDA, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Monitoring \[Feb 16, 2024 \- 15:30 PT][​](#monitoring-feb-16-2024---1530-pt "Direct link to Monitoring [Feb 16, 2024 - 15:30 PT]")


* **Actions:** We identified the root cause that resulted in this incident with the Churner service. We have successfully deployed the fixes, and are continuing to monitor the service. We don’t expect operators to face any further issues related to opting\-in of EigenDA, and can resume normal operations on Goerli testnet.
* **Additional Support:** If you (EigenLayer operators) are still encountering issues with the EigenDA opt\-in functionality, please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Investigating \[Feb 15, 2024 \- 15:00 PT][​](#investigating-feb-15-2024---1500-pt "Direct link to Investigating [Feb 15, 2024 - 15:00 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the EigenDA Churner that is not available. This incident is confined to the Goerli testnet.
* **Impact:** EigenLayer operators are unable to opt\-in to EigenDA on Goerli testnet. Request to the Churner service are failing with a 404 error response. Existing nodes are not impacted.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)


4 posts tagged with "goerli"
============================

[View All Tags](/status/tags)[\[Goerli Testnet] Incident Update: 
 EigenDA Blobs Not Retrieving](/status/goerli-eigenda-retrieving-outatge-feb-2024)
-----------------------------------------------------------------------------------------------------------------------

February 19, 2024 · 2 min read### Resolved \[Feb 19, 2024 \- 15:00 PT][​](#resolved-feb-19-2024---1500-pt "Direct link to Resolved [Feb 19, 2024 - 15:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues relating to EigenDA blob retrieval, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-eigenda channel.


### Monitoring \[Feb 19, 2024 \- 15:00 PT][​](#monitoring-feb-19-2024---1500-pt "Direct link to Monitoring [Feb 19, 2024 - 15:00 PT]")


* **Actions:** We identified the root cause of the issue as a race condition in the disperser that caused blobs to be encoded twice, resulting in the blob's dispersal metadata changing between one call to GetBlobStatus() and the next. We have successfully deployed [a fix](https://github.com/Layr-Labs/eigenda/pull/262) to testnet, and we are continuing to monitor the service. We don’t expect rollup operators to face any further issues relating to this, but testnet rollup operators may need to redeploy their Goerli chains with a new genesis in order to continue producing blocks.


### Investigating \[Feb 16, 2024 \- 15:00 PT][​](#investigating-feb-16-2024---1500-pt "Direct link to Investigating [Feb 16, 2024 - 15:00 PT]")


* **Incident Context:** We became aware that the Goerli EigenDA network was reporting blobs as confirmed and then later failing to retrieve these blobs. The error messages on retrieval include the string "there is no metadata for batch".
* **Impact:** Testnet rollup sequencers and nodes experience chain halts and are unable to recover without DA backup.
* **Actions:** Our team has declared this as an operational incident internally, and is initiating a thorough investigation to understand the cause of this issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[\[Goerli Testnet] Incident Update: 
 EigenDA Operator Opt\-In Churner function impacted on Goerli testnet](/status/goerli-eigenda-churner-outage-feb-2024)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

February 16, 2024 · 2 min read### Resolved \[Feb 16, 2024 \- 18:15 PT][​](#resolved-feb-16-2024---1815-pt "Direct link to Resolved [Feb 16, 2024 - 18:15 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with opting\-in into EigenDA, please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Monitoring \[Feb 16, 2024 \- 15:30 PT][​](#monitoring-feb-16-2024---1530-pt "Direct link to Monitoring [Feb 16, 2024 - 15:30 PT]")


* **Actions:** We identified the root cause that resulted in this incident with the Churner service. We have successfully deployed the fixes, and are continuing to monitor the service. We don’t expect operators to face any further issues related to opting\-in of EigenDA, and can resume normal operations on Goerli testnet.
* **Additional Support:** If you (EigenLayer operators) are still encountering issues with the EigenDA opt\-in functionality, please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-operators channel.


### Investigating \[Feb 15, 2024 \- 15:00 PT][​](#investigating-feb-15-2024---1500-pt "Direct link to Investigating [Feb 15, 2024 - 15:00 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the EigenDA Churner that is not available. This incident is confined to the Goerli testnet.
* **Impact:** EigenLayer operators are unable to opt\-in to EigenDA on Goerli testnet. Request to the Churner service are failing with a 404 error response. Existing nodes are not impacted.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
* [eigenda](/status/tags/eigenda)
[\[Goerli Testnet] Incident Update: 
 Native Restaking Withdrawals Impacted on Goerli testnet](/status/goerli-native-restaking-withdrawal-outage-feb-2024)
----------------------------------------------------------------------------------------------------------------------------------------------------------

February 1, 2024 · 2 min read### Resolved \[Feb 13, 2024 \- 16:30 PT][​](#resolved-feb-13-2024---1630-pt "Direct link to Resolved [Feb 13, 2024 - 16:30 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with EigenPod withdrawals (partial or full), please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.


### Monitoring \[Feb 07, 2024 \- 16:30 PT][​](#monitoring-feb-07-2024---1630-pt "Direct link to Monitoring [Feb 07, 2024 - 16:30 PT]")


* **Actions:** We identified some scalability bottlenecks that led to this incident. We deployed fixes this week, restored normal opertation, and are continuing to monitor our service. We don’t expect users to face any further issues, and can resume normal operations of partial and full withdrawals from EigenPods on Goerli testnet.
* **Additional Support:** If you are still encountering issues with EigenPod withdrawals (partial or full), please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.


### Investigating \[Feb 01, 2024 \- 11:50 PT][​](#investigating-feb-01-2024---1150-pt "Direct link to Investigating [Feb 01, 2024 - 11:50 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to withdrawal proof generation that supports native ETH restaking functionality. This incident was confined to the testnet, with no impact on our mainnet operations.
* **Impact:** Staking users are not able to initiate EigenPod partial and full withdrawal on Goerli testnet.
* **Safety of User Assets:** While we work on a fix, we assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)
[\[Goerli Testnet] Incident Update: 
 EigenPod Withdrawals Impacted due to Goerli Hard Fork](/status/goerli-hardfork-eigenpods-outage-jan-2024)
-----------------------------------------------------------------------------------------------------------------------------------------------

January 24, 2024 · 5 min read### Resolved \[Jan 26, 2024 \- 13:00 PT][​](#resolved-jan-26-2024---1300-pt "Direct link to Resolved [Jan 26, 2024 - 13:00 PT]")


* This incident has been resolved.
* Additional Support: If you are still encountering issues with EigenPod withdrawals (partial or full), please share via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.




---


### Monitoring \[Jan 25, 2024 \- 12:00 PT][​](#monitoring-jan-25-2024---1200-pt "Direct link to Monitoring [Jan 25, 2024 - 12:00 PT]")


* **Actions:** We successfully deployed the fixes yesterday, and are continuing to monitor the results for an additional day. We don’t expect users to face any further issues, and can resume normal operations for partial and full withdrawals from EigenPods on Goerli testnet.
* **Additional Support:** If you are still encountering issues with EigenPod withdrawals (partial or full), please raise your issue via the [EigenLayer Discord](https://discord.gg/eigenlayer) \#support\-restakers channel.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Next Update:** Jan 26, 2024 \- 11:00 PT




---


### Monitoring \[Jan 24, 2024 \- 16:30 PT][​](#monitoring-jan-24-2024---1630-pt "Direct link to Monitoring [Jan 24, 2024 - 16:30 PT]")


* **Restoration of EigenPod Functionalities on Goerli:** We identified and deployed a number of changes needed to the EigenPod contracts (see [PR: Layr\-Labs/eigenlayer\-contracts/pull/395](https://github.com/Layr-Labs/eigenlayer-contracts/pull/395)), and to the proof generation implementation ([tip of this branch](https://github.com/Layr-Labs/eigenpod-proofs-generation/pull/22)). At around 13:05 PT, we verified that this successfully restored both partial and full withdrawal functionalities on the Goerli network (successful Deneb withdrawal on Deneb state \- [Etherscan transaction](https://goerli.etherscan.io/tx/0x2ffe8814abc94439e5049ab24889cf4b5542230f8cc6e57095d0b5beb462d819) (timestamp of the withdrawal at validatorIndex:668660, timestamp:1705595700, post deneb). We re\-enabled the native staking (EigenPod) functionality on the Goerli web application at 13:30 PT.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Actions:** We have successfully deployed the fixes, and are monitoring the results. We don’t expect users to face any further issues, and can resume normal operations for partial and full withdrawals from EigenPods on Goerli testnet.
* **Next Update**: Jan 25, 2024 \- 12:00 PT




---


### Identified \[Jan 19, 2024 \- 10:40 PT][​](#identified-jan-19-2024---1040-pt "Direct link to Identified [Jan 19, 2024 - 10:40 PT]")


* **Summary:** The issue was identified as being triggered by the [Goerli hard fork event](https://cryptopotato.com/ethereums-dencun-upgrade-is-live-on-goerli-testnet-but-there-is-a-catch/) on 01/17/2024 (geth release v1\.13\.9 block height 1705473120\) wherein the consensus layer upgraded from Capella to Deneb consensus client specifications.
* **Root cause:** For context, the [Deneb consensus specs](https://github.com/ethereum/consensus-specs/blob/dev/specs/deneb/beacon-chain.md#executionpayload) (subsequent to the fork) for *ExecutionPayload* container contains 17 fields compared to that for [Capella consensus specs](https://github.com/ethereum/consensus-specs/blob/dev/specs/capella/beacon-chain.md#executionpayload) (prior to the fork) which contains 15 fields. The addition of these two new fields changes the Merkle tree height from 4 to 5 as the number of fields goes over the next power of two of (2^4 \= 16 fields). We found that our implementation of the [proofgen library](https://github.com/Layr-Labs/eigenpod-proofs-generation) was not compatible with the new set of consensus layer client specifications included as part of the Deneb fork due to the **additional 2 fields.**


More specifically, the proofgen library assumed a hard\-coded Merkle tree height of 4 for the ExecutionPayload container, meaning that it expected Merkle proofs of fields within the container to be of precisely length 4\. However, the Deneb fork changed the specification in a way that modified these proofs to be of length 5, but only for epochs after the fork (i.e., proofs against old state still had to be of length 4\). It is still necessary for some proofs to be made against the state in these past epochs, which occurred prior to this change. Due to this nuance, we were unable to resolve the issue by simply changing the hard\-coded “4” to a hard\-coded “5”. Fully resolving the issue ultimately required modifying the code to be more flexible, as it was necessary for it to be capable of flexibly handling both cases.
* **Safety of User Assets:** We assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident. There has been no impact on mainnet operations.
* **Actions:** We disabled native ETH restaking functions on the [Goerli testnet web application](https://goerli.eigenlayer.xyz/) to avoid further inconvenience to users. We are identifying the fixes necessary to restore the system, and will share an update once those changes are ready for implementation.




---


### Investigating \[Jan 18, 2024 \- 16:25 PT][​](#investigating-jan-18-2024---1625-pt "Direct link to Investigating [Jan 18, 2024 - 16:25 PT]")


* **Incident Context:** We became aware of an issue on the Goerli testnet related to the proof generation that supports native ETH restaking functionality. This incident was confined to the testnet, with no impact on our mainnet operations.
* **Impact:** Staking users are not able to initiate EigenPod partial and full withdrawal on Goerli testnet.
* **Safety of User Assets:** While we work on a fix, we assure all users that all funds on Goerli and mainnet have been safe and secure throughout the incident.
* **Actions:** Our team declared this as an operational incident internally, and initiated a thorough investigation to understand the cause and impact of the issue.
**Tags:*** [goerli](/status/tags/goerli)


  
Welcome to the EigenLayer Documentation Site
============================================

[### Intro to EigenLayer

Start your journey with an overview of the protocol including key terms, features, and whitepaper.](/eigenlayer/overview)[### Guides for Restakers

Understand the different ways to restake, including with LSTs (liquid) and EigenPods (natively).](/eigenlayer/restaking-guides/restaking-user-guide/)[### Guides for Node Operators

Learn how to run an EigenLayer node and set up to operate for AVSs.](/eigenlayer/operator-guides/operator-introduction)[### Guides for AVS Developers

Learn how to design, build, and launch an AVS (Actively Validated Service).](/eigenlayer/avs-guides/avs-developer-guide)[### EigenDA Resources for Rollups and Operators

Guides for rollup developers to integrate EigenDA and for Operators to join the EigenDA network.](/eigenda/overview)[### Platform Status

Outages, Status and Resolution details.](/status)

* 
* AVS Developer Guides
* Key Management
Key Management
==============

Key Management Guidelines

[📄️ Key Security Considerations for Developers
---------------------------------------------

When working with keys for nodes in an AVS, it is essential to consider the security aspects associated with key access and decryption. Keys should be encrypted either using a password or passphrase, understanding the unique security concerns posed by different access layers is crucial. By proactively addressing these concerns, you can enhance the overall security and integrity of the keys within your system:](/eigenlayer/avs-guides/key-management/middleware-developers)[PreviousDeveloper Support](/eigenlayer/avs-guides/support)[NextKey Security Considerations for Developers](/eigenlayer/avs-guides/key-management/middleware-developers)

* 
* AVS Developer Guides
* [Node Specification](/category/node-specification)
* Metrics
Metrics
=======

Metrics and Monitoring specifications

[📄️ Prometheus Metrics Specification
-----------------------------------

The table below defines metrics which may be captured by AVS Nodes which expose metrics to Prometheus. AVSs may expose additional metrics however these should not use the eigen\_ prefix.](/eigenlayer/avs-guides/spec/metrics/metrics-prom-spec)[📄️ Implementation reference
---------------------------

This guide is intended to showcase the practical application of the Prometheus metrics using authentic examples. Examples used are:](/eigenlayer/avs-guides/spec/metrics/metrics-examples)[PreviousImplementation reference](/eigenlayer/avs-guides/spec/api/api-examples)[NextPrometheus Metrics Specification](/eigenlayer/avs-guides/spec/metrics/metrics-prom-spec)

* 
* Integration Guides
* Dispersal to DA Network
* API Documentation
* Blob Serialization Requirements
On this pageBlob Serialization Requirements
===============================


BN254 Field Element Compatibility[​](#bn254-field-element-compatibility "Direct link to BN254 Field Element Compatibility")
---------------------------------------------------------------------------------------------------------------------------


Like EIP\-4844, EigenDA identifies blobs using KZG commitments. Properly
speaking, KZG commitments commit to a polynomial whose coefficients and
evaluations live in a specific field associated with an Elliptic Curve. When
EigenDA accepts a blob of data, it has to convert this blob into a polynomial
living on this field. This must be done in a careful manner in order to avoid
restricting possible use cases for clients building
on EigenDA.


EigenDA will convert each 32 bytes of the incoming blob into a field element
(like EIP\-4844\), which is in turn interpreted as a coefficient of the blob
polynomial (Unlike EIP\-4844\). Since a field element cannot store a full 32
bytes, each 32 byte array must be validated by finding the BigEndian integer
associated with the array and checking whether it is within the field modulus.



```
BLS_MODULUS = 21888242871839275222246405745257275088548364400416034343698204186575808495617  
  
def bytes_to_bls_field(b: Bytes32) -> BLSFieldElement:  
    """  
    Convert untrusted bytes to a trusted and validated BLS scalar field element.  
    This function does not accept inputs greater than the BLS modulus.  
    """  
    field_element = int.from_bytes(b, ENDIANNESS)  
    assert field_element < BLS_MODULUS  
    return BLSFieldElement(field_element)  

```

This validation means that an arbitrary string of bytes sent to EigenDA will
likely be rejected; instead of sending their raw bytes to EigenDA, users should
precondition the data in one of a few different ways to ensure that each 32 byte
chunk can be properly converted to a field element.


An obvious question that may arise is why EigenDA does not perform this
conversion for users; unfortunately, because Elliptic Curve field elements
cannot be represented by an integer number of bits, there is no generic lossless
conversion which does not require some validation; Moreover, hard\-coding a lossy
conversion means that not all polynomials can be represented in EigenDA, which
in turn restricts certain use cases.


### Using kzgpad[​](#using-kzgpad "Direct link to Using kzgpad")


If you do not adhere to this encoding scheme, you may encounter errors like these:



```
$ grpcurl \  
    -import-path ./api/proto \  
    -proto ./api/proto/disperser/disperser.proto \  
    -d '{"data": "hello"}' \  
    disperser-preprod-holesky.eigenda.xyz:443 disperser.Disperser/DisperseBlob  
  
ERROR:  
  Code: InvalidArgument  
  Message: rpc error: code = InvalidArgument desc = encountered an error to convert a 32-bytes into a valid field element, please use the correct format where every 32bytes(big-endian) is less than 21888242871839275222246405745257275088548364400416034343698204186575808495617  

```

The simplest way to resovlve this until we have a dedicated EigenDA CLI is to
use the `kzgpad` utility documented in the [tutorial](/eigenda/integrations-guides/dispersal/quick-start):



```
$ grpcurl \  
  -proto ./api/proto/disperser/disperser.proto \  
  -import-path ./api/proto \  
  -d '{"data": "'$(tools/kzgpad/bin/kzgpad -e hello)'"}' \  
  disperser-holesky.eigenda.xyz:443 disperser.Disperser/DisperseBlob  
  
{  
  "result": "PROCESSING",  
  "requestId": "OGEyYTVjOWI3Njg4MjdkZTVhOTU1MmMzOGEwNDRjNjY5NTljNjhmNmQyZjIxYjUyNjBhZjU0ZDJmODdkYjgyNy0zMTM3MzEzMjM2MzAzODM4MzYzOTMzMzgzMzMxMzYzMzM0MzYzNzJmMzAyZjMzMzMyZjMxMmYzMzMzMmZlM2IwYzQ0Mjk4ZmMxYzE0OWFmYmY0Yzg5OTZmYjkyNDI3YWU0MWU0NjQ5YjkzNGNhNDk1OTkxYjc4NTJiODU1"  
}  

```

Pad One Byte Codec ("kzgpad")[​](#pad-one-byte-codec-kzgpad "Direct link to Pad One Byte Codec (\"kzgpad\")")
-------------------------------------------------------------------------------------------------------------


One example golang encoding scheme for implementing the above validity rule is [copied from the EigenDA codesbase](https://github.com/Layr-Labs/eigenda/blob/master/encoding/utils/codec/codec.go#L12) below.



```
// ConvertByPaddingEmptyByte takes bytes and insert an empty byte at the front of every 31 byte.  
// The empty byte is padded at the low address, because we use big endian to interpret a fiedl element.  
// This ensure every 32 bytes are within the valid range of a field element for bn254 curve.  
// If the input data is not a multiple of 31, the reminder is added to the output by  
// inserting a 0 and the reminder. The output does not necessarily be a multipler of 32  
func ConvertByPaddingEmptyByte(data []byte) []byte {  
 dataSize := len(data)  
 parseSize := encoding.BYTES_PER_SYMBOL - 1  
 putSize := encoding.BYTES_PER_SYMBOL  
  
 dataLen := (dataSize + parseSize - 1) / parseSize  
  
 validData := make([]byte, dataLen*putSize)  
 validEnd := len(validData)  
  
 for i := 0; i < dataLen; i++ {  
  start := i * parseSize  
  end := (i + 1) * parseSize  
  if end > len(data) {  
   end = len(data)  
   // 1 is the empty byte  
   validEnd = end - start + 1 + i*putSize  
  }  
  
  // with big endian, set first byte is always 0 to ensure data is within valid range of  
  validData[i*encoding.BYTES_PER_SYMBOL] = 0x00  
  copy(validData[i*encoding.BYTES_PER_SYMBOL+1:(i+1)*encoding.BYTES_PER_SYMBOL], data[start:end])  
  
 }  
 return validData[:validEnd]  
}  
  
// RemoveEmptyByteFromPaddedBytes takes bytes and remove the first byte from every 32 bytes.  
// This reverses the change made by the function ConvertByPaddingEmptyByte.  
// The function does not assume the input is a multiple of BYTES_PER_SYMBOL(32 bytes).  
// For the reminder of the input, the first byte is taken out, and the rest is appended to  
// the output.  
func RemoveEmptyByteFromPaddedBytes(data []byte) []byte {  
 dataSize := len(data)  
 parseSize := encoding.BYTES_PER_SYMBOL  
 dataLen := (dataSize + parseSize - 1) / parseSize  
  
 putSize := encoding.BYTES_PER_SYMBOL - 1  
  
 validData := make([]byte, dataLen*putSize)  
 validLen := len(validData)  
  
 for i := 0; i < dataLen; i++ {  
  // add 1 to leave the first empty byte untouched  
  start := i*parseSize + 1  
  end := (i + 1) * parseSize  
  
  if end > len(data) {  
   end = len(data)  
   validLen = end - start + i*putSize  
  }  
  
  copy(validData[i*putSize:(i+1)*putSize], data[start:end])  
 }  
 return validData[:validLen]  
}  

```
[PreviousDispersal Rate Limits](/eigenda/integrations-guides/dispersal/api-documentation/metering-and-rate-limits)[NextAPI Error Codes](/eigenda/integrations-guides/dispersal/api-documentation/error-codes)* [BN254 Field Element Compatibility](#bn254-field-element-compatibility)
	+ [Using kzgpad](#using-kzgpad)
* [Pad One Byte Codec ("kzgpad")](#pad-one-byte-codec-kzgpad)


* 
* Integration Guides
* Dispersal to DA Network
* API Documentation
* API Error Codes
On this pageEigenDA API Error Codes
=======================


There are three categories of response status codes that the EigenDA GRPC API
may return to a requesting client:


1. Success
2. Client Error
3. Server Error


The *Client Error* category breaks down into 3 subcategories:


1. Invalid Request
2. Rate Limited
3. Not Found


This table summarizes all the current status codes and their mappings to HTTP codes.




| Status | gRPC Error Code | HTTP Error Code | Use cases |
| --- | --- | --- | --- |
| OK | `OK` | `200` OK | Applicable to all |
| Invalid Request | `InvalidArgument` | `400` Bad Request | Applicable to all |
| Too Many Requests | `ResourceExhausted` | `429` Too Many Requests | For Disperser and Churner rate limiting |
| Not Found | `NotFound` | `404` Not Found | For GetBlobStatus and RetrieveBlob |
| Internal Error | `Internal` | `500` Internal Server Error | Applicable to all |


API endpoints error reference[​](#api-endpoints-error-reference "Direct link to API endpoints error reference")
---------------------------------------------------------------------------------------------------------------


#### Disperser.DisperseBlobAuthenticated() and Disperser.DisperseBlob()[​](#disperserdisperseblobauthenticated-and-disperserdisperseblob "Direct link to Disperser.DisperseBlobAuthenticated() and Disperser.DisperseBlob()")




| Error String | Status Code | Description |
| --- | --- | --- |
| "error receiving next message: %v" | InvalidArgument (400\) | This error occurs when there is an issue receiving the next message from the gRPC stream. |
| "missing DisperseBlobRequest" | InvalidArgument (400\) | This error occurs when the `DisperseRequest` field is missing from the `AuthenticatedRequest` message. |
| "failed to decode public key (%v): %v" | InvalidArgument (400\) | This error occurs when there is an issue decoding the public key from the `AccountID` field of the `BlobAuthHeader`. |
| "context deadline exceeded" | InvalidArgument (400\) | This error occurs when the context deadline is exceeded while waiting for the next message from the gRPC stream. |
| "expected AuthenticationData" | InvalidArgument (400\) | This error occurs when the `AuthenticationData` field is missing from the `AuthenticatedRequest` message. |
| "failed to authenticate blob request: %v" | InvalidArgument (400\) | This error occurs when there is an issue authenticating the blob request using the provided authentication data. |
| "blob size cannot exceed 2 MiB" | InvalidArgument (400\) | This error occurs when the size of the blob data exceeds the maximum allowed size of 2 MiB. |
| "blob size must be greater than 0" | InvalidArgument (400\) | This error occurs when the size of the blob data is zero. |
| "number of custom\_quorum\_numbers must not exceed 256" | InvalidArgument (400\) | This error occurs when the number of custom quorum numbers provided in the request exceeds 256\. |
| "number of custom\_quorum\_numbers must not exceed number of quorums" | InvalidArgument (400\) | This error occurs when the number of custom quorum numbers provided in the request exceeds the total number of quorums. |
| "custom\_quorum\_numbers must be in range \[0, 254], but found %d" | InvalidArgument (400\) | This error occurs when a custom quorum number is outside the valid range of \[0, 254]. |
| "custom\_quorum\_numbers must be in range \[0, \<quorum count\>], but found %d" | InvalidArgument (400\) | This error occurs when a custom quorum number is outside the valid range of \[0, QuorumCount\-1]. |
| "custom\_quorum\_numbers must not contain duplicates" | InvalidArgument (400\) | This error occurs when the custom quorum numbers contain duplicate values. |
| "custom\_quorum\_numbers should not include the required quorums %v, but required quorum %d was found" | InvalidArgument (400\) | This error occurs when a custom quorum number includes a required quorum number. |
| "the blob must be sent to at least one quorum" | InvalidArgument (400\) | This error occurs when no quorums are specified for the blob dispersal. |
| "invalid request: %w" | InvalidArgument (400\) | This error occurs when the request contains invalid parameters, such as invalid security parameters. |
| "encountered an error to convert a 32\-bytes into a valid field element, please use the correct format where every 32bytes(big\-endian) is less than 21888242871839275222246405745257275088548364400416034343698204186575808495617" | InvalidArgument (400\) | This error occurs when the blob has not been encoded correctly. See [blob encoding](/eigenda/integrations-guides/dispersal/api-documentation/blob-serialization-requirements). |
| "request ratelimited: \<rate type\> for quorum %d" | ResourceExhausted (429\) | This error occurs when the request is rate limited for the specified quorum based on the configured rate limits. |


#### Disperser.GetBlobStatus()[​](#dispersergetblobstatus "Direct link to Disperser.GetBlobStatus()")




| Error String | Status Code | Description |
| --- | --- | --- |
| "request\_id must not be empty" | InvalidArgument (400\) | This error occurs when the `request_id` field is empty in the `BlobStatusRequest` message. |
| "failed to parse the requestID: %s" | InvalidArgument (400\) | This error occurs when there is an issue parsing the `request_id` field into a valid `BlobKey`. |
| "failed to get blob metadata, blobkey: %s" | Internal (500\) | This error occurs when there is an issue retrieving the blob metadata for the specified `BlobKey`. |
| "missing confirmation information: %s" | Internal (500\) | This error occurs when the confirmation information is missing from the blob metadata. |


#### Disperser.RetrieveBlob()[​](#disperserretrieveblob "Direct link to Disperser.RetrieveBlob()")




| Error String | Status Code | Description |
| --- | --- | --- |
| "ratelimiter error: %v" | Internal (500\) | This error occurs when there is an issue with the rate limiter, such as an internal error. |
| "request ratelimited" | ResourceExhausted (429\) | This error occurs when the request is rate limited based on the configured rate limits. |
| "Failed to retrieve blob metadata" | Internal (500\) | This error occurs when there is an issue retrieving the blob metadata for the specified batch header hash and blob index. |
| "failed to get blob data, please retry" | Internal (500\) | This error occurs when there is an issue retrieving the blob data from the blob store. |


#### Churner.Churn()[​](#churnerchurn "Direct link to Churner.Churn()")




| Error String | Status Code | Description |
| --- | --- | --- |
| "invalid request: %s" | InvalidArgument (400\) | This error occurs when the churn request is invalid due to various reasons such as invalid signature length, invalid pubkey lengths, or invalid salt length. |
| "previous approval not expired, retry in %d" | ResourceExhausted (429\) | This error occurs when the previous churn approval has not expired yet and the retry time is provided. |
| "failed to verify request signature: %s" | InvalidArgument (400\) | This error occurs when the request signature verification fails. |
| "rate limiter error: %s" | ResourceExhausted (429\) | This error occurs when the rate limit for the operator is exceeded. |
| "invalid signature length" | InvalidArgument (400\) | This error occurs when the signature length in the request is invalid. |
| "invalid operatorToRegisterPubkeyG1 length" | InvalidArgument (400\) | This error occurs when the operatorToRegisterPubkeyG1 length in the request is invalid. |
| "invalid operatorToRegisterPubkeyG2 length" | InvalidArgument (400\) | This error occurs when the operatorToRegisterPubkeyG2 length in the request is invalid. |
| "invalid salt length" | InvalidArgument (400\) | This error occurs when the salt length in the request is invalid. |
| "invalid quorumIds length %d" | InvalidArgument (400\) | This error occurs when the quorumIds length in the request is invalid. |
| "invalid request: security\_params must not contain duplicate quorum\_id" | InvalidArgument (400\) | This error occurs when the quorumIds in the request contain duplicate values. |
| "invalid request: the quorum\_id must be in range \[0, %d], but found %d" | InvalidArgument (400\) | This error occurs when the quorumId in the request is outside the valid range. |
| "operatorToRegisterPubkeyG1 and operatorToRegisterPubkeyG2 are not equivalent" | InvalidArgument (400\) | This error occurs when the operatorToRegisterPubkeyG1 and operatorToRegisterPubkeyG2 are not equivalent during signature verification. |
| "operatorRequestSignature is invalid" | InvalidArgument (400\) | This error occurs when the operatorRequestSignature is invalid during signature verification. |
| "operator is already registered in quorum" | InvalidArgument (400\) | This error occurs when the operator is already registered in the specified quorum. |
| "registering operator must have %f%% more than the stake of the lowest\-stake operator. Block number used for this decision: %d, registering operator address: %s, registering operator stake: %d, stake of lowest\-stake operator: %d, operatorId of lowest\-stake operator: %x, quorum ID: %d" | InvalidArgument (400\) | This error occurs when the registering operator does not have sufficient stake compared to the lowest\-stake operator to churn it out. |
| "operator to churn out must have less than %f%% of the total stake. Block number used for this decision: %d, operatorId of the operator to churn: %x, stake of the operator to churn: %d, total stake in quorum: %d, quorum ID: %d" | InvalidArgument (400\) | This error occurs when the operator to be churned out has more than the allowed percentage of the total stake in the quorum. |
| "operatorID Rate Limit Exceeded: %d" | ResourceExhausted (429\) | This error occurs when the rate limit for a specific operatorID is exceeded. |

[PreviousBlob Serialization Requirements](/eigenda/integrations-guides/dispersal/api-documentation/blob-serialization-requirements)[NextGolang Client](/eigenda/integrations-guides/dispersal/clients/golang-client)* [API endpoints error reference](#api-endpoints-error-reference)


* 
* Integration Guides
* Dispersal to DA Network
* API Documentation
* Dispersal Rate Limits
On this pageDispersal Rate Limits
=====================


Encoded Blob Size[​](#encoded-blob-size "Direct link to Encoded Blob Size")
---------------------------------------------------------------------------


When a blob is dispersed to EigenDA, its encoded size is used to charge against any rate limits or other metering systems. The encoded blob size can be approximately derived from two security parameters, the Confirmation Threshold and Adversary Threshold, via the following equation


(Encoded Blob Size)\=(Blob Size)/(Confirmation Threshold−Adversary Threshold))(\\text{Encoded Blob Size}) \= (\\text{Blob Size}) / (\\text{Confirmation Threshold} \- \\text{Adversary Threshold}))(Encoded Blob Size)\=(Blob Size)/(Confirmation Threshold−Adversary Threshold))
1. **Confirmation Threshold** is the minimum percentage of stake that must attest in
order to consider the blob dispersal successful. As such, this
setting affects liveness tolerance. For example, a lower confirmation
threshold means that a smaller set of operators are required to meet a dispersal
request, whereas a high quorum threshold requires more operators to be available
to provide liveness.
2. **Adversary Threshold** is the maximum percentage of the stake which can be
held by adversarial nodes before the availability of a blob is affected.


Rate Limits[​](#rate-limits "Direct link to Rate Limits")
---------------------------------------------------------


Currently, the EigenDA disperser enforces two types of rate limits:


* Data rate limit: Limits the total amount of data posted within a fixed (e.g. 10 minute) interval.
* Blob rate limit: Limits the total number of blobs posted within a 10 minute interval.


If a client exceeds either of these rate limits, they will receive a rate limit error and the request will not be processed. Rate limits are determined by [network defaults](/eigenda/networks/) or by reservation payments.

[PreviousOverview](/eigenda/integrations-guides/dispersal/api-documentation/overview)[NextBlob Serialization Requirements](/eigenda/integrations-guides/dispersal/api-documentation/blob-serialization-requirements)* [Encoded Blob Size](#encoded-blob-size)
* [Rate Limits](#rate-limits)


* 
* Integration Guides
* Dispersal to DA Network
* API Documentation
* Overview
On this pageOverview
========


The EigenDA disperser provides an API for dispersing and retrieving blobs to and from the EigenDA network in an untrusted fashion. (Note: as part of its essential data availability guarantee, the EigenDA network already supports direct communication with the EigenDA network for blob retrieval; permissionless dispersal of blobs to the EigenDA network is planned as a future protocol upgrade).


The source of truth for the Disperser API spec is [disperser.proto](https://github.com/Layr-Labs/eigenda/blob/8ec570b8c2b266fad20ea0af14f0f5d84906c39c/api/proto/disperser/disperser.proto), adjusted to the current release. The goal of this document is to explain this spec at a higher level.


Eigen Labs hosts one disperser endpoint for each EigenDA network. These endpoints are documented in respective network pages [indexed here](/eigenda/networks/).


The EigenDA Disperser exposes 4 endpoints:


1. `DisperseBlob()`
2. `DisperseBlobAuthenticated()`
3. `GetBlobStatus()`
4. `RetrieveBlob()`


These endpoints enable the blob lifecycle, from enqueuing blobs for dispersal to waiting for their dispersal finalization and finally to retrieving blobs from the EigenDA network. The following flowchart describes how move blobs through this lifecycle with respect to these endpoints:



The Disperser offers an asynchrounous API for dispersing blobs, where clients should poll the `GetBlobStatus()` endpoint with the dispersal request ID they received from calling one of the two disperse endpoints until the disperser reports the blob as successfully dispersed and finalized.


Endpoints[​](#endpoints "Direct link to Endpoints")
---------------------------------------------------


Here we provide a narrative\-level description of the major API endpoints. Please see [the repo](https://github.com/Layr-Labs/eigenda/tree/master/api/docs) for detailed, field\-level API documentation.


### DisperseBlob()[​](#disperseblob "Direct link to DisperseBlob()")


infoThis endpoint will be deprecated in future releases. All production traffic should prefer the `DisperseBlobAuthenticated` endpoint.


The `DisperseBlob()` is a simple unauthenticated endpoint which allows users to send test traffic to the EigenDA testnet and mainnet networks. Requests to the `DisperseBlob()` endpoint are rate limited based on IP address.


infoCurrently, all users can permissionlessly utilize the `DisperseBlob` endpoint on [testnet](/eigenda/networks/holesky) at free\-tier throughput levels. Mainnet users can request IP\-whitelisting via the [EigenDA Client Registration Form](https://forms.gle/3QRNTYhSMacVFNcU8), but should prefer the authenticated endpoint described in the next section.


The `DisperseBlob()` endpoint accepts a [DisperseBlobRequest](https://github.com/Layr-Labs/eigenda/blob/master/api/proto/disperser/disperser.proto#L72) and returns a [DisperseBlobReply](https://github.com/Layr-Labs/eigenda/blob/master/api/proto/disperser/disperser.proto#L92), as described below:


#### DisperseBlobRequest[​](#disperseblobrequest "Direct link to DisperseBlobRequest")




| Field Name | Type | Description |
| --- | --- | --- |
| `data` | \[]byte | The data to be dispersed. **The blob dispersed must conform to the [Blob Serialization Requirements](/eigenda/integrations-guides/dispersal/api-documentation/blob-serialization-requirements) which ensure that the blob's KZG commitment may be representative of the original data that was sent to the disperser.** |
| `custom_quorum_numbers` | \[]uint32 | The quorums to which the blob will be sent, in addition to the required quorums which are configured on the EigenDA smart contract. If required quorums are included here, an error will be returned. The disperser will ensure that the encoded blobs for each quorum are all processed within the same batch. |
| `account_id` | string | This field can be omitted when using the `DisperseBlob` endpoint. When using the `DisperseBlobAuthenticated` endpoint, `account_id` is a hex\-encoded string of the ECSDA public key corresponding to the key used by the client to sign the `BlobAuthHeader`. |


#### DisperseBlobReply[​](#disperseblobreply "Direct link to DisperseBlobReply")




| Field Name | Type | Description |
| --- | --- | --- |
| `result` | BlobStatus | The status of the blob associated with the request\_id. This field is returned in case the blob dispersal queuing fails immediately. If the blob was successfully dispersed, this field will be set to `PROCESSING` (`1`). |
| `request_id` | \[]byte | The request ID generated by the disperser corresponding to the dispersal. Once a request is accepted (although not processed), a unique request ID will be generated. Two different DisperseBlobRequests (determined by the hash of the DisperseBlobRequest) will have different IDs, and the same DisperseBlobRequest sent repeatedly at different times will also have different IDs. The client should use this ID to query the processing status of the request (via the `GetBlobStatus()` API). |


### DisperseBlobAuthenticated()[​](#disperseblobauthenticated "Direct link to DisperseBlobAuthenticated()")


`DisperseBlobAuthenticated()` provides a flow for authenticated dispersal to EigenDA networks. Ultimately, the purpose of authentication is to allow DA nodes to identify the source of a given blob request and map this to a payment source. Thus, the `DisperseBlobAuthenticated()` will ultimately serve as a convenient way for a client to provide an authorization which can be passed along to the DA nodes, without making any trust assumptions on the disperser as a service provider. The interface is expected to undergo an upgrade in order to support this use case over the next several months.


Clients authenticate a request to the disperser by providing an ECDSA signature of a `BlobAuthHeader` which can be passed to the DA nodes. This header should contain the KZG commitment of the blob itself, which may be inconvenient for a client to calculate given that it requres the storage of a large SRS file. The `DisperseBlobAuthenticated()` uses an interactive flow whereby the client can first send the blob, and then receive the KZG commitment back from the disperser, verify it, and send back the authenticating signature. The current interface implements this overall flow, but using a simple random challenge mechanism in the place of the KZG commitment, for the reason that the `BlobAuthHeader` will only be sent to the DA nodes once payments are released.


warningIn order to minimize security risks, we recommend that clients utilize a keypair for authentication not associated with any Ethereum founds.


infoClients looking to send authenticated traffic to EigenDA mainnet or testnet should reach out via the [EigenDA Client Registration Form](https://forms.gle/3QRNTYhSMacVFNcU8) so we can get in touch.


The following is a detailed description of the behavior of the `DisperseBlobAuthenticated()` endpoint. To quickly get started using this endpoint, you can use the golang client described in the quick start guide.



```
service Disperser {  
 rpc DisperseBlobAuthenticated(stream AuthenticatedRequest) returns (stream AuthenticatedReply);  
    ...  
}  
  
message AuthenticatedRequest {  
    oneof payload {  
        DisperseBlobRequest disperse_request = 1;  
        AuthenticationData authentication_data = 2;  
    }  
}  
  
message AuthenticatedReply {  
    oneof payload {  
        BlobAuthHeader blob_auth_header = 1;  
        DisperseBlobReply disperse_reply = 2;  
    }  
}  
  

```

1. The client opens a connection to `DisperseBlobAuthenticated()` endpoint, sending a `DisperseBlobRequest` message with the Ethereum address they wish to authenticate with as account\_id:



```
message DisperseBlobRequest {  
    bytes data = 1;  
    repeated uint32 custom_quorum_numbers = 2;  
  
    // The account ID of the client. This should be a hex-encoded string of the ECSDA public key  
    // corresponding to the key used by the client to sign the BlobAuthHeader.  
    string account_id = 3;  
}  

```

2. The server validates this request, sending back a challenge string in the form of a `BlobAuthHeader`:



```
message BlobAuthHeader {  
    uint32 challenge_parameter = 1;  
}  

```

3. The client ECDSA signs the challenge parameter bytes with the private key associated with the Ethereum address they sent in step 1, returning this to the server in an `AuthenticationData` message:



```
message AuthenticationData {  
    bytes authentication_data = 1;  
}  

```

4. The server validates the returned challenge. If the signature of the challenge verifies against the public key of the Ethereum address that was specified in step 1, then the request is granted, and the blob is dispersed. The server returns a `DisperseBlobReply` conforming to the following schema:



```
message DisperseBlobReply {  
    BlobStatus result = 1;  
    bytes request_id = 2;  
}  

```

### GetBlobStatus()[​](#getblobstatus "Direct link to GetBlobStatus()")


This endpoint returns the dispersal status and metadata associated with a given blob request ID, and is meant to be polled until the blob is reported as finalized and a DA certificate is returned.


#### BlobStatusRequest[​](#blobstatusrequest "Direct link to BlobStatusRequest")




| Field Name | Type | Description |
| --- | --- | --- |
| `request_id` | \[]byte | The ID of the blob that is being queried for its status. |


#### BlobStatusReply[​](#blobstatusreply "Direct link to BlobStatusReply")




| Field Name | Type | Description |
| --- | --- | --- |
| `status` | [BlobStatus](https://github.com/Layr-Labs/eigenda/blob/master/api/proto/disperser/disperser.proto#L142) | The dispersal status of the blob |
| `info` | BlobInfo | The blob info needed for clients to confirm the blob against the EigenDA contracts |


Since the BlobInfo type has many nested sub\-structs, it's easier to describe its schema by annotating an example:



```
{  
  "status":  "CONFIRMED", // means that the blob's batch metadata has been registered in the EigenDA manager contract, but the block in which it was registered has not yet finalized.  
  "info":  {  
    "blobHeader":  {  
      "commitment":  { // KZG commitment associated with the data that was dispersed  
        "x":  "EBXIwkZ7nXChaRx2Nz+SZyU/rX3WvZnLGeKpCW32OWs=", // BN254 X point  
        "y":  "LoTp8Bqz7pyhptnRBT5o01GAbPGXB52Ll+X+Pw+ibeg="  // BN254 Y point  
      },  
      "dataLength":  1,  
      "blobQuorumParams":  [  
        {  
          "adversaryThresholdPercentage":  33,  
          "confirmationThresholdPercentage":  55,  
          "chunkLength":  1  
        },  
        {  
          "quorumNumber":  1,  
          "adversaryThresholdPercentage":  33,  
          "confirmationThresholdPercentage":  55,  
          "chunkLength":  1  
        }  
      ]  
    },  
    "blobVerificationProof":  {  
      "batchId":  15219, // batchId and batchHeaderHash are the minimum fields necessary for later retrieving a blob.  
      "blobIndex":  687,  
      "batchMetadata":  {  
        "batchHeader":  {  
          "batchRoot":  "+yFLC9HFHJxkBixjGdFGv0psPC6R0DNynhowYgUvjtE=",  
          "quorumNumbers":  "AAE=",  
          "quorumSignedPercentages":  "VU4=",  
          "referenceBlockNumber":  1564355  
        },  
        "signatoryRecordHash":  "HG1kkSIGjTOX2kFexdGnuAj7zDJaat0XQQavHjjXdPs=",  
        "fee":  "AA==",  
        "confirmationBlockNumber":  1564476, // ethereum block number when the blob's dispersal metadata was registered  
        "batchHeaderHash":  "d1KhHvr0lhNCYiizYS5+v/2QWvSTsm7MeACChYDRli0=" // batchHeaderHash and batchId are the minimum fields necessary for later retrieving a blob.  
      },  
      "inclusionProof":  "3DDZAQV1jdb4Eb3pLAAVqAq69EMrmGMfwfcW9jQwShN8O4oqv7041DVjM09LARNO4VX1WUoVrSdXQ5ZXpaKKL7iREgnhNrHydYXfmJuGiS7dtxQubTDQ2O5bYTckzt/LZakvNf5hz87vEQdvHcYh2wpBugaX6/kgY/8OGiHLwocIXXwC5upaU92WSxFkHmd31xq7nAwDM5N8s7R9ktWBTbBGVFTtmTcctapohz551bskMoV79w28ie4Tc6NcdS5S9z1hR6tW9IGoHqeifynPjdvRaq51T/jnJWSC6gixbO6DOcw2qIU0+jhZsu6/ucHIwzxBQtvmp+7dLBthC7dZYllIOsc2nyTmUfp2mKXjP5vPEhbX+FLIMwagi3lGOI9zUdG/RYIpKxEIVoO5ffStDMotX4ZCgGZyQiTYR0maags/yc/ID27M8YVyu54nAAAyG89TpmqvVofJ1ove863ufA==", // this field proves that the blob was included within the batch specified by the batchHeaderHash.  
      "quorumIndexes":  "AAE="  
    }  
  }  
}  

```

### RetrieveBlob()[​](#retrieveblob "Direct link to RetrieveBlob()")


The `RetrieveBlob()` endpoint enables clients to retrieve an individual blob using a `(batch_header_hash, blob_index)` pair, originally derived from inside a `BlobInfo` object returned by `GetBlobStatus()`. Retrieving blobs via the Retrieve endpoint on the disperser is more efficient than directly retrieving from the DA Nodes (see detail about this approach in [retriever.proto](https://github.com/Layr-Labs/eigenda/blob/master/api/proto/retriever/retriever.proto). The blob should have been initially dispersed via this Disperser service for this API to work.

[PreviousQuick Start](/eigenda/integrations-guides/dispersal/quick-start)[NextDispersal Rate Limits](/eigenda/integrations-guides/dispersal/api-documentation/metering-and-rate-limits)* [Endpoints](#endpoints)
	+ [DisperseBlob()](#disperseblob)
	+ [DisperseBlobAuthenticated()](#disperseblobauthenticated)
	+ [GetBlobStatus()](#getblobstatus)
	+ [RetrieveBlob()](#retrieveblob)


* 
* Integration Guides
* Dispersal to DA Network
* Clients
* EigenDA Proxy
On this pageEigenDA Proxy
=============


The [EigenDA Proxy](https://github.com/Layr-Labs/eigenda-proxy) wraps the [high\-level EigenDA client](https://github.com/Layr-Labs/eigenda/blob/master/api/clients/eigenda_client.go) with an HTTP server, and performs additional verification tasks when reading and writing blobs that eliminate any trust assumption on the EigenDA disperser service. Instructions for building and running the EigenDA Proxy can be found [here](https://github.com/Layr-Labs/eigenda-proxy/blob/main/README.md).


### Security Features[​](#security-features "Direct link to Security Features")


When writing to EigenDA, the proxy verifies that the BN254 KZG commitment of the data matches the commitment that the EigenDA Disperser dispersed, ensuring that the Disperser hasn't tampered with the data during dispersal. The proxy also verifies the DA certificate returned by the disperser upon successful dispersal. It does this by checking that the batch was successfully dispersed, i.e. that the aggregated batch signature was written to the EigenDAServiceManager contract on Ethereum, that the signature was valid, and that the blob appears within the batch merkle tree.


When reading from EigenDA, the proxy does something similar. After retrieving a blob from the disperser, it recomputes the blob's KZG commitment and verifies that it matches the expected commitment in the DA certificate. This ensures that the sequencer could never read incorrect data from EigenDA, and avoids a trust assumption on the EigenDA disperser.

[PreviousGolang Client](/eigenda/integrations-guides/dispersal/clients/golang-client)[NextRollup Guides](/eigenda/integrations-guides/rollup-guides/)* [Security Features](#security-features)


* 
* Integration Guides
* Dispersal to DA Network
* Clients
* Golang Client
Using the Golang Client for Authenticated Dispersal
===================================================


EigenDA offers a low\-level golang client which wraps the bottom\-level GRPC client with ECDSA keypair authentication logic. That client is available in the EigenDA repo in [disperser\_client.go](https://github.com/Layr-Labs/eigenda/tree/5ff66ae6a15d77956a878fe4d2d02751444c9fa9/disperser). This is a tutorial for getting started using this client.


Dependencies:


* Golang must be installed on your machine. You can install [golang here](https://go.dev/doc/install).


First let's start by setting up a project directory:



```
mkdir ~/Workspace/eigenda-dispersal-program  
cd ~/Workspace/eigenda-dispsersal-program  

```

Next let's define our project. Take some time to read through main.go, understanding each line and its corresponding comment.



```
# go.mod  
module github.com/foobar/low-level-disperser-client-example  
  
go 1.21.1  
  
require (  
 github.com/Layr-Labs/eigenda v0.7.1  
 github.com/Layr-Labs/eigenda/api v0.7.1  
 google.golang.org/protobuf v1.33.0  
)  

```


```
# main.go  
package main  
  
import (  
 "context"  
 "fmt"  
 "time"  
  
 disperser_rpc "github.com/Layr-Labs/eigenda/api/grpc/disperser"  
 "github.com/Layr-Labs/eigenda/clients"  
 "github.com/Layr-Labs/eigenda/core/auth"  
 "github.com/Layr-Labs/eigenda/disperser"  
 "github.com/Layr-Labs/eigenda/encoding/utils/codec"  
 "google.golang.org/protobuf/encoding/protojson"  
 "google.golang.org/protobuf/proto"  
)  
  
func main() {  
 // Configuration for the disperser client  
 config := clients.NewConfig(  
  "disperser-holesky.eigenda.xyz",  
  "443",  
  time.Second*10, // request timeout  
  true,           // useSecureGrpcFlag, should be set to true unless running against a local disperser for testing  
 )  
  
  // Retrieve authentication with private key  
 eigendaAuthKey, ok := os.LookupEnv("EIGENDA_AUTH_PK")  
 if !ok {  
  fmt.Printf("No EIGENDA_AUTH_PK env var set")  
  return  
 }  
  
 // Set up authentication with private key  
 signer := auth.NewSigner(eigendaAuthKey)  
  
 // Create the disperser client  
 client := clients.NewDisperserClient(config, signer)  
  
 // Context with timeout  
 ctx, cancel := context.WithTimeout(context.Background(), time.Second*10)  
 defer cancel()  
  
 // Data to be dispersed (example data)  
 data := []byte("example data to disperse")  
  
 // encode data to be compatible with bn254 field element constraints  
 data = codec.ConvertByPaddingEmptyByte(data)  
  
 // Custom quorums (none for now, means we're dispersing to the default quorums)  
 quorums := []uint8{}  
  
 // Disperse the blob  
 blobStatus, requestID, err := client.DisperseBlob(ctx, data, quorums)  
 if err != nil || *blobStatus == disperser.Failed {  
  fmt.Printf("Error dispersing blob: %v\n", err)  
  return  
 }  
  
 // Print the initial result  
 fmt.Printf("Initial Blob Status: %+v\n", blobStatus)  
 fmt.Printf("Request ID: %s\n", string(requestID))  
  
 // Create a new context for each status request  
 statusOverallCtx, statusOverallCancel := context.WithTimeout(context.Background(), time.Minute*30)  
 defer statusOverallCancel()  
  
 ticker := time.NewTicker(time.Second * 5)  
  
 // Poll GetBlobStatus until the status is done  
 for {  
  select {  
  case <-ticker.C:  
   // Create a new context for each status request  
   statusCtx, statusCancel := context.WithTimeout(statusOverallCtx, time.Second*5)  
   defer statusCancel()  
  
   // Get the blob status  
   statusReply, err := client.GetBlobStatus(statusCtx, requestID)  
   if err != nil {  
    fmt.Printf("Error getting blob status: %v\n", err)  
    return  
   }  
  
   // Check if the status is done  
   if statusReply.Status == disperser_rpc.BlobStatus_FINALIZED {  
    fmt.Printf("Blob Status is finalized: %s\n", pprint(statusReply))  
    return  
   } else if statusReply.Status == disperser_rpc.BlobStatus_FAILED {  
    fmt.Printf("Error dispersing blob: %v\n", statusReply.Status)  
    return  
   } else {  
    fmt.Printf("Current Blob Status: %s\n", pprint(statusReply))  
   }  
  case <-statusOverallCtx.Done():  
   fmt.Printf("Timed out waiting for blob to finalize\n")  
   return  
  }  
 }  
}  
  
func pprint(m proto.Message) string {  
 marshaler := protojson.MarshalOptions{  
  Multiline: true,  
  Indent:    "  ",  
 }  
 jsonBytes, err := marshaler.Marshal(m)  
 if err != nil {  
  panic("Failed to marshal proto to JSON")  
 }  
 return string(jsonBytes)  
}  

```

Finally, let's install our dependencies:



```
go mod tidy  

```

If you run this you should see logs like these:



```
$ go run main.go  
Initial Blob Status: Processing  
Request ID: f9c979e84c19929dcdfc0c4f7ba65dc3ab47276e6d910480ed2d84ccbd4b8a3d-313731353939303238353532353837363539382f302f33332f312f33332fe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  
Current Blob Status: {  
  "status":  "PROCESSING",  
  "info":  {}  
}  
  
<many logs later, within 12 minutes>  
  
Current Blob Status: {  
  "status":  "CONFIRMED",  
  "info":  {  
    "blobHeader":  {  
      "commitment":  {  
        "x":  "EBXIwkZ7nXChaRx2Nz+SZyU/rX3WvZnLGeKpCW32OWs=",  
        "y":  "LoTp8Bqz7pyhptnRBT5o01GAbPGXB52Ll+X+Pw+ibeg="  
      },  
      "dataLength":  1,  
      "blobQuorumParams":  [  
        {  
          "adversaryThresholdPercentage":  33,  
          "confirmationThresholdPercentage":  55,  
          "chunkLength":  1  
        },  
        {  
          "quorumNumber":  1,  
          "adversaryThresholdPercentage":  33,  
          "confirmationThresholdPercentage":  55,  
          "chunkLength":  1  
        }  
      ]  
    },  
    "blobVerificationProof":  {  
      "batchId":  15219,  
      "blobIndex":  687,  
      "batchMetadata":  {  
        "batchHeader":  {  
          "batchRoot":  "+yFLC9HFHJxkBixjGdFGv0psPC6R0DNynhowYgUvjtE=",  
          "quorumNumbers":  "AAE=",  
          "quorumSignedPercentages":  "VU4=",  
          "referenceBlockNumber":  1564355  
        },  
        "signatoryRecordHash":  "HG1kkSIGjTOX2kFexdGnuAj7zDJaat0XQQavHjjXdPs=",  
        "fee":  "AA==",  
        "confirmationBlockNumber":  1564476,  
        "batchHeaderHash":  "d1KhHvr0lhNCYiizYS5+v/2QWvSTsm7MeACChYDRli0="  
      },  
      "inclusionProof":  "3DDZAQV1jdb4Eb3pLAAVqAq69EMrmGMfwfcW9jQwShN8O4oqv7041DVjM09LARNO4VX1WUoVrSdXQ5ZXpaKKL7iREgnhNrHydYXfmJuGiS7dtxQubTDQ2O5bYTckzt/LZakvNf5hz87vEQdvHcYh2wpBugaX6/kgY/8OGiHLwocIXXwC5upaU92WSxFkHmd31xq7nAwDM5N8s7R9ktWBTbBGVFTtmTcctapohz551bskMoV79w28ie4Tc6NcdS5S9z1hR6tW9IGoHqeifynPjdvRaq51T/jnJWSC6gixbO6DOcw2qIU0+jhZsu6/ucHIwzxBQtvmp+7dLBthC7dZYllIOsc2nyTmUfp2mKXjP5vPEhbX+FLIMwagi3lGOI9zUdG/RYIpKxEIVoO5ffStDMotX4ZCgGZyQiTYR0maags/yc/ID27M8YVyu54nAAAyG89TpmqvVofJ1ove863ufA==",  
      "quorumIndexes":  "AAE="  
    }  
  }  
}  
  
<many logs later, within another 12 minutes>  
  
Current Blob Status is finalized: {  
  "status":  "FINALIZED",  
  "info":  {  
    "blobHeader":  {  
      "commitment":  {  
        "x":  "EBXIwkZ7nXChaRx2Nz+SZyU/rX3WvZnLGeKpCW32OWs=",  
        "y":  "LoTp8Bqz7pyhptnRBT5o01GAbPGXB52Ll+X+Pw+ibeg="  
      },  
      "dataLength":  1,  
      "blobQuorumParams":  [  
        {  
          "adversaryThresholdPercentage":  33,  
          "confirmationThresholdPercentage":  55,  
          "chunkLength":  1  
        },  
        {  
          "quorumNumber":  1,  
          "adversaryThresholdPercentage":  33,  
          "confirmationThresholdPercentage":  55,  
          "chunkLength":  1  
        }  
      ]  
    },  
    "blobVerificationProof":  {  
      "batchId":  15219,  
      "blobIndex":  687,  
      "batchMetadata":  {  
        "batchHeader":  {  
          "batchRoot":  "+yFLC9HFHJxkBixjGdFGv0psPC6R0DNynhowYgUvjtE=",  
          "quorumNumbers":  "AAE=",  
          "quorumSignedPercentages":  "VU4=",  
          "referenceBlockNumber":  1564355  
        },  
        "signatoryRecordHash":  "HG1kkSIGjTOX2kFexdGnuAj7zDJaat0XQQavHjjXdPs=",  
        "fee":  "AA==",  
        "confirmationBlockNumber":  1564476,  
        "batchHeaderHash":  "d1KhHvr0lhNCYiizYS5+v/2QWvSTsm7MeACChYDRli0="  
      },  
      "inclusionProof":  "3DDZAQV1jdb4Eb3pLAAVqAq69EMrmGMfwfcW9jQwShN8O4oqv7041DVjM09LARNO4VX1WUoVrSdXQ5ZXpaKKL7iREgnhNrHydYXfmJuGiS7dtxQubTDQ2O5bYTckzt/LZakvNf5hz87vEQdvHcYh2wpBugaX6/kgY/8OGiHLwocIXXwC5upaU92WSxFkHmd31xq7nAwDM5N8s7R9ktWBTbBGVFTtmTcctapohz551bskMoV79w28ie4Tc6NcdS5S9z1hR6tW9IGoHqeifynPjdvRaq51T/jnJWSC6gixbO6DOcw2qIU0+jhZsu6/ucHIwzxBQtvmp+7dLBthC7dZYllIOsc2nyTmUfp2mKXjP5vPEhbX+FLIMwagi3lGOI9zUdG/RYIpKxEIVoO5ffStDMotX4ZCgGZyQiTYR0maags/yc/ID27M8YVyu54nAAAyG89TpmqvVofJ1ove863ufA==",  
      "quorumIndexes":  "AAE="  
    }  
  }  
}  

```

Congratulations you've now dispersed a blob using the low\-level EigenDA disperser client.

[PreviousAPI Error Codes](/eigenda/integrations-guides/dispersal/api-documentation/error-codes)[NextEigenDA Proxy](/eigenda/integrations-guides/dispersal/clients/eigenda-proxy)

* 
* Integration Guides
* Dispersal to DA Network
* Quick Start
On this pageQuick Start: Dispersing Your First Blob to Testnet
==================================================


Disperse and Retrieve Blob Examples[​](#disperse-and-retrieve-blob-examples "Direct link to Disperse and Retrieve Blob Examples")
---------------------------------------------------------------------------------------------------------------------------------


**Prerequisites:**


* Open a linux terminal.
* [Install grpccurl for your environment](https://github.com/fullstorydev/grpcurl#installation).
* Download the eigenda repository and change your current working directory. The
included Protobuf definitions will be required:



```
gh repo clone Layr-Labs/eigenda  
cd eigenda   

```

**Step 1: Build EigenDA Utils**


The next step requires the `kzgpad` utility, which you can build with the following:



```
make build  

```

**Step 2: Store (Disperse) a blob**


Invoke the Disperser/DisperseBlob endpoint.


Example request:



```
# Download the EigenDA repo via gh client or wget  
$ gh repo clone Layr-Labs/eigenda  
# Change your working directory to the eigenda folder in order to point to the  
# protobuf defintions correctly  
$ cd eigenda  
  
$ grpcurl \  
  -import-path ./api/proto \  
  -proto ./api/proto/disperser/disperser.proto \  
  -d '{"data": "'$(tools/kzgpad/bin/kzgpad -e hello)'"}' \  
  disperser-holesky.eigenda.xyz:443 disperser.Disperser/DisperseBlob  

```

**Step 3: Validate the blob was stored in a batch**


Invoke the Disperser/GetBlobStatus service in order to validate the blob was
correctly stored and dispersed to the EigenDA network. The GetBlobStatus service
will return a value via the BlobStatus enumerated type.


Best practice is for users to poll the GetBlobStatus service to monitor status
of the Blobs as needed. Rollups may Polling once every 5\-10 seconds to monitor
the status of a blob until it has successfully dispersed on the network with
status of CONFIRMED. Confirmation can take up to a few minutes after the blob
has been initially sent to the disperser, depending on network conditions.


Example request:



```
# Update the value of INSERT_REQUEST_ID with the result of your disperse call  
# above  
  
$ grpcurl \  
  -import-path ./api/proto \  
  -proto ./api/proto/disperser/disperser.proto \  
  -d '{"request_id": "INSERT_REQUEST_ID"}' \  
  disperser-holesky.eigenda.xyz:443 disperser.Disperser/GetBlobStatus  

```

**Step 4: Retrieve a blob**


Option A: invoke the Disperser/RetrieveBlob rpc endpoint. This is a recommended
function for anyone that would like to inspect a stored blob.


Example request:



```
  
# Note the value for batch_header_hash can be obtained from the result of your  
# call to GetBlobStatus via info.blob_verification_proof.batch_metadata.batch_header_hash.  
  
$ grpcurl \  
  -import-path ./api/proto \  
  -proto ./api/proto/disperser/disperser.proto \  
  -d '{"batch_header_hash": "INSERT_VALUE", "blob_index":"INSERT_VALUE"}' \  
  disperser-holesky.eigenda.xyz:443 disperser.Disperser/RetrieveBlob | \  
  jq -r .data | \  
  tools/kzgpad/bin/kzgpad -d -  

```

Option B: Retrieve the blob directly from EigenDA nodes. Integrate the
[Retrieval Client](https://github.com/Layr-Labs/eigenda/tree/master/retriever)
into your Go binary.


### Null Bytes Padding[​](#null-bytes-padding "Direct link to Null Bytes Padding")


When the blob is retrieved it may be appended by a number of null bytes, which
the caller will need to remove. This occurs because the Disperser pads the blob
with null bytes to fit the frame size for encoding.


Once the user decodes the data, the decoded data may have null bytes appended to
the end. [Here is an example](https://github.com/Layr-Labs/eigenda/blob/master/test/integration_test.go#L522)
on how we trim the appended null bytes from recovered data.


Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")
---------------------------------------------------------------------


If you encounter an error that looks like this:



```
ERROR:  
  Code: InvalidArgument  
  Message: rpc error: code = InvalidArgument desc = encountered an error to convert a 32-bytes into a valid field element, please use the correct format where every 32 bytes(big-endian) is less than 21888242871839275222246405745257275088548364400416034343698204186575808495617  

```

This means that you have stumbled upon an idiosyncracy of how EigenDA currently
works. Essentially what this means is that you have tried to disperse a blob
that is not encoded correctly, and that in order to disperse this blob you
should first encode it using `kzgpad`, a utility distributed in the `eigenda`
repo. This error is much more likely to be encountered when playing with EigenDA
using a raw GRPC CLI, since there is no encoding logic built\-in. Please see
[Blob Encoding Requirements](/eigenda/integrations-guides/dispersal/api-documentation/blob-serialization-requirements) for more detail.

[PreviousEigenDA Overview](/eigenda/overview)[NextOverview](/eigenda/integrations-guides/dispersal/api-documentation/overview)* [Disperse and Retrieve Blob Examples](#disperse-and-retrieve-blob-examples)
	+ [Null Bytes Padding](#null-bytes-padding)
* [Troubleshooting](#troubleshooting)


* 
* Integration Guides
* [Rollup Guides](/eigenda/integrations-guides/rollup-guides/)
* Optimistic Rollup Integration Strategies
On this pageOptimistic Rollup Integration Strategies
========================================


There are a few viable design strategies for securely deploying an optimistic rollup with
EigenDA. This document aims to describe them in detail to provide rollup
engineers with a strong understanding of how an EigenDA integration would impact
their tech stack and security model.


For any given rollup there are four main concerns inherent to an integration
with external DA:


1. **Dispersal.** The rollup batcher must write transaction batches to the DA
layer, wait for confirmation, and write the resulting DA certificate to the
rollup inbox.
2. **Certificate Verification.** Either the rollup inbox contract
or the rollup OS must verify that DA certificate is valid, i.e. that enough
operators have certified the blob available, before reading the DA cert's data
from the DA layer. This ensures that a transaction batch referenced by an
invalid certificate is not executed.
3. **Retrieval.** Rollup full nodes must retrieve EigenDA blobs as part of the
L2 derivation/challenge process. Otherwise they cannot keep up with the state of
the L2\.
4. **Data Verification.** The rollup's fraud arbitration protocol must be
capable of verifying that the EigenDA blob data used to generate a state root
matches the KZG commitment provided in the EigenDA cert posted to the rollup
inbox. In doing this verification, the chain ensures that the transaction data
used to generate the rollup's state root was not manipulated by the
sequencer/proposer.


Each strategy used to integrate EigenDA can be defined by how these four concerns
are handled.


Trusted Verification Strategy (M0\)[​](#M0 "Direct link to Trusted Verification Strategy (M0)")
-----------------------------------------------------------------------------------------------


![M0 chain finalization](/assets/images/optimistic-M0-dispersal-cb6127af07fb33eeabd6d1cbad572614.png)


The trusted verification strategy does not do certificate or data verification.
Instead it focuses on dispersal and retrieval for the sake of simplicity, but at
the cost of security. This is an integration model fit for testnet. Let's walk
through the lifecycle of an L2 batch:


1. The batcher component of the rollup sequencer prepares an L2 batch, and calls
the **DisperseBlob()** method on the EigenDA disperser, sending the batch data.
2. The disperser erasure\-encodes the blob into chunks, calculates the KZG
commitment, and calculates the KZG proof for each chunk. It then distributes the
chunks to the EigenDA operator set, where each operator receives a subset of
the chunks in proportion to its stake. Each operator then stores the chunks its
received, verifying that each chunk matches its KZG proof and KZG commitment.
If so, it signs a message certifying that the chunk has been stored and returns
it to the disperser.
3. The disperser aggregates the signatures from step 3 into a single BLS
signature and sends it and some blob metadata to to the EigenDA Manager contract on
Ethereum. The EigenDA Manager contract on Ethereum is responsible for verifying EigenDA
certificates, and if they verify, recording that verification in storage.
Verification consists of ensuring the aggregated signature is valid and is
based on the current EigenDA operator set. This blob verification status is
not used in this implementation strategy.
4. If the sequencer is using the EigenDA disperser, then it shouldn't just trust
the disperser when it says that the blob has successfully been dispersed, it
should verify by checking onchain. This is important in this integration
strategy because the rollup inbox does not perform this check. Without this
check the EigenDA disperser is trusted (in addition to the sequencer).
5. The batcher then sends a transaction to the rollup inbox contract on
Ethereum with the EigenDA blob id as calldata, which accepts the
EigenDA blob id.


On the derivation side, there is a similar flow in reverse. When an L2 full node
encounters an EigenDA certificate in the rollup inbox, it knows to retrieve the
underlying blob from the EigenDA operator set using the EigenDA client, and then
interpret the transactions inside.


Please keep in mind that this integration model is *insecure*. The rollup
sequencer is completely trusted in this scenario, because the fraud proof system
is disabled, and state roots cannot be challenged. This means the sequencer can
post whatever state roots they want to the bridge contract and potentially steal
funds.


L2 Inbox Certificate Verification Strategy (M1\)[​](#M1 "Direct link to L2 Inbox Certificate Verification Strategy (M1)")
-------------------------------------------------------------------------------------------------------------------------


The natural locations for dispersal, retrieval, and data verification logic are
unambiguous – dispersal logic can only live inside the rollup batcher, retrieval
logic can only live inside the derivation pipeline, and data verification logic
can only live inside the fraud proof system. That leaves certificate
verification logic, which could be placed either in the rollup's inbox contract
or inside the rollup virtual machine executing off\-chain. The question of where
to place this logic is the key distinguishing factor between the "M1" and
"M2" integration paths.


An instructive way to dive into the L2 inbox certificate verification strategy
is to follow an L2 transaction from origination to finalization on Ethereum. We
can further break this down into two stages, L2 chain finalization and L2 bridge
finalization.


### L2 Chain Finalization[​](#l2-chain-finalization "Direct link to L2 Chain Finalization")


![M1 chain finalization](/assets/images/optimistic-M1-dispersal-8ba9973ccd122884d5d529fd3d06d247.png)


First, L2 chain finalization. An L2 transaction is finalized with respect to the
L2 chain when the transaction has been sequenced in the L2 inbox contract. When
this process is complete, any L2 node can say with confidence that the
transaction is part of the canonical L2 chain and is not subject to a reorg.


For example, if you were selling your car and a buyer paid you by sending you
USDC on a secure rollup, it would be important to wait until the transaction had
reached L2 chain finalization before letting them drive away with your vehicle.


Let's walk through how EigenDA affects this process:


1. The batcher component of the rollup sequencer prepares an L2 batch of user
transactions and sends it to the EigenDA disperser.
2. The disperser erasure\-encodes the blob into chunks, calculates the KZG
commitment, and calculates the KZG proof for each chunk. It then distributes the
chunks to the EigenDA operator set, where each operator receives a subset of
the chunks in proportion to its stake. Each operator then stores the chunks its
received, verifying that each chunk matches its KZG proof and KZG commitment.
If so, it signs a message certifying that the chunk has been stored and returns
it to the disperser.
3. The disperser aggregates the signatures from step 3 into a single BLS
signature and sends it and some blob metadata to to the EigenDA Manager contract on
Ethereum. The EigenDA Manager contract on Ethereum is responsible for verifying EigenDA
certificates, and if they verify, recording that verification in storage.
Verification consists of ensuring the aggregated signature is valid and is
based on the current EigenDA operator set. This blob verification status is
used in step 5\.
4. Once the blob has been confirmed, the batcher sends a transaction to the
rollup inbox contract on Ethereum with the EigenDA blob certificate as calldata.
5. The rollup inbox contract is programmed not to accept the
EigenDA certificate unless it is valid. To avoid repeating work,
the rollup inbox contract can make a `verifyBlob()` call on the EigenDA
contract, passing in the EigenDA certificate. Inside the `verifyBlob()`
implementation, the EigenDA manager contract checks against its storage whether
the blob certificate was verified. If so `verifyBlob()` returns `true` and the
EigenDA certificate is allowed into the inbox. Otherwise the blob ID is rejected.


At this point the the user's transaction has been confirmed on the rollup. Once
the weak subjectivity window passes (\~13 minutes), the user's transaction can be
considered finalized.


### L2 Bridge Finalization[​](#l2-bridge-finalization "Direct link to L2 Bridge Finalization")


![M1 bridge finalization](/assets/images/optimistic-M1-settlement-b2dde36fe0eb7da935b3aa5b407e8cb3.png)


L2 bridge finalization is necessary for bridging assets or data from the L2 to
the L1\. Bridge finalization depends on the rollup bridge contract on the L1
arriving on an accurate L2 state root. This is where fraud or validity proofs
come in.


Every L2 full node is responsible for deriving the L2's state root from the L1\.
In the absence of fraud, this is a relatively simple process with EigenDA:


1. If an L2 full node reads an EigenDA cert from the rollup inbox, it knows this
DA cert is valid because otherwise it would have been rejected from the inbox.
So it uses the EigenDA client to retrieve the EigenDA blob using the EigenDA
cert.
2. The full node executes the L2 block as described in the L2 blob against the
current L2 state.
3. If the full node is a proposer/validator, it will post the state root of the
L2 state to the rollup bridge contract on Ethereum every few blocks.
4. If no fraud proof has been submitted within the challenge window (\~7 days),
then the state root in the rollup bridge contract is considered valid and any
outbound assets or messages are released by the bridge contract.


In the event of a fraud challenge, the process is more complex. There is a
second, equivalent state transition function for generating state roots which is
much slower but also much a more rigorous fraud prove.


That process models the L2 state as a virtual machine, complete with an operating
system, which continuously reads messages from the rollup inbox contract using a
special `ReadInboxMessage` opcode, and handles them accordingly. If an inbox
message describes a batch of raw L2 transactions, the L2 OS knows it should
execute them. If an inbox message describes an EigenDA cert, the L2 operating
system knows that it should pass the KZG commitment inside the cert to the
special `ReadPreImage` opcode to read the underlying data, and then handle the
messages returned.


This VM state transition function process is useful because it makes it possible
to rigorously prove that the state root was generated based on the exact data
referenced by the EigenDA cert.


Let's walk through a scenario where the proposer is dishonest, in order to
illustrate:


![M1 bridge challenge](/assets/images/optimistic-M1-challenge-a3419d006ec85b21a616aa796179b791.png)


1. The proposer encounters an EigenDA cert and rather than reading data from
EigenDA honestly, decides to read data from elsewhere, not committed to by the
KZG commitment in the EigenDA cert. The proposer generates a state root on the
basis of executing these messages, and posts this state root to the rollup
bridge contract.
2. A challenger sees that their state root for a given L2 block does not match
the one posted by the proposer in the bridge contract, and makes a contract call
to begin a challenge.
3. The challenger and the defender alternate narrowing the scope of their
disagreement to a specific opcode of the VM state transition function, until
they've narrowed their disagreement to a specific opcode. In this case, the
challenge opts to challenge the `ReadPreImage` opcode, since this is where the
correct EigenDA should have been read.
4. The challenger invokes the arbitration contract with the necessary VM state
to execute the `ReadPreImage` opcode, as well as necessary extra data for
proving that the opcode was executed correctly. This extra data includes the
chunk of data that should have been read (only 32 bytes of data are read at a
time) as well as a KZG proof showing that the data matches the KZG commitment
that the opcode was invoked with. The arbitration contract checks whether the
data matches the KZG commitment and proof.
5. If the winner of the verification is the challenger then the old state root is
replaced with the challenger's new state root.


In order to implement an EigenDA integration with fraud proofs, the underlying
rollup must support passing KZG commitments to `ReadPreImage` opcode. The rest
of the L2 VM design works as\-is for arbitrating fraud.


L2 OS Certificate Verification Strategy (M2\)[​](#M2 "Direct link to L2 OS Certificate Verification Strategy (M2)")
-------------------------------------------------------------------------------------------------------------------


The V2 integration strategy is similar to the V1 integration strategy, with the
difference that EigenDA certificates are not verified on Ethereum. Instead, they
are verified within the L2 itself, such that the validity of DA certs is
enforced by the same fraud proof mechanism that is used with all other L2 state.
In this mode, a rollup batcher may submit invalid EigenDA certs to the rollup
inbox, such that L2 nodes interpret these invalid DA certs and discard them. If
a rollup proposer submits a state root based on data referenced by an EigenDA
cert, it is possible to successfully challenge that state root.


This integration strategy depends on the ability of the L2 OS to validate
EigenDA certs, which requires an authenticated view into the current EigenDA
operator set. Specifically, the L2 OS must have access to L1 state roots, so
that Eigenlayer contract storage proofs may be verified.


Analysis[​](#analysis "Direct link to Analysis")
------------------------------------------------


Although the rollup inbox implementation is simpler, the L2 OS implementation is
more desirable since it avoids adding validity constraints to batch updates,
which would incur significant signature verification gas costs regardless of
whether the sequencer is honest. When placed within the rollup OS, DA
certificate verification only incurs on\-chain costs when the sequencer is
dishonest.

[PreviousArbitrum Orbit](/eigenda/integrations-guides/rollup-guides/orbit/)[NextOverview](/eigenda/operator-guides/overview)* [Trusted Verification Strategy (M0\)](#M0)
* [L2 Inbox Certificate Verification Strategy (M1\)](#M1)
	+ [L2 Chain Finalization](#l2-chain-finalization)
	+ [L2 Bridge Finalization](#l2-bridge-finalization)
* [L2 OS Certificate Verification Strategy (M2\)](#M2)
* [Analysis](#analysis)


* 
* Integration Guides
* [Rollup Guides](/eigenda/integrations-guides/rollup-guides/)
* OP Stack
On this pageOP Stack and EigenDA
====================


[OP Stack](https://stack.optimism.io/) is the set of [software
components](https://github.com/ethereum-optimism/optimism) that run the [Optimism](https://www.optimism.io/) rollup and can be
deployed independently to power third\-party rollups.


By default, OP Stack sequencers write batches to Ethereum in the form of calldata or 4844 blobs to commit to the transactions included in the canonical L2 chain. In Alt\-DA mode, OP Stack sequencers and full nodes are configured talk to a third\-party HTTP server for writing and reading tx batches to and from DA. Optimism's Alt\-DA [spec](https://specs.optimism.io/experimental/alt-da.html) contains a more in\-depth breakdown of how this works.


To implement this server spec, EigenDA provides the [EigenDA Proxy](/eigenda/integrations-guides/dispersal/clients/eigenda-proxy) sidecar, which can be run alongside OP Stack sequencers and full nodes to securely communicate with the EigenDA disperser.


Deploying[​](#deploying "Direct link to Deploying")
---------------------------------------------------


### Deploying EigenDA Proxy[​](#deploying-eigenda-proxy "Direct link to Deploying EigenDA Proxy")


First check out the version of the EigenDA proxy corresponding to the verison of OP Stack you are deploying, and follow there README in that version:




| OP Stack Version | Compatible EigenDA Proxy Version |
| --- | --- |
| [v1\.7\.6](https://github.com/ethereum-optimism/optimism/releases/tag/v1.7.6) | [v1\.0\.0](https://github.com/Layr-Labs/eigenda-proxy/releases/tag/v1.0.0) |
| [v1\.7\.7](https://github.com/ethereum-optimism/optimism/releases/tag/v1.7.7) | [v1\.2\.0](https://github.com/Layr-Labs/eigenda-proxy/releases/tag/v1.2.0) |


### Deploying OP Stack[​](#deploying-op-stack "Direct link to Deploying OP Stack")


Next deploy the OP Stack components according to the official OP Stack [deployment docs](https://docs.optimism.io/builders/chain-operators/tutorials/create-l2-rollup), but with the following modifications:


#### op\-node rollup.json configuration[​](#op-node-rollupjson-configuration "Direct link to op-node rollup.json configuration")


In the op\-node `rollup.json` configuration the following should be set:



```
{  
  "plasma_config": {  
    "da_challenge_contract_address": "0x0000000000000000000000000000000000000000",  
    "da_commitment_type": "GenericCommitment",  
    "da_challenge_window": 300,  
    "da_resolve_window": 300  
  }  
}  

```

#### op\-node CLI configuration[​](#op-node-cli-configuration "Direct link to op-node CLI configuration")


The following env config values should be set to ensure proper communication between op\-node and eigenda\-proxy, replacing `{EIGENDA_PROXY_URL}` with the URL of your EigenDA Proxy server.


* `OP_NODE_PLASMA_ENABLED=true`
* `OP_NODE_PLASMA_DA_SERVICE=true`
* `OP_NODE_PLASMA_VERIFY_ON_READ=false`
* `OP_NODE_PLASMA_DA_SERVER={EIGENDA_PROXY_URL}`


#### op\-batcher CLI configuration[​](#op-batcher-cli-configuration "Direct link to op-batcher CLI configuration")


The following env config values should be set accordingly to ensure proper communication between OP Batcher and EigenDA Proxy, replacing `{EIGENDA_PROXY_URL}` with the URL of your EigenDA Proxy server.


* `OP_BATCHER_PLASMA_ENABLED=true`
* `OP_BATCHER_PLASMA_DA_SERVICE=true`
* `OP_BATCHER_PLASMA_VERIFY_ON_READ=false`
* `OP_BATCHER_PLASMA_DA_SERVER={EIGENDA_PROXY_URL}`


### Mainnet Keypair Registration[​](#mainnet-keypair-registration "Direct link to Mainnet Keypair Registration")


When you are ready to onboard your rollup to mainnet you can fill out the following form to get your keypair whitelisted: <https://forms.gle/niMzQqj1JEzqHEny9>.


Security Guarrantees[​](#security-guarrantees "Direct link to Security Guarrantees")
------------------------------------------------------------------------------------


This setup provides Stage 0 security guarrantees without adding an unnecessary trust assumption on the EigenDA disperser. The EigenDA Proxy [docs page](/eigenda/integrations-guides/dispersal/clients/eigenda-proxy) and [repo readme](https://github.com/Layr-Labs/eigenda-proxy/blob/main/README.md) explain how this is achieved.


### OP Stack DA Challenge Contract[​](#op-stack-da-challenge-contract "Direct link to OP Stack DA Challenge Contract")


One new component of OP Alt\-DA interface is the [DA challenge contract](https://specs.optimism.io/experimental/alt-da.html#data-availability-challenge-contract), which allows L2 assetholders to delay a data withholding attack executed by the sequencer or DA network. This integration does not implement a DA challenge contract, because it would not provide any additional security to OP Stack deployment without fault proofs enabled. This is because the OP Sequencer is a trusted entity that unilaterally controls the liveness and safety of the L2 chain.


The chain's liveness assumption on the sequencer is unchanged, because if the sequencer posts an invalid commitment then any verifier nodes syncing from EigenDA will halt, as they'd be incapable of inspecting the batch. This is equivalent to the same DoS vector where the sequencer arbitrarily stops producing batches.


The safety property is unchanged, because although the DA challenge contract could theoretically prevent a malicious sequencer from peforming a data withholding attack, in a stage 0 deployment such a sequencer would already have unilateral control of the bridge, and so would be able to steal all the funds in broad daylight, even with all the data available to prove that they violated the chain's safety.


The EigenDA protocol integrations team has roadmap plans to implement an DA challenge contract with along fault proof support in order to provide full safety guarrantees to OP Stack x EigenDA deployments.


Roadmap[​](#roadmap "Direct link to Roadmap")
---------------------------------------------


The EigenDA Rollup Integrations team is working to support OP Stack fault proofs by the end of summer 2024, and will post updates to [@eigen\_da](https://x.com/eigen_da?lang=en).


Contact[​](#contact "Direct link to Contact")
---------------------------------------------


If you are a Rollup considering integrating with EigenDA and OP Stack \- reach
out to our team to discuss how we can support and accelerate your onboarding:
<https://contact.eigenda.xyz/>


If you are a Rollup developer and have questions on the integration \- reach out
to our Support team via:
<https://support.eigenlayer.xyz/>

[PreviousRollup Guides](/eigenda/integrations-guides/rollup-guides/)[NextArbitrum Orbit](/eigenda/integrations-guides/rollup-guides/orbit/)* [Deploying](#deploying)
	+ [Deploying EigenDA Proxy](#deploying-eigenda-proxy)
	+ [Deploying OP Stack](#deploying-op-stack)
	+ [Mainnet Keypair Registration](#mainnet-keypair-registration)
* [Security Guarrantees](#security-guarrantees)
	+ [OP Stack DA Challenge Contract](#op-stack-da-challenge-contract)
* [Roadmap](#roadmap)
* [Contact](#contact)


* 
* Integration Guides
* [Rollup Guides](/eigenda/integrations-guides/rollup-guides/)
* Arbitrum Orbit
On this pageArbitrum Orbit Overview
=======================


[Arbitrum
Orbit](https://docs.arbitrum.io/launch-orbit-chain/orbit-gentle-introduction) is
a Rollup Development Kit (RDK) developed by [Offchain
Labs](https://www.offchainlabs.com/) to enable rollup developers to build
rollups using the same software that powers *Arbitrum One* and *Arbitrum Nova*.
In partnership with AltLayer, we have forked the core component of Orbit,
[Nitro](https://github.com/layr-Labs/nitro), to add
[M0](/eigenda/integrations-guides/rollup-guides/integrations-overview#M0) support for EigenDA. The M0 status of
this integration means that it is only designed for testnet.


How to deploy an Orbit chain[​](#how-to-deploy-an-orbit-chain "Direct link to How to deploy an Orbit chain")
------------------------------------------------------------------------------------------------------------


A short guide on launching an Orbit L3 against the EigenDA testnet:


Follow the [Orbit
Quickstart](https://docs.arbitrum.io/launch-orbit-chain/orbit-quickstart)
documentation until step 9, skipping step 7\. When prompted to use the official
[orbit\-setup\-script repo](https://github.com/OffchainLabs/orbit-setup-script),
use the [forked repo](https://github.com/Layr-Labs/orbit-setup-script) instead.
At the end of step 8 you should have your `chainConfig.json` and
`orbitSetupScriptConfig.json` saved locally.


This fork of Nitro is on version v2\.2\.0, but the *Orbit chain deployment portal*
is on version v2\.1\.3, which means the `nodeConfig.json` must be updated to
reflect the new format, according to the configuration migration guide in the
[v2\.2\.0 release
notes](https://github.com/OffchainLabs/nitro/releases/tag/v2.2.0).


Finally, continue with steps 9\-11 with your updated configuration file. If
you've completed these steps successfully, congrats! You are now running an
Orbit rollup that uses EigenDA.


This documentation is under construction and will continue to change. For
technical questions and hand\-on support please reach out to
[contact.eigenda.xyz](https://contact.eigenda.xyz).

[PreviousOP Stack](/eigenda/integrations-guides/rollup-guides/op-stack/)[NextOptimistic Rollup Integration Strategies](/eigenda/integrations-guides/rollup-guides/integrations-overview)* [How to deploy an Orbit chain](#how-to-deploy-an-orbit-chain)


* 
* [Networks](/eigenda/networks/)
* Holesky
On this pageHolesky
=======


The EigenDA Holesky testnet is the current EigenDA testnet. The EigenDA Holesky testnet was preceded by the now\-sunset [EigenDA Goerli testnet](/eigenda/networks/goerli).


Quick Links[​](#quick-links "Direct link to Quick Links")
---------------------------------------------------------


* [AVS Page](https://holesky.eigenlayer.xyz/avs/eigenda)
* [Blob Explorer](https://blobs-holesky.eigenda.xyz/)
* [Deployed Contract Addresses](https://github.com/Layr-Labs/eigenlayer-middleware/?tab=readme-ov-file#current-testnet-deployment)


Specs[​](#specs "Direct link to Specs")
---------------------------------------




| Property | Value |
| --- | --- |
| Disperser Address | `disperser-holesky.eigenda.xyz:443` |
| Churner Address | `churner-holesky.eigenda.xyz:443` |
| Batch Confirmation Interval | Every 10 minutes (may vary based on network health) |
| Max Blob Size | 2 MB |
| Default Blob Dispersal Rate limit | No more than 1 blob every 100 seconds |
| Default Blob Size Rate Limit | No more than 1\.8 MB every 10 minutes |
| Stake Sync (AVS\-Sync) Interval | Every 24 hours |


Quorums[​](#quorums "Direct link to Quorums")
---------------------------------------------




| Quorum Number | Token |
| --- | --- |
| 0 | ETH, LSTs |
| 1 | [WETH](https://holesky.etherscan.io/address/0x94373a4919B3240D86eA41593D5eBa789FEF3848) |
| 2 | [reALT](https://holesky.etherscan.io/address/0x2ff89Aa21D2FB7B00F28A3d224ECf5854ea162f4) |

[PreviousGoerli (Deprecated)](/eigenda/networks/goerli)[NextMainnet](/eigenda/networks/mainnet)* [Quick Links](#quick-links)
* [Specs](#specs)
* [Quorums](#quorums)


* 
* Operator Guides
* Metrics and Monitoring
Metrics and Monitoring
======================


These instructions provide a quickstart guide to run the Prometheus, Grafana,
and Node exporter stack.


**Step 1:** Move your current working directory to the monitoring folder:



```
cd monitoring  
cp .env.example .env  

```

* Open the `.env` file, ensure the location of `prometheus.yml` is correct for your environment.
* In the `prometheus.yml` file:
	+ Update prometheus config [file](https://github.com/Layr-Labs/eigenda-operator-setup/blob/master/monitoring/prometheus.yml)
	is updated with the metrics port (`NODE_METRICS_PORT`) of the eigenda node in parent folder `.env` file
	+ Ensure the eigenda container name for `scrape_configs.targets` matches the value of the parent folder `.env` file (`MAIN_SERVICE_NAME`).
	+ Make sure the location of prometheus file is correct in [.env](https://github.com/Layr-Labs/eigenda-operator-setup/blob/master/monitoring/.env.example) file


**Step 2:** Run the following command to start the monitoring stack



```
docker compose up -d  

```

**Step 3:** Since eigenda is running in a different docker network we will need
to have prometheus in the same network. To do that, run the following command



```
docker network connect eigenda-network prometheus  

```

Note: `eigenda-network` is the name of the network in which eigenda is running.
You can check the network name in eigenda
[.env](https://github.com/Layr-Labs/eigenda-operator-setup/blob/master/mainnet/.env.example#L2)
file (`NETWORK_NAME`). This will ensure Prometheus can scrape the metrics from
Eigenda node.


Useful Dashboards: EigenDA offers a set of [Grafana
dashboards](https://github.com/Layr-Labs/eigenda-operator-setup/tree/master/monitoring/dashboards)
that are automatically imported when initializing the monitoring stack.


If you prefer to set up the metrics and monitoring stack manually, follow the
steps located [here](https://github.com/Layr-Labs/eigenda-operator-setup#metrics).

[PreviousSystem Upgrades](/eigenda/operator-guides/upgrades/system-upgrades)[NextTroubleshooting](/eigenda/operator-guides/troubleshooting)

* 
* Operator Guides
* FAQ
On this pageEigenDA Operator FAQ
====================


#### I have a static IP/DNS address. How do I register and fix this address for EigenDA?[​](#i-have-a-static-ipdns-address-how-do-i-register-and-fix-this-address-for-eigenda "Direct link to I have a static IP/DNS address. How do I register and fix this address for EigenDA?")


If you have a static IP address or DNS address set up to receive the traffic
(i.e. running on k8s or have a load balancer in front of your EigenDA node)
and you don't want EigenDA to automatically update IP which is sent to EigenDA
while registering, then follow the steps to make sure correct IP is registered:


* Update the [NODE\_HOSTNAME](https://github.com/Layr-Labs/eigenda-operator-setup/blob/31d99e2aa67962878969b81a15c7e8d13ee69750/mainnet/.env.example#L71) to the public IP where you will want to recieve traffic.
* Opt\-in using the [provided steps](/eigenda/operator-guides/run-a-node/registration/).
* In order to disable the node IP address from being automatically updated, set the value of [NODE\_PUBLIC\_IP\_CHECK\_INTERVAL](https://github.com/Layr-Labs/eigenda-operator-setup/blob/31d99e2aa67962878969b81a15c7e8d13ee69750/mainnet/.env.example#L65) to `0`.
[PreviousTroubleshooting](/eigenda/operator-guides/troubleshooting)[NextRegistration Protocol](/eigenda/operator-guides/registration-protocol)

* 
* Operator Guides
* Overview
Overview
========


This guide contains the steps needed to set up your node on the EigenDA testnet.
The testnet is used to test the operational and performance requirements for
running a node before deploying on mainnet. The testnet is under constant stress
tests and has frequent updates to the node software and other network
components. It’s important to check regularly for new updates to the software
and documentation.


Start by understanding the [Requirements](/eigenda/operator-guides/requirements/) for being an EigenDA operator and running an EigenDA node. If you are able to satisfy all of the elligibility requirements for becoming a node operator, proceed onward to [run your node](/eigenda/operator-guides/run-a-node/). It's important that you properly [configure and start your node](/eigenda/operator-guides/run-a-node/run-with-docker/) before [registering your operator with the network](/eigenda/operator-guides/run-a-node/registration/) and becoming subject to the SLA.


EigenDA is in a state of active development. Operators must make sure to listen for [node software updates](/eigenda/operator-guides/upgrades/software-upgrades/) in the correct channels and to implement these upgrades promptly.

[PreviousOptimistic Rollup Integration Strategies](/eigenda/integrations-guides/rollup-guides/integrations-overview)[NextNode Operator Requirements](/eigenda/operator-guides/requirements/)

* 
* Operator Guides
* Registration Protocol
On this pageRegistration Protocol Details
=============================


This page contains further background information about the registration process for EigenDA operators. The steps described in this section are performed automatically by the scripts referenced in the [registration instructions](/eigenda/operator-guides/run-a-node/registration/).


Registration Controls[​](#registration-controls "Direct link to Registration Controls")
---------------------------------------------------------------------------------------


The EigenDA network is designed to include the top N\=200 operators by quorum weight within each quorum. This design aims to maximize the total amount of securing stake, thereby enhancing the overall performance and security of the network.


Maintaining the information about the smallest operator by quorum weight on the smart contract is not feasible due to the high computational cost and complexity involved in sorting or maintaining a priority queue on chain. To manage this, the network employs the combination of an authorized off\-chain churn approver and a set of on\-chain checks.


### The EigenDA Churn Approver[​](#the-eigenda-churn-approver "Direct link to The EigenDA Churn Approver")


The churn approver perform a trusted service of supplying the smallest operator by quorum weight to the registration contracts.


When the network has reached its operator cap and a new operator wishes to join, the new operator can request a signature from the Churn Approver. The Churn Approver checks that the new operator meets stake requirements and provides a signature that approves the removal of the current lowest\-stake operator. The new operator then opts\-in to EigenDA, providing the Churn Approver’s signature and information on the lowest\-stake existing operator as additional inputs to EigenDA’s smart contract.


### Smart Contract Checks[​](#smart-contract-checks "Direct link to Smart Contract Checks")


The smart contract performs a series of checks to ensure the integrity of the operator replacement process:


1. It verifies the Churn Approver’s signature.
2. It performs checks against the stake of the newly\-joining and (to\-be\-ejected) current lowest\-stake operator:
	* The new operator needs at least 1\.1x the ejected operator’s stake.
	* The ejected operator must constitute less than 10\.01% of the total stake.


The parameters of checks performed in step 2 are configurable by the contract
governance.


If these validation steps succeed, the contract will ejects the lowest\-stake operator identified by the churner and proceeds with opting\-in the new operator, as normal.


Support for smart\-contract\-based operators[​](#support-for-smart-contract-based-operators "Direct link to Support for smart-contract-based operators")
--------------------------------------------------------------------------------------------------------------------------------------------------------


While the opt\-in scripts provided in [registration instructions](/eigenda/operator-guides/run-a-node/registration/) assume that the EigenDA operator will provision an ECDSA private key for signing transactions, it is possible in principle for EigenDA operators to register from a smart contract. Please contact us if you are in need of detailed guidance for performing this integration.

[PreviousFAQ](/eigenda/operator-guides/operator-faq)[NextNetworks](/eigenda/networks/)* [Registration Controls](#registration-controls)
	+ [The EigenDA Churn Approver](#the-eigenda-churn-approver)
	+ [Smart Contract Checks](#smart-contract-checks)
* [Support for smart\-contract\-based operators](#support-for-smart-contract-based-operators)


* 
* Operator Guides
* Requirements
Node Operator Requirements
==========================


Before deciding to operate an EigenDA node, be sure to fully understand the following aspects of node operation elligibility:


* [Delegation Requirements](/eigenda/operator-guides/requirements/delegation-requirements/): EigenDA currently only allows a limited number of operators to join the protocol. This means that in order to run a node, you must satisfy a minimum stake requirement which adjust over time as new operators and new stake join the protocol.
* [System Requirements](/eigenda/operator-guides/requirements/system-requirements/): Because EigenDA is a horizonally scaling architecture, operator node system requirements scale in accordance with the amount of stake delegated to the operator. Node operators must understand their requirements based on their amount of delegated stake, and be prepared to [upgrade their setups](/eigenda/operator-guides/upgrades/system-upgrades/) as needed in response to changing stake distributions.
* [Protocol SLA](/eigenda/operator-guides/requirements/protocol-SLA/): All operators are expected to satisfy a service level agreement, with violations having certain protocol level consequences.
[PreviousOverview](/eigenda/operator-guides/overview)[NextSystem Requirements](/eigenda/operator-guides/requirements/system-requirements)

* 
* Operator Guides
* [Requirements](/eigenda/operator-guides/requirements/)
* Delegation Requirements
On this pageDelegation Requirements
=======================


infoActive Operator Set Cap: the active operator set cap is currently
limited to 200 operators for both Mainnet and Holesky. We will review this operator cap on an ongoing basis,
and explicitly communicate future changes.


EigenDA currently only allows a limited number of operators to join the protocol. This restriction relates directly to the cost of bridging EigenDA availability attestations to the Ethereum L1 and will be relaxed as this cost is alleviated via various technological improvements.


The EigenDA operator cap means that in order to be an operator for EigenDA, you must first register as an EigenLayer operator and meet certain stake requirements. These requirements are evaluated on a per\-quorum basis, relative to the weighting for each quorum:


* Mainnet
* Holesky

* Minimum stake floor: Each operator must have
	+ at least 32 ETH to join the ETH quorum, or
	+ at least 1 EIGEN to join the EIGEN quorum.
* Congested operator set stake floor: When the global operator cap (200\) is reached for the quorum, the joining operator must have more than 1\.1X the quorum weight of the current lowest\-weighted operator in order to replace that operator.
* Minimum stake floor: Each operator must have at least 32 ETH.
* Congested operator set stake floor: When the global operator cap (200\) is reached for the quorum, the joining operator must have more than 1\.1X the quorum weight of the current lowest\-weighted operator in order to replace that operator.

Details about how these requirements are enforced and the process by which DA nodes join a quorum for which they are eligible can be found at the [Registration Protocol Overview](/eigenda/operator-guides/registration-protocol).


Checking eligibility[​](#checking-eligibility "Direct link to Checking eligibility")
------------------------------------------------------------------------------------


In order to determine the current TVL of the top 200 operators for each quorum, please visit our
AVS page ([Mainnet](https://app.eigenlayer.xyz/avs/eigenda), [Holesky](https://holesky.eigenlayer.xyz/avs/eigenda)) and sort by `TVL Descending.` Observe the first 200 operators listed for the quorum and the amount of ETH TVL
delegated to them. Please keep in mind that the AVS Page reflects the
operator stake on EigenLayer, which is used to update the EigenDA operator set
stake weights on a weekly basis (Wednesdays at 17:00 UTC), so the EigenDA stake
may lag the real\-time EigenLayer stake by at most 7 days.


Have I been churned?[​](#have-i-been-churned "Direct link to Have I been churned?")
-----------------------------------------------------------------------------------


Operators that have been ejected can verify the change in two ways:


1. Visit the EigenDA AVS application to observe whether your Operator is present
in the active operator set on the [AVS page](https://holesky.eigenlayer.xyz/avs/eigenda).
2. Observe your EigenDA Operator log for the following logs. If you see this
consistently, then your operator is not receiving any disperser traffic and you
may have been ejected. This is not an error but if you only see this log line
repeatedly then it means you may not be receiving any disperser traffic.



```
INFO [12-21|18:53:46.673|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=3  caller=node.go:233  

```
[PreviousSystem Requirements](/eigenda/operator-guides/requirements/system-requirements)[NextProtocol SLA](/eigenda/operator-guides/requirements/protocol-SLA)* [Checking eligibility](#checking-eligibility)
* [Have I been churned?](#have-i-been-churned)


* 
* Operator Guides
* [Requirements](/eigenda/operator-guides/requirements/)
* Protocol SLA
On this pageOperator Protocol SLA
=====================


When operators opt\-in to EigenDA, they assume responsibilities imposed by the protocol to provide the EigenDA node service honestly and with at least a certain level of availability and performance. Operators are held accountable for these responsibilities by the network and may face penalties such as ejection for unavailability faults.


Responsibilities[​](#responsibilities "Direct link to Responsibilities")
------------------------------------------------------------------------


The operator's responsibilities are the sum of the responsibilities it holds to all the quorums that it's registered in. Quorums are separate and independent from each other for attestation, so the exact entity to account for is each \<operator, quorum\> pair.


The following is the lifecycle of an \<operator, quorum\>, with responsibilities at different stages from when the operator opted\-in the quorum to opt\-out and beyond:


![EigenDA SLA Responsibilities](/img/eigenda/eigenda-sla-diagram.png)
### Operator Responsibilities[​](#operator-responsibilities "Direct link to Operator Responsibilities")


Operators have three primitive responsibilities:


1. **Verify, store and attest the blobs dispersed to it**
	1. An \<operator, quorum\> pair is responsible for a blob, if this quorum is requested by the blob in dispersal request
	2. The \<operator, quorum\> is responsible for a batch, if it's responsible for at least one of the blobs in the batch. When \<operator, quorum\> is responsible for a batch, it has to:
		1. Receive the batch header, all the blobs' headers, and the blobs in the batch that it's responsible for.
		2. Validate the batch as well as blobs received.
		3. Store the data if they are valid.
		4. Sign the batch: the signature signifies the operator's promise of having performed the attestation (validating and storing data) and will hold the future responsibility to serve the data.
2. **Store the blobs it attested (until the blobs' end of life)**
	1. The blob reaches the end of life `100,800 blocks` after onchain confirmation (roughly `14 days`).
3. **Serve the blobs it stored**
	1. Note: strictly, it's just attesting (dispersal) and serving (retrieval), as storing the data is implied by serving (the serving needs to be backed by data stored); separating storing out is to make it more clear here.


Note: When the operator opts in multiple quorums, the above will apply to each quorum.


### Responsibility Lifecycle[​](#responsibility-lifecycle "Direct link to Responsibility Lifecycle")


These responsibilities are mapped into following stages of \<operator, quorum\>'s lifecycle:


* **Live:** from \<operator, quorum\>'s registration to deregistration (from block `A` to `B-1`)
	+ Note: the \<operator, quorum\> will not be requested for dispersal with block `B` as reference block, because the \<operator, quorum\> won't be in the state produced by that block.
* **Full responsibility:** `attest+store+serve` (until block C)
	+ Note: after \<operator, quorum\> opted out, it's still responsible for dispersal for `BLOCK_STALE_MEASURE` blocks. This is because the dispersal can use a reference block that is in the past (but within a `BLOCK_STALE_MEASURE` window).
* **Partial responsibility (lame duck period):** `store+serve` (until block D)
	+ The operator will continue to be responsible for storing and serving the data it signed until all the data is expired.
* **Free:** The operator becomes free of responsibilities starting block `D+1`.


Note: if the operator re\-opts in the quorum at any point from `B` to `D`, the above lifecycle will be restarted.


Accountability Measurements, Policies, and Actions[​](#accountability-measurements-policies-and-actions "Direct link to Accountability Measurements, Policies, and Actions")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


**Responsibilities**


Operators are required to carry out both attestation and serving (retrieval) functions as part of their role within the EigenDA protocol. The assessment of their performance in these areas is conducted using the service level indicators (SLI) specified here.




| Responsibility | Rolling Daily SLI (measure) |
| --- | --- |
| Attesting | Signing rate: num\-batches\-signed / num\-batches\-responsible\-to\-sign |
| Serving | Serving availability: num\-requests\-success / num\-total\-requests |


Note that the SLI is evaluated over a rolling 24 hour interval.


**SLA**


Operators are required to maintain high availability of both attesting and serving (retrieval) in accordance with the amount of stake delegated to the operator, as indicated by the service level agreement (SLA) table below. Since the impact of an operator's failure to perform its responsibilities scales with the amount of stake delegated to the operator, operators holding a larger percentage of delegated stake are held to higher standards of availability.




| Share of Quorum Stake | Rolling Daily SLA (policy) | Nominal Maximum Daily Downtime |
| --- | --- | --- |
| Baseline | 90 % | 2\.4 hours |
| \> 5% | 95% | 1\.2 hours |
| \> 10% | 98% | 29 minutes |
| \> 15% | 99\.5% | 7 minutes |


Operators who hold delegated stake in multiple quorums must satisfy the SLA associated with each of their registered quorums. For instance, an operator holding 1% of stake in 'quorum 0' and 7% of stake in 'quorum 1' must keep its signing rate and serving availability above 90% for 'quorum 0' and 95% for 'quorum 1'.


**Enforcement Actions**


Operators can be subject to forced ejection from the protocol if they fail to meet their Rolling Daily SLA. This action can occur with or without prior notice and may follow initial soft enforcement steps, including the disclosure of the operator's SLI and overall ranking. Ejection is performed on a per quorum basis. An operator holding a 10% stake in 'quorum 0' who does not attest to blobs for 45 minutes may face immediate ejection from that quorum, particularly if their performance compromises the network's liveness. In addition to removal from quorums, following ejection operators will be unable to join any quorum for a cooldown period of 7 days.

[PreviousDelegation Requirements](/eigenda/operator-guides/requirements/delegation-requirements)[NextRun a node](/eigenda/operator-guides/run-a-node/)* [Responsibilities](#responsibilities)
	+ [Operator Responsibilities](#operator-responsibilities)
	+ [Responsibility Lifecycle](#responsibility-lifecycle)
* [Accountability Measurements, Policies, and Actions](#accountability-measurements-policies-and-actions)


* 
* Operator Guides
* [Requirements](/eigenda/operator-guides/requirements/)
* System Requirements
On this pageSystem Requirements
===================


General System Requirements[​](#general-system-requirements "Direct link to General System Requirements")
---------------------------------------------------------------------------------------------------------


The EigenDA network design dictates that operators with greater stake will
be asked to store a larger number of blob chunks/shards. As a result, an operator's node requirements are a
function of the total amount of stake they wield across all quorums, which we
call 'Total Quorum Stake' (TQS). For example, if an operator Foobar has 3% stake
on the restaked ETH quorum, and 5% ETH on a staked WETH quorum, then operator
Foobar's TQS is 8%.


Operators should use the following table to determine which [EigenLayer node class](/eigenlayer/operator-guides/eigenlayer-node-classes#general-purpose-eigenlayer-node-classes)
is appropriate for their level of stake:




| Total Quorum Stake (TQS) | Max Allocated Throughput | Node Class |
| --- | --- | --- |
| Up to 0\.03% (Solo staker) | 80 Kbps | General Purpose \- large |
| Up to 0\.2% | 500 Kbps | General Purpose \- xl |
| Up to 20% | 50 Mbps | General Purpose \- 4xl |


Here 'Max Allocated Throughput' refers to the maximum amount of blob shard traffic that
will be sent to a node based on their total quorum stake. This measure does not translate
directly to the networking capacity required by the node; operators should use the network
capacity requirements of the associated node class.


Professional operators with large or variable amounts of delegated stake should
select the `4xl` node class. The `large` class is intended to be used by solo
stakers with the minimal allowed quantity of stake.


We will update this specification to include new EigenLayer node classes as they
are introduced.


Node Storage Requirements[​](#node-storage-requirements "Direct link to Node Storage Requirements")
---------------------------------------------------------------------------------------------------


EigenDA nodes **must** provision high\-performance SSD storage in order to keep
up with network storage and retrieval tasks. Enterprise grade SSDs are recommended, such as `PCIe 4.0 x4 M.2/U.2 NVMe`.


Failure to maintain adequate
performance will result in unacceptable validation latency and [automatic ejection](/eigenda/operator-guides/requirements/protocol-SLA/).


The following table summarizes required storage capacity based on TQS:




| Total Quorum Stake (TQS) | Max Allocated Throughout | Required Storage |
| --- | --- | --- |
| Up to 0\.03% | 80 Kbps | 20 GB |
| Up to 0\.2% | 500 Kbps | 150 GB |
| Up to 1% | 2\.5 Mbps | 750 GB |
| Up to 10% | 25 Mbps | 4 TB |
| Up to 20% | 50 Mbps | 8 TB |


infoThe rough size of the message sent from the EigenDA disperser to a DA node can be estimated using the following formula:


```
<batch size (MB)>  = <throughput (MB/s)>  * <batch interval (s)>  * <coding rate> * <% stake>  

```
Where `<coding rate> = 5` for all current EigenDA quorums. So if the network is operating at 1MB/s with a 10 minute batch interval, and a node has 5% of the stake, then that node will receive roughly 150MB per message from the disperser.


System Upgrades[​](#system-upgrades "Direct link to System Upgrades")
---------------------------------------------------------------------


Since system requirements scale dynamically in accordance with the amount of stake delegated to the operator, node operators may from time to time need to upgrade their system setups in order to continue meeting the [Protocol SLA](/eigenda/operator-guides/requirements/protocol-SLA/). Guidance for performing such upgrades is covered in [System Upgrades](/eigenda/operator-guides/upgrades/system-upgrades/)


IP Stability Requirements[​](#ip-stability-requirements "Direct link to IP Stability Requirements")
---------------------------------------------------------------------------------------------------


Currently, the EigenDA protocol requires DA nodes to publish their IP address to the Ethereum L1 so providers and consumers of data can reach the node at this address. Consequently, node operators must be able to meet certain IP address stability and reachability requirements, as summarized in the table below.




|  | Shared IP | Dedicated IP |
| --- | --- | --- |
| Stable IP | ❌ Note: this will still work, if operators themselves figure out how to make the IP:Port reachable, e.g. configure port forwarding. | ✅ This is the ideal case for an EigenDA operator. |
| Unstable (Changing) IP | ❌ Note: this will still work, if operators themselves figure out how to make the IP:Port reachable, e.g. configure port forwarding. | ✅ Although this will work, operators are encouraged to have a stable IP, because changing IP will incur an Eth transaction (to update IP on\-chain) and cost gas. |

[PreviousNode Operator Requirements](/eigenda/operator-guides/requirements/)[NextDelegation Requirements](/eigenda/operator-guides/requirements/delegation-requirements)* [General System Requirements](#general-system-requirements)
* [Node Storage Requirements](#node-storage-requirements)
* [System Upgrades](#system-upgrades)
* [IP Stability Requirements](#ip-stability-requirements)


* 
* Operator Guides
* Run a Node
Run a node
==========


If you are able to satisfy all of the [elligibility requirements](/eigenda/operator-guides/requirements/)) for becoming a node operator, then you're ready to set up and run your node.


infoBefore registering as an operator for EigenDA, operators should [register as an operator with EigenLayer](https://docs.eigenlayer.xyz/operator-guides/operator-installation). This process will allow the operator to securely create BLS and ECDSA keys that will be needed during the DA node configuration steps outlined below.


Running an operator node consists of a few main steps:


1. Setting up the system environment and configuring the node (covered in [run with docker](/eigenda/operator-guides/run-a-node/run-with-docker/))
2. Starting the node software and confirming basic operation (covered in [run with docker](/eigenda/operator-guides/run-a-node/run-with-docker/))
3. [Registering the node](/eigenda/operator-guides/run-a-node/registration/) with one or more quorums.


Currently, we provide full documentation for performing the first two steps in the context of [running a node using docker](/eigenda/operator-guides/run-a-node/run-with-docker/). Operators utilizing other setups can still utilize these instructions as a guide.

[PreviousProtocol SLA](/eigenda/operator-guides/requirements/protocol-SLA)[NextRun with Docker](/eigenda/operator-guides/run-a-node/run-with-docker)

* 
* Operator Guides
* [Run a Node](/eigenda/operator-guides/run-a-node/)
* Register Your Operator
On this pageRegister Your Operator
======================


Your operator will not begin receiving traffic from the EigenDA disperser until it has registered for one or more quorums with EigenDA. Note, as discussed in [delegation requirements](/eigenda/operator-guides/requirements/delegation-requirements/), that registration with an EigenDA quorum requires that an operator already be [registered as an operator with EigenLayer](https://docs.eigenlayer.xyz/operator-guides/operator-installation) and to have a minimum amount of stake delegated within each quorum to be registered.


Opt\-in to an EigenDA Quorum[​](#opt-in-to-an-eigenda-quorum "Direct link to Opt-in to an EigenDA Quorum")
----------------------------------------------------------------------------------------------------------


If you meet the delegation requirements for opting into one or more [quorums](https://docs.eigenlayer.xyz/eigenlayer/operator-guides/operator-introduction#quorums), you can execute the following command from the `eigenda-operator-setup` folder to opt\-in to the desired quorums:


* Mainnet
* Holesky


```
cd mainnet  
  
./run.sh opt-in <quorum>  
  
# for opting in to quorum 0:  
./run.sh opt-in 0  
  
# for opting in to quorum 0 and 1:  
./run.sh opt-in 0,1   

```
Note: EigenDA maintains two [quorums](https://docs.eigenlayer.xyz/eigenda/networks/mainnet) on Mainnet: Restaked ETH (including Native and LST Restaked ETH) and EIGEN. EigenDA allows the Operator to opt\-in to either quorum or both quorums at once (aka dual\-quorum).

* ETH (Native \& LST) Quorum: `0`
* EIGEN Quorum: `1`
* Dual Quorum: `0,1`

You only need to provide the quorum which you want to opt into. For example, if you are already registered to quorum `0` and want to opt\-in one more quorum `1`, then you just need to set `<quorum>` as `1` while opting in again.

If you attempt to opt\-in to both quorums ('`0,1`') you must have sufficient TVL to opt\-in to the active Operator set for both quorums, otherwise the entire opt\-in attempt will fail for both quorums. The opt\-in attempt for both quorums is an "all or nothing" process.


```
cd holesky  
  
./run.sh opt-in <quorum>  
  
# for opting in to quorum 0:  
./run.sh opt-in 0  
  
# for opting in to quorum 0 and 1:  
./run.sh opt-in 0,1   
  
# for opting in to all quorums:  
./run.sh opt-in 0,1,2  

```
Note: EigenDA maintains three [quorums](https://docs.eigenlayer.xyz/eigenda/networks/holesky) on Holesky: Restaked ETH (including Native and LST Restaked ETH) and Restaked WETH. EigenDA allows the Operator to opt\-in to any quorum or all quorums at once.

* ETH (Native \& LST) Quorum: `0`
* WrappedEth (WETH) Quorum: `1`
* Restaked ALT (reALT) Quorum: `2`

You only need to provide the quorum which you want to opt into. For example, if you are already registered to quorum `0` and want to opt\-in one more quorum `1`, then you just need to set `<quorum>` as `1` while opting in again.

If you attempt to opt\-in to many quorums ('`0,1,2`') you must have sufficient TVL to opt\-in to the active Operator set for all quorums, otherwise the entire opt\-in attempt will fail for all quorums. The opt\-in attempt for all quorums is an "all or nothing" process.


warningOperators must wait for their stakes to be synced if the delegation happened after you opt\-in to the EigenDA AVS. EigenLayer's AVS\-Sync component runs at certain intervals to update the delegation totals on chain for each operator. If you are unable to opt in despite having sufficient delegated stake, please wait at least the amount necessary for staked to be synced, then retry opt\-in. This sync interval varies for different networks and you can check [here](https://docs.eigenlayer.xyz/eigenda/networks/).


The script will use the `NODE_HOSTNAME` from [.env](https://github.com/Layr-Labs/eigenda-operator-setup/blob/31d99e2aa67962878969b81a15c7e8d13ee69750/mainnet/.env.example#L71) as your current IP.


If your operator fails to opt\-in to EigenDA or is ejected by the Churn Approver then you may run the opt\-in command again after the rate limiting threshold has passed. The current rate limiting threshold is 5 minutes.


If you receive the error “error: failed to request churn approval .. Rate Limit Exceeded” you may retry after the threshold has passed. If you receive the error “insufficient funds”, you may increase your Operator’s delegated TVL to the required minimum and retry after the threshold has passed.


infoMore information about the registration process that is executed by the above commands can be found at the [Registration Protocol Overview](/eigenda/operator-guides/registration-protocol).


Check for network traffic[​](#check-for-network-traffic "Direct link to Check for network traffic")
---------------------------------------------------------------------------------------------------


EigenDA uses the operator state that is 75 blocks (15 minutes) behind the current chain head to ensure the state is not at risk of being reorg'd.
About 15 minutes after you have successfully opted into a quorum, you should begin to see logs indicating that your node is receiving, validating, and storing batches from the network, like the following:



```
Batch verify 1 frames of 256 symbols out of 1 blobs  
time=2024-03-22T19:34:39.858Z level=DEBUG source=/app/node/node.go:330 msg="Validate batch took" duration:=96.155565ms  
time=2024-03-22T19:34:39.858Z level=DEBUG source=/app/node/node.go:340 msg="Store batch took" duration:=0s  
time=2024-03-22T19:34:39.859Z level=DEBUG source=/app/node/node.go:346 msg="Signed batch header hash" pubkey=0x00cea342f086977a33b3f1bba57d09c6cdf8eaf20b9dec856dc874ab65414b6e2377a91ab3bc2360224f3ba071eb4753da650e957d9c0535b14922609a9ff052150595f3a89c06e87a78d3e3ebad09771f181b632bd971c1d58deb3e1fde9397087c1cc1097c48b1e900d418ef43538a8abdccde72921c3148ae4de5e0f39ef3  
time=2024-03-22T19:34:39.859Z level=DEBUG source=/app/node/node.go:349 msg="Sign batch took" duration=1.32679ms  
time=2024-03-22T19:34:39.860Z level=INFO source=/app/node/node.go:351 msg="StoreChunks succeeded"  
time=2024-03-22T19:34:39.860Z level=DEBUG source=/app/node/node.go:353 msg="Exiting process batch" duration=97.815499ms  

```

List Quorums[​](#list-quorums "Direct link to List Quorums")
------------------------------------------------------------


The following command lists the quorums the node is currently opted into.



```
./run.sh list-quorums  

```

Opt\-Out of an EigenDA Quorum[​](#opt-out-of-an-eigenda-quorum "Direct link to Opt-Out of an EigenDA Quorum")
-------------------------------------------------------------------------------------------------------------


warningPlease be careful to ensure that you only opt\-out of your current (or intended) quorum.


The following command can be used to opt out from the EigenDA AVS:



```
./run.sh opt-out <quorum>  
  
# for opting out to quorum 0:  
./run.sh opt-out 0  
  
# for opting out to quorum 0 and 1:  
./run.sh opt-out 0,1   

```
[PreviousRun with Docker](/eigenda/operator-guides/run-a-node/run-with-docker)[NextSoftware Upgrades](/eigenda/operator-guides/upgrades/software-upgrades)* [Opt\-in to an EigenDA Quorum](#opt-in-to-an-eigenda-quorum)
* [Check for network traffic](#check-for-network-traffic)
* [List Quorums](#list-quorums)
* [Opt\-Out of an EigenDA Quorum](#opt-out-of-an-eigenda-quorum)


* 
* Operator Guides
* [Run a Node](/eigenda/operator-guides/run-a-node/)
* Run with Docker
On this pageRun a node using docker
=======================


We provide an Operator Setup Repository which contains various templates that make it easy to run an EigenDA node using docker and docker compose. Operators wishing to make use of other setups can use the docker\-compose\-based setup as a template for constructing their own custom setups.


To proceed with these instructions, be sure to ensure that you have installed docker on your system.


* [Docker Engine on Linux](https://docs.docker.com/engine/install/ubuntu/).


EigenDA Node Configuration[​](#eigenda-node-configuration "Direct link to EigenDA Node Configuration")
------------------------------------------------------------------------------------------------------


#### Clone the Oprator Setup Repo and populate the environment variables[​](#clone-the-oprator-setup-repo-and-populate-the-environment-variables "Direct link to Clone the Oprator Setup Repo and populate the environment variables")


Run the following commands to clone the Oprator Setup Repo and create a new environment file from the provided template.
The `srs_setup.sh` script will also download the (\~8GB) structured reference string (SRS) used by the EigenDA node as part of its KZG verification to the `eigenda-operator-setup/resources` directory.


* Mainnet
* Holesky


```
git clone https://github.com/Layr-Labs/eigenda-operator-setup.git  
cd eigenda-operator-setup && ./srs_setup.sh  
cd mainnet && cp .env.example .env  

```

```
git clone https://github.com/Layr-Labs/eigenda-operator-setup.git  
cd eigenda-operator-setup && ./srs_setup.sh  
cd holesky && cp .env.example .env  

```

The provided `.env` contains many default configuration settings for the node. All sections marked with `TODO` must be updated to match your environment. We recommend that operators follow the steps in the next section to configure their node to run without access to their ECDSA private key.


infoAs described [here](/eigenda/operator-guides/run-a-node/registration), the ECDSA and BLS keys needed to populate your `.env` can be obtained via the process of registering as an operator for EigenLayer.


warningDo not modify the docker\-compose.yml file. If you choose to modify this file, unexpected behaviors can result.


#### Configure local storage locations[​](#configure-local-storage-locations "Direct link to Configure local storage locations")


Check that the `$USER_HOME`, `$EIGENLAYER_HOME`, `$EIGENDA_HOME` are properly set within your environment file and that all the folders exist as expected.



```
source .env  
ls $USER_HOME $EIGENLAYER_HOME $EIGENDA_HOME  

```

By default, the EigenDA node will use the following locations for log storage and blob shard storage, respectively.



```
NODE_LOG_PATH_HOST=${EIGENDA_HOME}/logs  
NODE_DB_PATH_HOST=${EIGENDA_HOME}/db  

```

Ensure that these locations correspond to high performance SSD storage with sufficient capaicity, as indicated in the [System Requirements](/eigenda/operator-guides/requirements/system-requirements#node-storage-requirements). Also ensure that the specific folders exist that the docker user has the correct write permissions:



```
mkdir -p ${NODE_LOG_PATH_HOST}  
mkdir -p ${NODE_DB_PATH_HOST}  

```

Note: The default environment setup assumes that you have cloned the `eigend-operator-setup` repo to the `$USER_HOME` directory, and the node will look in this location for several files necessary for operation:



```
NODE_G1_PATH_HOST=${USER_HOME}/eigenda-operator-setup/resources/g1.point  
NODE_G2_PATH_HOST=${USER_HOME}/eigenda-operator-setup/resources/g2.point.powerOf2  
NODE_CACHE_PATH_HOST=${USER_HOME}/eigenda-operator-setup/resources/cache  

```

#### (Recommended) Set up your your node to run without access to operator ECDSA keys[​](#recommended-set-up-your-your-node-to-run-without-access-to-operator-ecdsa-keys "Direct link to (Recommended) Set up your your node to run without access to operator ECDSA keys")


In [EigenDA v0\.6\.1](https://github.com/Layr-Labs/eigenda-operator-setup/releases/tag/v0.6.1), we added a feature where you can configure your node so that it doesn't need operator's ECDSA keys to run.
Your node still need access to BLS keys for attestation purposes.



> ***NOTE:*** You still need ECDSA and BLS keys to opt\-in to EigenDA.


To enable this feature by using our setup, follow the below commands:


* Remove the `"${NODE_ECDSA_KEY_FILE_HOST}:/app/operator_keys/ecdsa_key.json:readonly"` mount from `docker-compose.yml` file.
* Update the `NODE_ECDSA_KEY_FILE` in your `.env` file to be empty.
* Update the `NODE_ECDSA_KEY_PASSWORD` in your `.env` file to be empty.
* Update the `NODE_PUBLIC_IP_CHECK_INTERVAL` in your `.env` file to be `0` (This flag was used to check and update your IP onchain if your IP changes, so if your IP changes it's your responsibility to update).


Network Configuration[​](#network-configuration "Direct link to Network Configuration")
---------------------------------------------------------------------------------------


The EigenDA node must be properly reachable by various parties in order to fulfill its responsibilities to store and serve data.


### Retrieval Setup[​](#retrieval-setup "Direct link to Retrieval Setup")


In order for users to retrieve data from your node, you will need to open access to retrieval ports.


Ensure the port specified as `NODE_RETRIEVAL_PORT` in the `.env` has open access to the public internet.


Note that in the default setup this port is served by an NGINX reverse proxy that implements basic rate limitting to provide a level of protection against DoS attacks. If you decide to run a custom setup, you should replicate these protections using your own infrastructure.


### Dispersal Setup[​](#dispersal-setup "Direct link to Dispersal Setup")


warningIt is important to follow the instructions in this setup to keep your node from being vulnerable to DOS attacks.


The port specified as `NODE_DISPERSAL_PORT` in the `.env` should only be reachable by the EigenLabs hosted disperser.


Please configure the firewall, security groups, or other network settings so that this port can only be reached from the following IP addresses:


* Mainnet
* Holesky

* `3.216.127.6/32`
* `3.225.189.232/32`
* `52.202.222.39/32`
* `54.144.24.178/32`
* `34.232.117.230/32`
* `18.214.113.214/32`

Run the Node[​](#run-the-node "Direct link to Run the Node")
------------------------------------------------------------


### Start and Stop the EigenDA using Docker Compose[​](#start-and-stop-the-eigenda-using-docker-compose "Direct link to Start and Stop the EigenDA using Docker Compose")


Execute the following command to start the docker containers:



```
docker compose up -d  

```

The command will start the node and nginx containers and if you do `docker ps` you should see an output indicating all containers have status of “Up” with ports assigned.


To stop the node, run the following command.



```
docker compose down  

```

warningOnce you have [registered for a quorum](/eigenda/operator-guides/run-a-node/registration/), you must keep your node running until you have deregistered and satisfied all requirements of the [protocol SLA](/eigenda/operator-guides/requirements/protocol-SLA/)


### View the EigenDA Logs[​](#view-the-eigenda-logs "Direct link to View the EigenDA Logs")


You may view the container logs using and of the following commands



```
docker compose logs -f  
docker compose logs -f <container_name>  
docker logs -f <container_id>  

```

Upon successfully starting up, the DA node should produce logs similar to the following:



```
2024/03/22 19:33:28 maxprocs: Leaving GOMAXPROCS=16: CPU quota undefined  
2024/03/22 19:33:30 Initializing Node  
time=2024-03-22T19:33:34.503Z level=DEBUG source=/app/core/eth/tx.go:791 msg=Addresses blsOperatorStateRetrieverAddr=0xB4baAfee917fb4449f5ec64804217bccE9f46C67 eigenDAServiceManagerAddr=0xD4A7E1Bd8015057293f0D0A557088c286942e84b registryCoordinatorAddr=0x53012C69A189cfA2D9d29eb6F19B32e0A2EA3490 blsPubkeyRegistryAddr=0x066cF95c1bf0927124DFB8B02B401bc23A79730D  
2024/03/22 19:33:34     Reading G1 points (4194304 bytes) takes 5.981866ms  
2024/03/22 19:33:37     Parsing takes 3.144064399s  
numthread 8  
time=2024-03-22T19:33:38.141Z level=INFO source=/go/pkg/mod/github.com/!layr-!labs/[[email protected]](/cdn-cgi/l/email-protection)/metrics/eigenmetrics.go:81 msg="Starting metrics server at port :9092"  
time=2024-03-22T19:33:38.141Z level=INFO source=/app/node/node.go:174 msg="Enabled metrics" socket=:9092  
time=2024-03-22T19:33:38.141Z level=INFO source=/go/pkg/mod/github.com/!layr-!labs/[[email protected]](/cdn-cgi/l/email-protection)/nodeapi/nodeapi.go:104 msg="Starting node api server at address :9091"  
time=2024-03-22T19:33:38.141Z level=INFO source=/app/node/node.go:178 msg="Enabled node api" port=9091  
time=2024-03-22T19:33:38.141Z level=INFO source=/app/node/node.go:211 msg="The node has successfully started. Note: if it's not opted in on https://app.eigenlayer.xyz/avs/eigenda, then please follow the EigenDA operator guide section in docs.eigenlayer.xyz to register"  
time=2024-03-22T19:33:38.141Z level=INFO source=/go/pkg/mod/github.com/!layr-!labs/[[email protected]](/cdn-cgi/l/email-protection)/nodeapi/nodeapi.go:238 msg="node api server running" addr=:9091  
time=2024-03-22T19:33:38.141Z level=INFO source=/app/node/node.go:385 msg="Start checkRegisteredNodeIpOnChain goroutine in background to subscribe the operator socket change events onchain"  
time=2024-03-22T19:33:38.142Z level=INFO source=/app/node/node.go:231 msg="Start expireLoop goroutine in background to periodically remove expired batches on the node"  
time=2024-03-22T19:33:38.142Z level=INFO source=/app/node/node.go:408 msg="Start checkCurrentNodeIp goroutine in background to detect the current public IP of the operator node"  
time=2024-03-22T19:33:38.142Z level=INFO source=/app/node/grpc/server.go:123 msg=port 32004=address [::]:32004="GRPC Listening"  
time=2024-03-22T19:33:38.142Z level=INFO source=/app/node/grpc/server.go:99 msg=port 32005=address [::]:32005="GRPC Listening"  

```
[PreviousRun a node](/eigenda/operator-guides/run-a-node/)[NextRegister Your Operator](/eigenda/operator-guides/run-a-node/registration)* [EigenDA Node Configuration](#eigenda-node-configuration)
* [Network Configuration](#network-configuration)
	+ [Retrieval Setup](#retrieval-setup)
	+ [Dispersal Setup](#dispersal-setup)
* [Run the Node](#run-the-node)
	+ [Start and Stop the EigenDA using Docker Compose](#start-and-stop-the-eigenda-using-docker-compose)
	+ [View the EigenDA Logs](#view-the-eigenda-logs)


* 
* Operator Guides
* Troubleshooting
On this pageTroubleshooting
===============


#### Where do I check if my operator is a part of EigenDA set?[​](#where-do-i-check-if-my-operator-is-a-part-of-eigenda-set "Direct link to Where do I check if my operator is a part of EigenDA set?")


You can search using the below EigenLayer webapp links:


* [Holesky](https://holesky.eigenlayer.xyz/avs/eigenda)


#### I opted in into running EigenDA but I am not in the operator set anymore. What happened?[​](#i-opted-in-into-running-eigenda-but-i-am-not-in-the-operator-set-anymore-what-happened "Direct link to I opted in into running EigenDA but I am not in the operator set anymore. What happened?")


Either you are [churned out](/eigenda/operator-guides/requirements/delegation-requirements#have-i-been-churned) by another operator or you have been [ejected due to non\-signing](/eigenda/operator-guides/requirements/protocol-SLA/).
If neither of these reasons apply, please reach out to EigenLayer Support


#### How do I know if my node is signing EigenDA blobs correctly?[​](#how-do-i-know-if-my-node-is-signing-eigenda-blobs-correctly "Direct link to How do I know if my node is signing EigenDA blobs correctly?")


There are few ways you can confirm that your node is signing the blobs


* Ensure that you have monitoring setup according to the
[guide](/eigenda/operator-guides/metrics-and-monitoring/). Once you have added the provided
EigenDA Grafana dashboards, take a look at the graph saying **EigenDA number
of processed batches**. This graph should be increasing like below graph:


![EigenDA correct sign](/assets/images/eigenda-correct-sign-1051b9911688742947c4fa227844997a.png)


* If you have not setup metrics yet, you can still check the logs of your
EigenDA Node. If you are signing correctly, your logs should resemble those shown [here](/eigenda/operator-guides/run-a-node/registration#check-for-network-traffic)


#### Errors while opting in into EigenDA[​](#errors-while-opting-in-into-eigenda "Direct link to Errors while opting in into EigenDA")


##### failed to request churn approval[​](#failed-to-request-churn-approval "Direct link to failed to request churn approval")



```
Error: failed to opt-in EigenDA Node Network for operator ID: <OPERATOR_ID>, operator address: <OPERATOR_ADDRESS>, error: failed to request churn approval: rpc error: code = Unknown desc = failed to process churn request: registering operator must have 10.000000% more than the stake of the lowest-stake operator. Stake of registering operator: 0, stake of lowest-stake operator: 6301801525718228411481, quorum ID: 0  

```

This is because your operator doesn't have enough stake to run EigenDA. Please refer to [EigenDA Churn Management](/eigenda/operator-guides/requirements/delegation-requirements#have-i-been-churned) to learn more about this error.


##### failed to read or decrypt the BLS/ECDSA private key[​](#failed-to-read-or-decrypt-the-blsecdsa-private-key "Direct link to failed to read or decrypt the BLS/ECDSA private key")


Please make sure that the `NODE_ECDSA_KEY_FILE_HOST` and `NODE_BLS_KEY_FILE_HOST` variables in the `.env`
file are correctly populated.


#### My EigenDA node's logs look like these. What does it mean?[​](#my-eigenda-nodes-logs-look-like-these-what-does-it-mean "Direct link to My EigenDA node's logs look like these. What does it mean?")



```
INFO [01-10|20:49:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|20:52:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|20:55:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|20:58:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|21:01:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|21:04:53.437|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|21:07:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|21:10:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|21:13:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  
INFO [01-10|21:16:53.436|github.com/Layr-Labs/eigenda/node/node.go:233]             Complete an expiration cycle to remove expired batches "num expired batches found and removed"=0 caller=node.go:233  

```

These logs only contain intermittent INFO logs and they do not contain instances of logs that indicate your node is actively receiving new blobs from the Dispser. Healthy log files would include messages such as "Validate batch took", "Store batch took", "Signed batch header hash".


This means you node software is running but you are not opted\-in into EigenDA.
If you opted in into EigenDA successfully and still not receiving dispersal
traffic, make sure your network settings allow EigenDA's disperser to reach your
node. Please check that your network settings match the [prescribed settings](/eigenda/operator-guides/run-a-node/run-with-docker#network-configuration).


If you were previously opted\-in and were signing, it's possible you were [churned
out](/eigenda/operator-guides/requirements/delegation-requirements#have-i-been-churned) by another operator or you have been
[ejected due to non\-signing or other SLA violations](/eigenda/operator-guides/requirements/protocol-SLA/). Please try opting\-in
again.


#### What does the error "EIP1271 .. signature not from signer" mean?[​](#what-does-the-error-eip1271--signature-not-from-signer-mean "Direct link to What does the error \"EIP1271 .. signature not from signer\" mean?")


This indicates you have not imported your BLS key correctly. Please reconfirm the keys you imported to ensure there were no typos or mistakes.


#### Error message "failed to update operator's socket .. execution reverted"[​](#error-message-failed-to-update-operators-socket--execution-reverted "Direct link to Error message \"failed to update operator's socket .. execution reverted\"")


"msg\="failed to update operator's socket" !BADKEY\="execution reverted: RegistryCoordinator.updateSocket: operator is not registered"


This indicates the RPC endpoint may not be functioning correctly, or the operator config is misconfigured (eg pointing to the wrong chain\_id value), or the operator is not registered.


Please test your RPC endpoint via the following command `curl -I [rpc_url]`.


* A 400 series response indicates the server is down (unreachable).
* A 200 series response indicates the server is available and working properly.
[PreviousMetrics and Monitoring](/eigenda/operator-guides/metrics-and-monitoring)[NextFAQ](/eigenda/operator-guides/operator-faq)

* 
* Operator Guides
* Upgrade your Node
* Software Upgrades
On this pageSoftware Upgrades
=================


Please monitor the following channels for updates to EigenDA Operator software:


* [EigenLayer Discord](https://discord.gg/eigenlayer): \#support\-operators channel.
* [EigenDA Operator Setup](https://github.com/Layr-Labs/eigenda-operator-setup) repository: [configure your watch settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository) for notifications of new releases.


If you are running your node using docker compose, you can perform an upgrade by following the steps below:


#### Step 1: Pull the latest repo[​](#step-1-pull-the-latest-repo "Direct link to Step 1: Pull the latest repo")


* Mainnet
* Holesky


```
cd eigenda-operator-setup/mainnet  
git pull  

```

```
cd eigenda-operator-setup/holesky  
git pull  

```

Update the `MAIN_SERVICE_IMAGE` in your `.env` file with the latest EigenDA version as per the release notes.


infoIf there are any specific instructions that needs to be followed for any upgrade, those instructions will be given with the release notes of the specific release. Please check the latest [release notes](https://github.com/Layr-Labs/eigenda-operator-setup/releases) on GitHub and follow the instructions before starting the services again.


#### Step 2: Pull the latest docker images[​](#step-2-pull-the-latest-docker-images "Direct link to Step 2: Pull the latest docker images")



```
docker compose pull  

```

#### Step 3: Stop the existing services[​](#step-3-stop-the-existing-services "Direct link to Step 3: Stop the existing services")



```
docker compose down  

```

#### Step 4: Start your services again[​](#step-4-start-your-services-again "Direct link to Step 4: Start your services again")


Make sure your `.env` file still has correct values in the `TODO` sections before you restart your node.



```
docker compose up -d  

```
[PreviousRegister Your Operator](/eigenda/operator-guides/run-a-node/registration)[NextSystem Upgrades](/eigenda/operator-guides/upgrades/system-upgrades)

* 
* Operator Guides
* Upgrade your Node
* System Upgrades
On this pageSystem Upgrades
===============


Since system requirements scale dynamically in accordance with the amount of stake delegated to the operator, node operators may from time to time need to upgrade their system setups in order to continue meeting the [Protocol SLA](/eigenda/operator-guides/requirements/protocol-SLA/)


When performing a system upgrade, operators should be mindful of the following considerations:


* Maintain custody of BLS signing keys.
* Ensure that the upgraded node remains reachable at the previously registered address.
* Maintain the integrity of all blob data stored by the node.


Node migration[​](#node-migration "Direct link to Node migration")
------------------------------------------------------------------


If you followed the setup steps in our guide to [running with docker](/eigenda/operator-guides/run-a-node/run-with-docker/), then your node will store its data at the location specified by the `NODE_DB_PATH_HOST` in your `.env` file, which is bind\-mounted to the EigenDA docker container.


Generally speaking, suppose you want to migrate node to a new machine, you should follow the following sequence in order to maintain data integrity and remain meeting the [Protocol SLA](/eigenda/operator-guides/requirements/protocol-SLA/) during and after the migration:


**Old machine**:


1. Backup the keys stored at the machine as well as other configs you want to migrate
2. Opt\-out of all the quorums
3. Keep the node running for \>1h (note after this the node will stop receiving dispersal requests)
4. Continue to keep the node running (for retrieval traffic) while spinning up the new machine


**New machine**:


1. Copy over the files from old machine located at `NODE_DB_PATH_HOST`
2. Start the EigenDA Node (e.g. `docker-compose up -d`) with the files copied from the old machine (the file should be placed under the path per `NODE_DB_PATH_HOST`) and make sure node is reachable
3. Opt\-in the quorums with a new IP address (so the old machine remains reachable with original IP while this is setting up). If you are registering with DNS, you need to repoint the DNS to the new IP and then opt\-in the quorums.


Lastly, when the new node is working for both retrieval and dispersal, you can turn down the node at old machine (e.g. `docker-compose down`).

[PreviousSoftware Upgrades](/eigenda/operator-guides/upgrades/software-upgrades)[NextMetrics and Monitoring](/eigenda/operator-guides/metrics-and-monitoring)* [Node migration](#node-migration)


* 
* EigenDA Overview
On this pageEigenDA Overview
================

EigenDA is a data availability store made by
[EigenLabs](https://www.eigenlabs.org/) and built on top of
[EigenLayer](/eigenlayer/overview/), currently on mainnet since Q2 2024\.
It is also available on Holesky testnet for testing and development purposes.


EigenDA stores rollup transactions until their computed state is
finalized on the rollup bridge, and is...


* **Scalable.** EigenDA write throughput scales linearly with number of
operators. At launch EigenDA will provide 10 MB/s of write throughput. This is
5x greater than the nearest competitor.
* **Secure.** EigenDA is decentralized, and made up of hundreds of operators
registered in EigenLayer whose delegated stake imposes an economic cost to
misbehavior. EigenDA will have billions of dollars of economic security at
launch.
* **Decentralized.** EigenDA's design is inspired by Danksharding, which
promises to scale Ethereum\-native DA beyond EIP\-4844\. EigenDA blob writes are
registered with contracts on Ethereum, which natively subject operators to
certain slashing risks. Ethereum L2s using EigenDA avoid any trust assumption on
another chain's light client, which can be fooled by dishonest validator sets.


How EigenDA Works[​](#how-eigenda-works "Direct link to How EigenDA Works")
---------------------------------------------------------------------------


The core insight of EigenDA is that the problem of data availability does not
require independent consensus to solve. In building a decentralized transient
data store for Ethereum rollups, Ethereum can be used for aspects of
coordination required, and data storage can be handled by EigenDA operators
directly.


This approach gives EigenDA the ability to scale linearly. In the context of an
L1 blockchain, increasing throughput means either increasing block size or
decreasing block times. Beyond a certain point, increases in scalability come at
the cost of security or decentralization (see "blockchain trilemma"). One way
around this trilemma is through an emphasis on L2s, where DA can be moved
off\-chain such that transaction data need not be replicated to every node.
Instead, only DA metadata and accountability processes are processed on\-chain.
This enables DA to scale with respect to the bandwidth of the operator set.


EigenDA works on the basis of three components:


* Operators
* The Disperser (untrusted)
* Retrievers (untrusted)


EigenDA **operators** are third\-parties running the EigenDA node software,
registered in EigenLayer with stake delegated to them. EigenDA operators are
responsible for storing blobs associated with valid storage requests. Valid
storage requests are requests where fees are paid and the provided blob chunk
verifies against the provided KZG commitment and proof. In the case of a
successful verification the operator stores the blob and signs a message with
the KZG commitment and the chunk index they hold, and sends it back to the
disperser. EigenDA operators are collectively trusted – when writing a blob to
EigenDA clients must choose the exact threshold of stake with which they would
like their blob to be stored.


The EigenDA **disperser** is an untrusted service hosted by EigenLabs which is
responsible for interfacing between EigenDA clients, operators, and contracts.
EigenDA clients make dispersal requests to the disperser, which Reed\-Solomon
encodes the blob, calculates the encoded blob's KZG commitment, and generates a
KZG proof for each chunk. Then the disperser sends chunks, KZG commitment, and
KZG proofs to operators, who return signatures. The disperser then aggregates
these signatures and uploads it to Ethereum in the form of calldata to the
EigenDA contract. This step is a necessary precondition for slashing operators
for misbehavior.


The EigenDA **retriever** is a service that queries EigenDA operators for blob
chunks, verifies that blob chunks are accurate, and reconstructs the original
blob for the user. EigenDA hosts a retriever service but client rollups may also
host their own retriever as a sidecar to their sequencer.


### How Rollups Integrate[​](#how-rollups-integrate "Direct link to How Rollups Integrate")


![EigenDA Architecture](/assets/images/dispersal-flow-diagram-88b58ad56352c51660e19e8435f89e4a.png)


The diagram above shows the basic flow of data through EigenDA:


1. The rollup sequencer sends a batch of transactions as a blob to the EigenDA
disperser sidecar.
2. The EigenDA disperser sidecar erasure encodes the blob into chunks, generates a KZG
commitment and multi\-reveal proofs for each chunk, and disperses chunks to
EigenDA Operators, receiving signatures certifying storage in return.
3. After aggregating the received signatures, the disperser registers the blob
onchain by sending a transaction to the EigenDA Manager contract with the
aggregated signature and blob metadata.
4. The EigenDA Manager contract verifies the aggregated signature with the help
of the EigenDA Registry contract, and stores the result onchain.
5. Once the blob has been stored offchain and registered onchain, the
sequencer posts the EigenDA blob ID to its inbox contract in a transaction. A
blob ID is no more than 100 bytes long.
6. Before accepting the blob ID into the rollup's inbox, the inbox contract
consults the EigenDA manager contract on whether blob was certified available.
If it was, the blob ID is allowed into the inbox contract. If not, the blob ID
is discarded.


For more on how rollups integrate with EigenDA, check out [Integrations Overview](/eigenda/integrations-guides/rollup-guides/integrations-overview).

[NextQuick Start](/eigenda/integrations-guides/dispersal/quick-start)* [How EigenDA Works](#how-eigenda-works)
	+ [How Rollups Integrate](#how-rollups-integrate)


* 
* AVS Developer Guides
* AVS Dashboard Onboarding
On this pageAVS Dashboard Onboarding
========================

This document defines interfaces that AVSs must implement for us to be able to index their data for the V1 [AVS Marketplace](https://app.eigenlayer.xyz/avs).


New AVS Listings: in order for an AVS to have its name, information, and logo indexed, it must invoke `updateAVSMetadataURI()` on the [AVSDirectory contract](https://github.com/Layr-Labs/eigenlayer-contracts/blob/dev/src/contracts/core/AVSDirectory.sol).
It currently takes about 10 minutes for it to be indexed and the metadata to be updated on the dashboard.


Updating AVS Listings: if you deploy a new contract for a new version of your AVS, please be sure to remove the previous listing. Invoke the update metadata function with value of null, such as `updateAVSMetadataURI("")` to remove the previous listing. Your listing will then be removed from the application cache within one hour.


Interface[​](#interface "Direct link to Interface")
---------------------------------------------------



```
interface IServiceManager {  
// Below 3 functions are just proxies to the same-named functions in the AVSDirectory  
function registerOperatorToAVS(address operator, Signature memory signature);  
  
function deregisterOperatorFromAVS(address operator);  
  
function updateAVSMetadataURI(string calldata metadataURI);  
	  
// Below 2 functions are needed for your AVS to appear correctly on the UI  
function getOperatorRestakedStrategies(address operator) returns (address[] memory)  
  
function getRestakeableStrategies() returns (address[] memory);  
}  

```

### registerOperatorToAVS and deregisterOperatorFromAVS[​](#registeroperatortoavs-and-deregisteroperatorfromavs "Direct link to registerOperatorToAVS and deregisterOperatorFromAVS")


In order to have its list of operators displayed on the UI, an AVS MUST handle operator registration/deregistration by calling `registerOperatorToAVS()` and `deregisterOperatorFromAVS()` on EigenLayer’s AVSDirectory. Primarily, these functions serve to forward calls to the `AVSDirectory.sol` contract to confirm an operator's registration with the AVS.



```
function registerOperatorToAVS(  
        address operator,  
        ISignatureUtils.SignatureWithSaltAndExpiry memory operatorSignature  
    ) public virtual onlyRegistryCoordinator {  
        avsDirectory.registerOperatorToAVS(operator, operatorSignature);  
    }  
  
function deregisterOperatorFromAVS(address operator) public virtual onlyRegistryCoordinator {  
        avsDirectory.deregisterOperatorFromAVS(operator);  
    }  

```

### getOperatorRestakedStrategies[​](#getoperatorrestakedstrategies "Direct link to getOperatorRestakedStrategies")


This function must be implemented in order to provide the list of strategies that an operator has restaked with the AVS. This allows the AVS to have its total restaked value displayed on the UI. Given an operator, this function should:


* Retrieve the operator's quorum bitmap from the `RegistryCoordinator.sol` contract.
* Retrieve the addresses of the strategies for each quorum in the quorum bitmap


Note that there is no guarantee is made on whether the operator has shares for a strategy in a quorum or uniqueness of each element in the returned array. The off\-chain service should do that validation separately



```
function getOperatorRestakedStrategies(address operator) external view returns (address[] memory) {  
        bytes32 operatorId = registryCoordinator.getOperatorId(operator);  
        uint192 operatorBitmap = registryCoordinator.getCurrentQuorumBitmap(operatorId);  
  
        if (operatorBitmap == 0 || registryCoordinator.quorumCount() == 0) {  
            return new address[](0);  
        }  
  
        // Get number of strategies for each quorum in operator bitmap  
        bytes memory operatorRestakedQuorums = BitmapUtils.bitmapToBytesArray(operatorBitmap);  
        uint256 strategyCount;  
        for(uint256 i = 0; i < operatorRestakedQuorums.length; i++) {  
            strategyCount += stakeRegistry.strategyParamsLength(uint8(operatorRestakedQuorums[i]));  
        }  
  
        // Get strategies for each quorum in operator bitmap  
        address[] memory restakedStrategies = new address[](strategyCount);  
        uint256 index = 0;  
        for(uint256 i = 0; i < operatorRestakedQuorums.length; i++) {  
            uint8 quorum = uint8(operatorRestakedQuorums[i]);  
            uint256 strategyParamsLength = stakeRegistry.strategyParamsLength(quorum);  
            for (uint256 j = 0; j < strategyParamsLength; j++) {  
                restakedStrategies[index] = address(stakeRegistry.strategyParamsByIndex(quorum, j).strategy);  
                index++;  
            }  
        }  
        return restakedStrategies;          
    }  

```

### getRestakeableStrategies[​](#getrestakeablestrategies "Direct link to getRestakeableStrategies")


This function must be implemented in order to have all possible restakeable strategies for that AVS displayed on the UI correctly. These are the strategies that the AVS supports for restaking.



```
function getRestakeableStrategies() external view returns (address[] memory) {  
        uint256 quorumCount = registryCoordinator.quorumCount();  
  
        if (quorumCount == 0) {  
            return new address[](0);  
        }  
          
        uint256 strategyCount;  
        for(uint256 i = 0; i < quorumCount; i++) {  
            strategyCount += stakeRegistry.strategyParamsLength(uint8(i));  
        }  
  
        address[] memory restakedStrategies = new address[](strategyCount);  
        uint256 index = 0;  
        for(uint256 i = 0; i < _registryCoordinator.quorumCount(); i++) {  
            uint256 strategyParamsLength = _stakeRegistry.strategyParamsLength(uint8(i));  
            for (uint256 j = 0; j < strategyParamsLength; j++) {  
                restakedStrategies[index] = address(_stakeRegistry.strategyParamsByIndex(uint8(i), j).strategy);  
                index++;  
            }  
        }  
        return restakedStrategies;  
    }  
  

```

Refer to [ServiceManagerBase.sol](https://github.com/Layr-Labs/eigenlayer-middleware/blob/mainnet/src/ServiceManagerBase.sol) for a reference implementation of the interface.


Proxy and Implementation addresses for AVSDirectory contract are available at EigenLayer Contracts \-\> [Deployments](https://github.com/Layr-Labs/eigenlayer-contracts/?tab=readme-ov-file#deployments).


To look at EigenDA's AVS\-specific deployment \-\> [Deployments](https://github.com/Layr-Labs/eigenlayer-middleware/tree/dev?tab=readme-ov-file#deployments)


MetadataURI Format[​](#metadatauri-format "Direct link to MetadataURI Format")
------------------------------------------------------------------------------


The metadataURI should follow the format outlined in this [example](https://holesky-operator-metadata.s3.amazonaws.com/avs_1.json). The logo MUST be in PNG format.



```
{  
    "name": "EigenLabs AVS 1",  
    "website": "https://www.eigenlayer.xyz/",  
    "description": "This is my 1st AVS",  
    "logo": "https://raw.githubusercontent.com/layr-labs/eigendata/master/avs/eigenlabs/logo.png",  
    "twitter": "https://twitter.com/eigenlayer"  
}  

```

Note that for proper rendering of your logo on the UI, the logo *must* be hosted on GitHub and its reference must point to the raw file as the example above shows. If you need a repo for your logo to be hosted publicly, you can make a PR to the `eigendata` repo and have your logo added: [https://github.com/Layr\-Labs/eigendata](https://github.com/Layr-Labs/eigendata).


Holesky Dashboard onboarding[​](#holesky-dashboard-onboarding "Direct link to Holesky Dashboard onboarding")
------------------------------------------------------------------------------------------------------------


Once you've gone through the above steps and you've called the `updateAVSMetadataURI` function, your AVS will be reflected on the Holesky dashboard in about 10 minutes.


Mainnet Dashboard onboarding[​](#mainnet-dashboard-onboarding "Direct link to Mainnet Dashboard onboarding")
------------------------------------------------------------------------------------------------------------


Prior to planning your Mainnet onboarding, please test first on testnet. If not already connected to the Eigen Labs team regarding any onboarding questions, you can get in touch with the team by filling out [this form](https://forms.gle/8BJSntA3eYUnZZgs8).

[PreviousImplementation reference](/eigenlayer/avs-guides/spec/metrics/metrics-examples)[NextAVS Developer Security Best Practices](/eigenlayer/avs-guides/avs-developer-best-practices)* [Interface](#interface)
	+ [registerOperatorToAVS and deregisterOperatorFromAVS](#registeroperatortoavs-and-deregisteroperatorfromavs)
	+ [getOperatorRestakedStrategies](#getoperatorrestakedstrategies)
	+ [getRestakeableStrategies](#getrestakeablestrategies)
* [MetadataURI Format](#metadatauri-format)
* [Holesky Dashboard onboarding](#holesky-dashboard-onboarding)
* [Mainnet Dashboard onboarding](#mainnet-dashboard-onboarding)


* 
* AVS Developer Guides
* AVS Developer Security Best Practices
On this pageAVS Developer Security Best Practices
=====================================

AVS Developer Security Best Practices[​](#avs-developer-security-best-practices "Direct link to AVS Developer Security Best Practices")
---------------------------------------------------------------------------------------------------------------------------------------


* Containers should be able to run with least privilege. Least privilege is AVS\-dependent. AVS team should outline these privileges as part of the operator onboarding docs. In the case these privileges are not specified, it’s recommended the operators ask the AVS team directly.
* Emit runtime (logs) including security events
* Use Minimal Base Images
	+ Use [ko Go containers](https://ko.build/) or similar to build distro\-less minimal images. This reduces the attack surface significantly!
* Release updated images with security patches (for base OS etc ).
* Do not store key material on the container (refer to key management docs).
* Your default user id should start with AVS\-NAME\-randomness to ensure there are no conflicts with the host.
* Ensure ECDSA keys utilized by AVS are solely for updates, such as modifying IP and port details within a smart contract. These keys should not hold funds. A role\-based approach in smart contract design can address this issue effectively.
* AVS team should [sign their images](https://docs.docker.com/engine/security/trust/) for any releases, including upgrades
	+ If they publish to Docker, Docker will show the verified badge next to the image.
	+ Tag new releases via updated images.
* Establish communication channels (Discord, TG) with operators. This ensures coordinating upgrades occurs with minimal friction.
* Operators should be in control of upgrades to their AVS software. Avoid software upgrade patterns where an agent checks for updated software and automatically upgrades the software.
* Release Notes should explain new features including breaking changes / new hardware requirements etc.


Suggested Key Management for AVSs[​](#suggested-key-management-for-avss "Direct link to Suggested Key Management for AVSs")
---------------------------------------------------------------------------------------------------------------------------


For key management, refer to the new location for the docs on [Key Security Considerations for Developers](/eigenlayer/avs-guides/key-management/middleware-developers).

[PreviousAVS Dashboard Onboarding](/eigenlayer/avs-guides/avs-dashboard-onboarding)[NextAVS Rewards](/eigenlayer/avs-guides/rewards)* [AVS Developer Security Best Practices](#avs-developer-security-best-practices)
* [Suggested Key Management for AVSs](#suggested-key-management-for-avss)


* 
* AVS Developer Guides
* AVS Overview
On this pageAVS Overview
============

Before diving into what AVSs are and how you can design and build one, check out the [Intro to EigenLayer](https://docs.eigenlayer.xyz/eigenlayer/overview/) overview to quickly become familiar with what stakers and operators are.


Also, check out the resources in **[Awesome AVS](https://github.com/Layr-Labs/awesome-avs)** for more reference architectures, tutorials, and guides.


What is an AVS?[​](#what-is-an-avs "Direct link to What is an AVS?")
--------------------------------------------------------------------


An AVS is any system that requires its own distributed validation semantics for verification, such as sidechains, data availability layers, new virtual machines, keeper networks, oracle networks, bridges, threshold cryptography schemes, trusted execution environments and more.


Each AVS has its own set of contracts that hold state relevant to the service’s functionality, such as what operators are running the service and how much stake is securing the service.


Below is a high\-level overview of EigenLayer core contracts as well as how an AVS is built on top of it and consumed.


![AVS Architecture Overview](/assets/images/avs-architecture-v1-e6f15772a975b86e146bcec3d98c9042.png)


Let’s clarify some of the interactions demonstrated by the above diagram.


* The stakers interact with EigenLayer by depositing assets into the `StrategyManager`. To learn more about exactly how this works, [this doc](https://github.com/Layr-Labs/eigenlayer-contracts/blob/master/docs/core/StrategyManager.md) provides a deep dive on the `StrategyManager`.
* The stakers also interact with EigenLayer by choosing operators to delegate to. This delegation is handled by the `DelegationManager` and you can find a deep dive explanation on that [here](https://github.com/Layr-Labs/eigenlayer-contracts/blob/master/docs/core/DelegationManager.md).
* The operators are actors who run offchain client software that are specific to the AVSs they’ve opted into serving. This client software is independent of the core EigenLayer protocol. There’s a registration/deregistration process operators have to go through with EigenLayer’s `DelegationManager` contract to become EigenLayer operators. Operator registration is a requirement for these operators to opt into AVSs and serve them. Refer to [this doc](https://docs.eigenlayer.xyz/eigenlayer/operator-guides/operator-introduction) for how registration works.
* The dotted lines for the boxes represent components that are optional depending on the interface design.
* Each AVS developer can design and implement its own contracts as they see fit as long as their entry point (canonically called the `ServiceManager`) implements the interface expected by the EigenLayer protocol. Specific details expanding on this will be coming soon.


Additional Resources[​](#additional-resources "Direct link to Additional Resources")
------------------------------------------------------------------------------------


Visit [awesome\-avs](https://github.com/Layr-Labs/awesome-avs) to view learning resources for building an AVS and the latest community contributions.


Get in Touch[​](#get-in-touch "Direct link to Get in Touch")
------------------------------------------------------------


Once you have an idea of what you want to build on EigenLayer, submit an [AVS Questionnaire](https://bit.ly/avsquestions) and get in touch with us.

[PreviousRestaking Developer Guide](/eigenlayer/restaking-guides/restaking-developer-guide)[NextBuilding an AVS](/eigenlayer/avs-guides/how-to-build-an-avs)* [What is an AVS?](#what-is-an-avs)
* [Additional Resources](#additional-resources)
* [Get in Touch](#get-in-touch)


* 
* AVS Developer Guides
* Building an AVS
On this pageBuilding an AVS
===============

Step 1: Learn EigenLayer fundamentals[​](#step-1-learn-eigenlayer-fundamentals "Direct link to Step 1: Learn EigenLayer fundamentals")
--------------------------------------------------------------------------------------------------------------------------------------


Before diving into what AVSs are and how you can design and build one, check out the [Intro to EigenLayer](https://docs.eigenlayer.xyz/eigenlayer/overview/) overview to quickly become familiar with what stakers and operators are.


Review the materials available under [EigenLayer Learning Resources](/eigenlayer/resources/learning-resources), including:


* How EigenLayer works via [You Could've Invented EigenLayer](https://www.blog.eigenlayer.xyz/ycie/).
* Understand the type of trust you would need with [The Three Pillars of Programmable Trust: The EigenLayer End Game](https://www.blog.eigenlayer.xyz/the-three-dimensions-of-programmable-trust/).


Step 2: Idea to Code: Testing and Deploying your AVS Locally[​](#step-2-idea-to-code-testing-and-deploying-your-avs-locally "Direct link to Step 2: Idea to Code: Testing and Deploying your AVS Locally")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


The following content covers the minimum set of smart contract integrations and deployment scripts that a project needs to build in order to:


1. Be considered a fully functional AVS for demo and proof of concept purposes.
2. Prepare your AVS to integrate Rewards and Slashing functionality, which will be release soon.


infoTo begin the process below, fork the example repo here [hello\-world\-avs](https://github.com/Layr-Labs/hello-world-avs).


### Smart Contract Requirements[​](#smart-contract-requirements "Direct link to Smart Contract Requirements")


**1: Integration with EigenLayer Core (AVS Directory)**  

Implement an instance of ECDSAServiceManagerBase or ServiceManagerBase (BLS).  

Please see the example from hello\-world\-avs [here](https://github.com/Layr-Labs/hello-world-avs/blob/master/contracts/src/HelloWorldServiceManager.sol) and incredible\-squaring\-avs [here](https://github.com/Layr-Labs/incredible-squaring-avs/blob/master/contracts/src/IncredibleSquaringServiceManager.sol).


**2: On Chain Verification**  

Implement at least one on\-chain provable event. The most common approach is to write a ECDSA or BLS aggregate signature (APK) on\-chain.
This will be utilized in future versions of EigenLayer for Rewards and Slashing functionality.  

Please see the example from incredible\-squaring\-avs [here](https://github.com/Layr-Labs/incredible-squaring-avs/blob/8bd0ac663dcc2289cad02af4a7f0002ea07bc1d8/contracts/src/IncredibleSquaringTaskManager.sol#L102) and from hello\-world\-avs [here](https://github.com/Layr-Labs/hello-world-avs/blob/84ae1974c212c193a3992467f7d431bad39f74a3/src/index.ts#L130).


### Contract Deployment Requirements[​](#contract-deployment-requirements "Direct link to Contract Deployment Requirements")


Implement deployment scripts for your contracts to deploy to your [local anvil node](https://book.getfoundry.sh/reference/anvil/).


**1: Deploy of EigenLayer Contracts and State**  

Please see the example from hello\-world\-avs[here](https://github.com/Layr-Labs/hello-world-avs/blob/master/utils/anvil/deploy-eigenlayer-save-anvil-state.sh).


**2: Deploy your AVS contracts**  

Please see the example forge deployment script from hello\-world\-avs [here](https://github.com/Layr-Labs/hello-world-avs/blob/master/contracts/script/HelloWorldDeployer.s.sol) and bash deployment script [here](https://github.com/Layr-Labs/hello-world-avs/blob/master/utils/anvil/deploy-eigenlayer-save-anvil-state.sh).


### Operator (Off\-Chain) Requirements[​](#operator-off-chain-requirements "Direct link to Operator (Off-Chain) Requirements")


**1: Operator Registration to AVS**  

Provide a mechanism for the Operator register to the AVS.


Please see the example from hello\-world\-avs [here](https://github.com/Layr-Labs/hello-world-avs/blob/84ae1974c212c193a3992467f7d431bad39f74a3/src/index.ts#L41).


**2: At least one event written to your AVSs on chain contracts**  

The Operator binary (or off chain aggregation service code) must write at least one event to the AVSs on chain contracts to be used for future on\-chain verification, rewards, and slashing purposes.


Please see the example from hello\-world\-avs [here](https://github.com/Layr-Labs/hello-world-avs/blob/84ae1974c212c193a3992467f7d431bad39f74a3/src/index.ts#L25).


Step 3: Preparing and Deploying to Testnet[​](#step-3-preparing-and-deploying-to-testnet "Direct link to Step 3: Preparing and Deploying to Testnet")
-----------------------------------------------------------------------------------------------------------------------------------------------------


1. Package the Operator’s long running executable in a way that is easy for Operators to launch (via binary, docker container, or similar).
2. Author Testnet user and Operator documentation, including:


	* Trust Modeling: clarify any trust assumptions in your architecture to your users. Identify the components that are trusted (centralized) and untrusted (decentralized, trustless).
	* Operator instructions to install, register, deregister.
	* End user (aka “Consumer”) instructions to utilize your AVS service.
	* Communication channels that will be utilized for AVS upgrades.
	* Describe Operator monitoring tooling available, such as GraFana dashboards, log files or similar.
3. Follow the [AVS Developer Security Best Practices](/eigenlayer/avs-guides/avs-developer-best-practices).
4. Follow the guidance in [Key Manage Considerations for Developers](/eigenlayer/avs-guides/key-management/middleware-developers).
5. Implement the [Node Specification](https://docs.eigenlayer.xyz/eigenlayer/avs-guides/spec/intro) for your Operator executable package.
6. Follow the [Testnet Dashboard Onboarding instructions](https://docs.eigenlayer.xyz/eigenlayer/avs-guides/avs-dashboard-onboarding).


Step 4: Preparing and Deploying to Mainnet[​](#step-4-preparing-and-deploying-to-mainnet "Direct link to Step 4: Preparing and Deploying to Mainnet")
-----------------------------------------------------------------------------------------------------------------------------------------------------


1. Smart Contract Auditing: have your codebase audited with at least 2\-3 reputable audit firms.
2. Finalize User and Operator documentation.
3. Follow the [Mainnet Dashboard Onboarding instructions](https://docs.eigenlayer.xyz/eigenlayer/avs-guides/avs-dashboard-onboarding).


Get in Touch[​](#get-in-touch "Direct link to Get in Touch")
------------------------------------------------------------


Once you have an idea of what you want to build on EigenLayer, submit an [AVS Questionnaire](https://bit.ly/avsquestions) and get in touch with us.

[PreviousAVS Overview](/eigenlayer/avs-guides/avs-developer-guide)[NextIncredible Squaring](/eigenlayer/avs-guides/incredible-squaring)* [Step 1: Learn EigenLayer fundamentals](#step-1-learn-eigenlayer-fundamentals)
* [Step 2: Idea to Code: Testing and Deploying your AVS Locally](#step-2-idea-to-code-testing-and-deploying-your-avs-locally)
	+ [Smart Contract Requirements](#smart-contract-requirements)
	+ [Contract Deployment Requirements](#contract-deployment-requirements)
	+ [Operator (Off\-Chain) Requirements](#operator-off-chain-requirements)
* [Step 3: Preparing and Deploying to Testnet](#step-3-preparing-and-deploying-to-testnet)
* [Step 4: Preparing and Deploying to Mainnet](#step-4-preparing-and-deploying-to-mainnet)
* [Get in Touch](#get-in-touch)


* 
* AVS Developer Guides
* Incredible Squaring
On this pageIncredible Squaring
===================

What is Incredible Squaring?[​](#what-is-incredible-squaring "Direct link to What is Incredible Squaring?")
-----------------------------------------------------------------------------------------------------------


[Incredible Squaring](https://github.com/Layr-Labs/incredible-squaring-avs) is a demo of a minimum viable AVS with full Eigenlayer integration. The purpose of this demo is to illustrate how a value computed offchain (in this case, the square of a number) can be constructed as part of the work operators have signed up to perform as well as how this business logic relates to the AVS contracts. We take the offchan computation, have it signed by multiple Operators, then aggregate the Operators signatures, before finally validating and writing the value onchain. For a video walkthrough please see:
Incredible Squaring [Overall 5 min Walk\-Through](https://www.loom.com/share/50314b3ec0f34e2ba386d45724602d76?sid=cf176400-fdbb-4bdc-8563-22a68414985d)
Incredible Squaring [TaskManager 5 min Walk\-Through](https://www.loom.com/share/5f3f2a447bc54ffa9d37d203c32088de?sid=0f5c2c07-82c5-4640-bc6f-6e4327bb3d81)


Prior to the AVS becoming available for use, the following prerequisite steps must occur:


1. Operators register with the EigenLayer [DelegationManager](https://github.com/Layr-Labs/eigenlayer-middleware/blob/6a7a38593f466b1fefd2b575fb0d4f96520a946d/src/ServiceManagerBase.sol#L24) contract.
2. Incredible Squaring AVS is deployed and registered to an implementation of the [AVSDirectory contract](https://github.com/Layr-Labs/eigenlayer-middleware/blob/6a7a38593f466b1fefd2b575fb0d4f96520a946d/src/ServiceManagerBase.sol#L24).
3. Operators register with the AVS through its RegistryCoordinator.


Incredible Squaring AVS Lifecycle (Flow)[​](#incredible-squaring-avs-lifecycle-flow "Direct link to Incredible Squaring AVS Lifecycle (Flow)")
----------------------------------------------------------------------------------------------------------------------------------------------


Each request for a number to be squared, goes through the following lifecycle (flow)


1. The Task Generator entity sends the number to be squared to the AVS contract (IncredibleSquaringTaskManager.sol).
2. AVS contract emits an event (NewTaskCreated) to represent the new number to be squared.
3. Operators listen to the AVS contract for the event, square the number, sign the result with a [BLS signature](https://eth2book.info/capella/part2/building_blocks/signatures/) and send their signature to the Aggregator entity.
4. The Aggregator combines each into a single aggregated signature using [BLS signature aggregation](https://eth2book.info/capella/part2/building_blocks/signatures/#aggregation). Once the quorum threshold is met the Aggregator sends the aggregated signature back to the AVS contract.
5. AVS contract verifies that the quorum thresholds were met and that the aggregated signature is valid. If so, the squared number is accepted.


Note the [Incredible Squaring repo](https://github.com/Layr-Labs/incredible-squaring-avs) includes specific links to source code files for additional information.


Incredible Squaring Architecture Unique Characteristics[​](#incredible-squaring-architecture-unique-characteristics "Direct link to Incredible Squaring Architecture Unique Characteristics")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


The Incredible Squaring architecture includes the following components that are unique to its architecture, but not required for all AVSs:


1. BLS signature aggregation is used for aggregation of the Operator response (signatures). An [ECDSA version](https://github.com/Layr-Labs/incredible-squaring-avs/pull/20) is also available for testing (beta).
2. Task Generator: on\-chain task generation was used for Incredible Squaring, however other AVSs may choose to implement off\-chain task generation. Please see [EigenDA repo](https://github.com/Layr-Labs/eigenda?tab=readme-ov-file#overview) as an example of an off\-chain AVS.
3. Aggregator: an entity created to collect the signatures from the operators and aggregate them using BLS aggregation.
4. Centralized entities: the Aggregator, Task Generator entities are centralized in the Incredible Squaring demo. However, decentralizing each component of your architecture over time could be explored
5. RegistryCoordinator contract implementation: unique implementation of [BLSRegistryCoordinatorWithIndices](https://github.com/Layr-Labs/eigenlayer-middleware/blob/master/src/BLSRegistryCoordinatorWithIndices.sol) that allows any EigenLayer operator with at least 1 delegated mockerc20 token to opt\-in.


BLS vs ECDSA Use Cases within EigenLayer AVSs[​](#bls-vs-ecdsa-use-cases-within-eigenlayer-avss "Direct link to BLS vs ECDSA Use Cases within EigenLayer AVSs")
---------------------------------------------------------------------------------------------------------------------------------------------------------------


[BLS (Boneh\-Lynn\-Shacham)](https://en.wikipedia.org/wiki/BLS_digital_signature) is the default signature scheme used and is considered the most secure option. It is used for potential AVS logic if the AVS design requires aggregating AVS tasks.


* Used for potential AVS logic if the AVS design requires aggregating AVS tasks.
* Optional for registration to AVSs.


[ECDSA (Elliptic Curve Digital Signature Algorithm)](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) is an alternative signature scheme that AVS developers may choose to reduce on\-chain verification costs, although it is less secure than BLS.


* Required for Operator registration to the EigenLayer core protocol.
* Optional for registration to AVSs.


Note: please do not share (reuse) BLS and ECDSA keys across different AVSs.


Deploy the Incredible Squaring Demo Locally[​](#deploy-the-incredible-squaring-demo-locally "Direct link to Deploy the Incredible Squaring Demo Locally")
---------------------------------------------------------------------------------------------------------------------------------------------------------


Visit the [Incredible Squaring repo](https://github.com/Layr-Labs/incredible-squaring-avs?tab=readme-ov-file#incredible-squaring-avs) and run the local demo.

[PreviousBuilding an AVS](/eigenlayer/avs-guides/how-to-build-an-avs)[NextDeveloper Support](/eigenlayer/avs-guides/support)* [What is Incredible Squaring?](#what-is-incredible-squaring)
* [Incredible Squaring AVS Lifecycle (Flow)](#incredible-squaring-avs-lifecycle-flow)
* [Incredible Squaring Architecture Unique Characteristics](#incredible-squaring-architecture-unique-characteristics)
* [BLS vs ECDSA Use Cases within EigenLayer AVSs](#bls-vs-ecdsa-use-cases-within-eigenlayer-avss)
* [Deploy the Incredible Squaring Demo Locally](#deploy-the-incredible-squaring-demo-locally)


* 
* AVS Developer Guides
* [Key Management](/category/key-management)
* Key Security Considerations for Developers
On this pageKey Security Considerations for Developers
==========================================


When working with keys for nodes in an AVS, it is essential to consider the security aspects associated with key access and decryption. Keys should be encrypted either using a password or passphrase, understanding the unique security concerns posed by different access layers is crucial. By proactively addressing these concerns, you can enhance the overall security and integrity of the keys within your system:


* **Prompt for the passphrase and store it in memory:**


In this scenario, the input must remain hidden to prevent the secret phrase from being stored in the terminal session or used buffer. Attackers might search for this secret in the buffer history. The key should not be stored locally or remotely unless encrypted via the AVS's proprietary methods.
* **Request the path to a file containing the passphrase:**


Here, buffer vulnerability issues are absent unless the secret is printed or logged. However, an attacker with access to the machine running the AVS could potentially access this file.
* **Retrieve the key remotely:**


Encrypting the validator key offers markedly improved protection when the decryption passphrase is stored remotely. Since the passphrase is not located within the validator client's storage, obtaining an unencrypted key from on\-disk data becomes impossible. Instead, an attacker would need to execute considerably more advanced attacks, such as extracting the decrypted key from memory or impersonating the validator client process to receive the decryption key.


Nonetheless, despite the increased difficulty, a sophisticated attack could still potentially acquire the validator key. Moreover, the user may inadvertently sign undesirable messages.
* **Utilize remote signers:**


Employing remote signers involves delegating the signing process to an external service or device, which can offer additional security layers. The users are responsible for the availability and security of the remote signers, however, it is crucial to establish secure communication channels and verify the trustworthiness of the remote signer to prevent unauthorized access or tampering.


Supporting both local and remote signer methods is a good practice.


A good choice for a remote signer is [Web3signer](https://docs.web3signer.consensys.net/):


* Open\-source signing service developed under the Apache 2\.0 license, developed by Consensys, and written in Java.
* Capable of signing on multiple platforms using private keys stored in an external vault, or encrypted on a disk.
* Can sign payloads using secp256k1 and BLS12\-381 signing keys (AWS HSM can't at the moment, spring 2023\).
* Web3Signer uses REST APIs, and all the major Ethereum Consensus clients support it.


Key Management Recommendation for Developers[​](#key-management-recommendation-for-developers "Direct link to Key Management Recommendation for Developers")
------------------------------------------------------------------------------------------------------------------------------------------------------------


The AVS can implement a feasible and sufficient method of loading the keys. This is asking for a path to a keystore folder. This keystore needs to follow some structure that AVS knows how to read. Currently [eigenlayer\-cli](https://github.com/NethermindEth/eigenlayer#create-and-list-keys) supports creation of encrypted ecdsa and bn254 keys in the [web3 secret storage](https://ethereum.org/en/developers/docs/data-structures-and-encoding/web3-secret-storage/) format.


noteBy keys, we refer to any kind of secret, either in plain text or encrypted.


The path to this keystore folder can be provided via an environment variable or argument.

[PreviousKey Management](/category/key-management)[NextNode Specification](/category/node-specification)* [Key Management Recommendation for Developers](#key-management-recommendation-for-developers)


* 
* AVS Developer Guides
* AVS Rewards
On this pageAVS Rewards
===========

Overview[​](#overview "Direct link to Overview")
------------------------------------------------


The EigenLayer Rewards protocol enables AVSs to make rewards to stakers and operators. Operators earn rewards by opting in to AVSs that make `RewardsSubmissions` to the `RewardsCoordinator`, a core protocol contract. Within a single `RewardsSubmission`, an AVS can specify a time range for which the reward will be distributed, a list of weights for each `Strategy` for the reward, and an ERC20 token to give rewards in.


Operators will earn a flat 10% commission on rewards. The rest of the reward is passed on to the operator's delegated stakers. Rewards are proportional to:


* The amount of stake.
* The AVS's relative weighting of strategies in a rewards submission.


Rewards are calculated via an offchain process. Every week a merkle root is posted which represents the cumulative rewards across all earners. There is an additional 2 hour delay on testnet and 1 week delay on mainnet in order for the root to be claimable against. The deterministic calculation of the distribution of rewards is specified in our [technical docs](https://github.com/Layr-Labs/eigenlayer-contracts/blob/dev/docs/core/RewardsCoordinator.md).


AVS Integration[​](#avs-integration "Direct link to AVS Integration")
---------------------------------------------------------------------


The rewards protocol is currently live on testnet. AVSs can make rewards submissions via calling `createAVSRewardsSubmission` on the `RewardsCoordinator` contract. Each rewards submission specifies:


1. A time range for which the rewards submission is valid. Rewards submissions can be retroactive from the M2 upgrade and last up to 30 days in the future.
2. A list of strategies and multipliers, which enables the AVS to weigh the relative payout to each strategy within a single rewards submission.
3. The ERC20 token in which rewards should be denominated.
Rewards MUST come from an AVSs ServiceManager contract. An example integration can be found [here](https://github.com/Layr-Labs/eigenlayer-middleware/blob/v0.2.0-rc2-holesky-preprod-rewards/src/ServiceManagerBase.sol#L76-L104).


Integration Notes:


* The rewards passed on to earners are calculated daily. Rewards take 2 days to populate in the daily calculation. For example, if a reward submission was made on August 3rd, it would show up in the August 5th calculation
* Reward roots are posted weekly on mainnet and daily on testnet
* Reward roots are on a 7 day activation delay (ie. when it is claimable against) on mainnet and 2 hour activation delay on testnet
* If the AVS does not have any operators opted into the AVS on a day of an active reward, those tokens are not distributed pro\-rata to future days.
* Rewards cannot be clawed back by AVSs.
* Operators will only be distributed rewards on **entire** days that they have opted into the AVS.
* Due to the rounding in the off\-chain process, we recommend not making range submission token amounts with more than 15 significant digits of precision. If more than 15 significant digits are provided, the extra precision will be truncated.
* Rewards can be made in multiple ERC\-20 tokens by calling `createAVSRewardsSubmission` for each ERC\-20 token to reward in.
* There are several requirements for successfully calling `createAVSRewardsSubmission`. It's recommended to read further details [here](https://github.com/Layr-Labs/eigenlayer-contracts/blob/v0.3.0-rc3-holesky-preprod-rewards/docs/core/RewardsCoordinator.md#createavsrewardssubmission).


FAQ[​](#faq "Direct link to FAQ")
---------------------------------


### When are rewards submissions including in daily calculation?[​](#when-are-rewards-submissions-including-in-daily-calculation "Direct link to When are rewards submissions including in daily calculation?")


An AVS' reward submission is included in the calculation 2 days after it is submitted. For example, if the AVS submits a rewards submission on August 2nd, it will be included in the August 4th rewards calculation.


### How long will stakers and operators of my AVS have to wait to claim their rewards?[​](#how-long-will-stakers-and-operators-of-my-avs-have-to-wait-to-claim-their-rewards "Direct link to How long will stakers and operators of my AVS have to wait to claim their rewards?")


Worst case, stakers and operators of an AVS will have to wait 16 days to claim a reward (2 day calculation delay \+ 7 day root submission cadence \+ 7 day activation delay).


### How can I display the symbol and name of my reward token?[​](#how-can-i-display-the-symbol-and-name-of-my-reward-token "Direct link to How can I display the symbol and name of my reward token?")


An automated process for this is being finalized.

[PreviousAVS Developer Security Best Practices](/eigenlayer/avs-guides/avs-developer-best-practices)[NextMultisig Governance](/eigenlayer/security/multisig-governance)* [Overview](#overview)
* [AVS Integration](#avs-integration)
* [FAQ](#faq)
	+ [When are rewards submissions including in daily calculation?](#when-are-rewards-submissions-including-in-daily-calculation)
	+ [How long will stakers and operators of my AVS have to wait to claim their rewards?](#how-long-will-stakers-and-operators-of-my-avs-have-to-wait-to-claim-their-rewards)
	+ [How can I display the symbol and name of my reward token?](#how-can-i-display-the-symbol-and-name-of-my-reward-token)


* 
* AVS Developer Guides
* [Node Specification](/category/node-specification)
* [AVS Node API](/category/avs-node-api)
* AVS Node API
On this pageAVS Node API
============


The AVS Node HTTP RESTful API provides a common interface for Nodes designed for the EigenLayer protocol.


Base URL[​](#base-url "Direct link to Base URL")
------------------------------------------------


The base URL for the API is:



```
/eigen  

```

API Versioning[​](#api-versioning "Direct link to API Versioning")
------------------------------------------------------------------


This document describes the AVS Node API version `v0.0.1`. The API version follows the same EigenLayer AVS Node specification version.


The API version can be included in the query string as follows:



```
/eigen/endpoint?version=0.0.2  

```

In case of handling a request without the version query parameter, the API will respond with the latest version of the API.


If the requested version is not supported, the API will respond with a 404 Not Found error and the following message:



```
{  
  "message": "API version not found"  
}  

```

Node[​](#node "Direct link to Node")
------------------------------------


Endpoints to query Node related information.


### GET /eigen/node[​](#get-eigennode "Direct link to GET /eigen/node")


Provides AVS Node and API identity information in a format similar to [HTTP User\-Agent](https://www.rfc-editor.org/rfc/rfc7231#section-5.5.3).


#### Parameters[​](#parameters "Direct link to Parameters")


No parameters


#### Responses[​](#responses "Direct link to Responses")


**200** \- Request successful


**Content\-Type:** `application/json`


* Example Value
* Schema


```
{  
  "node_name": "EigenLayer-AVS",  
  "spec_version": "v0.0.1",  
  "node_version": "v1.0.0"  
}  

```

```
{  
  "type": "object",  
  "properties": {  
    "node_name": {  
      "type": "string",  
      "description": "Name of the node"  
    },  
    "spec_version": {  
      "type": "string",  
      "description": "AVS Specification version"  
    },  
    "node_version": {  
      "type": "string",  
      "description": "Version of the node"  
    }  
  },  
  "required": [  
    "node_name",  
    "spec_version",  
    "node_version"  
  ]  
}  

```

**500** \- Internal server error


**Content\-Type:** `application/json`


* Example Value
* Schema


```
{  
  "message": "Internal server error"  
}  

```

```
{  
  "type": "object",  
  "properties": {  
    "message": {  
      "type": "string",  
      "description": "Error message"  
    }  
  },  
  "required": [  
    "message"  
  ]  
}  

```

### GET /eigen/node/health[​](#get-eigennodehealth "Direct link to GET /eigen/node/health")


Returns AVS Node health status in HTTP status codes.


#### Parameters[​](#parameters-1 "Direct link to Parameters")


No parameters


#### Responses[​](#responses-1 "Direct link to Responses")


**200** \- AVS Node is healthy


**206** \- AVS Node is partially healthy. It is either initializing or some backing services are not healthy.


**503** \- AVS Node is unhealthy or having issues.


### GET /eigen/node/services[​](#get-eigennodeservices "Direct link to GET /eigen/node/services")


Returns a list of all backing services that are currently registered with the AVS Node setup. Useful to determine if a service is currently registered with the AVS Node and to get the service ID for health endpoint.


#### Parameters[​](#parameters-2 "Direct link to Parameters")


No parameters


#### Responses[​](#responses-2 "Direct link to Responses")


**200** \- Request successful


**Content\-Type:** `application/json`


* Example Value
* Schema


```
{  
  "services": [  
    {  
      "id": "db-1",  
      "name": "Database",  
      "description": "Database description",  
      "status": "Up",  
    },  
    {  
      "id": "idx-2",  
      "name": "Indexer",  
      "description": "Indexer description",  
      "status": "Down",  
    }  
  ]  
}  

```

```
{  
  "type": "object",  
  "properties": {  
    "services": {  
      "type": "array",  
      "description": "List of backing services",  
      "items": {  
        "type": "object",  
        "properties": {  
          "id": {  
            "type": "string",  
            "description": "Service ID"  
          },  
          "name": {  
            "type": "string",  
            "description": "Service name"  
          },  
          "description": {  
            "type": "string",  
            "description": "Service description"  
          },  
          "status": {  
            "type": "string",  
            "description": "Service status. Possible values are Up, Down, or Initializing."  
  
          }  
        },  
        "required": [  
          "id",  
          "name",  
          "description"  
        ]  
      }  
    }  
  },  
  "required": [  
    "services"  
  ]  
}  

```

**500** \- Internal server error


**Content\-Type:** `application/json`


* Example Value
* Schema


```
{  
  "message": "Internal server error"  
}  

```

```
{  
  "type": "object",  
  "properties": {  
    "message": {  
      "type": "string",  
      "description": "Error message"  
    }  
  },  
  "required": [  
    "message"  
  ]  
}  

```

### GET `/eigen/node/services/{service_ID}/health`[​](#get-eigennodeservicesservice_idhealth "Direct link to get-eigennodeservicesservice_idhealth")


Returns the health status of the given service in HTTP status codes. The service ID is the service ID returned by the `/eigen/services` endpoint. The service is considered healthy if the service is registered with the AVS Node and the service is currently online.


#### Parameters[​](#parameters-3 "Direct link to Parameters")


**service\_ID** `string` `(path)` \- Service ID


#### Responses[​](#responses-3 "Direct link to Responses")


**200** \- Backing service is healthy


**206** \- Backing service is partially healthy. It is either initializing or not ready yet.


**503** \- Backing service is unhealthy or having issues.

[PreviousAVS Node API](/category/avs-node-api)[NextImplementation reference](/eigenlayer/avs-guides/spec/api/api-examples)* [Base URL](#base-url)
* [API Versioning](#api-versioning)
* [Node](#node)
	+ [GET /eigen/node](#get-eigennode)
	+ [GET /eigen/node/health](#get-eigennodehealth)
	+ [GET /eigen/node/services](#get-eigennodeservices)
	+ [GET `/eigen/node/services/{service_ID}/health`](#get-eigennodeservicesservice_idhealth)


* 
* AVS Developer Guides
* [Node Specification](/category/node-specification)
* [AVS Node API](/category/avs-node-api)
* Implementation reference
On this pageImplementation reference
========================


This guide is intended to showcase the practical application of the AVS Node API using authentic examples. Examples used are:


* EigenDA


EigenDA Example[​](#eigenda-example "Direct link to EigenDA Example")
---------------------------------------------------------------------


### GET /eigen/node[​](#get-eigennode "Direct link to GET /eigen/node")


### Response[​](#response "Direct link to Response")



```
{  
    "node_name": "EigenDA-AVS",  
    "spec_version": "v0.0.1",  
    "node_version": "v1.0.0"  
}  

```

### GET /eigen/node/health[​](#get-eigennodehealth "Direct link to GET /eigen/node/health")


### Response[​](#response-1 "Direct link to Response")



```
200 OK  

```

### GET /eigen/node/services[​](#get-eigennodeservices "Direct link to GET /eigen/node/services")


### Response[​](#response-2 "Direct link to Response")



```
{  
  "services": [  
    {  
      "id": "graph-node-da",  
      "name": "graph-node",  
      "description": "Indexer graph node description",  
      "status": "Up",  
    },  
    {  
      "id": "ipfs-da",  
      "name": "ipfs",  
      "description": "ipfs instance description",  
      "status": "Down",  
    },  
    {  
      "id": "postgres-da",  
      "name": "postgres",  
      "description": "Postgres DB description",  
      "status": "Initializing",  
    }  
  ]  
}  

```

### GET /eigen/node/services/graph\-node\-da/health[​](#get-eigennodeservicesgraph-node-dahealth "Direct link to GET /eigen/node/services/graph-node-da/health")


### Response[​](#response-3 "Direct link to Response")



```
200 OK  

```

### GET /eigen/node/services/ipfs\-da/health[​](#get-eigennodeservicesipfs-dahealth "Direct link to GET /eigen/node/services/ipfs-da/health")


### Response[​](#response-4 "Direct link to Response")



```
503 Service Unavailable  

```

### GET /eigen/node/services/postgres\-da/health[​](#get-eigennodeservicespostgres-dahealth "Direct link to GET /eigen/node/services/postgres-da/health")


### Response[​](#response-5 "Direct link to Response")



```
206 Partial Content  

```
[PreviousAVS Node API](/eigenlayer/avs-guides/spec/api/)[NextMetrics](/category/metrics)* [EigenDA Example](#eigenda-example)
	+ [GET /eigen/node](#get-eigennode)
	+ [Response](#response)
	+ [GET /eigen/node/health](#get-eigennodehealth)
	+ [Response](#response-1)
	+ [GET /eigen/node/services](#get-eigennodeservices)
	+ [Response](#response-2)
	+ [GET /eigen/node/services/graph\-node\-da/health](#get-eigennodeservicesgraph-node-dahealth)
	+ [Response](#response-3)
	+ [GET /eigen/node/services/ipfs\-da/health](#get-eigennodeservicesipfs-dahealth)
	+ [Response](#response-4)
	+ [GET /eigen/node/services/postgres\-da/health](#get-eigennodeservicespostgres-dahealth)
	+ [Response](#response-5)


* 
* AVS Developer Guides
* [Node Specification](/category/node-specification)
* Introduction
On this pageIntroduction
============

This is a specification for running AVS Nodes.The current version of the specification is `v0.0.1`.


cautionThe current version of the AVS Node specification should be considered a public alpha version. Therefore, it may undergo rapid changes and experience incompatibility issues until the first stable version is released.


The description of the Specification is divided into the following sections:


* [AVS Node API](/eigenlayer/avs-guides/spec/api/): HTTP RESTful API for AVS Nodes.
* [Metrics](/eigenlayer/avs-guides/spec/metrics/metrics-prom-spec): Prometheus standard metrics for AVS implementations.


Definitions[​](#definitions "Direct link to Definitions")
---------------------------------------------------------


### MUST[​](#must "Direct link to MUST")


When the term "**MUST**" is used in this documentation, it denotes an absolute requirement. Failing to follow a "**MUST**" directive may result in the AVS not functioning as intended or could lead to undesirable outcomes. It is imperative that operators and AVS developers adhere to any instruction or guideline marked with "**MUST**" to ensure the correct and optimal operation of the AVS.


Example Usage:


* "Operators **MUST** safeguard their keys."
* "The AVS **MUST** be updated to the latest version to access new features."


### SHOULD[​](#should "Direct link to SHOULD")


The term "**SHOULD**" in this documentation indicates a strong recommendation. While not an absolute requirement like "**MUST**", following a "**SHOULD**" directive is highly advised to achieve the best possible experience or outcome. Ignoring a "**SHOULD**" guideline might not break the AVS, but it could lead to suboptimal results or missed opportunities for enhanced functionality.


Example Usage:


* "Operators **SHOULD** regularly back up their data to prevent potential loss."
* "For optimal performance, you **SHOULD** stick to the AVS hardware requirements."
[PreviousNode Specification](/category/node-specification)[NextAVS Node API](/category/avs-node-api)* [Definitions](#definitions)
	+ [MUST](#must)
	+ [SHOULD](#should)


* 
* AVS Developer Guides
* [Node Specification](/category/node-specification)
* [Metrics](/category/metrics)
* Implementation reference
On this pageImplementation reference
========================


This guide is intended to showcase the practical application of the Prometheus metrics using authentic examples. Examples used are:


* EigenDA


Some metrics and endpoints are very straightforward, but having a reference for the responses and labels can be helpful.


EigenDA Example[​](#eigenda-example "Direct link to EigenDA Example")
---------------------------------------------------------------------


Prometheus Metrics[​](#prometheus-metrics "Direct link to Prometheus Metrics")
------------------------------------------------------------------------------


### Economics metrics[​](#economics-metrics "Direct link to Economics metrics")


* `eigen_registered_stakes{quorum_number=1, quorum_name="beaconChainEth"}`


### Perfomance metrics[​](#perfomance-metrics "Direct link to Perfomance metrics")


* `eigen_performance_score`


### RPC metrics[​](#rpc-metrics "Direct link to RPC metrics")


* `eigen_rpc_request_duration_seconds{method="eth_getBlockByNumber", client_version="nethermind/v1.17.2"}`
* `eigen_rpc_request_total{method="eth_estimateGas", client_version="nethermind/v1.17.2"}`
[PreviousPrometheus Metrics Specification](/eigenlayer/avs-guides/spec/metrics/metrics-prom-spec)[NextAVS Dashboard Onboarding](/eigenlayer/avs-guides/avs-dashboard-onboarding)* [EigenDA Example](#eigenda-example)
* [Prometheus Metrics](#prometheus-metrics)
	+ [Economics metrics](#economics-metrics)
	+ [Perfomance metrics](#perfomance-metrics)
	+ [RPC metrics](#rpc-metrics)


* 
* AVS Developer Guides
* [Node Specification](/category/node-specification)
* [Metrics](/category/metrics)
* Prometheus Metrics Specification
On this pagePrometheus Metrics Specification
================================


The table below defines metrics which may be captured by AVS Nodes which expose metrics to Prometheus. AVSs may expose additional metrics however these should not use the `eigen_` prefix.


Economics metrics[​](#economics-metrics "Direct link to Economics metrics")
---------------------------------------------------------------------------




| Name | Metric Type | Definition | Labels |
| --- | --- | --- | --- |
| `eigen_registered_stakes` | Gauge | Operator stakes in AVS registry contract. Most commonly represents a weighted combination of delegated shares in the `DelegationManager` EigenLayer contract. | `quorum_number`, `quorum_name` |


noteA definition of a strategy contract can be found in [Key Terms](/eigenlayer/overview/key-terms).


tipThe `quorum_name` label of the `eigen_registered_stakes` metric is optional and can be omitted.


Performance metrics[​](#performance-metrics "Direct link to Performance metrics")
---------------------------------------------------------------------------------




| Name | Metric Type | Definition | Labels |
| --- | --- | --- | --- |
| `eigen_performance_score` | Gauge | The performance metric is a score between 0 and 100 and each developer can define their own way of calculating the score. The score is calculated based on the performance of the AVS Node and the performance of the backing services. |  |


RPC metrics[​](#rpc-metrics "Direct link to RPC metrics")
---------------------------------------------------------




| Name | Metric Type | Definition | Labels |
| --- | --- | --- | --- |
| `eigen_rpc_request_duration_seconds` | Histogram | Duration of json\-rpc `<method>` in seconds from Ethereum Execution client `<client>` | `method`, `client_version` |
| `eigen_rpc_request_total` | Counter | Total of json\-rpc `<method>` requests from Ethereum Execution client `<client>` | `method`, `client_version` |


Notation examples[​](#notation-examples "Direct link to Notation examples")
---------------------------------------------------------------------------


* `eigen_registered_stakes{quorum_number=0, quorum_name="ethLST"}`
* `eigen_performance_score{}`
* `eigen_rpc_request_duration_seconds{method="eth_getBlockByNumber", client_version="nethermind/v1.17.2"}`
* `eigen_rpc_request_total{method="eth_getBlockByNumber", client_version="nethermind/v1.17.2"}`
[PreviousMetrics](/category/metrics)[NextImplementation reference](/eigenlayer/avs-guides/spec/metrics/metrics-examples)* [Economics metrics](#economics-metrics)
* [Performance metrics](#performance-metrics)
* [RPC metrics](#rpc-metrics)
* [Notation examples](#notation-examples)


* 
* Contract Addresses and Docs
On this pageContract Addresses and Docs
===========================

EigenLayer Core Restaking Contracts[​](#eigenlayer-core-restaking-contracts "Direct link to EigenLayer Core Restaking Contracts")
---------------------------------------------------------------------------------------------------------------------------------


The EigenLayer core contracts are located in this repo: [`Layr-Labs/eigenlayer-contracts`](https://github.com/Layr-Labs/eigenlayer-contracts). They enable restaking of liquid staking tokens (LSTs) and beacon chain ETH to secure new services, called AVSs (actively validated services).


### Deployment Addresses[​](#deployment-addresses "Direct link to Deployment Addresses")


An up\-to\-date reference of our current mainnet and testnet contract deployments can be found in the core repository README: [`eigenlayer-contracts/README.md#deployments`](https://github.com/Layr-Labs/eigenlayer-contracts?tab=readme-ov-file#deployments).


### Technical Documentation[​](#technical-documentation "Direct link to Technical Documentation")


Our most up\-to\-date contract\-level documentation can be found in the core repository's docs folder: [`eigenlayer-contracts/docs`](https://github.com/Layr-Labs/eigenlayer-contracts/tree/dev/docs).

[PreviousTerms of Service](/eigenlayer/legal/terms-of-service)[NextLearning Resources](/eigenlayer/resources/learning-resources)* [EigenLayer Core Restaking Contracts](#eigenlayer-core-restaking-contracts)
	+ [Deployment Addresses](#deployment-addresses)
	+ [Technical Documentation](#technical-documentation)


* 
* Legal
* EigenLayer Privacy Policy
On this pageEigenLayer Privacy Policy
=========================


***Last Revised on March 20, 2024***


This Privacy Policy for Eigen Labs, Inc. ("Company", "we", "us" "our") describes how we collect, use and disclose information about users of the Company's website (eigenlayer.xyz), and any related services, tools and features, including the EigenLayer service (collectively, the "Services"). For the purposes of this Privacy Policy, "you" and "your" means you as the user of the Services. ​ Please read this Privacy Policy carefully. By using, accessing, or downloading any of the Services, you agree to the collection, use, and disclosure of your information as described in this Privacy Policy. If you do not agree to this Privacy Policy, please do not use, access or download any of the Services. ​


UPDATING THIS PRIVACY POLICY[​](#updating-this-privacy-policy "Direct link to UPDATING THIS PRIVACY POLICY")
------------------------------------------------------------------------------------------------------------


​We may modify this Privacy Policy from time to time in which case we will update the "Last Revised" date at the top of this Privacy Policy. If we make material changes to the way in which we use information we collect, we will use reasonable efforts to notify you (such as by emailing you at the last email address you provided us, by posting notice of such changes on the Services, or by other means consistent with applicable law) and will take additional steps as required by applicable law. If you do not agree to any updates to this Privacy Policy please do not access or continue to use the Services. ​


COMPANY'S COLLECTION AND USE OF INFORMATION[​](#companys-collection-and-use-of-information "Direct link to COMPANY'S COLLECTION AND USE OF INFORMATION")
--------------------------------------------------------------------------------------------------------------------------------------------------------


​ When you access or use the Services, we may collect certain categories of information about you from a variety of sources, which comprises: ​


* The following information about you: name, email address, and Discord Tag. We collect your email address and Discord Tag in order to communicate with you through the Services and through third party platforms, such as Discord.
* Information included in any identity documents you provide to us, including without limitation driver’s license or passport number, date of birth and/or country of residence. We collect this in limited circumstances for the purposes of identification of the jurisdiction of residence of certain users or as otherwise needed to satisfy certain regulatory obligations.
* The following third\-party wallet ("Wallet") information: public wallet address and token holdings. We collect third\-party Wallet information in order to facilitate your use of the Services. ​
* Any other information you choose to include in communications with us, for example, when sending a message through the Services. ​


We also automatically collect certain information about your interaction with the Services ("Usage Data"). To do this, we may use cookies, web beacons/clear gifs and other geolocation tracking technologies ("Tracking Technologies"). Usage Data comprises of: ​


* Device information (e.g., unique device identifier, device type, IP address, operating system) ​
* Browser information (e.g., browser type) ​
* Location information (e.g., approximate geolocation) ​
* Other information regarding your interaction with the Services (e.g., log data, date and time stamps, clickstream data, ​ We use Usage Data to tailor features and content to you and to run analytics and better understand user interaction with the Services. For more information on how we use Tracking Technologies and your choices, see the section below, Cookies and Other Tracking Technologies. ​ In addition to the foregoing, we may use any of the above information to comply with any applicable legal obligations, to enforce any applicable terms of service, and to protect or defend the Services, our rights, and the rights of our users or others. ​


HOW THE COMPANY SHARES YOUR INFORMATION[​](#how-the-company-shares-your-information "Direct link to HOW THE COMPANY SHARES YOUR INFORMATION")
---------------------------------------------------------------------------------------------------------------------------------------------


​In certain circumstances, the Company may share your information with third parties for legitimate purposes subject to this Privacy Policy. Such circumstances comprise of: ​


* With vendors or other service providers, such as ​
* Blockchain analysis service providers, including Chainanalysis ​
* Data analytics vendors, including Google Analytics ​
* To comply with applicable law or any obligations thereunder, including cooperation with law
enforcement, judicial orders, and regulatory inquiries ​
* In connection with an asset sale, merger, bankruptcy, or other business transaction ​
* To enforce any applicable terms of service ​
* To ensure the safety and security of the Company and/or its users ​
* When you request us to share certain information with third parties, such as through your use of login integrations ​
* With professional advisors, such as auditors, law firms, or accounting firms ​


COOKIES AND OTHER TRACKING TECHNOLOGIES[​](#cookies-and-other-tracking-technologies "Direct link to COOKIES AND OTHER TRACKING TECHNOLOGIES")
---------------------------------------------------------------------------------------------------------------------------------------------


​Do Not Track Signals ​ Your browser settings may allow you to transmit a "Do Not Track" signal when you visit various websites. Like many websites, our website is not designed to respond to "Do Not Track" signals received from browsers. To learn more about "Do Not Track" signals, you can visit [http://www.allaboutdnt.com/.](http://www.allaboutdnt.com) ​ Cookies and Other Tracking Technologies ​ Most browsers accept cookies automatically, but you may be able to control the way in which your devices permit the use of cookies, web beacons/clear gifs, other geolocation tracking technologies. If you so choose, you may block or delete our cookies from your browser; however, blocking or deleting cookies may cause some of the Services, including any portal features and general functionality, to work incorrectly. If you have questions regarding the specific information about you that we process or retain, as well as your choices regarding our collection and use practices, please contact us using the information listed below. ​ To opt out of tracking by Google Analytics, click [here](https://tools.google.com/dlpage/gaoptout). ​ Your browser settings may allow you to transmit a "Do Not Track" signal when you visit various websites. Like many websites, our website is not designed to respond to "Do Not Track" signals received from browsers. To learn more about "Do Not Track" signals, you can visit [http://www.allaboutdnt.com/.](http://www.allaboutdnt.com) ​


SOCIAL NETWORKS AND OTHER THIRD PARTY WEBSITES AND LINKS[​](#social-networks-and-other-third-party-websites-and-links "Direct link to SOCIAL NETWORKS AND OTHER THIRD PARTY WEBSITES AND LINKS")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


​We may provide links to websites or other online platforms operated by third parties, including third\-party social networking platforms, such as Twitter, Discord, or Medium, operated by third parties (such platforms are "Social Networks"). If you follow links to sites not affiliated or controlled by us, you should review their privacy and security policies and other terms and conditions. We do not guarantee and are not responsible for the privacy or security of these sites, including the accuracy, completeness, or reliability of information found on these sites. Information you provide on public or semi\-public venues, including information you share or post on Social Networks, may also be accessible or viewable by other users of the Services and/or users of those third\-party online platforms without limitation as to its use by us or by a third party. Our inclusion of such links does not, by itself, imply any endorsement of the content on such platforms or of their owners or operators, except as disclosed on the Services. ​


THIRD PARTY WALLET EXTENSIONS[​](#third-party-wallet-extensions "Direct link to THIRD PARTY WALLET EXTENSIONS")
---------------------------------------------------------------------------------------------------------------


​Certain transactions conducted via our Services, will require you to connect a Wallet to the Services. By using such Wallet to conduct such transactions via the Services, you agree that your interactions with such third party Wallets are governed by the privacy policy for the applicable Wallet. We expressly disclaim any and all liability for actions arising from your use of third party Wallets, including but without limitation, to actions relating to the use and/or disclosure of personal information by such third party Wallets.


CHILDREN'S PRIVACY[​](#childrens-privacy "Direct link to CHILDREN'S PRIVACY")
-----------------------------------------------------------------------------


​Children under the age of 18 are not permitted to use the Services, and we do not seek or knowingly collect any personal information about children under 13 years of age. If we become aware that we have unknowingly collected information about a child under 13 years of age, we will make commercially reasonable efforts to delete such information from our database. ​ If you are the parent or guardian of a child under 13 years of age who has provided us with their personal information, you may contact us using the below information to request that it be deleted. ​


DATA SECURITY[​](#data-security "Direct link to DATA SECURITY")
---------------------------------------------------------------


​Please be aware that, despite our reasonable efforts to protect your information, no security measures are perfect or impenetrable, and we cannot guarantee "perfect security." Please further note that any information you send to us electronically, while using the Services or otherwise interacting with us, may not be secure while in transit. We recommend that you do not use unsecure channels to communicate sensitive or confidential information to us. ​


HOW TO CONTACT US[​](#how-to-contact-us "Direct link to HOW TO CONTACT US")
---------------------------------------------------------------------------


Should you have any questions about our privacy practices or this Privacy Policy, please email us at [\[email protected]](/cdn-cgi/l/email-protection#5a34352e33393f291a3f333d3f34363b38297435283d) or contact us at 15790 Redmond Way \#1176, Redmond, WA 98052 .

[PreviousRisk FAQ](/eigenlayer/risk/risk-faq)[NextTerms of Service](/eigenlayer/legal/terms-of-service)* [UPDATING THIS PRIVACY POLICY](#updating-this-privacy-policy)
* [COMPANY'S COLLECTION AND USE OF INFORMATION](#companys-collection-and-use-of-information)
* [HOW THE COMPANY SHARES YOUR INFORMATION](#how-the-company-shares-your-information)
* [COOKIES AND OTHER TRACKING TECHNOLOGIES](#cookies-and-other-tracking-technologies)
* [SOCIAL NETWORKS AND OTHER THIRD PARTY WEBSITES AND LINKS](#social-networks-and-other-third-party-websites-and-links)
* [THIRD PARTY WALLET EXTENSIONS](#third-party-wallet-extensions)
* [CHILDREN'S PRIVACY](#childrens-privacy)
* [DATA SECURITY](#data-security)
* [HOW TO CONTACT US](#how-to-contact-us)


* 
* Legal
* Terms of Service
Terms of Service
================


***Last Revised on March 13, 2024***


These Terms of Service (these "**Terms**") explain the terms and conditions by which you may access and use our website, [www.eigenlayer.xyz](http://www.eigenlayer.xyz) (the "**Website**"), operated by or on behalf of Eigen Labs, Inc. ("**Company**", "**we**" or "**us**"), our App (as defined below), our EigenLayer App testnet ("**Testnet**"), our application programming interfaces ("**APIs**"), our research forum available at [research.eigenlayer.xyz](http://research.eigenlayer.xyz) ("**Research Forum**") and any other Services provided by the Company, including any related content, tools, documentation, features and functionality which are collectively referred to herein as the "**Services**".


These Terms govern your access to and use of the Services. Please read these Terms carefully, as they include important information about your legal rights. By accessing and/or using the Services, you are agreeing to these Terms. If you do not understand or agree to these Terms, please do not use the Services.


For purposes of these Terms, "**you**" and "**your**" means you as the user of the Services. If you use the Services on behalf of a company or other entity then "you" includes you and that entity, and you represent and warrant that (a) you are an authorized representative of the entity with the authority to bind the entity to these Terms, and (b) you agree to these Terms on the entity's behalf.



> SECTION 9 CONTAINS AN ARBITRATION CLAUSE AND CLASS ACTION WAIVER. BY AGREEING TO THESE TERMS, YOU AGREE (A) TO RESOLVE ALL DISPUTES (WITH LIMITED EXCEPTION) RELATED TO THE COMPANY'S SERVICES AND/OR PRODUCTS THROUGH BINDING INDIVIDUAL ARBITRATION, WHICH MEANS THAT YOU WAIVE ANY RIGHT TO HAVE THOSE DISPUTES DECIDED BY A JUDGE OR JURY, AND (B) TO WAIVE YOUR RIGHT TO PARTICIPATE IN CLASS ACTIONS, CLASS ARBITRATIONS, OR REPRESENTATIVE ACTIONS, AS SET FORTH BELOW. YOU HAVE THE RIGHT TO OPT\-OUT OF THE ARBITRATION CLAUSE AND THE CLASS ACTION WAIVER AS EXPLAINED IN SECTION 9\.


1. **THE SERVICES**


	1. Services. The Services provide a front\-end interface (the "**App**") that display data that facilitates users interfacing with a set of decentralized open\-sourced smart contracts that allow for the restaking of digital assets, such as Ether (ETH). These underlying smart contracts are referred to herein as the "**EigenLayer Protocol**”. The Services may also reference or provide an App or APIs related to smart contracts that provide a data availability service built on top of Ethereum. These underlying smart contracts are referred to herein as the “**EigenDA Protocol**”. Collectively, the EigenLayer Protocol and EigenDA Protocol are referred to herein as the **“Protocols**”). The Services also provide documentation available at [docs.eigenlayer.xyz](https://docs.eigenlayer.xyz) related to the App and Protocol ("**Documentation**"). **The Protocols are not part of the Services, and your use of the Protocols is entirely at your own risk. Additionally, the third party technologies required to be used or interacted with in order to interact with the Protocols, including but not limited to a Wallet (as defined below, and collectively the “Third\-Party Tools”), are not part of the Services, and your use of such Third\-Party Tools are entirely at your own risk.** The App is separate and distinct from either of the Protocols and any Third\-Party Tools. The App is not essential to accessing the Protocols. The App merely displays blockchain data and provides a web application that reduces the complexity of using the Third\-Party Tools or otherwise accessing either of the Protocols. All activity on each of the Protocols is run by permissionless smart contracts, and other developers are free to create their own interfaces to function with the Protocols.
	2. Wallets. To use certain of the Services you may need to link a third\-party digital wallet (**"Wallet"**) with the Services. By using a Wallet in connection with the Services, you agree that you are using the Wallet under the terms and conditions of the applicable third\-party provider of such Wallet. Wallets are not associated with, maintained by, supported by or affiliated with the Company. You acknowledge and agree that we are not party to any transactions conducted while accessing our App, and we do not have possession, custody or control over any digital assets appearing on the Services. When you interact with the App, you retain control over your digital assets at all times. The Company accepts no responsibility or liability to you in connection with your use of a Wallet, and makes no representations and warranties regarding how the Services will operate with any specific Wallet. **The private keys and/or seed phrases necessary to access the assets held in a Wallet are not held by the Company. The Company has no ability to help you access or recover your private keys and/or seed phrases for your Wallet, so please keep them in a safe place.**
	3. Updates; Monitoring. We may make any improvement, modifications or updates to the Services, including but not limited to changes and updates to the underlying software, infrastructure, security protocols, technical configurations or service features (the "**Updates**") from time to time. Your continued access and use of the Services are subject to such Updates and you shall accept any patches, system upgrades, bug fixes, feature modifications, or other maintenance work that arise out of such Updates. We are not liable for any failure by you to accept and use such Updates in the manner specified or required by us. Although the Company is not obligated to monitor access to or participation in the Services, it has the right to do so for the purpose of operating the Services, to ensure compliance with the Terms and to comply with applicable law or other legal requirements.
	4. The Company may charge or pass through fees for some or part of the Services we make available to you, including transaction or processing fees, blockchain gas or similar network fees. We will disclose the amount of fees we will charge or pass through to you for the applicable Service at the time you access, use or otherwise transact with the Services. Although we will attempt to provide accurate fee information, any such information reflects our estimate of fees, which may vary from the fees actually paid to use the Services and interact with the applicable blockchain with which the Services are compatible. Additionally, your external Wallet provider may impose a fee to transact on the Services. We are not responsible for any fees charged by a third party. All transactions processed through the Services are non\-refundable. You will be responsible for paying any and all taxes, duties and assessments now or hereafter claimed or imposed by any governmental authority associated with your use of the Services. In certain cases, your transactions through the Services may not be successful due to an error with the blockchain or the Wallet. We accept no responsibility or liability to you for any such failed transactions, or any transaction or gas fees that may be incurred by you in connection with such failed transactions. You acknowledge and agree that all information you provide with respect to transactions on the Services, including, without limitation, credit card, bank account, PayPal or other payment information is accurate, current and complete, and you have the legal right to use such payment method.
	5. Rewards. In your use of the Services, you may be attributed certain reputation indicators, points, or other intangible rewards (“**Rewards”**). Rewards are not, and may never convert to, accrue to, be used as basis to calculate, or become any other tokens or virtual assets or distribution thereof. Rewards are virtual items with no monetary value. Rewards do not constitute any currency or property of any type and are not redeemable, refundable, or eligible for any fiat or virtual currency or anything else of value. Rewards are not transferable between users, and you may not attempt to sell, trade, or transfer any Rewards, or obtain any manner of credit using any Rewards. Any attempt to sell, trade, or transfer any Rewards or tokens redeemable for or representing any Rewards will be null and void.
2. **Who May Use the Services**


	1. You must be 18 years of age or older and not be a Prohibited Person to use the Services. A "**Prohibited Person**" is any person or entity that is (a) listed on any U.S. Government list of prohibited or restricted parties, including without limitation the U.S. Treasury Department's list of Specially Designated Nationals or the U.S. Department of Commerce Denied Person's List or Entity List, (b) located or organized in any U.S. embargoed countries or region any country or region that has been designated by the U.S. Government as "terrorist supporting", or (c) owned or controlled by such persons or entities listed in (a)\-(b). You acknowledge and agree that you are solely responsible for complying with all applicable laws of the jurisdiction you are located or accessing the Services from in connection with your use of the Services. By using the Services, you represent and warrant that you meet these requirements and will not be using the Services for any illegal activity or to engage in the prohibited activities in Section 5\.3\.
	2. To use certain of the Services, such as the Research Forum, you need to create an account or link another account ("**Account**"). You agree to provide us with accurate, complete and updated information for your Account. You are solely responsible for any activity on your Account and maintaining the confidentiality and security of your password. We are not liable for any acts or omissions by you in connection with your Account. You must immediately notify us at [\[email protected]](/cdn-cgi/l/email-protection#6f01001b060c0a1c2f0a06080a01030e0d1c41001d08) if you know or have any reason to suspect that your Account or password have been stolen, misappropriated or otherwise compromised, or in case of any actual or suspected unauthorized use of your Account. You agree not to create any Account if we have previously removed yours, or we previously banned you from any of our Services, unless we provide written consent otherwise.
	3. We may require you to provide additional information and documents regarding your use of the Services, including at the request of any competent authority or in case of application of any applicable law or regulation, including laws related to anti\-money laundering or for counteracting financing of terrorism. We may also require you to provide additional information or documents in cases where we have reason to believe: (i) that your Wallet is being used for illegal money laundering or for any other illegal activity; (ii) you have concealed or reported false identification information or other details; or (iii) you are a Prohibited Person. You agree that if it is determined in our sole discretion that you may be violating this Section 2 or engaging in any activities prohibited in these Terms, we may disable your ability to use the Services including the App, which may include but is not limited to preventing you from restaking assets or withdrawing previously restaked assets.
3. **The Testnet**


	1. Purpose and Participation. The Testnet is designed to demonstrate the functionality and features of the App (or any portion thereof) and to improve participant experiences prior to the App's launch. YOUR PARTICIPATION IN THE TESTNET IS ENTIRELY VOLUNTARY, BUT IF YOU ARE PARTICIPATING IN THE TESTNET, YOU MUST STRICTLY ADHERE TO THESE TERMS. We make no representation or warranty that the Testnet will accurately or completely simulate, duplicate or replicate the App.
	2. Duration. The availability of the Testnet will commence on the date prescribed by the Company and continue until terminated by the Company in its sole discretion. Notwithstanding any other information provided by the Company regarding the Testnet (including on the Website, blog posts or through other communications (such as forums, Telegram, Github, Discord, or other channels)), the Company may change, discontinue, or terminate, temporarily or permanently, all or any part of the Testnet, at any time and without notice, at its sole discretion (including prior to providing any incentives or rewards). The Company may retain control or upgradeability over certain aspects of the Testnet that it will not retain on Mainnet.
	3. The Testnet Eligibility. Your participation in the Testnet (or any portion thereof) may be subject to eligibility criteria determined by the Company in its sole discretion (including, without limitation, geographical distribution and applicant reputation). By applying or registering, there is no promise or guarantee that you will be able to participate in the Testnet. Notwithstanding any other information provided by the Company regarding the Testnet (including on the Website, blog posts or through other communications (such as forums, Telegram, Github, Discord, or other channels)), the Company may change or modify at any time the number of participants eligible to participate in the Testnet or the requirements of the Testnet and terminate any participant's participation in the Testnet at any time. The Testnet may operate in certain phases. Your selection or participation in any one phase of the Testnet does not imply that you will be selected for any other phases of the Testnet. The Company reserves the right to block your access to the Testnet at any time in its sole discretion.
	4. No Monetary Value. In your use of the Testnet, you may interact with or transfer certain cryptocurrencies or other digital assets on the Testnet ("**Testnet Tokens**"), such as Testnet Tokens obtained through a faucet. Testnet Tokens are not, and shall never convert to or accrue to become any other tokens or virtual assets. Testnet Tokens are virtual items with no monetary value. Testnet Tokens do not constitute any currency or property of any type and are not redeemable, refundable, or eligible for any fiat or digital currency or anything else of value. Testnet Tokens are not transferable between users outside of the Testnet, and you may not attempt to sell, trade, or transfer any Testnet Tokens outside of the Testnet, or obtain any manner of credit using any Testnet Tokens. Any attempt to sell, trade, or transfer any Testnet Tokens outside of the Testnet will be null and void. Testnet Tokens will not be converted into any future rewards offered by the Company.
4. **Location of Our Privacy Policy**


	1. Privacy Policy. Our Privacy Policy describes how we handle the information you provide to us when you use the Services. For an explanation of our privacy practices, please visit our [Privacy Policy here](/eigenlayer/legal/eigenlayer-privacy-policy).
	2. Research Forum Community Guidelines. Our Research Forum Community Guidelines available at [https://research.eigenlayer.xyz/t/welcome\-to\-eigenlayer\-research/4](https://research.eigenlayer.xyz/t/welcome-to-eigenlayer-research/4) describe our rules of behavior and engagement when you use the Research Forum, which are intended to foster a positive and engaging community. All content that you upload or share to the Research Forum must comply with the Research Forum Community Guidelines.
5. **Rights We Grant You**


	1. Right to Use Services. We hereby permit you to use the Services for your personal non\-commercial use only, provided that you comply with these Terms in connection with all such use. If any software, content or other materials owned or controlled by us are distributed to you as part of your use of the Services, we hereby grant you, a personal, non\-assignable, non\-sublicensable, non\-transferrable, and non\-exclusive right and license to access and display such software, content and materials provided to you as part of the Services, in each case for the sole purpose of enabling you to use the Services as permitted by these Terms. Your access and use of the Services may be interrupted from time to time for any of several reasons, including, without limitation, the malfunction of equipment, periodic updating, maintenance or repair of the Service or other actions that Company, in its sole discretion, may elect to take.
	2. Right to Use Our APIs. Subject to these Terms, we hereby grant you a non\-exclusive, non\-transferable, non\-sublicensable, worldwide, revocable right and license to use our APIs for the limited purposes set forth in the documentation for the Services. Your use of our APIs must comply with the technical documentation, usage guidelines call volume limits, and other documentation maintained at <https://docs.eigenlayer.xyz/> or such other location we may designate from time to time. We may terminate your right to use the API from time to time at any time.
	3. Restrictions On Your Use of the Services. You may not do any of the following in connection with your use of the Services, unless applicable laws or regulations prohibit these restrictions or you have our written permission to do so:
		1. download, modify, copy, distribute, transmit, display, perform, reproduce, duplicate, publish, license, create derivative works from, or offer for sale any information contained on, or obtained from or through, the Services, except for temporary files that are automatically cached by your web browser for display purposes, or as otherwise expressly permitted in these Terms;
		2. duplicate, decompile, reverse engineer, disassemble or decode the Services (including any underlying idea or algorithm), or attempt to do any of the same;
		3. use, reproduce or remove any copyright, trademark, service mark, trade name, slogan, logo, image, or other proprietary notation displayed on or through the Services;
		4. use automation software (bots), hacks, modifications (mods) or any other unauthorized third\-party software designed to modify the Services;
		5. exploit the Services for any commercial purpose, including without limitation communicating or facilitating any commercial advertisement or solicitation;
		6. access or use the Services in any manner that could disable, overburden, damage, disrupt or impair the Services or interfere with any other party's access to or use of the Services or use any device, software or routine that causes the same;
		7. attempt to gain unauthorized access to, interfere with, damage or disrupt the Services, accounts registered to other users, or the computer systems, wallets, accounts, protocols or networks connected to the Services;
		8. circumvent, remove, alter, deactivate, degrade or thwart any technological measure or content protections of the Services or the computer systems, wallets, accounts, protocols or networks connected to the Services;
		9. use any robot, spider, crawlers or other automatic device, process, software or queries that intercepts, "mines," scrapes or otherwise accesses the Services to monitor, extract, copy or collect information or data from or through the Services, or engage in any manual process to do the same;
		10. introduce any viruses, trojan horses, worms, logic bombs or other materials that are malicious or technologically harmful into our systems;
		11. submit, transmit, display, perform, post or store any content that is inaccurate, unlawful, defamatory, obscene, lewd, lascivious, filthy, excessively violent, pornographic, invasive of privacy or publicity rights, harassing, threatening, abusive, inflammatory, harmful, hateful, cruel or insensitive, deceptive, or otherwise objectionable, use the Services for illegal, harassing, bullying, unethical or disruptive purposes, or otherwise use the Services in a manner that is obscene, lewd, lascivious, filthy, excessively violent, harassing, harmful, hateful, cruel or insensitive, deceptive, threatening, abusive, inflammatory, pornographic, inciting, organizing, promoting or facilitating violence or criminal or harmful activities, defamatory, obscene or otherwise objectionable;
		12. violate any applicable law or regulation in connection with your access to or use of the Services; or
		13. access or use the Services in any way not expressly permitted by these Terms.
	4. Interactions with Other Users on the Services. You are responsible for your interactions with other users on or through the Services. While we reserve the right to monitor interactions between users, we are not obligated to do so, and we cannot be held liable for your interactions with other users, or for any user's actions or inactions. If you have a dispute with one or more users, you release us (and our affiliates and subsidiaries, and our and their respective officers, directors, employees and agents) from claims, demands and damages (actual and consequential) of every kind and nature, known and unknown, arising out of or in any way connected with such disputes. In entering into this release you expressly waive any protections (whether statutory or otherwise) that would otherwise limit the coverage of this release to include only those claims which you may know or suspect to exist in your favor at the time of agreeing to this release.
6. **Ownership and Content**


	1. Ownership of the Services. The Services, including their "look and feel" (e.g., text, graphics, images, logos), proprietary content, information and other materials, are protected under copyright, trademark and other intellectual property laws. You agree that the Company and/or its licensors own all right, title and interest in and to the Services (including any and all intellectual property rights therein) and you agree not to take any action(s) inconsistent with such ownership interests. We and our licensors reserve all rights in connection with the Services and its content, including, without limitation, the exclusive right to create derivative works.
	2. Ownership of Trademarks. The Company's name, trademarks and logos and all related names, logos, product and service names, designs and slogans are trademarks of the Company or its affiliates or licensors. Other names, logos, product and service names, designs and slogans that appear on the Services are the property of their respective owners, who may or may not be affiliated with, connected to, or sponsored by us.
	3. Ownership of Feedback. We welcome feedback, bug reports, comments and suggestions for improvements to the Services ("**Feedback**"). You acknowledge and expressly agree that any contribution of Feedback does not and will not give or grant you any right, title or interest in the Services or in any such Feedback. All Feedback becomes the sole and exclusive property of the Company, and the Company may use and disclose Feedback in any manner and for any purpose whatsoever without further notice or compensation to you and without retention by you of any proprietary or other right or claim. You hereby assign to the Company any and all right, title and interest (including, but not limited to, any patent, copyright, trade secret, trademark, show\-how, know\-how, moral rights and any and all other intellectual property right) that you may have in and to any and all Feedback.
	4. Your Content License Grant. In connection with your use of the Services, you may be able to post, upload, or submit content to be made available through the Services ("Your Content"), including on our Research Forum. In order to operate the Service, we must obtain from you certain license rights in Your Content so that actions we take in operating the Service are not considered legal violations. Accordingly, by using the Service and uploading Your Content, you grant us a license to access, use, host, cache, store, reproduce, transmit, display, publish, distribute, and modify (for technical purposes, e.g., making sure content is viewable on smartphones as well as computers and other devices) Your Content but solely as required to be able to operate, improve and provide the Services. You agree that these rights and licenses are royalty free, transferable, sub\-licensable, worldwide and irrevocable (for so long as Your Content is stored with us), and include a right for us to make Your Content available to, and pass these rights along to, others with whom we have contractual relationships related to the provision of the Services, solely for the purpose of providing such Services, and to otherwise permit access to or disclose Your Content to third parties if we determine such access is necessary to comply with our legal obligations. As part of the foregoing license grant you agree that the other users of the Services shall have the right to comment on and/or tag Your Content and/or to use, publish, display, modify or include a copy of Your Content as part of their own use of the Services; except that the foregoing shall not apply to any of Your Content that you post privately for non\-public display on the Services. To the fullest extent permitted by applicable law, the Company reserves the right, and has absolute discretion, to remove, screen, edit, or delete any of Your Content at any time, for any reason, and without notice. By posting or submitting Your Content through the Services, you represent and warrant that you have, or have obtained, all rights, licenses, consents, permissions, power and/or authority necessary to grant the rights granted herein for Your Content. You agree that Your Content will not contain material subject to copyright or other proprietary rights, unless you have the necessary permission or are otherwise legally entitled to post the material and to grant us the license described above.
	5. Notice of Infringement \-\- DMCA (Copyright) Policy.If you believe that any text, graphics, photos, audio, videos or other materials or works uploaded, downloaded or appearing on the Services have been copied in a way that constitutes copyright infringement, you may submit a notification to our copyright agent in accordance with 17 USC 512(c) of the Digital Millennium Copyright Act (the "**DMCA**"), by providing the following information in writing:


	1. identification of the copyrighted work that is claimed to be infringed;
	2. identification of the allegedly infringing material that is requested to be removed, including a description of where it is located on the Service;
	3. information for our copyright agent to contact you, such as an address, telephone number and e\-mail address;
	4. a statement that you have a good faith belief that the identified, allegedly infringing use is not authorized by the copyright owners, its agent or the law;
	5. a statement that the information above is accurate, and under penalty of perjury, that you are the copyright owner or the authorized person to act on behalf of the copyright owner; and
	6. the physical or electronic signature of a person authorized to act on behalf of the owner of the copyright or of an exclusive right that is allegedly infringed.Notices of copyright infringement claims should be sent by mail to: Eigen Labs, Inc., Attn: Legal, 15790 Redmond Way \#1176 Redmond, WA 98052 ; or by e\-mail to [\[email protected]](/cdn-cgi/l/email-protection#a2cccdd6cbc1c7d1e2c7cbc5c7cccec3c0d18ccdd0c5). It is our policy, in appropriate circumstances and at our discretion, to disable or terminate the accounts of users who repeatedly infringe copyrights or intellectual property rights of others.


A user of the Services who has uploaded or posted materials identified as infringing as described above may supply a counter\-notification pursuant to sections 512(g)(2\) and (3\) of the DMCA. When we receive a counter\-notification, we may reinstate the posts or material in question, in our sole discretion. To file a counter\-notification with us, you must provide a written communication (by fax or regular mail or by email) that sets forth all of the items required by sections 512(g)(2\) and (3\) of the DMCA. Please note that you will be liable for damages if you materially misrepresent that content or an activity is not infringing the copyrights of others.
7. **Third Party Services and Materials**


	1. Third Party Services and Materials. The Services may allow you to browse the availability of certain (i) actively validated services (“**AVSs**”) (ii) operators that offer to run certain AVSs in connection with your restaked digital assets and/or (iii) other services or products developed or run by third parties displayed on the Services, including the App (“**Third\-Party Services**”) and may display, include or make available content, data, information, applications or materials from third parties (“**Third\-Party Materials**”) or provide links to certain third party websites. The Company does not endorse or recommend any Third\-Party Materials, the use of any provider of any Third\-Party Services, or the restaking or delegation of any assets to any Third\-Party Services. You agree that your access and use of such Third\-Party Services and Third\-Party Materials is governed solely by the terms and conditions of such Third\-Party Services and Third\-Party Materials, as applicable. The Company is not responsible or liable for, and make no representations as to any aspect of such Third\-Party Materials and Third\-Party Services, including, without limitation, their content or the manner in which they handle, protect, manage or process data or any interaction between you and the provider of such Third\-Party Services. The Company is not responsible for examining or evaluating the content, accuracy, completeness, availability, timeliness, validity, copyright compliance, legality, decency, quality, security or any other aspect of such Third Party Services or Third Party Materials or websites. You irrevocably waive any claim against the Company with respect to such Third\-Party Services and Third\-Party Materials. We are not liable for any damage or loss caused or alleged to be caused by or in connection with your enablement, access or use of any such Third\-Party Services or Third\-Party Materials, or your reliance on the privacy practices, data security processes or other policies of such Third\-Party Services. Third\-Party Services, Third\-Party Materials and links to other websites are provided solely as a convenience to you. Certain Third\-Party Services or Third\-Party Materials may automatically populate on the Company’s Services. The Company reserves the right to remove any Third\-Party Services or Third\-Party Materials from the Services, including without limitation, any AVSs or operators for any reason whatsoever.
8. **Disclaimers, Limitations of Liability and Indemnification**


	1. Disclaimers. Your access to and use of the Services and any Protocols are at your own risk. You understand and agree that the Services are provided to you on an "AS IS" and "AS AVAILABLE" basis. Without limiting the foregoing, to the maximum extent permitted under applicable law, the Company, its parents, affiliates, related companies, officers, directors, employees, agents, representatives, partners and licensors (the "**Company Entities**") and MultiSig Committee Members (as defined below) DISCLAIM ALL WARRANTIES AND CONDITIONS, WHETHER EXPRESS, IMPLIED OR STATUTORY, INCLUDING WITHOUT LIMITATION ANY WARRANTIES RELATING TO TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON\-INFRINGEMENT, USAGE, QUALITY, PERFORMANCE, SUITABILITY OR FITNESS OF THE SERVICES AND THE PROTOCOLS FOR ANY PARTICULAR PURPOSE, OR AS TO THE ACCURACY, QUALITY, SEQUENCE, RELIABILITY, WORKMANSHIP OR TECHNICAL CODING THEREOF, OR THE ABSENCE OF ANY DEFECTS THEREIN WHETHER LATENT OR PATENT. The Company Entities and MultiSig Committee Members make no warranty or representation and disclaim all responsibility and liability for: (a) the completeness, accuracy, availability, timeliness, security or reliability of the Services, including the Research Forum, and the Protocols; (b) any harm to your computer system, loss of data, or other harm that results from your access to or use of the Services or the Protocols; (c) the operation or compatibility with any other application or any particular system or device, including any Wallets; (d) whether the Services or the Protocols will meet your requirements or be available on an uninterrupted, secure or error\-free basis; and (e) the deletion of, or the failure to store or transmit, Your Content and other communications maintained by the Services. No advice or information, whether oral or written, obtained from the Company Entities or the MultiSig Committee Members or through the Services, including the Research Forum, will create any warranty or representation not expressly made herein. You should not rely on the Services, including the Research Forum, for advice of any kind, including legal, tax, investment, financial or other professional advice.
	2. Limitations of Liability. TO THE EXTENT NOT PROHIBITED BY LAW, YOU AGREE THAT IN NO EVENT WILL THE COMPANY ENTITIES AND MULTISIG COMMITTEE MEMBERS BE LIABLE (A) FOR DAMAGES OF ANY KIND, INCLUDING DIRECT, INDIRECT, SPECIAL, EXEMPLARY, INCIDENTAL, CONSEQUENTIAL OR PUNITIVE DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES, LOSS OF USE, DATA OR PROFITS, BUSINESS INTERRUPTION OR ANY OTHER DAMAGES OR LOSSES, ARISING OUT OF OR RELATED TO YOUR USE OR INABILITY TO USE THE SERVICES), HOWEVER CAUSED AND UNDER ANY THEORY OF LIABILITY, WHETHER UNDER THESE TERMS OR OTHERWISE ARISING IN ANY WAY IN CONNECTION WITH THE SERVICES OR THESE TERMS AND WHETHER IN CONTRACT, STRICT LIABILITY OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) EVEN IF THE COMPANY ENTITIES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE, OR (B) FOR ANY OTHER CLAIM, DEMAND OR DAMAGES WHATSOEVER RESULTING FROM OR ARISING OUT OF OR IN CONNECTION WITH THESE TERMS OR THE DELIVERY, USE OR PERFORMANCE OF THE SERVICES. THE COMPANY ENTITIES' AND MULTISIG COMMITTEE MEMBERS' TOTAL LIABILITY TO YOU FOR ANY DAMAGES FINALLY AWARDED SHALL NOT EXCEED ONE HUNDRED DOLLARS ($100\.00\) RESPECTIVELY. SOME JURISDICTIONS (SUCH AS THE STATE OF NEW JERSEY) DO NOT ALLOW THE EXCLUSION OR LIMITATION OF INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO THE ABOVE EXCLUSION OR LIMITATION MAY NOT APPLY TO YOU.
	3. Assumption of Risks.
		1. By using the Services, you represent that you have sufficient knowledge and experience in business and financial matters, including a sufficient understanding of blockchain or cryptographic tokens and technologies and other digital assets, storage mechanisms (such as Wallets), blockchain\-based software systems, and blockchain technology, to be able to assess and evaluate the risks and benefits of the Services contemplated hereunder, and will bear the risks thereof, including loss of all amounts paid, and the risk that the tokens may have little or no value. You acknowledge and agree that there are risks associated with purchasing and holding cryptocurrency, using blockchain technology and staking cryptocurrency. These include, but are not limited to, risk of losing access to cryptocurrency due to slashing, loss of private key(s), custodial error or purchaser error, risk of mining or blockchain attacks, risk of hacking and security weaknesses, risk of unfavorable regulatory intervention in one or more jurisdictions, risk related to token taxation, risk of personal information disclosure, risk of uninsured losses, volatility risks, and unanticipated risks. You acknowledge that cryptocurrencies are not (i) deposits of or guaranteed by a bank (ii) insured by the FDIC or by any other governmental agency and (iii) that we do not custody and cannot transfer any cryptocurrency or digital assets you may interact with on the Services or Protocols.
		2. There are certain multi\-signature crypto wallets (the "**MultiSigs**", and the signatories to such MultiSigs, the "**MultiSig Committee Members**") that have certain controls related to one or more of the Protocols, that may include, but are not limited to, the ability to pause certain functionality of the Protocols, reverse or pause slashing, implement or influence upgrades to the Protocols (or any aspect thereof) and certain other controls of the functionality of the Protocols as described in the documentation or in public communications made by us. Certain MultiSigs may be controlled by us or MultiSig Committee Members that are employed or engaged by us, and certain other MultiSigs will be controlled partially or entirely by MultiSig Committee Members that are unaffiliated third parties over which we have no or limited control. We will not be able to control the actions of such MultiSig Committee Members if they are not employed or engaged by us and thus certain MultiSigs will be outside of our control.
		3. The regulatory regime governing blockchain technologies, cryptocurrencies and other digital assets is uncertain, and new regulations or policies may materially adversely affect the potential utility or value of such cryptocurrencies and digital assets. There also exists the risks of new taxation of the purchase or sale of cryptocurrencies and other digital assets.
		4. We cannot control how third\-party exchange platforms quote or value cryptocurrencies and other digital assets and we expressly deny and disclaim any liability to you and deny any obligations to indemnify or hold you harmless for any losses you may incur as a result of fluctuations in the value of cryptocurrencies or other digital assets.
		5. Smart contracts execute automatically when certain conditions are met. Since smart contracts typically cannot be stopped or reversed, vulnerabilities in their programming and design or other vulnerabilities that may arise due to hacking or other security incidents can have adverse effects to restaked assets, including but not limited to significant volatility and risk of loss.
		6. Certain protocols and networks subject staked assets to slashing upon certain conditions, including, but not limited to, if a validator or operator engages in harmful or malicious behavior, fails to perform their role as a validator or operator properly, or incorrectly validates a transaction, and we expressly deny and disclaim any liability to you and deny any obligations to indemnify or hold you harmless for any losses you may incur as a result of slashing.
		7. Certain protocols and networks require that a certain amount of staked assets be locked for a certain period of time while staking, and withdrawal of staked assets may be delayed. We do not guarantee the security or functionality of any third\-party protocol, software or technology intended to be compatible with restaked assets.
	4. Indemnification. By entering into these Terms and accessing or using the Services, you agree that you shall defend, indemnify and hold the Company Entities and MultiSig Committee Members harmless from and against any and all claims, costs, damages, losses, liabilities and expenses (including attorneys’ fees and costs) incurred by the Company Entities or MultiSig Committee Members arising out of or in connection with: (a) your violation or breach of any term of these Terms or any applicable law or regulation; (b) your violation of any rights of any third party; (c) your misuse of the Services; or (d) your negligence or wilful misconduct; or (e) your Content. If you are obligated to indemnify any Company Entity or MultiSig Committee Members hereunder, then you agree that the Company (or, at its discretion, the applicable Company Entity) or MultiSig Committee Members, as applicable, will have the right, in its sole discretion, to control any action or proceeding and to determine whether the Company or MultiSig Committee Member, as applicable, wishes to settle, and if so, on what terms, and you agree to fully cooperate with the Company or MultiSig Committee Members in the defense or settlement of such claim.
	5. Third Party Beneficiaries. You and the Company acknowledge and agree that the Company Entities (other than the Company) and the MultiSig Committee Members are third party beneficiaries of these Terms, including under Section 8 and 9\.
9. **ARBITRATION AND CLASS ACTION WAIVER**


	1. PLEASE READ THIS SECTION CAREFULLY \-\- IT MAY SIGNIFICANTLY AFFECT YOUR LEGAL RIGHTS, INCLUDING YOUR RIGHT TO FILE A LAWSUIT IN COURT AND TO HAVE A JURY HEAR YOUR CLAIMS. IT CONTAINS PROCEDURES FOR MANDATORY BINDING ARBITRATION AND A CLASS ACTION WAIVER.
	2. Informal Process First. You and the Company agree that in the event of any dispute between you and the Company Entities or the MultiSig Committee Members, either party will first contact the other party and make a good faith sustained effort to resolve the dispute before resorting to more formal means of resolution, including without limitation, any court action, after first allowing the receiving party 30 days in which to respond. Both you and the Company agree that this dispute resolution procedure is a condition precedent which must be satisfied before initiating any arbitration against you, any Company Entity or any MultiSig Committee Members, as applicable.
	3. Arbitration Agreement and Class Action Waiver. After the informal dispute resolution process, any remaining dispute, controversy, or claim (collectively, "**Claim**") relating in any way to the Services, including the App, any use or access or lack of access thereto, and any other usage of the Protocols even if interacted with outside of the Services or App, will be resolved by arbitration, including threshold questions of arbitrability of the Claim. You and the Company agree that any Claim will be settled by final and binding arbitration, using the English language, administered by JAMS under its Comprehensive Arbitration Rules and Procedures (the "**JAMS Rules**") then in effect (those rules are deemed to be incorporated by reference into this section, and as of the date of these Terms). Because your contract with the Company, these Terms, and this Arbitration Agreement concern interstate commerce, the Federal Arbitration Act ("FAA") governs the arbitrability of all disputes. However, the arbitrator will apply applicable substantive law consistent with the FAA and the applicable statute of limitations or condition precedent to suit. Arbitration will be handled by a sole arbitrator in accordance with the JAMS Rules. Judgment on the arbitration award may be entered in any court that has jurisdiction. Any arbitration under these Terms will take place on an individual basis \-\- class arbitrations and class actions are not permitted. You understand that by agreeing to these Terms, you and the Company are each waiving the right to trial by jury or to participate in a class action or class arbitration.
	4. Exceptions. Notwithstanding the foregoing, you and the Company agree that the following types of disputes will be resolved in a court of proper jurisdiction: (i) disputes or claims within the jurisdiction of a small claims court consistent with the jurisdictional and dollar limits that may apply, as long as it is brought and maintained as an individual dispute and not as a class, representative, or consolidated action or proceeding; (ii) disputes or claims where the sole form of relief sought is injunctive relief (including public injunctive relief); or (iii) intellectual property disputes.
	5. Costs of Arbitration. Payment of all filing, administration, and arbitrator costs and expenses will be governed by the JAMS Rules, except that if you demonstrate that any such costs and expenses owed by you under those rules would be prohibitively more expensive than a court proceeding, the Company will pay the amount of any such costs and expenses that the arbitrator determines are necessary to prevent the arbitration from being prohibitively more expensive than a court proceeding (subject to possible reimbursement as set forth below).
	
	
		1. Fees and costs may be awarded as provided pursuant to applicable law. If the arbitrator finds that either the substance of your claim or the relief sought in the Demand is frivolous or brought for an improper purpose (as measured by the standards set forth in Federal Rule of Civil Procedure 11(b)), then the payment of all fees will be governed by the JAMS rules. In that case, you agree to reimburse the Company for all monies previously disbursed by it that are otherwise your obligation to pay under the applicable rules. If you prevail in the arbitration and are awarded an amount that is less than the last written settlement amount offered by the Company before the arbitrator was appointed, the Company will pay you the amount it offered in settlement. The arbitrator may make rulings and resolve disputes as to the payment and reimbursement of fees or expenses at any time during the proceeding and upon request from either party made within fourteen (14\) days of the arbitrator's ruling on the merits.
	6. **Opt\-Out. You have the right to opt\-out and not be bound by the arbitration provisions set forth in these Terms by sending written notice of your decision to opt\-out to [\[email protected]](/cdn-cgi/l/email-protection#c4aaabb0ada7a1b784a1ada3a1aaa8a5a6b7eaabb6a3). The notice must be sent to the Company within thirty (30\) days of your first registering to use the Services or agreeing to these Terms; otherwise you shall be bound to arbitrate disputes on a non\-class basis in accordance with these Terms. If you opt out of only the arbitration provisions, and not also the class action waiver, the class action waiver still applies. You may not opt out of only the class action waiver and not also the arbitration provisions. If you opt\-out of these arbitration provisions, the Company also will not be bound by them.**
	7. WAIVER OF RIGHT TO BRING CLASS ACTION AND REPRESENTATIVE CLAIMS. TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, YOU AND THE COMPANY EACH AGREE THAT ANY PROCEEDING TO RESOLVE ANY DISPUTE, CLAIM OR CONTROVERSY WILL BE BROUGHT AND CONDUCTED ONLY IN THE RESPECTIVE PARTY'S INDIVIDUAL CAPACITY AND NOT AS PART OF ANY CLASS (OR PURPORTED CLASS), CONSOLIDATED, MULTIPLE\-PLAINTIFF, OR REPRESENTATIVE ACTION OR PROCEEDING ("CLASS ACTION"). YOU AND THE COMPANY AGREE TO WAIVE THE RIGHT TO PARTICIPATE AS A PLAINTIFF OR CLASS MEMBER IN ANY CLASS ACTION. YOU AND THE COMPANY EXPRESSLY WAIVE ANY ABILITY TO MAINTAIN A CLASS ACTION IN ANY FORUM. IF THE DISPUTE IS SUBJECT TO ARBITRATION, THE ARBITRATOR WILL NOT HAVE THE AUTHORITY TO COMBINE OR AGGREGATE CLAIMS, CONDUCT A CLASS ACTION, OR MAKE AN AWARD TO ANY PERSON OR ENTITY NOT A PARTY TO THE ARBITRATION. FURTHER, YOU AND THE COMPANY AGREE THAT THE ARBITRATOR MAY NOT CONSOLIDATE PROCEEDINGS FOR MORE THAN ONE PERSON'S CLAIMS, AND IT MAY NOT OTHERWISE PRESIDE OVER ANY FORM OF A CLASS ACTION. FOR THE AVOIDANCE OF DOUBT, HOWEVER, YOU CAN SEEK PUBLIC INJUNCTIVE RELIEF TO THE EXTENT AUTHORIZED BY LAW AND CONSISTENT WITH THE EXCEPTIONS CLAUSE ABOVE.
	3\. IF THIS CLASS ACTION WAIVER IS LIMITED, VOIDED, OR FOUND UNENFORCEABLE, THEN, UNLESS THE PARTIES MUTUALLY AGREE OTHERWISE, THE PARTIES' AGREEMENT TO ARBITRATE SHALL BE NULL AND VOID WITH RESPECT TO SUCH PROCEEDING SO LONG AS THE PROCEEDING IS PERMITTED TO PROCEED AS A CLASS ACTION. IF A COURT DECIDES THAT THE LIMITATIONS OF THIS PARAGRAPH ARE DEEMED INVALID OR UNENFORCEABLE, ANY PUTATIVE CLASS, PRIVATE ATTORNEY GENERAL OR CONSOLIDATED OR REPRESENTATIVE ACTION MUST BE BROUGHT IN A COURT OF PROPER JURISDICTION AND NOT IN ARBITRATION.
10. **Additional Provisions**


	1. Updating These Terms. We may modify these Terms from time to time in which case we will update the "**Last Revised**" date at the top of these Terms. If we make changes that are material, we will use reasonable efforts to attempt to notify you, such as by e\-mail and/or by placing a prominent notice on the first page of the Website. However, it is your sole responsibility to review these Terms from time to time to view any such changes. The updated Terms will be effective as of the time of posting, or such later date as may be specified in the updated Terms. Your continued access or use of the Services after the modifications have become effective will be deemed your acceptance of the modified Terms. No amendment shall apply to a dispute for which an arbitration has been initiated prior to the change in Terms.
	2. Suspension; Termination. If you breach any of the provisions of these Terms, all licenses granted by the Company will terminate automatically. Additionally, the Company may, in its sole discretion, suspend or terminate your Account and/or access to or use of any of the Services, with or without notice, for any or no reason, including, without limitation, (i) if we believe, in our sole discretion, you have engaged in any of the prohibited activities set forth in Section 5\.3; (ii) if you provide any incomplete, incorrect or false information to us; (iii) if you have breached any portion of these Terms; (iv) if we suspect you may be a Prohibited Person or any Wallet used to access the Services is linked with any illegal or high\-risk activity; and/or (v) if we determine such action is necessary to comply with these Terms, any of our policies, procedures or practices, or any law rule or regulation. If the Company deletes your Account for any suspected breach of these Terms by you, you are prohibited from re\-registering for the Services under a different name. In the event of Account deletion for any reason, the Company may, but is not obligated to, delete any of Your Content. the Company shall not be responsible for the failure to delete or deletion of Your Content. All sections which by their nature should survive the termination of these Terms shall continue in full force and effect subsequent to and notwithstanding any termination of this Agreement by the Company or you. Termination will not limit any of the Company’s other rights or remedies at law or in equity.
	3. Injunctive Relief. You agree that a breach of these Terms will cause irreparable injury to the Company for which monetary damages would not be an adequate remedy and the Company shall be entitled to equitable relief in addition to any remedies it may have hereunder or at law without a bond, other security or proof of damages.
	4. California Residents. If you are a California resident, in accordance with Cal. Civ. Code § 1789\.3, you may report complaints to the Complaint Assistance Unit of the Division of Consumer Services of the California Department of Consumer Affairs by contacting them in writing at 1625 North Market Blvd., Suite N 112 Sacramento, CA 95834, or by telephone at (800\) 952\-5210\.
	5. Export Laws. You agree that you will not export or re\-export, directly or indirectly, the Services and/or other information or materials provided by the Company hereunder, to any country for which the United States or any other relevant jurisdiction requires any export license or other governmental approval at the time of export without first obtaining such license or approval. In particular, but without limitation, the Services may not be exported or re\-exported (a) into any U.S. embargoed countries or any country that has been designated by the U.S. Government as a "terrorist supporting" country, or (b) to anyone listed on any U.S. Government list of prohibited or restricted parties, including the U.S. Treasury Department's list of Specially Designated Nationals or the U.S. Department of Commerce Denied Person's List or Entity List. By using the Services, you represent and warrant that you are not located in any such country or on any such list. You are responsible for and hereby agree to comply at your sole expense with all applicable United States export laws and regulations.
	6. Force Majeure. We will not be liable or responsible to you, nor be deemed to have defaulted under or breached these Terms, for any failure or delay in fulfilling or performing any of our obligations under these Terms or in providing the Services, when and to the extent such failure or delay is caused by or results from any events beyond our ability to control, including acts of God; flood, fire, earthquake, epidemics, pandemics, tsunami, explosion, war, invasion, hostilities (whether war is declared or not), terrorist threats or acts, riot or other civil unrest, government order, law, or action, embargoes or blockades, strikes, labor stoppages or slowdowns or other industrial disturbances, shortage of adequate or suitable Internet connectivity, telecommunication breakdown or shortage of adequate power or electricity, and other similar events beyond our control.
	7. Miscellaneous. If any provision of these Terms shall be unlawful, void or for any reason unenforceable, then that provision shall be deemed severable from these Terms and shall not affect the validity and enforceability of any remaining provisions. These Terms and the licenses granted hereunder may be assigned by the Company but may not be assigned by you without the prior express written consent of the Company. No waiver by either party of any breach or default hereunder shall be deemed to be a waiver of any preceding or subsequent breach or default. The section headings used herein are for reference only and shall not be read to have any legal effect. The Services are operated by us in the United States. Those who choose to access the Services from locations outside the United States do so at their own initiative and are responsible for compliance with applicable local laws. These Terms are governed by the laws of the State of New York, without regard to conflict of laws rules, and the proper venue for any disputes arising out of or relating to any of the same will be the state and federal courts located in New York, New York.
	8. How to Contact Us. You may contact us regarding the Services or these Terms by e\-mail at **[\[email protected]](/cdn-cgi/l/email-protection#96f8f9e2fff5f3e5d6f3fff1f3f8faf7f4e5b8f9e4f1)**.
[PreviousEigenLayer Privacy Policy](/eigenlayer/legal/eigenlayer-privacy-policy)[NextContract Addresses and Docs](/eigenlayer/deployed-contracts/)

* 
* Operator Guides
* Operator Security Risks, Mitigations, and Best Practices
On this pageOperator Security Risks
=======================


Malicious AVS[​](#malicious-avs "Direct link to Malicious AVS")
---------------------------------------------------------------


* Guest container breaking into host machine:


	+ Kernel Exploits: Containers share the same kernel as the host. If there are vulnerabilities in the kernel, a container might exploit them to gain elevated privileges on the host.
	+ Escape to Host: There have been vulnerabilities in the past that allowed processes within a container to escape and get access to the host. This is especially dangerous if containers are run with elevated privileges.
	+ Inter\-container Attacks: If one container is compromised, an attacker might try to move laterally to other containers on the same host.
* Access to the host’s network. Because containers run in a home stakers environment, they have access to a home network or a k8s environment.
* Malware in the container or via a supply chain attack or AVS is malicious.


AVS Implementation and Deployment Bugs[​](#avs-implementation-and-deployment-bugs "Direct link to AVS Implementation and Deployment Bugs")
------------------------------------------------------------------------------------------------------------------------------------------


* Running outdated software.
* Misconfigured ports and services open to the internet.
* Running containers with elevated privileges.


What can operators do to mitigate malicious AVS risks?
======================================================


Operator Best Practices[​](#operator-best-practices "Direct link to Operator Best Practices")
---------------------------------------------------------------------------------------------


* Regularly update and patch containers and the host system.
* Don't share your keys between AVSs / ETH validator. Refer to key management section.
* Monitor container runtime (logs) behavior for any suspicious activities and setup alerts as relevant.
* Do not run containers with privileged flag.It can give them almost unrestricted access to the host.
* Limit Resources to a container so it doesn’t take down the cluster / node
* Data Theft: Do not mount entire volumes into containers to prevent data leak, container escapes etc.
* Follow Network Access / Least privilege principles in your organization to reduce attack surface


Infrastructure[​](#infrastructure "Direct link to Infrastructure")
------------------------------------------------------------------


General


* Only allow Network traffic to ports / from whitelisted ip's required by the AVS.
* Do not expose critical services like ssh to the internet.
* Configure your firewall with a DENY ALL approach and explicitly allow traffic that is required.


Docker Infra


* Network Segmentation: Use Docker's network policies to segment containers and limit inter\-container communication.
* Regular Audits: audit and monitor container activities using tools like \- Docker Bench for Security or Clair.
* Isolation
	+ Through VMs: lightweight VMs (like Kata Containers or gVisor) combine container \- flexibility with VM isolation.
	+ User namespaces, seccomp, AppArmor, and SELinux etc can help further restrict the container.


K8’s Infra


* Network Segmentation: Limit the services your AVSs can talk to. Follow least privilege principles via [Kubernetes Documentation Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).


Incident Response Plan:


* Have a plan in place for how to respond if a container is compromised. This includes isolating affected containers, analyzing, and restoring services.
* Regular Backups: Regularly backup your data and configurations to recover from any malicious changes.
* Stay Updated: Always keep an eye on Docker's official documentation, security advisories, and community forums for the latest best practices and updates.
[PreviousTroubleshooting](/eigenlayer/operator-guides/troubleshooting)[NextIntroduction](/eigenlayer/operator-guides/key-management/intro)* [Malicious AVS](#malicious-avs)
* [AVS Implementation and Deployment Bugs](#avs-implementation-and-deployment-bugs)
* [Operator Best Practices](#operator-best-practices)
* [Infrastructure](#infrastructure)


* 
* Operator Guides
* EigenLayer Node Classes
On this pageEigenLayer Node Classes
=======================


EigenLayer is introducing a standardized set of node classes for AVS developers and node operators to use as a coordination tool that will aid in the emergence of an efficient marketplace.


EigenLayer's standardized node classes enable AVS developers to communicate system requirements, reducing complexity in development processes. These classes categorize nodes based on their capabilities, performance characteristics, and other relevant attributes. This standardization means developers can choose a node class that aligns with their application's specific needs without having to delve into the technicalities of each individual node


For node operators, this standardization means supporting fewer system types, streamlining their operations and focusing their resources more effectively. This can be achieved by applying the following strategies:


1. **Adoption of Standardized Node Classes**: By adopting the standardized node classes defined by EigenLayer, node operators can categorize their nodes into these predefined classes. This categorization means they no longer need to support a wide range of custom configurations or unique system types tailored to individual developers' specifications. Instead, they can align their nodes with these standard classes.
2. **Infrastructure Optimization**: Node operators can optimize their infrastructure to efficiently support these standardized classes. This might involve upgrading hardware, tuning software, or adjusting network capacities to align with the specific requirements of each class. By focusing on a limited number of optimized configurations, operators can reduce the complexity and diversity of their systems.
3. **Resource Allocation and Management**: With fewer system types to support, node operators can more effectively allocate and manage their resources. This includes better utilization of computational power, storage, and network bandwidth, as well as more efficient deployment of human resources for maintenance and support tasks.
4. **Training and Skill Development**: Training technical staff to specialize in the standardized node classes can lead to more expert knowledge in specific areas rather than a broader, more general skill set. This specialized knowledge enhances the quality of service and support provided by the operators


Node class specifications encompass the following attributes:


* Number and generation of virtual CPUs
* Quantity of Memory
* Networking Capacity (up/down)
* Specialization (e.g., general purpose, compute\-optimized, memory\-optimized, etc.)


The storage requirements for each AVS are unbundled from the EigenLayer node classes and must be specified separately by the AVS.


General Purpose EigenLayer Node classes[​](#general-purpose-eigenlayer-node-classes "Direct link to General Purpose EigenLayer Node classes")
---------------------------------------------------------------------------------------------------------------------------------------------




| Class | vCPUs (10th gen\+) | Memory | Networking Capacity |
| --- | --- | --- | --- |
| General Purpose \- large | 2 | 8 GB | 5 Mbps |
| General Purpose \- xl | 4 | 16 GB | 25 Mbps |
| General Purpose \- 4xl | 16 | 64 GB | 5 Gbps |


NOTE: The EigenLayer node class specification will expand over time as we collect more data from AVS developers and operators.

[PreviousInstallation](/eigenlayer/operator-guides/operator-installation)[NextOperator FAQ](/eigenlayer/operator-guides/operator-faq)* [General Purpose EigenLayer Node classes](#general-purpose-eigenlayer-node-classes)


* 
* Operator Guides
* Key Management
* Key Management Best Practices for Node Operators
Key Management Best Practices for Node Operators
================================================


* Secure keys, including secrets such as passphrases or mnemonics, using services like AWS Secrets Manager or Hashicorp Vault. These services can be seamlessly integrated with automated mechanisms that safely retrieve secrets or keys (e.g., remote signers). If resources permit, consider running your own Hashicorp Vault instance, which grants full custody of keys and secrets while sacrificing the service provider's availability and security guarantees.
* Avoid generating all keys with the same mnemonic. Minimize the attack surface by employing a new mnemonic for every 200 or 1000 validator keys, depending on your preference. This approach also reduces the risk of losing key generation capabilities if a single mnemonic is lost, and limits the impact if an attacker gains access to a few mnemonics.
* Given that AVS keys are likely to be much fewer, not using the same seed to generate the keys is probably safer; generate each AVS key independently if possible.
* Use a remote signer like **[Web3signer](https://github.com/ConsenSys/web3signer)** or, better yet, distributed signers to eliminate single points of failure.
* Develop a custom solution involving tailor\-made tools. For instance, use Web3signer for remote signing and store keys on AWS Secrets Manager. A custom tool can manage automatic key storage in Secrets Manager and facilitate interactions with Web3signer.


Smart Contract Operators
========================


We encourage institutional operators to register with EigenLayer using an [erc\-1271](https://eips.ethereum.org/EIPS/eip-1271) smart contract wallet. This allows a lot more fine\-grained control, such as multisig authorization and key rotation, which is currently not possible for EOA operators.

[PreviousIntroduction](/eigenlayer/operator-guides/key-management/intro)[NextKey Management Best Practices for Solo Stakers](/eigenlayer/operator-guides/key-management/solo-stakers)

* 
* Operator Guides
* Key Management
* Introduction
On this pageIntroduction
============


This section presents key management suggestions for operators. Within the context of EigenLayer, operators ought to be acquainted with proper practices concerning key loading, particularly signing keys.


Keys[​](#keys "Direct link to Keys")
------------------------------------


Central to every Proof of Stake mechanism lies a signature scheme. Signatures serve to authenticate the identity of every validator, enabling the attribution of their actions, whether positive or negative, to them. A validator's honesty can be confirmed by examining their signed messages, while malicious behavior can be demonstrated through messages that contravene consensus rules.


### Ethereum[​](#ethereum "Direct link to Ethereum")


Focusing on Ethereum validator keys exemplifies keys necessitating optimal security and accessibility measures, as they may maintain a robust connection with Nodes, further underlining their importance. Indeed, in Ethereum, a validator's identity is synonymous with their public key. To be precise, each validator possesses two sets: a signing and withdrawal keys.


#### Signing keys[​](#signing-keys "Direct link to Signing keys")


A *signing key* is the key a validator needs to sign attestations and propose blocks. Because a validator needs to sign a message at least once per epoch, the client software must have custody of the key.


#### Withdrawal keys[​](#withdrawal-keys "Direct link to Withdrawal keys")


Because the client software is always connected to the internet, there is a chance that one’s signing key is compromised. To reduce the impact of such a breach, the actions a validator can perform are split between two keys.


The signing key, as explained above, is used for the validator to perform their duties. On the other hand, the *withdrawal key* has the power to control a validator's funds (transferring and withdrawing ETH).


A validator should only need to use their withdrawal keys a few times over the lifetime of being a validator. This means they can be put into cold storage and stored with high security (offline).


### EigenLayer[​](#eigenlayer "Direct link to EigenLayer")


EigenLayer works differently from Ethereum due to it being natively a delegated PoS system. This means operators don't need to custody a separate key for each 32 Eth; they only need a single key per EigenLayer operator. This does imply that proper key management tools are even more important.


Contrary to Ethereum, where an operator controls a bunch of (signing, withdrawal) key pairs, an EigenLayer operator controls a single operator key, as well as a separate key (or a small number of keys) for each AVS they are registered in.


#### Operator keys[​](#operator-keys "Direct link to Operator keys")


An operator's operator key is the ecdsa key that is used to authenticate any interaction with the EigenLayer core contracts, and hence control an operator's actions such as registering to an AVS, changing its operator parameters, force undelegating a staker, etc.


The operator key should NEVER be used as an AVS key. They should also only be used to interact with the EigenLayer core contracts via the [eigenlayer\-cli](https://github.com/Layr-Labs/eigenlayer-cli) or other operator\-built tools, and should NOT be loaded into any node software. Any action that needs to be programatically triggered on the AVS contracts should be authorized via an AVS key, not the operator key.


#### AVS signing keys[​](#avs-signing-keys "Direct link to AVS signing keys")


AVS keys are actively used by node software to sign messages for AVSs. AVSs that use the [eigenlayer\-middleware](https://github.com/Layr-Labs/eigenlayer-middleware) contracts would typically use a bn254 key as the AVS signing key, but other AVSs might require an ecdsa, ed25519, or any other key type.



> \[!WARNING] We strongly advise operators to use a different key for every AVS, and NEVER to reuse their operator key as an AVS signing key.

[PreviousOperator Security Risks, Mitigations, and Best Practices](/eigenlayer/operator-guides/avs-operator-risks-mitigations-bp)[NextKey Management Best Practices for Node Operators](/eigenlayer/operator-guides/key-management/institutional-operators)* [Keys](#keys)
	+ [Ethereum](#ethereum)
	+ [EigenLayer](#eigenlayer)


* 
* Operator Guides
* Key Management
* Key Management Best Practices for Solo Stakers
On this pageKey Management Best Practices for Solo Stakers
==============================================


Individuals managing a limited number of validator keys typically do not require intricate distributed infrastructure for running nodes or employing remote signers. For these individuals, extensive staking services may be excessive and unnecessary. This means they will often store the keys with the decryption keys locally with the validator client or Node (which they maintain), which increases the vulnerability of the secrets, but, while stakers must safeguard validator keys against attacks, most key losses typically result from mundane reasons, such as losing the hardware containing the key. Users necessitate a backup strategy, mindful that if an attacker accesses the backed\-up keys, they can sign any message deemed valid against the validator's public key. Appropriate precautions should be implemented to guarantee that backed\-up validator keys are as inaccessible as feasible, ideally being completely offline and physically secure. Some of these precautions can be listed:


* Use hardware wallets: Store backed\-up keys on secure hardware wallets such as Ledger or Trezor devices. These wallets provide an additional layer of protection by isolating the keys from internet\-connected devices.
* Create multiple backups: Generate multiple copies of your backed\-up keys and store them in separate, secure locations, such as safety deposit boxes, fireproof safes, or encrypted USB drives.
* Encrypt backups: Ensure your backed\-up keys are encrypted using robust encryption algorithms. This protects the keys from unauthorized access in case the storage medium falls into the wrong hands.
* Implement physical security: Ensure the stored locations for backed\-up keys are secure, with controlled access and protection against theft or damage.
* Regularly test recovery: Periodically test the recovery of your backed\-up keys to ensure that they remain accessible and functional in case of an emergency.
* Employ secure communication channels: When transferring backed\-up keys, use secure communication methods such as end\-to\-end encrypted messaging or other secure channels to prevent interception by malicious actors.
* Limit access: Restrict access to backed\-up keys to a select few trusted individuals, and consider implementing a multi\-signature scheme to require multiple parties for key recovery.
* Maintain secrecy: Avoid discussing the location or existence of your backed\-up keys with others, and do not store any written records that could lead an attacker to their location.
* Continuously update security measures: Regularly assess and update the security measures in place to protect your backed\-up keys, staying informed about the latest threats and best practices.
* Use an air\-gapped device: Consider using an air\-gapped device, such as a computer not connected to the internet, to store backed\-up keys. This provides an additional layer of security against remote attacks. Use USB devices or QR codes for sharing the keys with the air\-gapped device.


Securing Mnemonic or Seed Phrases for Key Generation[​](#securing-mnemonic-or-seed-phrases-for-key-generation "Direct link to Securing Mnemonic or Seed Phrases for Key Generation")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


The mnemonic (if applicable) or seed phrase utilized for generating keys should not be stored on any device, and the aforementioned precautions should be taken into account for safekeeping. Avoid key generation tools that write the mnemonic to the Terminal, an insecure buffer, or a file. Aim to generate keys on an air\-gapped device, ensuring the mnemonic and passphrase are securely stored or loaded into memory.

[PreviousKey Management Best Practices for Node Operators](/eigenlayer/operator-guides/key-management/institutional-operators)[NextWebapp Content Guidelines](/eigenlayer/operator-guides/operator-content-guidelines)* [Securing Mnemonic or Seed Phrases for Key Generation](#securing-mnemonic-or-seed-phrases-for-key-generation)


* 
* Operator Guides
* Webapp Content Guidelines
On this pageWebapp Content Guidelines
=========================


Operator Page[​](#operator-page "Direct link to Operator Page")
---------------------------------------------------------------


The following are guidelines (**“Guidelines”**) for what content Operators should include in their listing of their Operator on app.eigenlayer.xyz (the “**App**”). These Guidelines are intended to help ensure that Operators are providing relevant information from which restakers can select an Operator.


The content in the Operator tile may include the following:


* Factual information relating to:
	+ The company or team running the Operator
	+ The technical ability or experience relevant to the competence of the Operator
* Links to website or social profiles associated with the Operator
* Logos associated with the Operator


The following content is **not permitted** to be displayed in the Operator tile:


* Any offer or promotion of illegal activities
* Any (i) vulgar or profane language or content or (ii) links to vulgar or profane content
* Promotions or incentives for stakers including offering of tokens
* Any false or misleading content
* Any links to content that is not owned or controlled by the Operator
* Any links to social profiles other than those associated with the Operator
* Any content that violates the intellectual property rights of any other person or entity (including using the branding or logo of EigenLayer or Eigen Labs)
* Anything violating the [Terms of Service](/eigenlayer/legal/terms-of-service)


Eigen Labs, Inc. (“**Eigen Labs**”) reserves the right to update these Guidelines at any time and without notice. If you violate these Guidelines, Eigen Labs may delist you or otherwise decrease your visibility on the App.


Reporting a Violation or Remediation of Guidelines[​](#reporting-a-violation-or-remediation-of-guidelines "Direct link to Reporting a Violation or Remediation of Guidelines")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Please use our [Support channel](https://support.eigenlayer.xyz/) for reporting either of the following:


* Operator violations of Webapp Content Guidelines.
* Appeal to review and whitelist an Operator who has remediated their violation of the guidelines.


Click on the Intercom chat icon in the bottom right of your screen, then choose “Create a Ticket: Operator Blocklist”.

[PreviousKey Management Best Practices for Solo Stakers](/eigenlayer/operator-guides/key-management/solo-stakers)[NextRestaking User Guide](/eigenlayer/restaking-guides/restaking-user-guide/)* [Operator Page](#operator-page)
* [Reporting a Violation or Remediation of Guidelines](#reporting-a-violation-or-remediation-of-guidelines)


* 
* Operator Guides
* Operator FAQ
On this pageOperator FAQ
============

#### Am I required to publicly host metadata url?[​](#am-i-required-to-publicly-host-metadata-url "Direct link to Am I required to publicly host metadata url?")


Yes. You are required to host the metadata url publicly. The `metadata` url should always be available and should return a proper json response like [this](https://holesky-operator-metadata.s3.amazonaws.com/metadata.json)


#### Am I required to publicly host logo in metadata json?[​](#am-i-required-to-publicly-host-logo-in-metadata-json "Direct link to Am I required to publicly host logo in metadata json?")


Yes. You are required to host the logo publicly like [this](https://holesky-operator-metadata.s3.amazonaws.com/eigenlayer.png)


#### Are there any restrictions to the logo image?[​](#are-there-any-restrictions-to-the-logo-image "Direct link to Are there any restrictions to the logo image?")


Yes. We only support `.png` format and we strictly check the content of image. If your image doesn't satisfy the requirement then the EigenLayer App will not display the logo of your operator.


#### What if I lose access to my keys?[​](#what-if-i-lose-access-to-my-keys "Direct link to What if I lose access to my keys?")


When you [create/import](/eigenlayer/operator-guides/operator-installation#create-and-list-keys) keys for the first time, it will ask a password to encrypt keys and once created, it will also show plaintext private key. Please make sure to backup the private key and the password. If you lose both you won't be able to get your keys back. If you lose the plaintext private key and still have your password you can run the [export](/eigenlayer/operator-guides/operator-installation#export-keys) command to get your plaintext private key.


#### What is my operator addresss?[​](#what-is-my-operator-addresss "Direct link to What is my operator addresss?")


After you [create/import](/eigenlayer/operator-guides/operator-installation#create-and-list-keys) ecdsa key you will be shown below log message



```
? Enter password to encrypt the ecdsa private key:  
ECDSA Private Key (Hex):  b3eba201405d5b5f7aaa9adf6bb734dc6c0f448ef64dd39df80ca2d92fca6d7b  
Please backup the above private key hex in safe place.  
  
Key location: /home/ubuntu/.eigenlayer/operator_keys/test.ecdsa.key.json  
Public Key hex:  f87ee475109c2943038b3c006b8a004ee17bebf3357d10d8f63ef202c5c28723906533dccfda5d76c1da0a9f05cc6d32085ca1af8aaab5a28171474b1ad0aa68  
Ethereum Address 0x6a8c0D554a694899041E52a91B4EC3Ff23d8aBD5  

```

Your operator address is the `Ethereum Address` in the logs.


#### What if I want to change the password of my encrypted keys?[​](#what-if-i-want-to-change-the-password-of-my-encrypted-keys "Direct link to What if I want to change the password of my encrypted keys?")


If you want to change the password of your encrypted keys, you have two options based on what information you have readily available:


1. If you know your private keys then you can just [re\-import](/eigenlayer/operator-guides/operator-installation#import-keys) and when importing, choose a different name and the new password.
2. If you don't know your private keys, you can get them using [export](/eigenlayer/operator-guides/operator-installation#export-keys). Once you have the private keys you can use option 1 to re\-import.


#### What if I want to deactivate/deregister my operator from EigenLayer?[​](#what-if-i-want-to-deactivatederegister-my-operator-from-eigenlayer "Direct link to What if I want to deactivate/deregister my operator from EigenLayer?")


Currently, there's no way to deregister your operator but you can
update the name of your operator in metadata url to be `Deactivated` or something similar. This will help display your operator as not active on the webapp.


#### Is there a limit to the number of AVSs that an Operator can opt\-in to?[​](#is-there-a-limit-to-the-number-of-avss-that-an-operator-can-opt-in-to "Direct link to Is there a limit to the number of AVSs that an Operator can opt-in to?")


There is no limit on the number of AVSs that an Operator can opt\-in to. However, the Operator needs to ensure they have sufficient infrastructure capacity for the AVSs they opt\-in to.


#### What is the process for rotating the keys for an existing operator? How can I register again and carry over the stake to a new key?[​](#what-is-the-process-for-rotating-the-keys-for-an-existing-operator-how-can-i-register-again-and-carry-over-the-stake-to-a-new-key "Direct link to What is the process for rotating the keys for an existing operator? How can I register again and carry over the stake to a new key?")


This operation is not supported at this time.

[PreviousEigenLayer Node Classes](/eigenlayer/operator-guides/eigenlayer-node-classes)[NextTroubleshooting](/eigenlayer/operator-guides/troubleshooting)

* 
* Operator Guides
* Installation
On this pageInstallation
============


Node Operator Checklist[​](#node-operator-checklist "Direct link to Node Operator Checklist")
---------------------------------------------------------------------------------------------


### **Software Requirements**[​](#software-requirements "Direct link to software-requirements")


* Docker: Ensure that Docker is installed on your system. To download Docker, follow the instructions listed [here](https://docs.docker.com/get-docker/).
* Docker Compose: Make sure Docker Compose is also installed and properly configured. To download Docker Compose, follow the instructions listed [here](https://docs.docker.com/compose/install/).
* Linux Environment: EigenLayer is supported only on Linux. Ensure you have a Linux environment, such as Docker, for installation.
	+ If you choose to install eigenlayer\-cli using the Go programming language, ensure you have Go installed, version 1\.21 or higher. You can find the installation guide [here](https://go.dev/doc/install).




---


### Checking for Requirements[​](#checking-for-requirements "Direct link to Checking for Requirements")


On a native Linux system, you can use the lsb\_release \-a command to get information about your Linux distribution.


**Check for Docker**
If you are not using a native Linux system and want to use EigenLayer, you can check if Docker is installed:


* Open a terminal or command prompt.
* Run the following command to check if Docker is installed and running:`css`



```
docker --version  

```

If Docker is installed and running, EigenLayer can be used within a Docker container, which provides a Linux environment.


By following these steps, you can determine if you have a suitable Linux environment for EigenLayer installation.




---


CLI Installation[​](#cli-installation "Direct link to CLI Installation")
------------------------------------------------------------------------


### Install CLI using Binary[​](#install-cli-using-binary "Direct link to Install CLI using Binary")


To download a binary for latest release, run:



```
curl -sSfL https://raw.githubusercontent.com/layr-labs/eigenlayer-cli/master/scripts/install.sh | sh -s  

```

The binary will be installed inside the `~/bin` directory.


To add the binary to your path, run:



```
export PATH=$PATH:~/bin  

```

#### Install CLI in A Custom Location[​](#install-cli-in-a-custom-location "Direct link to Install CLI in A Custom Location")


To download the binary in a custom location, run:



```
curl -sSfL https://raw.githubusercontent.com/layr-labs/eigenlayer-cli/master/scripts/install.sh | sh -s -- -b <custom_location>  

```



---


### Install CLI Using Go[​](#install-cli-using-go "Direct link to Install CLI Using Go")


Now we’re going to install the eigenlayer\-CLI using Go. The following command will install eigenlayer’s executable along with the library and its dependencies in your system.



```
go install github.com/Layr-Labs/eigenlayer-cli/cmd/eigenlayer@latest  

```

To check if the GOBIN is not in your PATH, you can execute `echo $GOBIN` from the Terminal. If it doesn't print anything, then it is not in your PATH. To add GOBIN to your PATH, add the following lines to your $HOME/.profile:



```
export GOBIN=$GOPATH/bin  
export PATH=$GOBIN:$PATH  

```

Changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, run the shell commands directly or execute them from the profile using a command such as source $HOME/.profile.




---


### Install CLI from Source[​](#install-cli-from-source "Direct link to Install CLI from Source")


To pursue this installation method you need to have Go. Please ensure that you installed Go with a minimum version of 1\.21 [here](https://go.dev/doc/install).


With this method, you generate the binary manually, downloading and compiling the source code.



```
git clone https://github.com/Layr-Labs/eigenlayer-cli.git  
cd eigenlayer-cli  
mkdir -p build  
go build -o build/eigenlayer cmd/eigenlayer/main.go  

```

or if you have **make** installed:



```
git clone https://github.com/Layr-Labs/eigenlayer-cli.git  
cd eigenlayer-cli  
make build  

```

The executable will be in the build folder.


In case you want the binary in your PATH (or if you used the [Go](https://github.com/Layr-Labs/eigenlayer-cli#install-eigenlayer-cli-using-go) method and you don't have $GOBIN in your PATH), please copy the binary to /usr/local/bin:




---


Create and List Keys[​](#create-and-list-keys "Direct link to Create and List Keys")
------------------------------------------------------------------------------------


ECDSA keypair corresponds to the operator Ethereum address and key for interacting with Eigenlayer. The BLS key is used for attestation purposes within the EigenLayer protocol. BLS key is used when you register an AVS to EigenLayer.


### Create Keys[​](#create-keys "Direct link to Create Keys")


Generate encrypted ECDSA and BLS keys using the CLI:



```
eigenlayer operator keys create --key-type ecdsa [keyname]  
eigenlayer operator keys create --key-type bls [keyname]  

```

* `[keyname]` \- This will be the name of the created key file. It will be saved as `<keyname>.ecdsa.key.json` or `<keyname>.bls.key.json`.


This will prompt a password which you can use to encrypt the keys. Keys will be stored in a local disk and will be shown once keys are created. It will also show the private key only once, so that you can back it up in case you lose the password or key file.


You can also create keys by piping your password to this command. This can help in automated key creation and will not prompt for password. This support got added in [v0\.6\.2](https://github.com/Layr-Labs/eigenlayer-cli/releases/tag/v0.6.2)



```
echo "password" | eigenlayer operator keys create --key-type ecdsa [keyname]  

```

#### Input Command[​](#input-command "Direct link to Input Command")



```
eigenlayer operator keys create --key-type ecdsa test  

```

The tool is requesting a password to encrypt the ECDSA private key for security purposes. The password input is hidden for security reasons.


#### Output[​](#output "Direct link to Output")



```
? Enter password to encrypt the ecdsa private key:  
ECDSA Private Key (Hex):  b3eba201405d5b5f7aaa9adf6bb734dc6c0f448ef64dd39df80ca2d92fca6d7b  
Please backup the above private key hex in safe place.  
  
Key location: /home/ubuntu/.eigenlayer/operator_keys/test.ecdsa.key.json  
Public Key hex:  f87ee475109c2943038b3c006b8a004ee17bebf3357d10d8f63ef202c5c28723906533dccfda5d76c1da0a9f05cc6d32085ca1af8aaab5a28171474b1ad0aa68  
Ethereum Address 0x6a8c0D554a694899041E52a91B4EC3Ff23d8aBD5  
  

```

### Import Keys[​](#import-keys "Direct link to Import Keys")


You can import existing ECDSA and BLS keys using the CLI, which are required for operator registration and other on\-chain operations. This is useful if you already have an address which you want to use as your operator.


To import an ECDSA key, use the command: `eigenlayer operator keys import --key-type ecdsa [keyname] [privatekey]`.


To import a BLS key, use the command: `eigenlayer operator keys import --key-type bls [keyname] [privatekey]`.


* `[keyname]` is the name of the imported key file, and it will be saved as `<keyname>.ecdsa.key.json` or `<keyname>.bls.key.json`.
* `privatekey` is the private key of the key you wish to import.
	+ For BLS keys, it should be a large number.
	+ For ECDSA keys, it should be in hex format.


You can also import keys by piping your password to this command. This can help in automated key creation and will not prompt for password. This support got added in [v0\.6\.2](https://github.com/Layr-Labs/eigenlayer-cli/releases/tag/v0.6.2)



```
echo "password" | eigenlayer operator keys import --key-type ecdsa [keyname] [privatekey]  

```

#### Input Command[​](#input-command-1 "Direct link to Input Command")


This part of the command tells the EigenLayer tool that you want to import a key.



```
eigenlayer operator keys import --key-type ecdsa test 6842fb8f5fa574d0482818b8a825a15c4d68f542693197f2c2497e3562f335f6  

```

#### Output[​](#output-1 "Direct link to Output")


This is a prompt asking you to enter a password to encrypt the ECDSA private key.



```
? Enter password to encrypt the ecdsa private key: *******  
ECDSA Private Key (Hex):  6842fb8f5fa574d0482818b8a825a15c4d68f542693197f2c2497e3562f335f6  
Please backup the above private key hex in safe place.  
  
Key location: /home/ubuntu/.eigenlayer/operator_keys/test.ecdsa.key.json  
Public Key hex:  a30264c19cd7292d5153da9c9df58f81aced417e8587dd339021c45ee61f20d55f4c3d374d6f472d3a2c4382e2a9770db395d60756d3b3ea97e8c1f9013eb1bb  
Ethereum Address 0x9F664973BF656d6077E66973c474cB58eD5E97E1  
  

```

This will initiate a password prompt that you can use to encrypt the keys. The keys will be stored on your local disk and will be displayed after they are created.


The private key will also be shown only once, enabling you to create a backup in case you forget the password or lose the key file.


### List Keys[​](#list-keys "Direct link to List Keys")


This is the command you can use to retrieve a list of the keys you have created with the EigenLayer cli tool.



```
eigenlayer operator keys list  

```

When you run the Eigenlayer operator keys list command, it will display a list of all the keys that were generated using this specific command, along with their corresponding public keys.


This information can be useful for managing and identifying the keys you've created. Public keys are typically used for encryption, authentication, and verifying digital signatures.


### Export keys[​](#export-keys "Direct link to Export keys")


If you want to see the private key of the existing keys, you can use the below command. This will only work if your keys are in default location (`~/.eigenlayer/operator_keys`)



```
eigenlayer operator keys export --key-type ecdsa [keyname]  

```

This will also prompt for the password used to encrypt the key.


If your keys is not in the default location, you can give the full path to the key file using \-\-key\-path flag. You don't need to provide the key name in that case.



```
eigenlayer operator keys export --key-type ecdsa --key-path [path]  

```



---


Fund ECDSA Wallet[​](#fund-ecdsa-wallet "Direct link to Fund ECDSA Wallet")
---------------------------------------------------------------------------


Send **at least 1 ETH** to the “address” field referenced in your operator.yaml file. This ETH will be used to cover the gas cost for operator registration in the subsequent steps.


If you are deploying to Testnet, please follow the instructions in [Obtaining Testnet ETH](https://docs.eigenlayer.xyz/restaking-guides/restaking-user-guide/testnet/obtaining-testnet-eth-and-liquid-staking-tokens-lsts) to fund a web3 wallet with HolEth.




---


Operator Configuration and Registration[​](#operator-configuration-and-registration "Direct link to Operator Configuration and Registration")
---------------------------------------------------------------------------------------------------------------------------------------------


**Step 1:** Create the config files needed for operator registration using the below command:



```
eigenlayer operator config create  

```

When prompted for operator address, make sure your operator address is same as the ecdsa key address you created/imported in key creation steps.


The command will create two files: `operator.yaml` and `metadata.json`.


**Step 2:** Upload Logo Image, Configure `metadata.json`, and Upload Both


Upload the logo of the operator to a publicly accessible location and set the url in your `metadata.json` file. Operator registration only supports `.png` images for now and must be less than 1MB in size.


The `name` and `description` should comply with the regex mention [here](https://github.com/Layr-Labs/eigensdk-go/blob/master/utils/utils.go#L29). You can use services like [https://regex101\.com/](https://regex101.com/) to validate your fields.


Complete your the details in `metadata.json`. The `metadata.json` must be less than 4KB in size. Upload the file to a publicly accessible location and set that url in `operator.yaml`. Please note that a **publicly accessible** metadata url is required for successful registration. An example operator.yaml file is provided for your reference here: [operator.yaml](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/pkg/operator/config/operator-config-example.yaml) .


infoFor Mainnet Operators \- the `metadata.json` and operator logo .png files MUST be hosted via github.com repositories specifically. Caveat: **gist.github.com** hosted files are not permitted.
These requirements do not apply to Testnet Operators.


warningWhen using Github for hosting please ensure you link to the raw file ([example](https://raw.githubusercontent.com/Layr-Labs/eigenlayer-cli/master/pkg/operator/config/metadata-example.json)), rather than the github repo URL ([example](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/pkg/operator/config/metadata-example.json)).


**Step 3:** Configure RPC Node:


The EigenLayer CLI requires access to an Ethereum RPC node in order to post registration. Please plan to either leverage an RPC node provider or run your own local RPC node to reference in operator.yaml.


Please find example lists of RPC node providers here:


* <https://chainlist.org/>
* [https://www.alchemy.com/list\-of/rpc\-node\-providers\-on\-ethereum](https://www.alchemy.com/list-of/rpc-node-providers-on-ethereum)


Ensure that your Operator server can reach your RPC provider at this point. You may run the following command from your Operator server:
`curl -I [your_server_url]`


**Step 4:** DelegationManager Contract Address


You must configure the correct DelegationManager contract address for your environment.


* Navigate to [EigenLayer Contracts: Deployments](https://github.com/Layr-Labs/eigenlayer-contracts?tab=readme-ov-file#deployments) and locate the Proxy address for `DelegationManager` for your environment (Mainnet, Testnet).
* Set the value for `el_delegation_manager_address` in your operator config file to the address for your environment.


**Optional:** Set Delegation Approver


Operators have the option to set [delegationApprover](https://github.com/Layr-Labs/eigenlayer-contracts/blob/mainnet/src/contracts/interfaces/IDelegationManager.sol#L30) when they register. If the `delegationApprover` is set to a nonzero value, then the `delegationApprover` address will be required sign its approval of new delegations from Stakers to this Operator. If the default value is left as the zero address (0x000\...) then all new delegations will be automatically approved without the need for any signature. Please see [delegationApprover Design Patterns](#delegationapprover-design-patterns) below for more detail.


The EigenLayer Web App simulates transactions to check for contract reversions. If the delegate call will revert for any reason the button will be disabled.


**Step 5:** Registration Command


This is the command you can use to register your operator.



```
eigenlayer operator register operator.yaml  

```


> *Note: ECDSA key is required for operator registration. You may choose to either* [*create*](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/README.md#create-keys) *your own set of keys using the EigenLayer CLI (recommended for first time users) or* [*import*](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/README.md#import-keys) *your existing keys (recommended for advanced users who already have keys created) as outlined in the previous section.*




---


Checking Status of Registration[​](#checking-status-of-registration "Direct link to Checking Status of Registration")
---------------------------------------------------------------------------------------------------------------------


This is the command you can use to inquire about the registration status of your operator.



```
eigenlayer operator status operator.yaml  

```



---


Metadata Updates[​](#metadata-updates "Direct link to Metadata Updates")
------------------------------------------------------------------------


### General metadata update[​](#general-metadata-update "Direct link to General metadata update")


This is the command you can use to make changes or updates to the metadata of your operator. Post v0\.9\.0, this command will not update metadata uri. Please use [below](#update-metadata-uri-post-v090) command to update it.



```
eigenlayer operator update operator.yaml  

```

### Update metadata URI (Post v0\.9\.0\)[​](#update-metadata-uri-post-v090 "Direct link to Update metadata URI (Post v0.9.0)")


In [v0\.9\.0](https://github.com/Layr-Labs/eigenlayer-cli/releases/tag/v0.9.0), we have introduced a new comamnd to update metadata uri.



```
eigenlayer operator update-metadata-uri operator.yaml  

```

delegationApprover Design Patterns[​](#delegationapprover-design-patterns "Direct link to delegationApprover Design Patterns")
------------------------------------------------------------------------------------------------------------------------------


Delegation Approver functionality can be used in multiple ways to give Operators additional programmatic control over which Restakers they accept delegation from.


### Passing Signatures from the DelegationApprover to Stakers[​](#passing-signatures-from-the-delegationapprover-to-stakers "Direct link to Passing Signatures from the DelegationApprover to Stakers")


One series of designs involves passing a unique signature from the Operator to the Restaker requesting approval. The unique signature will have a corresponding ‘salt’ (unique value used once) and an ‘expiry’. The Restaker passes the signature (salt \& expiry) into the `DelegationManager.delegateTo` function ([source here](https://github.com/Layr-Labs/eigenlayer-contracts/blob/mainnet/src/contracts/core/DelegationManager.sol#L135-L155)). This function uses EIP1271 to check the signature, so either:


* A) The Operator has set an EOA as their `delegationApprover` and the DelegationManager simply checks that the signature is a valid ECDSA signature from the EOA.
* OR B) The Operator has set a smart contract as their `delegationApprover` and the DelegationManager calls the isValidSignature function on the `delegationApprover` and checks if the contract returns `0x1626ba7e` (as defined in the [EIP\-1271 specification](https://eips.ethereum.org/EIPS/eip-1271#specification)).


If the delegationApprover themself calls the DelegationManager.delegateToBySignature function, then they need to provide a [signature from the Restaker](https://github.com/Layr-Labs/eigenlayer-contracts/blob/mainnet/src/contracts/core/DelegationManager.sol#L157-L204). The approverSignatureAndExpiry input is ignored if the caller is themselves the delegationApprover. One potential drawback to this approach is the delegationApprover would pay the gas for the transaction.


**Whitelisting and Blacklisting Restakers for Delegation**


If the Operator uses option B above, a smart contract for their `delegationApprover`, they can also maintain an approved whitelist. The contract can store a Merkle root of approved signature hashes and provide each Restaker with a Merkle proof when they delegate. [This branch](https://github.com/Layr-Labs/eigenlayer-contracts/blob/feat-example-operator-delegation-whitelist/src/contracts/examples/DelegationApproverWhitelist.sol) provides a PoC of what such a smart contract could look like.


The example above could be modified to act as a “blacklist” by using Merkle proofs of non\-inclusion instead of Merkle proofs of inclusion.

[PreviousIntroduction](/eigenlayer/operator-guides/operator-introduction)[NextEigenLayer Node Classes](/eigenlayer/operator-guides/eigenlayer-node-classes)* [Node Operator Checklist](#node-operator-checklist)
	+ [**Software Requirements**](#software-requirements)
	+ [Checking for Requirements](#checking-for-requirements)
* [CLI Installation](#cli-installation)
	+ [Install CLI using Binary](#install-cli-using-binary)
	+ [Install CLI Using Go](#install-cli-using-go)
	+ [Install CLI from Source](#install-cli-from-source)
* [Create and List Keys](#create-and-list-keys)
	+ [Create Keys](#create-keys)
	+ [Import Keys](#import-keys)
	+ [List Keys](#list-keys)
	+ [Export keys](#export-keys)
* [Fund ECDSA Wallet](#fund-ecdsa-wallet)
* [Operator Configuration and Registration](#operator-configuration-and-registration)
* [Checking Status of Registration](#checking-status-of-registration)
* [Metadata Updates](#metadata-updates)
	+ [General metadata update](#general-metadata-update)
	+ [Update metadata URI (Post v0\.9\.0\)](#update-metadata-uri-post-v090)
* [delegationApprover Design Patterns](#delegationapprover-design-patterns)
	+ [Passing Signatures from the DelegationApprover to Stakers](#passing-signatures-from-the-delegationapprover-to-stakers)


* 
* Operator Guides
* Introduction
On this pageIntroduction
============


What is a Node Operator within EigenLayer?[​](#what-is-a-node-operator-within-eigenlayer "Direct link to What is a Node Operator within EigenLayer?")
-----------------------------------------------------------------------------------------------------------------------------------------------------


Operators, who can be either individuals or organizations, play an active role in the EigenLayer protocol. By registering within EigenLayer, they enable ETH stakers to delegate their staked assets, whether in the form of native ETH or LSTs. The Node Operators then opt\-in to provide a range of services to AVSs, enhancing the overall security and functionality of their networks.




---


Operator Eligibility and Restaking Criteria[​](#operator-eligibility-and-restaking-criteria "Direct link to Operator Eligibility and Restaking Criteria")
---------------------------------------------------------------------------------------------------------------------------------------------------------


Becoming an Operator in the EigenLayer ecosystem does not require a specific amount of delegated restaked TVL. Essentially, any Ethereum address can serve as an Operator. An address can function as both a Restaker, engaging in either liquid or native restaking, and as an Operator simultaneously. However, it is important to note that this dual role is not mandatory. An Operator can participate in the EigenLayer network without having any restaked tokens.


Most Operators will receive token delegations sourced from other Restakers within the network, otherwise Operators can choose to self\-delegate by allocating their restaked token balance.


Quorums[​](#quorums "Direct link to Quorums")
---------------------------------------------


Quorums are a grouping of Strategies (Restaked Assets) to be used by an AVS for shared security measures. Operators can choose to opt into quorums of one or more tokens, depending on their preference and the designs of the AVS operate.


An Operator can opt into as many quorums as they like as long as they have sufficient TVL for those quorums.


Rewards[​](#rewards "Direct link to Rewards")
---------------------------------------------


Head over to the [rewards claiming](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/rewards-claiming-overview) documentation on how to claim rewards.

[PreviousWhitepapers](/eigenlayer/overview/whitepaper)[NextInstallation](/eigenlayer/operator-guides/operator-installation)* [What is a Node Operator within EigenLayer?](#what-is-a-node-operator-within-eigenlayer)
* [Operator Eligibility and Restaking Criteria](#operator-eligibility-and-restaking-criteria)
* [Quorums](#quorums)
* [Rewards](#rewards)


* 
* Operator Guides
* Troubleshooting
On this pageTroubleshooting
===============


Before creating an issue with EigenLayer support please check this page to see if you can resolve your issues. If you are still stuck, please create a support ticket


#### Getting "no contract code at given address"[​](#getting-no-contract-code-at-given-address "Direct link to Getting \"no contract code at given address\"")


If you are getting this issue then either you are using a wrong rpc in your [operator.yaml](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/pkg/operator/config/operator-config-example.yaml#L32) file or you have wrong smart contract address in your [config](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/pkg/operator/config/operator-config-example.yaml#L25).


* Please make sure you have correct rpc node chosen for your network and that it is also reachable via your machine.
* Please find the correct smart contract addresses listed in the [Operator Installation](/eigenlayer/operator-guides/operator-installation) section.


#### How to resolve the error "No contract code at given address" imply?[​](#how-to-resolve-the-error-no-contract-code-at-given-address-imply "Direct link to How to resolve the error \"No contract code at given address\" imply?")


Ensure that your operator is pointing to the correct RPC service and that it is accessible from your operator ([example](https://chainlist.org/)).


#### My operator's metadata (name, description, logo) is not showing up in the webapp[​](#my-operators-metadata-name-description-logo-is-not-showing-up-in-the-webapp "Direct link to My operator's metadata (name, description, logo) is not showing up in the webapp")


Please make sure to comply with our metadata [guidelines](/eigenlayer/operator-guides/operator-installation#operator-configuration-and-registration)

[PreviousOperator FAQ](/eigenlayer/operator-guides/operator-faq)[NextOperator Security Risks, Mitigations, and Best Practices](/eigenlayer/operator-guides/avs-operator-risks-mitigations-bp)

* 
* Overview
On this pageIntro to EigenLayer
===================


What is EigenLayer?[​](#what-is-eigenlayer "Direct link to What is EigenLayer?")
--------------------------------------------------------------------------------


EigenLayer is a protocol built on Ethereum that introduces restaking, a new primitive in cryptoeconomic security. This primitive enables the reuse of ETH on the consensus layer. Users that stake ETH natively or with a liquid staking token (LST) can opt\-in to EigenLayer smart contracts to restake their ETH or LST and extend cryptoeconomic security to additional applications on the network to earn additional rewards.


Why Build with EigenLayer?[​](#why-build-with-eigenlayer "Direct link to Why Build with EigenLayer?")
-----------------------------------------------------------------------------------------------------


With EigenLayer, Ethereum stakers can help secure many services by restaking their staked ETH and opting\-in to many services simultaneously, providing [**pooled security**](/eigenlayer/overview/key-terms)**.** Reusing ETH to provide security across many services reduces capital costs for a staker to participate and significantly increases the trust guarantees to individual services.


Anyone building a new decentralized service for Ethereum must bootstrap a new trust network to secure their system, fragmenting security. EigenLayer solves this problem by enabling any service, regardless of its composition (e.g. EVM\-compatibility), to tap into the pooled security of Ethereum's stakers, creating an environment for permissionless innovation and free\-market governance.


EigenLayer Architecture Overview[​](#eigenlayer-architecture-overview "Direct link to EigenLayer Architecture Overview")
------------------------------------------------------------------------------------------------------------------------


* **Restaking** enables stakers to restake their Native ETH or Liquid Staking Tokens (LST) to provide greater security for services in the EigenLayer ecosystem, known as Actively Validated Services (AVSs).
* **Operators** are entities that help run AVS software built on EigenLayer. They register in EigenLayer and allow stakers to delegate to them, then opt in to provide various services (AVSs) built on top of EigenLayer.
* **Delegation** is the process where stakers delegate their staked ETH to operators or run validation services themselves, effectively becoming an operator. This process involves a double opt\-in between both parties, ensuring mutual agreement. Restakers retain agency over their stake and choose which AVSs they opt\-in to validate for.
* **Actively Validated Services (AVSs)** are services built on the EigenLayer protocol that leverage Ethereum's shared security.
	+ Operators perform validation tasks for AVSs, contributing to the security and integrity of the network.
	+ AVSs deliver services to users (**AVS Consumers**) and the broader Web3 ecosystem.


![](/img/overview/eigenlayer-arch-v2.png)
To learn more about EigenLayer please read the [**Whitepaper**](/assets/files/EigenLayer_WhitePaper-88c47923ca0319870c611decd6e562ad.pdf) or visit the [**Learn**](https://www.eigenlayer.xyz/learn) section of the EigenLayer website.

[NextKey Terms](/eigenlayer/overview/key-terms)* [What is EigenLayer?](#what-is-eigenlayer)
* [Why Build with EigenLayer?](#why-build-with-eigenlayer)
* [EigenLayer Architecture Overview](#eigenlayer-architecture-overview)


* 
* [Overview](/eigenlayer/overview/)
* EIGEN Token Overview
On this pageEIGEN Token Overview
====================

### What is the EIGEN token?[​](#what-is-the-eigen-token "Direct link to What is the EIGEN token?")


The EIGEN token is a universal intersubjective work token. We will break down the terms here. First, by work token, we mean that a token that can be staked to perform some work within a blockchain platform. This work could be an execution task or validation task. Existing work tokens often have the following limitations:


* **Special\-purpose:** Existing work tokens are designed to provide cryptoeconomic security to only one enshrined specific digital task. For example, before ETH restaking in EigenLayer, ETH was specialized for securing only Ethereum’s consensus.
* **Objective:** ETH restaking expanded the scope of ETH. With ETH restaking, the ETH staked can now be used to secure those services that have objectively attributable faults and can be proven onchain by means of an optimistic dispute resolution mechanism. Resolution of faults is done by means of mathematics and cryptography.
However, there is a much wider class of digital tasks where the faults in their execution are not provable onchain in a smart contract but are observable by any observer outside the chain and a wide agreement can be achieved among the honest observers. We call this category of faults **intersubjectively attributable faults**. By having staking with EIGEN, the goal is to secure AVSs that have **any** intersubjectively attributable faults and penalize the EIGEN stake of the operators who participate in these faults. This lends a universal nature to the EIGEN token.


### What are intersubjectively attributable faults?[​](#what-are-intersubjectively-attributable-faults "Direct link to What are intersubjectively attributable faults?")


The core property of intersubjectively attributable faults is that in the event of such a fault, there will be wide agreement among observers outside the chain about the occurrence of the fault. Unlike objectively attributable faults, intersubjectively attributable faults might not be provable mathematically and cryptographically onchain. Examples of intersubjectively attributable faults are:


* Is data available in the Data Availability layer at a certain point in time? This can be observed externally by means of data availability sampling, but any unavailability or otherwise can’t be proven in a smart contract.
* Is an AI inference result accurate within a margin of error? Given the description of hardware spec, random seeds used and input data, it can verify whether the inference is within a confidence interval or not.


An important note is that any objectively attributable fault is also an intersubjectively attributable fault. For example, any fault in executing a deterministic VM such as EVM is an objectively attributable fault that all honest observers outside the chain will agree with.


**Intersubjectively attributable faults are different from subjective faults**. The set of intersubjectively attributable faults doesn’t include subjectivity in the observer's response. In digital tasks with subjective faults, it implies that no wide agreement can be achieved among the observers about the occurrence of fault. Examples of subjective faults are: Is Paris the most beautiful city? What will be the price of a particular NFT in 1 year? And so on.


### What are the core ideas behind how staking with EIGEN enables resolution of intersubjectively attributable faults?[​](#what-are-the-core-ideas-behind-how-staking-with-eigen-enables-resolution-of-intersubjectively-attributable-faults "Direct link to What are the core ideas behind how staking with EIGEN enables resolution of intersubjectively attributable faults?")


Resolving intersubjectively attributable fault using EIGEN staking utilizes three core ideas: (1\) setup and execution phase, (2\) slashing and (3\) token forking.


The first core idea is the concept of setup phase and execution phase that is applicable to any coordination system. The setup phase represents the process of discussing, agreeing on and codifying (a) the set of execution rules that will be used for execution of any digital task in the system and, (b) the set of monitoring and verification rules among the observers about any fault while executing. Once the setup phase is over, it is the execution phase where these pre\-agreed rules are executed. These rules should enable detection of faults to be self\-evident and self\-verifiable by any user in the social consensus such that it precludes meeting in\-person or in a discord channel. An example of the setup phase is the ratification of the US constitution and now in the execution phase any law passed has to be compliant with the constitution. In the context of blockchains, an example would be the agreement to use the longest\-chain consensus rule which is then used for determining the latest block in bitcoin.


The second core idea is slashing. Slashing allows any adversarial participant in a proof\-of\-stake network to be punished for their misbehavior during the execution phase by taking away their stake. This lends to cryptoeconomic benefits to any PoS system in the form of karma. You can read more about the benefits of slashing in [this blog post](https://a16zcrypto.com/posts/article/the-cryptoeconomics-of-slashing/).


The third core idea is token forking. Most of the current systems attempt to resolve intersubjectively attributable faults either by slashing the stake of operators whose response to the task diverged from the majority response, or by using a committee to slash the operators whose claims are not concordant with the “true” answer. However, both mechanisms are vulnerable to the tyranny\-of\-majority. A third way is forking of the chain state itself, which is used in the context of resolving intersubjective fault of lack of chain growth in Ethereum. This involves empowering social consensus of the chain to slash the adversarial validators in the event of majority corruption of the validator set. Token forking uses this fact to fork just the token, without forking the chain state, to induce cryptoeconomic penalties on malicious stakers. With EIGEN staking, if the majority of EIGEN stakers were to turn malicious and cause an intersubjectively attributable fault, then a new fork of EIGEN can be started by anyone where the malicious stakers can be penalized by restricting them from being able to redeem the tokens from the new fork. As the new fork comes to be considered as canonical by the social consensus, the malicious stakers end up being penalized.


### What are the key features of the EIGEN staking?[​](#what-are-the-key-features-of-the-eigen-staking "Direct link to What are the key features of the EIGEN staking?")


There are four key features in EIGEN staking: (1\) universality, (2\) isolation, (3\) metering, and (4\) compensation.


* **Universality**. The setup phase of EIGEN stipulates that EIGEN can be universally used for resolving any intersubjectively attributable fault, not just one specific fault. Any AVS that wants to use the cryptoeconomic benefits of EIGEN must encode their rules of coordination that they have agreed on in their respective setup phase. These AVS\-specific rules, such as slashing conditions, are akin to amendments to EIGEN. Furthermore, these slashing conditions of the AVSs must ensure that any intersubjectively attributable fault is self\-verifiable beyond a reasonable doubt.
* **Isolation**. The second core feature of EIGEN is isolation. To appreciate this feature, consider an alternate design where any fork in the token would require DeFi markets to be aware of the fork, and the token is no longer usable for going into long\-term DeFi positions. To avoid this undesirable externality on DeFi, EIGEN has a two\-token model. The first token, bEIGEN, is used for staking and can be subjected to forking. As for the other token, EIGEN, our design offers the benefit of remaining unaware of forks in bEIGEN to any holder of EIGEN who is using it for DeFi or any non\-staking applications.
* **Metering**. Resolving any intersubjective fault incurs a cost to social consensus for switching from one token to another, or rejecting a malicious fork. Therefore, any claim to fork the token should require depositing a bond in bEIGEN to deter malicious challenges. This bond needs to be higher than the cost incurred by the social consensus (users and AVSs) to consider and reject a malicious fork. Additionally, any successful challenge results in a significant cost to the broader ecosystem in the form of contract upgrades for incorporating the new fork in daily operations. A challenge, therefore, should only be raised if a sufficient amount of staked EIGEN can be considered malicious and burnt, resulting in a lower token supply for the remaining EIGEN.
* **Compensation**. The protocol for intersubjective staking ensures that if an AVS is attacked due to a malicious quorum of EIGEN stakers, that AVS is able to slash and redistribute the malicious stake back to the AVS users. If the AVS ensures that this “attributable security” is greater than the harm done to its users, then it achieves “strong cryptoeconomic security,” which specifies that no honest user suffers any harm. Strong cryptoeconomic security is a user\-centric characterization and does not need to make any assumptions on the adversary or even the other users’ incentive structure. For example, when there are multiple AVSs, as long as a given AVS ensures that it has enough attributable security, this particular AVS is protected even if the system is, in sum total, not secure because other AVSs do not have enough security.
Furthermore, using EIGEN for resolving intersubjectively attributable fault ensures that Ethereum’s social consensus is not overloaded.


### How does EIGEN staking complement ETH restaking?[​](#how-does-eigen-staking-complement-eth-restaking "Direct link to How does EIGEN staking complement ETH restaking?")


EIGEN staking and ETH restaking play complementary roles within EigenLayer. In many mature AVS protocols, safety properties are secured through objective slashing, while liveness and censorship\-resistance, which previously relied on majority\-assumptions and stake decentralization, are achieved through EIGEN staking. For a service that uses restaking for safety and EIGEN staking for liveness, fees can be split between the two quorums. Furthermore, for core services provided to the Ethereum ecosystem, we envision many services that will use dual staking between ETH and EIGEN. The ETH restaking absorbs the decentralization/collusion resistance and operator alignment that comes with it, and the EIGEN staking can support cryptoeconomic slashing. In this model, the former serves as a mechanism to obtain majority trust from the Ethereum participants, and the latter serves as a mechanism to obtain economic security.


In keeping with the spirit of open innovation, EigenLayer allows AVSs to mix and match these two modalities of objective staking from ETH and intersubjective staking from EIGEN, in addition to utilizing the native AVS tokens for providing additional validation from an aligned community of AVS token stakers.


### How does EIGEN staking accelerate innovation in AVSs with objectively attributable faults?[​](#how-does-eigen-staking-accelerate-innovation-in-avss-with-objectively-attributable-faults "Direct link to How does EIGEN staking accelerate innovation in AVSs with objectively attributable faults?")


EIGEN staking can support digital tasks that could potentially be secured via objective fraud proofs, but doing so would involve significant technical complexity and associated risk. Specifically, when envisioning the lifecycle of a new objective AVS, we can identify a progression that leverages EIGEN staking for security early in the protocol's bootstrapping phase, transitioning to restaking or even native protocol adoption as the protocol matures, ossifies, and more faults become objective.


### What are some examples of Actively Validated Services (AVS) that could be secured using the EIGEN token?[​](#what-are-some-examples-of-actively-validated-services-avs-that-could-be-secured-using-the-eigen-token "Direct link to What are some examples of Actively Validated Services (AVS) that could be secured using the EIGEN token?")


* Some of the foundational primitives that can now be secured using EIGEN staking are:
* Censorship\-resistance: Ensuring that propagated transactions are eventually included in the \- ledger.
* Ledger growth: Ensuring that new transactions keep getting added to the ledger.
* Data Availability: Guaranteeing the availability and accessibility of data across the network.
* Oracles: Providing reliable and verifiable real\-world data to blockchain applications.


With these foundational modules, one can build a plethora of new services:


* New Chains: Building new blockchain networks with customizable security and features for different modules.
* Intents and MEV (Miner Extractable Value): Managing transaction ordering and preventing malicious activities related to MEV.
* AI Training, Benchmarking, and Inference: Ensuring the validity and security of AI models and their execution.
* Prediction Markets: Creating decentralized prediction markets.
* Storage Services: Building secure and decentralized storage solutions.
* Cloud Microservices: Migrating traditional cloud services like Kafka to blockchain with cryptoeconomic security and slashability.
* Gaming Virtual Machines: Securing the execution of gaming environments on the blockchain.
* Databases: Such execution environments have complex dispute resolution which can be substituted with the intermediate step of being secured by EIGEN staking.


### EIGEN Token Restaking FAQ[​](#eigen-token-restaking-faq "Direct link to EIGEN Token Restaking FAQ")


Please see the [EIGEN Token Restaking FAQ page](/eigenlayer/restaking-guides/restaking-user-guide/EIGEN-faq) for more information.

[PreviousKey Terms](/eigenlayer/overview/key-terms)[NextCommunity and EIGEN Claim Support](/eigenlayer/overview/support)* [What is the EIGEN token?](#what-is-the-eigen-token)
* [What are intersubjectively attributable faults?](#what-are-intersubjectively-attributable-faults)
* [What are the core ideas behind how staking with EIGEN enables resolution of intersubjectively attributable faults?](#what-are-the-core-ideas-behind-how-staking-with-eigen-enables-resolution-of-intersubjectively-attributable-faults)
* [What are the key features of the EIGEN staking?](#what-are-the-key-features-of-the-eigen-staking)
* [How does EIGEN staking complement ETH restaking?](#how-does-eigen-staking-complement-eth-restaking)
* [How does EIGEN staking accelerate innovation in AVSs with objectively attributable faults?](#how-does-eigen-staking-accelerate-innovation-in-avss-with-objectively-attributable-faults)
* [What are some examples of Actively Validated Services (AVS) that could be secured using the EIGEN token?](#what-are-some-examples-of-actively-validated-services-avs-that-could-be-secured-using-the-eigen-token)
* [EIGEN Token Restaking FAQ](#eigen-token-restaking-faq)


* 
* [Overview](/eigenlayer/overview/)
* Key Terms
Key Terms
=========

* **Actively Validated Services (AVS):** Any system that requires its own distributed validation semantics for verification, such as sidechains, data availability layers, new virtual machines, keeper networks, oracle networks, bridges, threshold cryptography schemes, and trusted execution environments.
* **AVS Developer**: development team that builds an AVS service.
* **Cryptoeconomic security:** security model that uses economic incentives and cryptography to ensure the proper functioning and security of a network.
* **Delegation in EigenLayer:** feature that allows restakers holding ETH or LSTs to delegate their assets to other entities who will operate off\-chain software containers of service modules built on EigenLayer, rather than operating the software themselves.
* **EigenPod:** contract that is deployed on a per\-user basis that facilitates native restaking.
* **Free\-market governance:** EigenLayer provides an open market mechanism that allows stakers to choose which services to opt into, based on their own risk and reward analysis.
* **Liquid Staking:** a service that enables users to deposit their ETH into a staking pool and receive a liquid staking token. This token represents a claim on their ETH and its staking yield. Liquid staking tokens can be traded in the DeFi ecosystem and redeemed for their underlying ETH value after a waiting period.
* **LST Restaking:** a method where LST holders restake their Liquid Staking Tokens (LSTs) by transferring them into the EigenLayer smart contracts.
* **Native Restaking:** a method where Ethereum stakers restake their staked ETH natively by pointing their withdrawal credentials to the EigenLayer contracts.
* **On\-chain slashing contract:** a smart contract deployed by service modules on EigenLayer that enforces slashing, specifying and penalizing any misbehavior.
* **Operator:** an entity who helps run AVS software built on top of EigenLayer. Operators register in EigenLayer and allow Stakers to delegate to them, then opt in to provide various services (AVSs) built on top of EigenLayer. Operators may also be Stakers; these are not mutually exclusive.
* **Pooled security via restaking:** when multiple parties combine their resources to provide greater security for a system. In EigenLayer, Ethereum stakers can “restake” their ETH or Liquid Staking Tokens (LST) by opting into new services built on EigenLayer.
* **Quorum**: grouping of Strategies to be used by an AVS for shared security measures.
* **Quorum Threshold**: the minimum amount of Operator responses and their stake % that must be received by the Aggregator entity.
* **Restaker**: a person who restakes Native or LST ETH to the EigenLayer protocol.
* **Restaking Points:** a measure of your total EigenLayer restaking contribution. Based on amount of ETH staked over time, in units of ETH per second. For a precise definition of how Restaking Points are calculated, please refer to the [next](/eigenlayer/restaking-guides/restaking-user-guide/restaked-points) section.
* **Stake**: the amount of ETH delegated to the current set of Operators.
* **Strategies**: assets that are restaked into the platform.
* **Withdrawals**
	+ **Full Withdrawals:** 32ETH Stake \+ Eth Staking Rewards (until now).
	+ **Partial Withdrawals:** ETH consensus layer rewards (until now).
[PreviousIntro to EigenLayer](/eigenlayer/overview/)[NextEIGEN Token Overview](/eigenlayer/overview/eigen-token-overview)

* 
* [Overview](/eigenlayer/overview/)
* Community and EIGEN Claim Support
Community and EIGEN Claim Support
=================================


For any discussion, engagement, and learning about EigenLayer, please join the [EigenLayer Community Discord](https://discord.gg/eigenlayer).


Restaker, Operator, and AVS Development Support
===============================================


For issues with the dApp, LST and restaking issues and Operator questions you may send us a question via our AI\-enabled chatbot and Support team here: [EigenLayer Support Desk](javascript:void(0))


$EIGEN Claim Support
====================


For any issues concerning $EIGEN including token claims and stakedrop issues, please visit the stakedrop\-support channel in the [EigenLayer Community Discord](https://discord.gg/eigenlayer). The Eigen Foundation support team can address your question there. Please see docs.eigenfoundation.org for information related to EIGEN token claims.


Please beware of any fraudulent tokens, dApps, and phishing sites:


* The only site to claim $EIGEN is: claims.eigenfoundation.org .
* The $EIGEN token contract address is: `0xec53bF9167f50cDEB3Ae105f56099aaaB9061F83` .
* The only support website is: docs.eigenlayer.xyz .


For a complete list of links and more information, please visit the: [EigenLayer Community Discord](https://discord.gg/eigenlayer).

[PreviousEIGEN Token Overview](/eigenlayer/overview/eigen-token-overview)[NextWhitepapers](/eigenlayer/overview/whitepaper)

* 
* [Overview](/eigenlayer/overview/)
* Whitepapers
Whitepapers
===========


**EigenLayer: The Restaking Collective** ([PDF](/assets/files/EigenLayer_WhitePaper-88c47923ca0319870c611decd6e562ad.pdf) / [HTML](/html/EigenLayer_WhitePaper-converted-xodo.html)): the research paper that formed the basis of the EigenLayer protocol development. The document discusses the original architecture of EigenLayer, the Restaking primitive, and the concept of AVSs.


**EIGEN The Universal Intersubjective Work Token:**([PDF](/assets/files/EIGEN_Token_Whitepaper-0df8e17b7efa052fd2a22e1ade9c6f69.pdf) / [HTML](/html/EIGEN_Token_Whitepaper-converted-xodo.html)): the research paper that introduces the structure of the EIGEN token, a universal intersubjective work token. We view this intersubjective work token as a first step towards the goal of building the Verifiable Digital Commons.

[PreviousCommunity and EIGEN Claim Support](/eigenlayer/overview/support)[NextIntroduction](/eigenlayer/operator-guides/operator-introduction)

* 
* Resources
* EigenLayer Infinite Hackathon
On this pageEigenLayer Infinite Hackathon
=============================

The EigenLayer Infinite Hackathon encourages submissions from developers building on EigenLayer, EigenLayer AVSs, EigenDA, and rollups built on EigenDA at any hackathon happening anywhere at any time now and in the future, both in\-person and online.


Submit your project [here](https://airtable.com/appnYZo360sWuEYLS/shrrnj9BWIPevjc5c).


If you're in the process of hacking in the EigenLayer ecosystem, join us in the EigenLayer Hacker group chat [here](https://airtable.com/appnYZo360sWuEYLS/shrz6Pstds7EXjC5N)!


![EigenLayer Infinite Hackathon](/assets/images/infinite-hackathon-7ec9c1db1c2832b854c617707b231049.png)


If you are building within the EigenLayer ecosystem as part of your hackathon project, you are qualified to submit and be eligible for prizes in the following categories.


1\. AVSs and open source AVS reference architectures[​](#1-avss-and-open-source-avs-reference-architectures "Direct link to 1. AVSs and open source AVS reference architectures")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Any new AVS or AVS reference architecture. Emphasis on code quality, documentation quality, and real world utility.


1. Ether \- $7,500\.00
2. Finney \- $5,000\.00
3. Gwei \- $2,500\.00
4. Wei \- $1,000\.00


To learn more about building AVSs, see [Awesome AVS](https://github.com/Layr-Labs/awesome-avs).


2\. Apps[​](#2-apps "Direct link to 2. Apps")
---------------------------------------------


Any new application that is built on EigenLayer AVSs or EigenDA rollups. Emphasis on code quality, documentation quality, and real world utility.


1. Ether \- $7,500\.00
2. Finney \- $5,000\.00
3. Gwei \- $2,500\.00
4. Wei \- $1,000\.00


You can see AVSs live on EigenLayer mainnet [here](https://www.eigenlayer.xyz/ecosystem?category=AVS), and rollups live on EigenDA [here](https://www.eigenlayer.xyz/ecosystem?category=EigenDA).


3\. EigenDA and rollups[​](#3-eigenda-and-rollups "Direct link to 3. EigenDA and rollups")
------------------------------------------------------------------------------------------


Any new tooling for, or rollups built, on EigenDA. Emphasis on code quality, documentation quality, and real world utility.


1. Ether \- $7,500\.00
2. Finney \- $5,000\.00
3. Gwei \- $2,500\.00
4. Wei \- $1,000\.00


To learn more about EigenDA, see the documentation [here](https://docs.eigenlayer.xyz/eigenda/overview).


### Eligibility Criteria[​](#eligibility-criteria "Direct link to Eligibility Criteria")


Participants of hackathons that are already hosted by, or that include prizes offered by, Eigen Labs or Eigen Foundation are not eligible.


Projects must be submitted within 14 days of original hackathon deadline.


Project code must be open source.


Full Hackathon Terms of Service are available [here](https://docs.google.com/document/d/1ZmW_WakvPobyps5XP_fkNs_AEAyXp-bq/edit?usp=sharing&ouid=115843462632021279280&rtpof=true&sd=true)

[PreviousAPIs, Dashboards, and Tooling](/eigenlayer/resources/apis-and-dashboards)[NextEigenLayer MicroHacks Hackathons](/eigenlayer/resources/avs-microhacks)* [1\. AVSs and open source AVS reference architectures](#1-avss-and-open-source-avs-reference-architectures)
* [2\. Apps](#2-apps)
* [3\. EigenDA and rollups](#3-eigenda-and-rollups)
	+ [Eligibility Criteria](#eligibility-criteria)


* 
* Resources
* Learning Resources
On this pageEigenLayer Learning Resources
=============================


### Start here[​](#start-here "Direct link to Start here")


* [Boys Club Ep 127: What is EigenLayer?](https://open.spotify.com/episode/2aR83WBag0pj0ldRRm2vZD)
* [You Could've Invented EigenLayer (Video)](https://www.youtube.com/watch?v=fCl_PucMytU)
* [The Three Pillars of Programmable Trust: The EigenLayer End Game](https://www.blog.eigenlayer.xyz/the-three-dimensions-of-programmable-trust/)
* [Shared Security: The Four Superpowers](https://twitter.com/sreeramkannan/status/1742949397523304600)


### Blog posts[​](#blog-posts "Direct link to Blog posts")


* [EigenLayer Blog](https://www.blog.eigenlayer.xyz/)
* [You Could've Invented EigenLayer (Blog)](https://www.blog.eigenlayer.xyz/ycie/)
* [The EigenLayer Universe: Ideas for Building the Next 15 Unicorns](https://www.blog.eigenlayer.xyz/eigenlayer-universe-15-unicorn-ideas/)
* [Dual Staking](https://www.blog.eigenlayer.xyz/dual-staking/)
* [EigenLayer for Developers](https://nader.substack.com/p/beyond-restaking-eigenlayer-for-developers)
* [EigenLayer: Intersubjective Faults, Token forking, bEIGEN \& more](https://mirror.xyz/edatweets.eth/l3QtrWv-27h5DVkrSdFMq96MRJ8AotemvmZIQ23Ew3A)


### Videos and podcasts[​](#videos-and-podcasts "Direct link to Videos and podcasts")


* [Official EigenLayer YouTube](https://www.youtube.com/@EigenLayer)
* [Unchained Podcast EigenLayer interview](https://www.youtube.com/watch?v=16p7YG8S3ec)
* [EigenLayer in 2024](https://www.youtube.com/watch?v=ms94dx9HvL0)
* [EigenLayer: The Endgame Coordination Layer](https://www.youtube.com/watch?v=o9y_pZUr0Nc)


### Developer resources[​](#developer-resources "Direct link to Developer resources")


* [Awesome AVS](https://github.com/Layr-Labs/awesome-avs)
* [Hello World AVS](https://github.com/Layr-Labs/hello-world-avs)
* [Incredible Squaring AVS](https://github.com/Layr-Labs/incredible-squaring-avs)
* [Eigen Go SDK](https://github.com/Layr-Labs/eigensdk-go)
* [EigenLayer Contracts](https://github.com/Layr-Labs/eigenlayer-contracts)
* [EigenLayer Middleware](https://github.com/Layr-Labs/eigenlayer-middleware)
* [EigenLayer CLI](https://github.com/Layr-Labs/eigenlayer-cli)
* [EigenDA](https://github.com/Layr-Labs/eigenda)


### Community[​](#community "Direct link to Community")


* [EigenLayer Forum](https://forum.eigenlayer.xyz/)
* [EigenLayer Research Forum](https://research.eigenlayer.xyz/)
* [Discord](https://discord.com/invite/eigenlayer)
* [EigenLayer Twitter](https://twitter.com/eigenlayer)
* [BuildOnEigen Twitter](https://x.com/buildoneigen)
[PreviousContract Addresses and Docs](/eigenlayer/deployed-contracts/)[NextAPIs, Dashboards, and Tooling](/eigenlayer/resources/apis-and-dashboards)* [Start here](#start-here)
* [Blog posts](#blog-posts)
* [Videos and podcasts](#videos-and-podcasts)
* [Developer resources](#developer-resources)
* [Community](#community)


* 
* Restaking Guides
* Restaking Guides
On this pageRestaking User Guide
====================


These guides will walk you through how EIGEN token holders, LST holders and Native Stakers can restake, withdraw and earn points on the [EigenLayer Web App](https://app.eigenlayer.xyz/).


**Liquid vs Native Restaking**[​](#liquid-vs-native-restaking "Direct link to liquid-vs-native-restaking")
----------------------------------------------------------------------------------------------------------


**Liquid restaking** is the process of depositing liquid staking tokens (LSTs) and EIGEN tokens into the EigenLayer smart contracts. At this time, the protocol supports the following tokens:


* EIGEN (EigenLayer)
* stETH (Lido)
* rETH (Rocket Pool)
* cbETH (Coinbase)
* wBETH (Binance)
* osETH (Stakewise)
* swETH (Swell)
* AnkrETH (Ankr)
* EthX (Stader)
* OETH (Origin ETH)
* sfrxETH (Frax Ether)
* lsETH (Liquid Staked ETH)
* mETH (Mantle Staked Ether)


The protocol plans to support additional liquid staking tokens in the future. If you would like to introduce your LST to the EigenLayer community, please do so on [the forum](https://forum.eigenlayer.xyz/t/about-the-new-lst-token-on-eigenlayer-category/6641).


**Native restaking** describes the process of setting an Ethereum validator's `withdrawCredential` to EigenLayer's smart contracts (EigenPod). You must operate an Ethereum Validator node in order to participate in Native Restaking.


Escrow Period (Withdrawal Delay)[​](#escrow-period-withdrawal-delay "Direct link to Escrow Period (Withdrawal Delay)")
----------------------------------------------------------------------------------------------------------------------


EigenLayer contracts feature a **7\-day** withdrawal delay for LST tokens and Native Restaking, a critical security measure for instances of vulnerability disclosure or when anomalous behavior is detected by monitoring systems. The withdrawal window for EIGEN token is **24\-days**, which is necessary to support future planned functionality unique to the token. Please see [Withdrawal Delay](/eigenlayer/security/withdrawal-delay) for more detail.

[PreviousWebapp Content Guidelines](/eigenlayer/operator-guides/operator-content-guidelines)[NextRestake and Delegate](/eigenlayer/restaking-guides/restaking-user-guide/liquid-restaking/restake-lsts)* [**Liquid vs Native Restaking**](#liquid-vs-native-restaking)
* [Escrow Period (Withdrawal Delay)](#escrow-period-withdrawal-delay)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* EIGEN Token Restaking FAQ
On this pageEIGEN Token Restaking FAQ
=========================

Please see the [EigenFoundation documentation site](https://docs.eigenfoundation.org/) for full details on the EIGEN token. This page will only cover behaviors of EIGEN token related to Restaking on the EigenLayer protocol.


### Can I Restake and Delegate EIGEN without Restaking and Delegating another type of asset (LST or Native Restaked ETH)?[​](#can-i-restake-and-delegate-eigen-without-restaking-and-delegating-another-type-of-asset-lst-or-native-restaked-eth "Direct link to Can I Restake and Delegate EIGEN without Restaking and Delegating another type of asset (LST or Native Restaked ETH)?")


Yes.


### Can I undelegate (and unstake) EIGEN without also undelegating (and unstaking) other assets?[​](#can-i-undelegate-and-unstake-eigen-without-also-undelegating-and-unstaking-other-assets "Direct link to Can I undelegate (and unstake) EIGEN without also undelegating (and unstaking) other assets?")


No. Per the [Undelegate from an Operator and Initiate Withdrawal](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/undelegate-from-an-operator-and-initiate-withdrawal), the action of Undelegation queues withdrawal (unstaking) for all restaked assets simultaneously.


### What is the contract address for EIGEN?[​](#what-is-the-contract-address-for-eigen "Direct link to What is the contract address for EIGEN?")


Please see the Deployments table [here](https://github.com/Layr-Labs/eigenlayer-contracts/?tab=readme-ov-file#strategies---eigen).


### Does restaking it give restaked points, etc.[​](#does-restaking-it-give-restaked-points-etc "Direct link to Does restaking it give restaked points, etc.")


Restaking EIGEN does not currently earn Restaked Points in the EigenLayer Web App. Please see [Will I earn rewards for staking EIGEN?](https://docs.eigenfoundation.org/faq/staking#will-i-earn-rewards-for-staking-eigen) for more detail.

[PreviousRestaked Points](/eigenlayer/restaking-guides/restaking-user-guide/restaked-points)[NextRestaking Developer Guide](/eigenlayer/restaking-guides/restaking-developer-guide)* [Can I Restake and Delegate EIGEN without Restaking and Delegating another type of asset (LST or Native Restaked ETH)?](#can-i-restake-and-delegate-eigen-without-restaking-and-delegating-another-type-of-asset-lst-or-native-restaked-eth)
* [Can I undelegate (and unstake) EIGEN without also undelegating (and unstaking) other assets?](#can-i-undelegate-and-unstake-eigen-without-also-undelegating-and-unstaking-other-assets)
* [What is the contract address for EIGEN?](#what-is-the-contract-address-for-eigen)
* [Does restaking it give restaked points, etc.](#does-restaking-it-give-restaked-points-etc)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* Liquid Restaking
* Restake and Delegate
Restake and Delegate
====================


Restake your LSTs \& Stake EIGEN by following the steps below.


**Step 1:** Open the EigenLayer App and connect your Web3 wallet. Visit EigenLayer on the Ethereum Mainnet at app.eigenlayer.xyz.


![](/assets/images/lst-restake-1-b77a8aef89c2673836996ec759f8d38b.png)


**Step 2:** Click **Restake**.


**Step 3:** Click on the asset you wish to restake. Choose the the amount of the asset you wish to restake. Click **Submit** to continue.


![](/assets/images/lst-restake-2-6f440184a93b733a41fef8a3bbc9ff16.png)


If you have not yet delegated your assets to an Operator, you will be prompted to do so at this step. Click on an Operator then click **Submit** to continue.


![](/assets/images/lst-restake-2.1-86eaa60fd313c95d153587c22492e90b.png)


**Step 4:** Token Approval, Deposit, and Delegate transactions:


* If this is your first time depositing a token on EigenLayer, you'll need to **Approve** token spending before you can restake. [Token Approval](https://support.metamask.io/hc/en-us/articles/6174898326683-What-is-a-token-approval-) gives a dApp permission to move the specified token from your wallet.
* If you have not yet delegated assets to an Operator, you will receive two transaction prompts: one for the **Deposit** transaction and second for the **Delegate** transaction.


**Step 5:** **Sign** the transaction(s) via your Web3 wallet to continue.


**Step 6:** Observe the confirmation that the Restake operation is completed.


![](/assets/images/lst-restake-3-1efbe41349b1e40b95b6045137e29b4e.png)

[PreviousRestaking User Guide](/eigenlayer/restaking-guides/restaking-user-guide/)[NextUnstake and Withdraw](/eigenlayer/restaking-guides/restaking-user-guide/liquid-restaking/withdraw-from-eigenlayer)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* Liquid Restaking
* Unstake and Withdraw
Unstake and Withdraw
====================


infoAll funds unstaked from EigenLayer will go through an escrow period before being eligible to be fully withdrawn. Please see the [Escrow Period](/eigenlayer/restaking-guides/restaking-user-guide/#escrow-period-withdrawal-delay) section for more detail.


**Step 1:** Navigate to the token asset you wish to unstake. Click **Unstake** to continue.


![](/assets/images/lst-unstake-1-743d9aac64c7b466b267aaad73bda386.png)


**Step 2:** Choose the the amount of the asset you wish to restake. Click **Submit** to continue.


![](/assets/images/lst-unstake-2-995ce0284a922191e59b35a65171e801.png)


**Step 3:** Click **Confirm** to sign the queue withdrawal transaction when prompted by your wallet.


**Step 4:** Observe the Unstake confirmation page. Your withdrawal is now in escrow. **Wait** for the escrow period to complete.


![](/assets/images/lst-unstake-3-168faef89f497ca05fdc301a58cbd74f.png)


**Step 5:** Once the escrow completes, you'll see the withdrawable balance under Available to Withdraw. Click **Withdraw** to complete the withdrawal. **Sign** the transaction when prompted by your Web3 wallet.


![](/assets/images/lst-unstake-4-c56a7f10b469bb5a96504cb4789d465a.png)


After the transaction is completed your withdrawn assets will be visible in your Web3 wallet.

[PreviousRestake and Delegate](/eigenlayer/restaking-guides/restaking-user-guide/liquid-restaking/restake-lsts)[NextNative Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* Native Restaking
On this pageNative Restaking
================


Native restaking describes the process of changing an Ethereum validator's [withdrawal credentials](https://notes.ethereum.org/@launchpad/withdrawals-faq#Q-What-are-withdrawals) to EigenLayer's smart contracts. You must operate an Ethereum Validator node in order to participate in Native Restaking. To learn more or set up your Ethereum Validator please follow this link from the [Ethereum Foundation](https://launchpad.ethereum.org/).


warningPlease read this entire guide before launching your new validator or integrating your existing validator.

Before you deploy a new validator you must plan to either:

* Initially provision the withdrawal credentials to your EigenPod address (created on the next page).
* Initially provision the withdrawal credentials to an 0x00 address. You can then later modify your withdrawal credentials to your EigenPod address.

Native Restaking on EigenLayer consists of the following actions:


1. Create New EigenPod, Set Withdrawal Credentials, Enable Restaking
2. Upgrade Existing EigenPod
3. Withdraw from EigenLayer


Stage 1 EigenPods Upgrade Requirement[​](#stage-1-eigenpods-upgrade-requirement "Direct link to Stage 1 EigenPods Upgrade Requirement")
---------------------------------------------------------------------------------------------------------------------------------------


Existing Stage 1 EigenPods will need to be **Upgraded** in order to be **actively restaked**. After the Eigenlayer contracts are updated for Stage 2 the EigenPod's "Current Restaked" amount will be moved to "Awaiting Restake" and the "Upgrade EigenPod" button will be clickable. EigenPods can then become actively Restaked by following the instructions in Upgrade Existing Eigenpod(link).


Deposit and Withdrawal Costs[​](#deposit-and-withdrawal-costs "Direct link to Deposit and Withdrawal Costs")
------------------------------------------------------------------------------------------------------------


Native Restaking Deposit and Withdrawal transactions will incur additional gas fees due to the required proof verification. Restaking with EigenLayer requires proof of beacon chain staking and active validator status. This proof is generated off chain during Deposit and Withdrawal then verified on chain. The verification process will incur a gas fee of approximately 200k gas \+ some fixed gas per proof. Please plan and budget accordingly for associated costs.


Safe Wallets and Native Restaking[​](#safe-wallets-and-native-restaking "Direct link to Safe Wallets and Native Restaking")
---------------------------------------------------------------------------------------------------------------------------


Restakers are welcome to leverage Safe Wallets for Native Restaking with EigenLayer. Restakers can choose either:


* Native Restaking via the [EigenLayer Web App](https://app.eigenlayer.xyz/), [Safe and WalletConnect](https://help.safe.global/en/articles/108235-how-to-connect-a-safe-to-a-dapp-using-walletconnect). This option will provide the simplest user experience.
* Restaking via Smart Contracts. Users with more advanced development and smart contract experience are welcome to:
	+ Learn how EigenLayer Native Restaking contracts work via reviewing our [eigenlayer\-contracts documentation](https://github.com/Layr-Labs/eigenlayer-contracts/tree/dev/docs#common-user-flows).
	+ Initiate the required transactions via [Safe Core or Safe Wallet](https://docs.safe.global/home/what-is-safe).
[PreviousUnstake and Withdraw](/eigenlayer/restaking-guides/restaking-user-guide/liquid-restaking/withdraw-from-eigenlayer)[NextCreate EigenPod and Set Withdrawal Credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/)* [Stage 1 EigenPods Upgrade Requirement](#stage-1-eigenpods-upgrade-requirement)
* [Deposit and Withdrawal Costs](#deposit-and-withdrawal-costs)
* [Safe Wallets and Native Restaking](#safe-wallets-and-native-restaking)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* Confirm Validator Withdrawal and Execution Addresses (Optional)
On this pageConfirm Validator Withdrawal and Execution Addresses (Optional)
===============================================================


Verifying your Validator’s Withdrawal and Execution addresses can help ensure you have configured your Native Restaking with EigenLayer safely. The instructions below will help you ensure that your Withdrawal address is set to your EigenPod and that your Execution address (aka “Fee Recipient”) is not set to your EigenPod. If you set the fee recipient to your EigenPod, execution layer rewards will be lost.


Please note in the documentation and API below, the following terms will be used:


* Consensus Client will also be referred to as Beacon Node client.
* Execution client will also be referred to as Validator client.


Confirming Withdrawal Address[​](#confirming-withdrawal-address "Direct link to Confirming Withdrawal Address")
---------------------------------------------------------------------------------------------------------------


Find your withdrawal credentials (which should match your EigenPod), via the following URL:


[https://beaconcha.in/validator/\[validator\_pubkey]\#deposits](https://beaconcha.in/validator/%5Bvalidator_pubkey%5D#deposits)


Confirming Execution Address[​](#confirming-execution-address "Direct link to Confirming Execution Address")
------------------------------------------------------------------------------------------------------------


To list your validator's Execution address (aka “Fee Recipient”), please refer to your Consensus Client specific documentation. For example:


* [Lighthouse: Querying the fee recipient](https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html#querying-the-fee-recipient)
* [Prysm: Configure fee recipient](https://docs.prylabs.network/docs/execution-node/fee-recipient#configure-fee-recipient)
* [Teku: Proposer configuration file attributes: fee\_recipient](https://docs.teku.consensys.io/how-to/configure/use-proposer-config-file)
[PreviousVerify Validator Withdrawal Prefix (Optional)](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/validator-eligibility-withdrawal-prefix)[NextDelegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/)* [Confirming Withdrawal Address](#confirming-withdrawal-address)
* [Confirming Execution Address](#confirming-execution-address)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* Create EigenPod and Set Withdrawal Credentials
Create EigenPod and Set Withdrawal Credentials
==============================================


An [EigenPod](https://github.com/Layr-Labs/eigenlayer-contracts/blob/master/docs/core/EigenPodManager.md) is a smart contract managed by users, designed to facilitate the EigenLayer protocol in monitoring and managing balance and withdrawal statuses. Please review the following considerations when planning your EigenPod and validator operations:


* You may repoint any number of validators to a single EigenPod.
* An Ethereum address can only deploy a single EigenPod.
* The address that deploys an EigenPod becomes the owner of the contract and gains permission for restaking and withdrawal operations.
* Ownership of an EigenPod cannot be transferred.


**Step 1:** Open the [EigenLayer App](https://app.eigenlayer.xyz/) and connect your Web3 wallet, making sure you are connected to Ethereum mainnet.


![](/assets/images/native-create-pod1-553be959c255beeb5e614f487b9ba69c.png)


**Step 2:** Click **Create EigenPod** to continue.


**Step 3:** Review the fee recipient warning and click **Create EigenPod**


![](/assets/images/native-create-pod2-94cde1a91b3a13a50bf8c17f1f3a0f5b.png)


If successful, you should receive a confirmation and the EigenPod Address will be displayed:
![](/assets/images/native-create-pod3-702ce54ce1aeeb689b598ad42cc378fd.png)


infoThis address is responsible for all subsequent restaking and withdrawal activities associated with that EigenPod.


dangerValidators SHOULD NOT direct execution rewards (`suggested_fee_recipient`) to their EigenPod. These funds may be irretrievably stuck.

[PreviousNative Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)[NextSet Validator Withdrawal Credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/repointing-a-validators-withdrawal-credentials)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* [Create EigenPod and Set Withdrawal Credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/)
* Enable Restaking
Enable Restaking
================


After your Beacon chain ETH balance has been proven and verified on chain, you will be able to Restake that ETH balance with EigenLayer. EigenLayer manages this process automatically via its beacon chain oracle service. Once the process is complete, you will see the balance in "Awaiting Restake" updated to reflect your Native Restaked balance.


warningThis process can take **up to 4 hours** after your validators have entered the active state on the beacon chain. You may use [beaconcha.in](https://beaconcha.in) as a reference during this process.


**Step 1:** Click **Restake** from the Beacon Chain Ether page.


**Step 2:** Observe the app is fetching beacon chain proofs and validating them on\-chain.


**Step 3:** **Confirm** the transaction via your Web3 wallet.


**Step 4:** Observe your Beacon Chain Restaked and Total Restaked balances have increased accordingly.

[PreviousSet Validator Withdrawal Credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/repointing-a-validators-withdrawal-credentials)[NextEigenPod Upgrade Guide](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/upgrade-eigenpod)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* [Create EigenPod and Set Withdrawal Credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/)
* Set Validator Withdrawal Credentials
On this pageSet Validator Withdrawal Credentials
====================================


infoIf you do not know your withdrawal prefix, please review [Validator Withdrawal Prefix](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/validator-eligibility-withdrawal-prefix) before starting this guide.


This guide provides a step\-by\-step walkthrough for users to set their validators' withdrawal credentials using one of three available methods: via [ethdo](#option-1-ethdo), through the [Consensus Client](#option-2-consensus-client), or directly from their [staking hardware device](#option-3-dappnode-avado-etc).


### Option 1: ethdo[​](#option-1-ethdo "Direct link to Option 1: ethdo")


ethdo is a CLI developed by independent Ethereum contributors. It abstracts a lot of complexity and has clear documentation.


1. Install [ethdo](https://github.com/wealdtech/ethdo)
2. Copy your **EigenPod address** from the EigenLayer app
3. Follow the [basic](https://github.com/wealdtech/ethdo/blob/master/docs/changingwithdrawalcredentials.md#basic-operation) or [advanced](https://github.com/wealdtech/ethdo/blob/master/docs/changingwithdrawalcredentials.md#advanced-operation) guide for changing your validator's withdrawal credentials.


infoInput the address copied in **step 2** as the **`--withdrawal-address`** flag.


4. Check that your validator has its withdrawal credentials correctly set by running the following command and replacing **VALIDATOR\_INDEX** with your validator's index.



```
ethdo validator credentials get --validator=VALIDATOR_INDEX  

```

### Option 2: Consensus Client[​](#option-2-consensus-client "Direct link to Option 2: Consensus Client")


Some consensus clients also have their own, implementation\-specific, support for withdrawal credential repointing.


1. Copy your `EigenPod address` from the EigenLayer app.
2. Follow your validator's consensus client guide and set the withdrawal address to the **EigenPod address**.


* [Prysm](https://docs.prylabs.network/docs/wallet/withdraw-validator#option-1-partial-earnings-withdrawals)
* [Teku](https://docs.teku.consensys.net/HowTo/Withdrawal-Keys)
* [Lighthouse](https://lighthouse-book.sigmaprime.io/voluntary-exit.html#faq)
* [Nimbus](https://nimbus.guide/withdrawals.html#updating-your-withdrawal-credentials)


For further information, please refer to the [notes](https://notes.ethereum.org/@launchpad/withdrawals-faq#Q-How-do-I-fully-withdraw-exit-my-validator) from the Ethereum organization


### Option 3: DAppNode, Avado, etc.[​](#option-3-dappnode-avado-etc "Direct link to Option 3: DAppNode, Avado, etc.")


1. Use this tool: [https://github.com/stake\-house/wagyu\-key\-gen/releases](https://github.com/stake-house/wagyu-key-gen/releases)
	* Click on "use existing recovery phrase" and generate BLS signature, which lets you unstake from the beacon chain and receive staking funds back in the execution layer.
	* We encourage airgapping (disconnect from the internet) while typing in your seed phrase.
2. Locate your validator ID in the Beacon chain explorer ([beaconcha.in](https://beaconcha.in/))
3. Broadcast the signature you generated in step 1 using this tool: <https://beaconcha.in/tools/broadcast>


warningValidators SHOULD NOT direct execution rewards (`suggested_fee_recipient`) to their EigenPod. These funds may be irretrievably stuck.

[PreviousCreate EigenPod and Set Withdrawal Credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/)[NextEnable Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/enable-restaking)* [Option 1: ethdo](#option-1-ethdo)
* [Option 2: Consensus Client](#option-2-consensus-client)
* [Option 3: DAppNode, Avado, etc.](#option-3-dappnode-avado-etc)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* EigenPod Upgrade Guide
EigenPod Upgrade Guide
======================


If your EigenPod was created prior to Stage 2, you will need to upgrade your EigenPod per the steps below.


EigenLayer Stage 2 enables proving the state of your validators from the beacon chain to EigenLayer smart contracts to confirm the amount restaked. As a result EigenPods that were created prior to M2 contract upgrades are required to have their balances reset to zero, then generate the proofs through the EigenLayer app in order to ensure proof accounting is accurate.


**Step 1:** Click **Upgrade EigenPod**.


**Step 2:** Review the fee recipient warning and click **Continue**.


**Step 3:** Review the disclaimer that you are about to trigger a withdrawal of Consensus Rewards from your EigenPod. Click **Confirm** to continue.


**Step 4:** Observe the Restaking Activated confirmation and explanation that Restaking will be available after the next beacon state update.

[PreviousEnable Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/enable-restaking)[NextUnstake and Withdraw](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* Verify Validator Withdrawal Prefix (Optional)
On this pageVerify Validator Withdrawal Prefix (Optional)
=============================================


Beacon chain validators contain a field known 'withdrawal credentials', which can be utilized in the future to withdraw funds from the validator's balance on the beacon chain. The first two bytes of these credentials are known as the [**withdrawal prefix**](https://notes.ethereum.org/@launchpad/withdrawals-faq#Q-What-are-0x00-and-0x01-withdrawal-credentials-prefixes).


The prefix can either be `0x00` or `0x01`:


* Validators with `0x00` prefix: These are specific to BLS\-style withdrawal credentials, common to early ETH stakers. Validators with this prefix can easily restake on EigenLayer, by [repointing](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/repointing-a-validators-withdrawal-credentials) their withdrawal credentials.
* Validators with `0x01` prefix: This newer method is derived from Ethereum addresses. While beacon chain rewards are much easier for these validators, restaking on EigenLayer is quite difficult. In order for `0x01` validators to restake, they have to completely exit from the beacon chain, re\-enter on the beacon chain as a new validator, and then repoint withdrawal credentials to the EigenLayer smart contract.


**New Validators**[​](#new-validators "Direct link to new-validators")
----------------------------------------------------------------------


ETH stakers planning to create new validators can set their withdrawal credential directly to their EigenPod or deploy with 0x00 prefixed withdrawal credentials for an easier transition to EigenLayer later. In order to use the 0x00 prefix, do not set *\-\-execution\_address* or *\-\-eth1\_withdrawal\_address* flags [when setting up new validators.](https://github.com/ethereum/staking-deposit-cli#commands)


**Existing Validators**[​](#existing-validators "Direct link to existing-validators")
-------------------------------------------------------------------------------------


### **How do I check if I have a `0x00` or an `0x01` address?**[​](#how-do-i-check-if-i-have-a-0x00-or-an-0x01-address "Direct link to how-do-i-check-if-i-have-a-0x00-or-an-0x01-address")


There are multiple methods to do this; the easiest is using [`ethdo`](https://github.com/wealdtech/ethdo).



```
ethdo validator info --validator=<yourvalidatorIndex> --verbose  

```

This outputs a **withdrawal credentials** field which either begins with `0x00` or `0x01`.


Additionally, you can check [beaconcha.in](http://beaconcha.in/), navigate to your validator page, and check the **Beaconchain Deposits** field under the Deposits tab.


### **Prefix Migration from 0x00 to 0x01**[​](#prefix-migration-from-0x00-to-0x01 "Direct link to prefix-migration-from-0x00-to-0x01")


If you have 0x00\-prefixed credentials, you can only [migrate once](https://notes.ethereum.org/@launchpad/withdrawals-faq#Q-Once-I-have-changed-my-credential-to-0x01-can-I-change-it-to-an-alternative-withdrawal-address) to a 0x01\-prefixed credential per the Ethereum protocol rules. You may choose to either:


* Migrate your withdrawal credential to your EigenPod address.
* Migrate (convert) your withdrawal credential from a [BLS address (0x00\) to an execution address (0x01\)](https://notes.ethereum.org/@launchpad/withdrawals-guide#BLS-to-execution-with-ethdo), noting that an EigenPod qualifies as an execution address. It's crucial to understand that if the withdrawal credential is set to a 0x01 address that does not correspond to your EigenPod, you will be unable to restake. In such a scenario, exiting your validators becomes a necessary step.


If you update your credentials **before** restaking on EigenLayer, you will have to go through the withdrawal queue and then restart the ETH validator staking process.


dangerThis migration is a **one\-time** process, so please proceed cautiously.


### Existing Validators with 0x01 Prefixes[​](#existing-validators-with-0x01-prefixes "Direct link to Existing Validators with 0x01 Prefixes")


If you have validators with 0x01 prefixes that are not pointed to an EigenPod, you will have to go through the withdrawal queue. In this case, you'll need to withdraw your ETH, create a new Ethereum validator with the withdrawn ETH, and set the withdrawal credentials to an EigenPod to restake on EigenLayer.

[PreviousFull Withdrawal](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/full-withdrawal)[NextConfirm Validator Withdrawal and Execution Addresses (Optional)](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/confirm-withdraw-exec-addrs)* [**New Validators**](#new-validators)
* [**Existing Validators**](#existing-validators)
	+ [**How do I check if I have a `0x00` or an `0x01` address?**](#how-do-i-check-if-i-have-a-0x00-or-an-0x01-address)
	+ [**Prefix Migration from 0x00 to 0x01**](#prefix-migration-from-0x00-to-0x01)
	+ [Existing Validators with 0x01 Prefixes](#existing-validators-with-0x01-prefixes)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* Unstake and Withdraw
Unstake and Withdraw
====================


Please refer to the Ethereum Foundation’s documentation on [how withdrawal payments work](https://ethereum.org/en/staking/withdrawals/#how-do-withdrawals-work).


There are two kinds of withdrawals from native restaking in EigenLayer:


* **Partial** withdrawals: balances in excess of 32 ETH (earned rewards) are withdrawn to an Ethereum address. The validator will continue to be a part of the beacon chain and validate as expected.
* **Full** withdrawals: users have the ability to cease their staking activities entirely. By choosing this option, they initiate the process of unlocking the entire balance held by their validator, including both the initial stake and any accumulated rewards. This action effectively ends their validator's participation in the network.
[PreviousEigenPod Upgrade Guide](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/upgrade-eigenpod)[NextPartial Withdrawals](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/partial-withdrawals)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* [Unstake and Withdraw](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/)
* Full Withdrawal
Full Withdrawal
===============


Full Withdrawal is the process of unlocking the entire balance held by their validator, including both the initial stake and any accumulated rewards. The following order of operations are required to complete a Full withdrawal of your natively restaked ETH and avoid proof generation errors.


**Step 1:** Ensure you have [repointed your validator's withdrawal credentials](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/create-eigenpod-and-set-withdrawal-credentials/repointing-a-validators-withdrawal-credentials) to your EigenPod.


**Step 2:** Fully exit your validator from the beacon chain. You may monitor its activity via beaconcha.in/validator/\[yourvalidatorindex] or \[yourvalidatorpublickey] .


**Step 3:** Wait for the final beacon chain withdrawal to be deposited to your EigenPod. There can be a lag of up to 24 hours to 7 days between the validator appearing as "exited" and the withdrawal amount deposited to EigenPod. Please see the "Withdrawals" tab and "Time" column for your validator via beaconcha.in/validator/\[yourvalidatorid]\#withdrawals .


**Step 4:**. Queue the full withdrawal from your Eigenpod. Navigate to the **Beacon Ether** asset page in the (EigenLayer App)\[<https://app.eigenlayer.xyz/>].


**Step 5:** Enter the amount in the text box next to the Unstake button.


You can queue a withdrawal for any amount. However, when you choose to complete the withdrawal, you will be required to exit enough validators and have the proofs generated for the required amount.


**Step 6:** Click **Unstake**. **Sign** the transaction using your Web3 wallet.


**Step 7:** Wait for the escrow period to complete. Observe the Unstaking balance has increased during the escrow period.


**Step 8:** Observe the Unstaked Beacon Chain balance has increased after the escrow period. The Execution Chain amount should have increased by the amount of those exited validators.


infoThe Redeposit button is available at this point to allow the user to Restake back into EigenLayer in case the withdrawal was queued by mistake.


**Step 9:** Click Withdraw to complete your withdrawal. **Sign** the transaction using your Web3 wallet.


infoRedelegation is available for a user who accidentally queues a withdrawal, but would like to resume staking and delegation without having to exit and re\-enter their validators from the beacon chain.

[PreviousPartial Withdrawals](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/partial-withdrawals)[NextVerify Validator Withdrawal Prefix (Optional)](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/validator-eligibility-withdrawal-prefix)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Native Restaking](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/)
* [Unstake and Withdraw](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/)
* Partial Withdrawals
Partial Withdrawals
===================


infoDue to how withdrawals from Ethereum are designed, users can only initiate one partial withdrawal per [sequential sweep](https://ethereum.org/en/staking/withdrawals/#validator-sweeping) of all validators (which takes approximately 4\-5 days).

All funds unstaked from EigenLayer go through a escrow period before being able to be withdrawn. After you unstake and queue the withdrawal, you must wait for the escrow period to end before being able to withdraw your assets.


Partial withdrawals require on\-chain proofs in order to process the withdrawal. Please consider deferring your withdrawals until full withdrawals are needed due to the gas costs associated with the proof.


The verification process will incur a gas fee of approximately 200k gas \+ some fixed gas per proof. Each of these proofs will be able to prove up to 20 beacon chain withdrawals (batched into one transaction). The user will be prompted to sign additional transactions \- one per each additional batch.


**Step 1:** Note the values for "Validator ETH Yield" and "Redeemable".


warningThe Redeemable value may temporarily appear lower than the Validator ETH Yield (beacon chain) due to the time lag associated with the EigenLayer beacon chain oracle. This sync occurs approximately every 4 hours.


**Step 2:** Click **Redeem** to initiate the escrow period.


**Step 3:** Observe the gas fee warning. Click **Continue**.


**Step 4:** Enter the amount you wish to withdraw. Click **Confirm**.


If the Awaiting Restake value is greater than zero, the confirmation step above will generate proofs to restake that amount first.


**Step 5:** Observe the Fetching Proofs status message. Proofs will be submitted on chain and you will be prompted to sign the transaction to proceed.


Note: if the user has more than 16 partial withdrawal transactions queued on the beacon chain, additional transactions will be generated for each batch of partial withdrawals in increments of 16 partial withdrawals.


Observe the Unstaking balance has increased after the transaction is confirmed on chain.


**Step 6:** Click **Withdraw** after the escrow period to withdraw funds. Two wallet transactions will be generated for you to approve and proceed.


Observe your funds have been sent to your wallet.

[PreviousUnstake and Withdraw](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/)[NextFull Withdrawal](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/withdraw-from-eigenlayer/full-withdrawal)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* Restaked Points
On this pageRestaked Points
===============

Overview[ ​](#overview "Direct link to Overview")
-------------------------------------------------


Restaked points are a measure of your contribution to the shared security of the EigenLayer ecosystem. They are a measure of staking participation equal to the time\-integrated amount staked in units of ETH ⋅\\cdot⋅ hours.


Calculations[​](#calculations "Direct link to Calculations")
------------------------------------------------------------


In the formulas that follow, iii represents the index of a staker, while jjj represents the index of a token.


The participation measure of a staker iii for a token jjj is given by the formula


Pij\=∫t\=0TSij(t)dtP\_{ij} \= \\int\_{t\=0}^T S\_{ij}(t)dtPij​\=∫t\=0T​Sij​(t)dt
where Sij(t)S\_{ij}(t)Sij​(t) represents the amount of token jjj held by staker iii at time ttt, measured in nominal units of ETH. For the purposes of the nominal participation measure, we treat all tokens, such as Native Restaked ETH and Liquid Staked ETH (LSTs) equivalently and calculate the total participation measure in units of ETH ⋅\\cdot⋅ hours. Points are accrued for each Ethereum block that a token is actively staked.


For instance, a user who stakes 1 stETH for 10 days should accrue 240 restaking points over this time period (1 ETH ×\\times× 10 days ×\\times× 24 hours/day \= 240 ETH ⋅\\cdot⋅ hours).


For natively staked ETH, we treat Sij(t)S\_{ij}(t)Sij​(t) as a step function for each validator which transitions from 0 to 32ETH at the validator's activation epoch or BLS to execution change epoch and then back to 0 at the validator's exit epoch.


To obtain the total participation measure for a staker iii, we sum the measures for each token held by that staker:


Pi\=∑jPij.P\_i \= \\sum\_j P\_{ij}.Pi​\=j∑​Pij​.
Finally, the restaked ratio gives the ratio of a given staker iii's participation measure to the aggregated participation measures across all stakers:


Ri\=Pi∑i′Pi′.R\_i \= \\frac{P\_i}{\\sum\_{i'} P\_{i'}}.Ri​\=∑i′​Pi′​Pi​​.
Additional clarifications for Native Restaking:


* Consensus layer rewards are not included in the points calculation. Restaked points for native restaked is based on the validator's Effective Balance (capped at 32 ETH), rather than the validator's Current Balance (which includes rewards).
* For Native and LST Restaking, points accrual ends at the “Complete Withdrawal” action when the funds have exited EigenLayer completely.
* ​Currently users do not earn restaked points for staking EIGEN. Please see the [FAQ here](https://docs.eigenfoundation.org/faq/staking#will-i-earn-rewards-for-staking-eigen) for more information.
[PreviousRewards Claiming FAQ](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/rewards-claiming-faq)[NextEIGEN Token Restaking FAQ](/eigenlayer/restaking-guides/restaking-user-guide/EIGEN-faq)* [Overview](#overview)
* [Calculations](#calculations)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* Delegation
On this pageDelegation
==========


Delegation is the process of assigning Restaked balance to an Operator. The Restaker will receive fees according to the AVSs that the Operator chooses to run. Restakers can undelegate their balance to end their assignment to the Operator and later redelegate the balance to a new Operator.


Caveats:


* Stakers can only delegate to a single Operator at a time.
* Delegation is an "all or nothing" operation. You must delegate all of your available Restaked balance to a single Operator.
* Delegation is not possible for Native Restakers while their validators are in the activation (aka entry) queue. Native Restaked tokens must be fully Restaked and proven on\-chain before they can be delegated.
* If you have already delegated your stake to an operator in any quorum, all new stakes will be delegated to the same operator automatically.
* If the delegated Operator is no longer in the active set of an AVS (such as due to [Churning in EigenDA](/eigenda/operator-guides/requirements/delegation-requirements) for example), the Restaker has the option to Redelegate their TVL balance to another Operator. Please see the [Undelegate from an Operator and Initiate Withdrawal](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/undelegate-from-an-operator-and-initiate-withdrawal) page for specific instructions.


**Staker and Operator Roles Clarification**[​](#staker-and-operator-roles-clarification "Direct link to staker-and-operator-roles-clarification")
-------------------------------------------------------------------------------------------------------------------------------------------------


Operators are not required to be Restakers. An Ethereum address can be both a Restaker (via liquid or native restaking) and simultaneously an Operator, however this is not a requirement. An Operator can have zero restaked tokens in EigenLayer.


For Operators who self delegate as Restakers we recommend the Operator use **separate addresses** for Restaking and Operating activities. A single address that is used for both Restaking and Operators cannot undelegate from itself, it can only withdraw restaked funds. For this reason we recommend Operators use separate Restaking addresses if they wish avoid this limitation.


An Operator is required to have tokens delegated to their address. The delegation can come from other Restakers or they can self\-delegate their restaked token balance.

[PreviousConfirm Validator Withdrawal and Execution Addresses (Optional)](/eigenlayer/restaking-guides/restaking-user-guide/native-restaking/confirm-withdraw-exec-addrs)[NextDelegate to an Operator](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/delegate-to-an-operator)* [**Staker and Operator Roles Clarification**](#staker-and-operator-roles-clarification)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Delegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/)
* Delegate to an Operator
Delegate EIGEN, LSTs, and Native Restaked ETH to an Operator
============================================================


Follow the steps below to initiate delegation of your Restaked balance to an Operator of your choice. This Restaked balance includes EIGEN tokens, LST tokens, and Native Restaked TVL.


Delegation is a unified step in the standard EIGEN and LST Restaking flow. For Native Restakers or scenarios where the unified Restaking flow was not completed, the following steps will allow you to delegate your stake directly.


**Step 1:** Navigate to the **Operator** page to view a list of available Operators.


![](/assets/images/delegate-1-3c0ee46fa17b481863d77340de883657.png)


**Step 2:** Search for operators via their name or Ethereum address. Click on the **Operator's tile** to view their Detail page.


![](/assets/images/delegate-2-f10c94706261e74d7a7c49e653a47097.png)


**Step 3:** Click **Delegate** to initiate a delegation of all your staked assets to that operator.


**Step 4:** Confirm the transaction in your Web3 wallet.


**Step 5:** Note the delegating progress message.


**Step 6:** After the transaction has been confirmed, please note your stake will show as Delegated for that Operator.


![](/assets/images/delegate-3-5ebfefaa1c45e2a6f9f907693f0b35b9.png)

[PreviousDelegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/)[NextUndelegate and Initiate Withdrawal](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/undelegate-from-an-operator-and-initiate-withdrawal)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Delegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/)
* Change Your Delegation
On this pageChange Your Delegation to a New Operator
========================================


The following steps are necessary for a Restaker to **move** their Delegated balance to a New Operator. The process below requires users to perform each of the following steps in order:


* **Undelegate** assets, which automatically queues a **withdrawal**. The Undelegate and Queue Withdrawal transactions are combined due to the security architecture of EigenLayer smart contracts.
* **Redeposit** each asset.
* **Delegate** to the new Operator.


warningPlease follow the recommended steps below carefully to avoid a "partially delegated state". A partially delegated state is when some portion of your assets in Delegated state and other assets in a "queued for withdrawal" or "withdrawal ready for completion" state.


Process to Change Your Delegation to a New Operator[​](#process-to-change-your-delegation-to-a-new-operator "Direct link to Process to Change Your Delegation to a New Operator")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


**Step 1:** Visit the **Operator** page for your currently delegated Operator. Click **Undelegate**.


![undelegate button](/assets/images/delegate-3-5ebfefaa1c45e2a6f9f907693f0b35b9.png)


**Step 2:** **Confirm** the Undelegate transaction in your Web3 wallet.


**Step 3:** **Observe** that your Restaked balances are now 0\.0 TVL. Those assets are now undelegated from the previous Operator appear in "Pending Withdraw" state.


**Step 4:** **Wait** for the escrow period to end before continuing. Please see [Testnet vs Mainnet differences for detail](/eigenlayer/restaking-guides/restaking-user-guide/testnet/#testnet-vs-mainnet-differences).


**Step 5:** Manually Redeposit each asset. **Navigate** to each asset page individually. Navigate to the **Unstake** tab, click **Redeposit**. This will prompt a Redeposit transaction for each asset that you will confirm in your Web3 wallet.


**Step 6:** After all assets have been redeposited, **navigate** to the Operator page for the new operator you wish to delegate to. Click **Delegate** button.


![](/assets/images/delegate-2-f10c94706261e74d7a7c49e653a47097.png)


**Step 7:** **Observe** that your delegation has been changed to the new Operator.


infoDo not click the **Redelegate** button on the Operator page. The button is intended to be used only for users that have funds in a "partially delegated state".

[PreviousUndelegate and Initiate Withdrawal](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/undelegate-from-an-operator-and-initiate-withdrawal)[NextTestnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)* [Process to Change Your Delegation to a New Operator](#process-to-change-your-delegation-to-a-new-operator)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Delegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/)
* Undelegate and Initiate Withdrawal
On this pageUndelegate from an Operator and Initiate Withdrawal
===================================================


Restakers can Undelegate their balance from an Operator at any time. Undelegation flows are the same for both Native and LST Restakers.


infoInitiating an Undelegate transaction will also **automatically queue a withdrawal**, but not complete (finalize) the withdrawal. The Undelegate and Queue Withdrawal transactions are combined due to the security architecture of EigenLayer smart contracts. If you wish to redeposit, you can do so immediately after the escrow period ends. If you want to complete the withdrawal, you can do so immediately after the escrow period ends.


Instructions to Undelegate and Queue Withdraw[​](#instructions-to-undelegate-and-queue-withdraw "Direct link to Instructions to Undelegate and Queue Withdraw")
---------------------------------------------------------------------------------------------------------------------------------------------------------------


**Step 1:** Navigate to the Operator tab, click the tile for the Operator you have delegated your funds to. Click the Undelegate button to continue.


![](/assets/images/delegate-4-a772a3fa598b65345dfe758d90c1bc9f.png)


**Step 2:** Confirm the Undelegate transaction in your Web3 wallet.


**Step 3:** Observe that your Restaked balances are now 0\.0 TVL.


**Step 4:** Wait for the escrow period to end before continuing. Please see [Testnet vs Mainnet differences for detail](/eigenlayer/restaking-guides/restaking-user-guide/testnet/#testnet-vs-mainnet-differences).


**Step 5:** Visit any individual page for your unstaked assets and observe your **Unstaked** balance has increased by the corresponding amount.


**Step 6:** Click **Withdraw** to finalize the withdrawal for the asset.


![](/assets/images/delegate-5-91f2b91c1d9e3a9669bfe7fadf26fe4c.png)


infoThe "Redeposit" button is also available for the user to Restake funds in case the withdrawal was initiated by mistake.


**Step 7:** Repeat steps 5 and 6 above for any remaining assets where you wish to finalize withdrawal.

[PreviousDelegate to an Operator](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/delegate-to-an-operator)[NextChange Your Delegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/redelegation-process)* [Instructions to Undelegate and Queue Withdraw](#instructions-to-undelegate-and-queue-withdraw)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* Testnet Restaking
On this pageTestnet Restaking
=================

Testing Restaking on the Holesky Testnet[​](#testing-restaking-on-the-holesky-testnet "Direct link to Testing Restaking on the Holesky Testnet")
------------------------------------------------------------------------------------------------------------------------------------------------


Users are encouraged to first test their staking approach on the Holesky Testnet prior to restaking on ETH Mainnet.


* Follow the instructions in [obtaining\-testnet\-eth\-and\-liquid\-staking\-tokens\-lsts.md](/eigenlayer/restaking-guides/restaking-user-guide/testnet/obtaining-testnet-eth-and-liquid-staking-tokens-lsts "mention") to fund your Testnet wallet.
* Visit [**holesky.eigenlayer.xyz**](https://holesky.eigenlayer.xyz/) for the most recent EigenLayer Testnet app.
* Users should only use the native restaking path if they already have their own validators on Holesky or know how to set one up. Otherwise, please go down the Liquid Restaking path.


Testnet vs Mainnet Differences[​](#testnet-vs-mainnet-differences "Direct link to Testnet vs Mainnet Differences")
------------------------------------------------------------------------------------------------------------------


* Withdraw (Escrow) Period:
	+ All funds unstaked from *EigenLayer Testnet* go through a delay (escrow period) of 10 blocks (roughly 2 minutes) before being able to be withdrawn.
	+ LST tokens and Native Restaking funds unstaked from *EigenLayer Mainnet* will go through a 7\-day escrow period before being able to be withdrawn. EIGEN token will go through a 24\-day escrow period.
* Holesky Testnet will not include Restaked Points calculations.
[PreviousChange Your Delegation](/eigenlayer/restaking-guides/restaking-user-guide/restaker-delegation/redelegation-process)[NextObtaining Testnet ETH \& Liquid Staking Tokens (LSTs)](/eigenlayer/restaking-guides/restaking-user-guide/testnet/obtaining-testnet-eth-and-liquid-staking-tokens-lsts)* [Testing Restaking on the Holesky Testnet](#testing-restaking-on-the-holesky-testnet)
* [Testnet vs Mainnet Differences](#testnet-vs-mainnet-differences)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Testnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)
* Obtaining Testnet ETH \& Liquid Staking Tokens (LSTs)
On this pageObtaining Testnet ETH \& Liquid Staking Tokens (LSTs)
=====================================================


In this guide, we will show you how to use a Holesky faucet to load your wallet with [testnet ETH](https://ethereum.org/en/developers/docs/networks/#ethereum-testnets) and how to obtain Holesky Liquid Staking Tokens so you can start testing liquid restaking.


### Prerequisites[​](#prerequisites "Direct link to Prerequisites")


Before you can use a faucet to load your wallet with testnet ETH, you will need:


* An Ethereum\-compatible wallet (e.g. MetaMask). Take note of its public address.
* Add Holesky network to your Web3 wallet (example instructions [here](https://www.coingecko.com/learn/holesky-testnet-eth#add-the-holesky-testnet-to-metamask)) if it does not automatically appear.


Obtain Holesky ETH (aka holETH) via a Faucet[​](#obtain-holesky-eth-aka-holeth-via-a-faucet "Direct link to Obtain Holesky ETH (aka holETH) via a Faucet")
----------------------------------------------------------------------------------------------------------------------------------------------------------


Once you have a Holesky compatible wallet and a Holesky ETH address, you can use a faucet to load your wallet with testnet ETH. Here are options available to obtain holETH:


* [Holešky PoW Faucet](https://holesky-faucet.pk910.de)
* [Quicknode Faucet](https://faucet.quicknode.com/ethereum/holesky)
* [Automata Faucet](https://www.holeskyfaucet.io/)


Swap holETH for wETH (Wrapped ETH)​[​](#swap-holeth-for-weth-wrapped-eth "Direct link to Swap holETH for wETH (Wrapped ETH)​")
------------------------------------------------------------------------------------------------------------------------------


* Send holETH to address 0x94373a4919B3240D86eA41593D5eBa789FEF3848\.
* Import the WETH token address (0x94373a4919B3240D86eA41593D5eBa789FEF3848\) to your web3 wallet to view your token balance.


Swap holETH for stETH (Lido)​[​](#swap-holeth-for-steth-lido "Direct link to Swap holETH for stETH (Lido)​")
------------------------------------------------------------------------------------------------------------


* Visit: [https://stake\-holesky.testnet.fi/](https://stake-holesky.testnet.fi/)
* Connect your web3 wallet, choose the amount and click **Stake**.
* Import the [Lido and stETH token (proxy)](https://docs.lido.fi/deployed-contracts/holesky/) address for Holesky stETH token to your web3 wallet to view your token balance.
* Note: Lido on Holesky staking is rate\-limited to 1500 holETH per rolling 24hr window.


Swap holETH for ETHx (Stader)​[​](#swap-holeth-for-ethx-stader "Direct link to Swap holETH for ETHx (Stader)​")
---------------------------------------------------------------------------------------------------------------


* Visit the Stader Holesky proxy contract’s Write as Proxy contract in Etherscan here: [0x7F09ceb3874F5E35Cd2135F56fd4329b88c5d119](https://holesky.etherscan.io/address/0x7F09ceb3874F5E35Cd2135F56fd4329b88c5d119#writeProxyContract).
* Click *Connect to Web3* to connect your web3 wallet.
* Click either of the **1\.deposit()** or **2\.deposit()** functions to expand their section:
* payableAmount: Enter the ETH amount you wish to deposit.
* \_receiver: the recipient of the ETHx. Most likely this will be your wallet address.
* \_referralId (string): use the empty string (“”), if prompted.
* Click *Write* to initiate the transaction. Approve the transaction in your web3 wallet.
* Import the Holesky ETHx token address (0xB4F5fc289a778B80392b86fa70A7111E5bE0F859\) to your web3 wallet to view your token balance.


Stake holETH for ankrETH (Ankr)​[​](#stake-holeth-for-ankreth-ankr "Direct link to Stake holETH for ankrETH (Ankr)​")
---------------------------------------------------------------------------------------------------------------------


* Visit [testnet.ankr.com/staking/stake/ethereum](https://testnet.ankr.com/staking/stake/ethereum/).
* Follow the instructions on screen to stake (convert) your desired amount of Holesky ETH for Holesky ankrETH.
* Click “Add ankrETH to wallet” to add the ankrETH token to your web3 wallet and view your available balance.


Mint osETH (Stakewise)[​](#mint-oseth-stakewise "Direct link to Mint osETH (Stakewise)")
----------------------------------------------------------------------------------------


* Visit the [Stakewise Holesky Vault Marketplace](https://app.stakewise.io/vaults?networkId=holesky).
* Select a vault to mint osETH.
* Input the amount you wish to stake and click **Stake** and verify the transaction in your Web3 wallet.
* Click *Mint* to convert your staked holETH to osETH and verify the transaction in your Web3 wallet.
* Click “Add osETH to your Wallet”
* Or import the osETH address (0xF603c5A3F774F05d4D848A9bB139809790890864\) for Holesky stETH token to your web3 wallet to view your token balance.


Mint and Stake to Swap holETH for sfrxETH[​](#mint-and-stake-to-swap-holeth-for-sfrxeth "Direct link to Mint and Stake to Swap holETH for sfrxETH")
---------------------------------------------------------------------------------------------------------------------------------------------------


* Add Holesky to your Web3 wallet (example instructions [here](https://www.coingecko.com/learn/holesky-testnet-eth#add-the-holesky-testnet-to-metamask)).
* Manually switch your wallet to the Holesky network. The Frax Finance app does not allow the user to choose Holesky directly.
* Open the Frax Finance Mint app: [app.frax.finance/frxeth/mint](https://app.frax.finance/frxeth/mint) .
* Enter the amount you wish to mint and click **Mint \& Stake**.
* Import the Holesky sfrxETH token address (0xa63f56985F9C7F3bc9fFc5685535649e0C1a55f3\) to your web3 wallet to view your token balance.


Swap holETH for mETH (Mantle ETH)​[​](#swap-holeth-for-meth-mantle-eth "Direct link to Swap holETH for mETH (Mantle ETH)​")
---------------------------------------------------------------------------------------------------------------------------


* Visit the MantleETH proxy contract’s Write as Proxy contract in Etherscan here: [0xbe16244EAe9837219147384c8A7560BA14946262](https://holesky.etherscan.io/address/0xbe16244EAe9837219147384c8A7560BA14946262#writeProxyContract).
* Click **Connect to Web3** to connect your web3 wallet.
* Click on the **19\.stake()** function to expand its section:
	+ payableAmount: Enter the ETH amount you wish to deposit.
	+ minMETHAmount: set to 0\.
* Click **Write** to initiate the transaction. Approve the transaction in your web3 wallet.
* Import the Holesky mETH token address (0xe3C063B1BEe9de02eb28352b55D49D85514C67FF) to your web3 wallet to view your token balance.
[PreviousTestnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)[NextRewards Claiming Overview](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/rewards-claiming-overview)* [Prerequisites](#prerequisites)
* [Obtain Holesky ETH (aka holETH) via a Faucet](#obtain-holesky-eth-aka-holeth-via-a-faucet)
* [Swap holETH for wETH (Wrapped ETH)​](#swap-holeth-for-weth-wrapped-eth)
* [Swap holETH for stETH (Lido)​](#swap-holeth-for-steth-lido)
* [Swap holETH for ETHx (Stader)​](#swap-holeth-for-ethx-stader)
* [Stake holETH for ankrETH (Ankr)​](#stake-holeth-for-ankreth-ankr)
* [Mint osETH (Stakewise)](#mint-oseth-stakewise)
* [Mint and Stake to Swap holETH for sfrxETH](#mint-and-stake-to-swap-holeth-for-sfrxeth)
* [Swap holETH for mETH (Mantle ETH)​](#swap-holeth-for-meth-mantle-eth)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Testnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)
* Rewards Claiming
* Claim Rewards
* Using CLI
On this pageUsing CLI
=========


Follow the instructions below step by step in order to claim your currently available rewards in the EigenLayer web app via EigenLayer CLI. Rewards can be claimed by a Staker or Operator.


### Step 1: Install the latest version of EigenLayer CLI[​](#step-1-install-the-latest-version-of-eigenlayer-cli "Direct link to Step 1: Install the latest version of EigenLayer CLI")


Head over to the [installation instructions](https://github.com/Layr-Labs/eigenlayer-cli#install-eigenlayer-cli-using-a-binary) for getting the binary with your preferred way.


Below steps assume that you have used the default binary installation command and your binary is installed at `./bin/` location


### Step 2: Check if installation is correct[​](#step-2-check-if-installation-is-correct "Direct link to Step 2: Check if installation is correct")



```
./bin/eigenlayer --version  

```

This should output the version of EigenLayer CLI installed



```
eigenlayer version v<X.X.X>  

```

### Step 3: Check if rewards are available to claim[​](#step-3-check-if-rewards-are-available-to-claim "Direct link to Step 3: Check if rewards are available to claim")


* Mainnet
* Holesky


```
./bin/eigenlayer rewards show \  
  --network mainnet \  
  --earner-address <earner-address> \  
  --claim-type unclaimed  
  

```

```
./bin/eigenlayer rewards show \  
  --network holesky \  
  --earner-address <earner-address> \  
  --claim-type unclaimed  

```

This will output the token address and the amount of unclaimed rewards available



```
---------------------------------------------------------------------------------------  
Token Address                              | Wei Amount  
---------------------------------------------------------------------------------------  
0x554c393923c753d146aa34608523ad7946b61662 | 6324648267039518  
0xdf3b00151bf851e8c4036ceda284d38a2f1d09df | 132817613607829878  
---------------------------------------------------------------------------------------  

```

### Step 4: Ensure you have your keys in place[​](#step-4-ensure-you-have-your-keys-in-place "Direct link to Step 4: Ensure you have your keys in place")


Claiming rewards requires you to have access to your wallet keys.
Supported Key Management options are listed [here](https://github.com/Layr-Labs/eigenlayer-cli/blob/master/README.md#supported-key-management-backends)


infoIf you already have your keys in either of the supported key management options, you can skip this step.


In case you have your keys in some browser wallet, you can import your keys to local keystore file by using the following command



```
./bin/eigenlayer keys import \  
  --key-type <key-type> <private-key-hex>  

```

This will ask you to set a password to protect your keystore file.


Refer your browser wallet documentation to get the `private-key-hex`.


### Step 5: Claim the rewards[​](#step-5-claim-the-rewards "Direct link to Step 5: Claim the rewards")


Make sure the keys you are using to claim is the claimer you have set.


* Mainnet
* Holesky

If you are using local keystore file, use the following command to claim rewards


```
./bin/eigenlayer rewards claim \  
  --network holesky \  
  --eth-rpc-url <mainnet-eth-rpc-url> \  
  --earner-address <earner-address> \  
  --recipient-address <address-to-send-rewards-to> \  
  --path-to-key-store /path/to/key/store-json \  
  --token-addresses <comma-separated-list-of-token-addresses> \  
  --broadcast  

```
`comma-separated-list-of-token-addresses` \- You can get this from output of [Step 3](#step-3-check-if-rewards-are-available-to-claim)

If you are using local keystore file, use the following command to claim rewards


```
./bin/eigenlayer rewards claim \  
  --network holesky \  
  --eth-rpc-url <holesky-eth-rpc-url> \  
  --earner-address <earner-address> \  
  --recipient-address <address-to-send-rewards-to> \  
  --path-to-key-store /path/to/key/store-json \  
  --token-addresses <comma-separated-list-of-token-addresses> \  
  --broadcast  

```
`comma-separated-list-of-token-addresses` \- You can get this from output of Step 3


If you are using private key hex, fireblocks or web3 signer check the command help for the respective key management backend.



```
./bin/eigenlayer rewards claim --help  

```

### Step 6: (Optional) Check the rewards paramters[​](#step-6-optional-check-the-rewards-paramters "Direct link to Step 6: (Optional) Check the rewards paramters")


If you want to see the rewards parameters before claiming, you can use the following command


* Mainnet
* Holesky

If you are using local keystore file, use the following command to claim rewards


```
./bin/eigenlayer rewards claim \  
  --network holesky \  
  --eth-rpc-url <mainnet-eth-rpc-url> \  
  --earner-address <earner-address> \  
  --token-addresses <comma-separated-list-of-token-addresses>  

```
`comma-separated-list-of-token-addresses` \- You can get this from output of [Step 3](#step-3-check-if-rewards-are-available-to-claim)

If you are using local keystore file, use the following command to claim rewards


```
./bin/eigenlayer rewards claim \  
  --network holesky \  
  --eth-rpc-url <holesky-eth-rpc-url> \  
  --earner-address <earner-address> \  
  --token-addresses <comma-separated-list-of-token-addresses>  

```
`comma-separated-list-of-token-addresses` \- You can get this from output of Step 3

[PreviousUsing WebApp](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/claim-rewards/via-ui)[NextRewards Claiming FAQ](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/rewards-claiming-faq)* [Step 1: Install the latest version of EigenLayer CLI](#step-1-install-the-latest-version-of-eigenlayer-cli)
* [Step 2: Check if installation is correct](#step-2-check-if-installation-is-correct)
* [Step 3: Check if rewards are available to claim](#step-3-check-if-rewards-are-available-to-claim)
* [Step 4: Ensure you have your keys in place](#step-4-ensure-you-have-your-keys-in-place)
* [Step 5: Claim the rewards](#step-5-claim-the-rewards)
* [Step 6: (Optional) Check the rewards paramters](#step-6-optional-check-the-rewards-paramters)


* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Testnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)
* Rewards Claiming
* Claim Rewards
* Using WebApp
Using WebApp
============


Follow the instructions below step by step in order to claim your currently available rewards in the EigenLayer web app. Rewards can be claimed by a Staker or Operator.


**Step 1**: Navigate to EigenLayer web app **Dashboard**.


![...](/assets/images/rewards-claim1-e2ea1e465d33076ade97365cb1f58d8c.png)


**Step 2**: Click **Claim Rewards** button.


**Step 3**: Select tokens individually you wish to claim rewarsd for or click **Select All** to claim all token rewards at once.


![...](/assets/images/rewards-claim2-8df6241590072b35d5de55c4ce153da9.png)


![...](/assets/images/rewards-claim3-ca16323063d57ced23e4afc87353f4a9.png)


**Step 4**: Click **Claim Tokens** button. This will initiate a transaction in your Web3 wallet to include claim proofs. **Sign** the transaction.


**Step 5**: View the summary of Rewards claimed successfully.
![...](/assets/images/rewards-claim5-630bdf4627a2efba655108a1f5648581.png)

[PreviousRewards Claiming Overview](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/rewards-claiming-overview)[NextUsing CLI](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/claim-rewards/via-cli)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Testnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)
* Rewards Claiming
* Rewards Claiming FAQ
On this pageRewards Claiming FAQ
====================

#### When can I claim my rewards?[​](#when-can-i-claim-my-rewards "Direct link to When can I claim my rewards?")


After a root is posted, rewards are claimable after an activation delay. On mainnet this delay is 1 week and on testnet it is 2 hours.


#### What portion of rewards goes to my operator?[​](#what-portion-of-rewards-goes-to-my-operator "Direct link to What portion of rewards goes to my operator?")


Operators get a fixed 10% portion rewards, though this is subject to change in a future release to be variable.


#### How can I receive rewards on testnet?[​](#how-can-i-receive-rewards-on-testnet "Direct link to How can I receive rewards on testnet?")


To accumulate rewards on testnet for testing purposes you must be an operator (or delegate to one) who has opted into an AVS with active rewards. EigenDA is one such AVS.

[PreviousUsing CLI](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/claim-rewards/via-cli)[NextRestaked Points](/eigenlayer/restaking-guides/restaking-user-guide/restaked-points)

* 
* Restaking Guides
* [Restaking Guides](/eigenlayer/restaking-guides/restaking-user-guide/)
* [Testnet Restaking](/eigenlayer/restaking-guides/restaking-user-guide/testnet/)
* Rewards Claiming
* Rewards Claiming Overview
On this pageRewards Overview
================


Overview[​](#overview "Direct link to Overview")
------------------------------------------------


The EigenLayer Rewards protocol enables AVSs to make rewards to stakers and operators. Operators earn rewards by opting in to AVSs that make `RewardsSubmissions` to the `RewardsCoordinator`, a core protocol contract. Within a single `RewardsSubmission`, an AVS can specify a time range for which the reward will be distributed, a list of weights for each `Strategy` for the reward, and an ERC20 token to make rewards in.


Operators will earn a flat 10% commission on rewards. The rest of the reward is passed on to the operator's delegated stakers. Rewards are proportional to:


* The amount of stake.
* The AVS's relative weighting of strategies in a rewards submission.


Rewards are calculated via an offchain process. Every week a merkle root is posted which represents the cumulative rewards across all earners. There is an additional 2 hour delay on testnet and 1 week delay on mainnet after posting in order for the root to be claimable against with a valid merkle proof. The deterministic calculation of the distribution of rewards is specified in our [technical docs](https://github.com/Layr-Labs/eigenlayer-contracts/blob/dev/docs/core/RewardsCoordinator.md).


Reward Earners (Stakers and Operators) can set a claimer address that can claim rewards for the tokens they've earned. An Earner is its own claimer by default and only the claimer address can claim rewards. If a new claimer is set, the new address can claim all of the previously unclaimed rewards. The earner can always configure their designated claimer address.


AVS Integrations[​](#avs-integrations "Direct link to AVS Integrations")
------------------------------------------------------------------------


Refer to [AVS Guide: AVS Rewards](/eigenlayer/avs-guides/rewards).


Rewards Contract Configurations[​](#rewards-contract-configurations "Direct link to Rewards Contract Configurations")
---------------------------------------------------------------------------------------------------------------------


### Earners[​](#earners "Direct link to Earners")


Operators and Stakers are both categorized as "Earners" when it comes to claiming and are distinct by their addresses. Actual reward calculations are explained further in the [technical docs](https://github.com/Layr-Labs/eigenlayer-contracts/blob/dev/docs/core/RewardsCoordinator.md). To summarize, reward calculations are performed daily by snapshotting the on\-chain state. Once a week on mainnet and daily on testnet, a Merkle root is posted to the contract that allows earners to claim their updated earnings.


Note: Earners or their designated claimers do not have to claim weekly against every single Merkle root to receive all their earnings up to that point. Earnings are calculated cumulatively so simply claiming one time against the latest Merkle root posted on the `RewardsCoordinator` contract will reward them with all their cumulative earnings even if there was several roots posted to the contract that were not claimed against.


### Setting Designated Claimers[​](#setting-designated-claimers "Direct link to Setting Designated Claimers")


Earners can set designated claimer addresses on the `RewardsCoordinator` contract. By default, if this is not configured then the Earner address can claim their earnings themselves but this optionality allows a third party to claim on an Earner's behalf.


### Rewards Recipient Address[​](#rewards-recipient-address "Direct link to Rewards Recipient Address")


Not to be confused with the designated claimer address specified above, the recipient address is the address that will actually receive the ERC20 token rewards. The designated claimer (or the earner themselves) has the ability to call `RewardsCoordinator.processClaim` for the earner while also specifying a recipient address to receive all the rewards.

[PreviousObtaining Testnet ETH \& Liquid Staking Tokens (LSTs)](/eigenlayer/restaking-guides/restaking-user-guide/testnet/obtaining-testnet-eth-and-liquid-staking-tokens-lsts)[NextUsing WebApp](/eigenlayer/restaking-guides/restaking-user-guide/testnet/rewards-claiming/claim-rewards/via-ui)* [Overview](#overview)
* [AVS Integrations](#avs-integrations)
* [Rewards Contract Configurations](#rewards-contract-configurations)
	+ [Earners](#earners)
	+ [Setting Designated Claimers](#setting-designated-claimers)
	+ [Rewards Recipient Address](#rewards-recipient-address)


* 
* Risk
* Risk FAQ
On this pageRisk FAQ
========


General Questions[​](#general-questions "Direct link to General Questions")
---------------------------------------------------------------------------


**Is EigenLayer a DeFi protocol?**


No, EigenLayer is not a DeFi protocol. EigenLayer is a platform to bootstrap new proof of stake (PoS) systems. Through the EigenLayer protocol, users CANNOT engage in any financial activities such as swapping and lending.


However, for the decentralized services built on top of EigenLayer (we call them AVSs, Actively Validated Services), these services could be DeFi applications themselves or support key functionalities in other DeFi protocols. These AVSs are external to the EigenLayer contracts.


Moreover, another class of protocols built on top of EigenLayer is called liquid restaking token (LRT). They function similarly to liquid staking tokens. They are permissionlessly built on EigenLayer. We urge users to do their own research before interacting with LRTs.


**Does EigenLayer reuse the same economic security?**


Yes, EigenLayer does reuse the same economic security by enabling different AVSs to share a common economic security base. This concept is known as 'pooled security.' Similar to how various dApps share Ethereum's economic security, EigenLayer allows different decentralized PoS networks share the same economic security base.


Pooling allows various AVSs to contribute to a larger, shared economic security base, enhancing economic safety. This is because the cost to compromise any individual AVS increases significantly. For instance, consider 100 AVSs each with $1B in economic security versus 100 AVSs sharing $100B in economic security. The cost to attack any single AVS in the pooled system has effectively multiplied by 100\.


In addition to pooled security, EigenLayer will let each AVS acquire additional attributable security. Unlike pooled security, attributable security is specific to each AVS and will only be slashable by one AVS. This arrangement can provide game\-theoretic guarantees for AVS customers.


Imagine a bridge protocol with a shared security base of $10B and an attributable portion of $10B. If a malfunction occurs, the protocol can assure the AVS customer that up to $10B can still be securing the bridge through the attributable part. Attributable security also enables the flexible scaling of economic security. As an AVS, you can adjust your security budget based on user demand, catering to varying user needs at different times.


Furthermore, EigenLayer aims to achieve economies of scale by allowing AVSs to share the same underlying smart contract infrastructure. If a DeFi application uses services from five different AVSs and requests $100B in economic security, these AVSs can collectively purchase attributable security instead of each buying $100B individually. This is feasible because if any of them fail, the $100B could be compensated to the DeFi protocol.


In conclusion, EigenLayer will not only allow AVSs to share economic security but will also enable individual AVSs to acquire additional attributable security. The combination of pooled and attributable security allows EigenLayer to flexibly and efficiently scale economic security.


**Why is EigenLayer's contract licensed under BSL?**


EigenLayer's core contract operates under BSL due to the numerous market forces at play. EigenLayer is not isolated; it operates within a broader ecosystem. Innovators can utilize the comprehensive decentralized trust network of the Ethereum economy with EigenLayer, eliminating the need for new token creation.


Without the need for a new token, this makes it easy for other entities, particularly those with extensive product distribution, to replicate and utilize the code. This situation applies to AVS building on EigenLayer and EigenLayer itself.


In scenarios where major LSTs have a much larger distribution and no new token is required for new networks, it becomes crucial to establish boundaries to safeguard open innovation. This protection ensures that individual LSTs do not consume open innovation and that existing protocols are not easily copying AVS designs. Consequently, EigenLayer's core operates under the BSL, transitioning to the MIT (Massachusetts Institute of Technology) license after two years, a practice also followed by some AVSs.


We are also exploring new licensing models that combine the benefits of protected licensing, which ensures value accumulation for innovators with permissionless innovation, which allows the creation of derivatives without needing explicit permission. Until we finalize these new models, we will continue using the tried\-and\-tested BSL model. If Ethereum core developers express an interest in enshrining EigenLayer before the BSL expires, we are more than open to collaboration as well.


Staker Related
==============


**Is EigenLayer rehypothecating my staked tokens?**


No, EigenLayer does not engage in rehypothecation.


Rehypothecation is the practice that allows collateral posted by, say, a hedge fund to its prime broker to be used again as collateral by that *prime broker* for its own funding.


Rehypothecation in traditional finance implies:


1. Depositor no longer have direct control of their assets.
2. Depositors have little say in the financial activities conducted by the intermediary.
3. Depositors are subject to substantial liquidity and counterparty risks.


Whereas in EigenLayer:


1. Stakers retain full control over their staked tokens.
2. Stakers have autonomy over the services they wish to validate.
3. Stakers are not exposed to counterparty liquidity risks.


There are clear differences between EigenLayer and rehypothecation.


AVS Related[​](#avs-related "Direct link to AVS Related")
---------------------------------------------------------


**Doesn't EigenLayer remove all the utility from an AVS network token?**


No, EigenLayer doesn't remove the value of any hypothetical AVS tokens, but adds more value to it.


Firstly, Ethereum's L2 networks serve as a greatest counterpoint to this line of logic. Despite outsourcing their network security to Ethereum, L2 tokens maintain significant value within their respective networks.


Secondly, if an individual AVS decides to incorporate its own token for staking and network operations, EigenLayer supports [dual staking](https://www.blog.eigenlayer.xyz/dual-staking/). In this setup, an AVS can be secured by two types of assets, likely one in ETH and one in its native token.


It's important to note that in the dual staking model, AVS governance always has the ability to adjust the balance between AVS's native token and ETH within its network.


During the initial phase, an AVS may choose to rely more heavily on ETH, giving it greater weight to mitigate the inherent risk of relying solely on its native token, which could potentially lead to a downward spiral. However, as the AVS matures and gains more adoption, the governance can adjust the balance to give more weight to the AVS token, thereby increasing its value.


These points provide individual AVS with more options than the current status quo. Building on EigenLayer, therefore, doesn't negate the utility of an AVS token. Instead, through these additional options, we enhance their value.


**Given the answer above, does it mean EigenLayer provides little value beyond the bootstrapping phase?**


No, EigenLayer offers significant value at any stage of the AVS's economic security phase.


Firstly, the use of ETH as the shared security set inherently reduces the endogenous risk associated with a native AVS token.


Secondly, as the AVS ecosystem matures, interoperability between different AVSs and the resulting synergy will become a crucial factor enabling AVSs to leverage EigenLayer.


Thirdly, the flexible security that EigenLayer provides proves beneficial in handling security demand shocks for AVSs. If an AVS needs to secure a large customer transaction suddenly, it can quickly access the necessary security.


Finally, building on the synergy point, as AVSs begin to serve more customers collectively, the economic scale of insurance will enable AVSs to meet their customers' need for cryptoeconomic security more affordably.


LRT Related[​](#lrt-related "Direct link to LRT Related")
---------------------------------------------------------


**What roles does LRTs serve?**


LRTs safeguard EigenLayer and AVSs from external financial risks tied to staked positions. In EigenLayer, stakers don't receive a transferable receipt post\-staking. Despite this, we expect some stakers to try and financialize their positions.


In the absence of LRTs, if a financialized staker's position gets liquidated, the staked tokens must be withdrawn from EigenLayer. This is the case because staked position cannot be transferred, negatively affecting AVS's economic security. However, with LRTs, withdrawals become unnecessary. The liquidator can simply assume the staker's position.


This feature is especially crucial during substantial market downturns. As the price of ETH falls, so does the system's total economic security. If liquidation leads to more ETH leaving EigenLayer, it would worsen the downward spiral. LRTs can significantly mitigate this risk, thereby protecting both AVS and EigenLayer from potential financial risks related to staker positions.


**Is there an LRT looping risk that would potentially cause potential liquidation cascade?**


No, looping LRTs in EigenLayer is not possible because depositing LRTs into EigenLayer is currently not allowed.


However, in lending markets, looping LRTs may occur based on the risk analysis of individual LRTs. We advise caution when taking this step as it involves financial leverage and exposes LRT holders to significant risks.


Looping LRTs in lending markets can lead to a cascade of liquidations. This risk is limited to individual lending markets and does not affect the security of EigenLayer. This is similar to the stETH depeg incident in 2022\. During the event, the price risk of stETH is contained within the lending market, and Ethereum consensus remains unaffected.


Ethereum Related[​](#ethereum-related "Direct link to Ethereum Related")
------------------------------------------------------------------------


**Does EigenLayer rely on Ethereum social consensus?**


No, EigenLayer does not depend on Ethereum's social consensus. EigenLayer aims for responsible decentralization. Instead of shifting unwarranted slashing risks to Ethereum or external protocols, EigenLayer includes a slashing veto committee. This internalizes social consensus and safeguards against slashing risks.


The veto committee functions similarly to the relay in MEV\-Boost. MEV\-Boost relies on a double\-trusted party, known as a relay, who is trusted by both proposers and builders. Any individual trusted by both parties can serve as a relay, effectively removing any entrenched actor.


In EigenLayer, a veto committee will serve as a doubly\-trusted intermediary between AVS and staker. The solution is the same as the relay, but instead of having a specific veto committee, anyone will be able to establish a veto committee. As long as both parties trust the committee, the staker and AVS can interact through it.


The intention is to upgrade to a version of EigenLayer without a canonical veto committee. Instead, there will be a marketplace of veto committees. Operators and AVSs would both be able to define their veto committee preference. AVSs and Operator veto committee choices would need to overlap in order for an operator to opt in to an AVS. This promotes inter\-subjectivity, as operators and AVSs coordinate their choices based on their subjective views of safety.


**Does EigenLayer increase centralization pressure on the validator set?**


If EigenLayer imposes additional computational demands on Ethereum validators, it unavoidably becomes a centralization vector for Ethereum. With this principle in mind, EigenLayer discourages the increase in node requirements for Ethereum validators and promotes the use of lightweight AVSs, such as [EigenDA](https://twitter.com/eigen_da).


For more computationally demanding AVSs, EigenLayer's delegation features allow Home stakers to secure Ethereum while delegating the operation of other AVSs to a different operator.


Ongoing research is focused on mechanisms, such as the [Optimistic Delegation Framework](https://research.eigenlayer.xyz/t/optimistic-delegation-framework-idea-to-allow-for-native-restaking-without-delegation/39) and [AVS for PBS](https://www.youtube.com/watch?v=7xCqa_Ufv0A), to reduce the computational load on Ethereum validators in a trust\-minimized manner.


From an economic standpoint, we are exploring the possibility of directly incentivizing individual stakers through a rewards sharing scheme. Consider, for instance, allocating a certain percentage (x%) of all rewards processed through EigenLayer to solo validators.


If you are interested in discussing these mechanisms and incentive issues further, please share your thoughts on [research.eigenlayer.xyz](http://research.eigenlayer.xyz)


**Does EigenLayer eat away into the security margin of Ethereum?**


No, EigenLayer does not compromise Ethereum's security margin.


When the stake in EigenLayer is significantly less than the total staked ETH, it does not impact Ethereum's security.


If the stake in EigenLayer makes up a large part of the total staked ETH, EigenLayer doesn't put the entire stake at risk. Instead, it sets aside a portion as a buffer for Ethereum, offering only the remaining stake for security. This approach ensures that we can consistently safeguard Ethereum's security margin.


For a better understanding of the required security level for Ethereum, we suggest readers refer to [StakeSure](https://arxiv.org/abs/2401.05797).


**Does EigenLayer need to self\-limit like other liquid staking protocols?**


No, EigenLayer doesn't require self\-limiting.


The danger of a liquid staking protocol owning a substantial portion of the network is the potential imposition of a specific validator set on the Ethereum network. This risk doesn't apply to EigenLayer. Even if all staked ETH is restaked through EigenLayer, it doesn't control Ethereum's validator set. That control remains solely with Ethereum's stakers and validators.


If EigenLayer self\-limits, the surplus restaking demand will likely revert to liquid staking protocols, increasing centralization pressure at the protocol's base layer. If EigenLayer didn't exist, dominant LST protocols would likely offer restaking services only to their internal stakers. These centralized restaking services could considerably strengthen the dominant LST's central position. More restaking services mean additional yield, leading to further consolidation of the LST. This scenario resembles the situation with MEV, where large stakers, including professional operators and LSTs, can negotiate MEV order flow guarantees that smaller stakers can't participate in.


In contrast to the centralized restaking mechanisms mentioned above, EigenLayer is developing a credibly neutral, decentralized restaking platform. All participants, whether small or large LSTs, small or large node operators, or institutional and home stakers, can all participate in additional validation opportunities. This approach helps prevent a monopoly in LST or LRT, fostering decentralization and neutrality among node operators.


EigenLayer doesn't define an operator set, so it doesn't threaten Ethereum's censorship resistance or operator decentralization.


Self\-limiting EigenLayer offers no significant benefit. Instead, if EigenLayer proves successful in the market, it could even be integrated into the Ethereum protocol as a native service.


**Does EigenLayer experience the principal\-agent problem between stakers and operators?**


EigenLayer, as with other PoS protocols, does experience the principal\-agent problem. However, our goal is to minimize this issue as much as possible.


It's important to highlight that EigenLayer operators never retain custody of the staker's tokens, which limits the potential for malicious activities to only slashing events.


We have established several strategies to further limit the operator's capacity for harmful actions:


1. Technical Trust: EigenLayer operators can utilize an anti\-slasher within a Trusted Execution Environment (TEE) to verify its response to any validation task. The operator then sends the associated TEE certificate with its response for the task, confirming that the anti\-slasher was utilized. Another technical solution to address the principal\-agent problem is to structure the EigenLayer operator with decentralized DVT nodes.
2. Economic Trust: Similar to RocketPool, a specific LRT protocol might require operators to stake proportionally to the delegation they receive. This approach assumes a certain amount that can be slashed and a probability for that occurrence. By encouraging the operator nodes to behave correctly, the principal\-agent problem can be mitigated.
3. Social Trust: A staker always has the option to self\-delegate and operate the nodes for AVSs or delegate it to a trusted operator. In this scenario, the staker trusts the operator to perform only the stipulated operations and not engage in any malicious activities. This practice is common in the real world, where service providers like AWS offer services.
[PreviousWithdrawal Delay](/eigenlayer/security/withdrawal-delay)[NextEigenLayer Privacy Policy](/eigenlayer/legal/eigenlayer-privacy-policy)* [General Questions](#general-questions)
* [AVS Related](#avs-related)
* [LRT Related](#lrt-related)
* [Ethereum Related](#ethereum-related)


* 
* Security
* Audits
Audits
======


As a key component of our development process, please see the most recent audits that help assess the robustness and reliability of our systems:


* [Sigma Prime](https://github.com/Layr-Labs/eigenlayer-contracts/blob/dev/audits/M2%20Mainnet%20-%20Sigma%20Prime%20-%20Feb%202024.pdf)
* [Dedaub](https://github.com/Layr-Labs/eigenlayer-middleware/blob/dev/audits/M2%20Mainnet%20-%20Dedaub%20-%20Feb%202024.pdf)
* [Cantina](https://github.com/Layr-Labs/eigenlayer-contracts/blob/dev/audits/M2%20Mainnet%20-%20Cantina%20-%20Apr%202024.pdf)


Please see the following repositories for all current and past audits:


* [EigenLayer\-Contracts / Audits](https://github.com/Layr-Labs/eigenlayer-contracts/tree/dev/audits)
* [EigenLayer\-Middleware / Audits](https://github.com/Layr-Labs/eigenlayer-middleware/tree/dev/audits)


We encourage you to review all audits carefully as they offer an in\-depth analysis of our technology's capabilities, security measures, and overall reliability.


Instructions are also available for [Installation and Running Tests / Analyzers](https://github.com/Layr-Labs/eigenlayer-contracts#installation) via the Github repo.

[PreviousMultisig Governance](/eigenlayer/security/multisig-governance)[NextBug Bounty](/eigenlayer/security/bug-bounty)

* 
* Security
* Multisig Governance
Multisig Governance
===================


EigenLayer is designed with upgradeable smart contracts, the ability to pause functionality, and various adjustable parameters. The ability and responsibility to make decisions regarding contract upgrades, pausing functionality, and adjusting parameters initially have been delegated to three main governance multisigs.


**The Operations Multisig**


The Operations Multisig is a 3\-of\-6 and can execute routine upgrades and maintenance through a timelock that enforces a minimum 10\-day delay on all safety\-critical actions. It can also pause EigenLayer functionality in emergency situations.


**The Pauser Multisig**


The Pauser Multisig is a 1\-of\-14 multisig that can also pause EigenLayer functionality in emergency situations, but holds no other powers.


**The Community Multisig**


The Community Multisig is a 9\-of\-13 multisig composed of members of the Ethereum community. In normal circumstances, the signers of the Community Multisig will simply act as observers, receiving regular updates on the Operations Multisig’s transactions, including notifications of the Operations Multisig queuing new time\-locked actions. In extraordinary circumstances, the Community Multisig can perform emergency actions, including immediately executing time\-critical upgrades or replacing the Operations Multisig in the event of private key compromise.


The Community Multisig members include:


* Tim Beiko \- Ethereum Foundation
* Viktor Bunin \- Coinbase
* Uma Roy \- Succinct
* Brian Retford \- RISC Zero
* Pramod Viswanath \- Witness Chain
* Swapnil Raj \- Nethermind
* Dimitry Ukhanov \- P2P
* Tarun Chitra \- Robot Ventures
* Anna Rose \- ZK Validator
* Curtis Spencer \- Electric Capital
* Yuan Han Li \- Blockchain Capital
* Ben Rodriguez \- Coinbase Cloud
* Rob Pellecchia \- Figment Capital


Finally, there is an *Executor Multisig* which only has the (automated) role of executing functionality passed to it by either the Operations or Community Multisig.


The contract addresses for the Operations, Pauser, Community and Executor Multisig are available at the [Deployed Contracts page](/eigenlayer/deployed-contracts/).


On a technical level, the governance architecture looks like the following:


![](/img/googleusercontentbackup/tdLYguBq5wyfQbJRkyVo7pqT1tBasCLxXP-aA60GZGXlqKDkLtQIN9guogHXdSRObApuLHT3LpPfIxZWJruxaAJBH5skfRY3EQAPya0sxxUnj1EoDgkUCxItwETv-dpaVVAV86JCzpYduZcpLQlH9-0.png)




These multisigs represent a rudimentary but working system of transparent initial governance, with appropriate checks and balances. As the protocol continues to evolve, so will its governance, and we are continuously evaluating our options for potential future governance mechanics.


Decentralized governance practices are rapidly evolving, continuously pushing boundaries and exploring innovative approaches. In addition to the above, EigenLayer anticipates the emergence of novel mechanisms that have yet to be designed and is excited to research them and facilitate implementation.

[PreviousAVS Rewards](/eigenlayer/avs-guides/rewards)[NextAudits](/eigenlayer/security/audits)

* 
* Security
* Withdrawal Delay
Withdrawal Delay
================


EigenLayer contracts feature a withdrawal delay for LST tokens, EIGEN token, and Native Restaking, a critical security measure for instances of vulnerability disclosure or when anomalous behavior is detected by monitoring systems. The delays serve as a preventive mechanism and also allows, in certain cases, to help mitigate protocol attacks. When contracts are paused and withdrawals disabled, the system enables arbitrary state or code changes to the contracts through upgrades. While technically feasible, such interventions are not a routine practice and should be approached with caution.


The Withdrawal Delay is also referred to as the Escrow Period. Please see Restaking [Escrow Period](/eigenlayer/restaking-guides/restaking-user-guide/#escrow-period-withdrawal-delay) for details on the specific duration.


There are two main caveats to this system. The first is the potential for a vulnerability that can bypass the withdrawal delay. The second is the risk of a flaw in the code managing requests after they have undergone the delay period.


To mitigate these risks, the approach involves optimizing complex code processes before the delay, while ensuring simpler code operations post\-delay. This is coupled with the aim of developing a robust and foolproof delay framework, thereby enhancing the overall security and resilience of the system.

[PreviousGuardrails](/eigenlayer/security/guardrails)[NextRisk FAQ](/eigenlayer/risk/risk-faq)