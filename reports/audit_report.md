# Secure File Transfer Monitoring System — Audit Report

Generated: 2026-11-06T22:14:47.951023+00:00
Monitoring period: 2026-11-06T22:13:20.212828+00:00 to 2026-11-06T22:13:54.038716+00:00

## Totals by event type
| Event | Count |
|---|---:|
| BULK | 1 |
| COPY | 5 |
| CREATE | 200 |
| DELETE | 1 |
| MODIFY | 207 |
| MOVE | 1 |

## Totals by severity
| Severity | Count |
|---|---:|
| CRITICAL | 2 |
| HIGH | 6 |
| INFO | 407 |

## Violations
| Time | Rule | Severity | File | Destination | Message |
|---|---|---|---|---|---|
| 2026-11-06T22:13:23.139580+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-06T22:13:24.578298+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-06T22:13:26.046867+00:00 | R1 | HIGH | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | Sensitive file moved outside approved location |
| 2026-11-06T22:13:27.476853+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-06T22:13:28.978324+00:00 | R3 | CRITICAL | demo_workspace/network_share_sim/passwords_backup.txt |  | Integrity Failure: File hash mismatch detected |
| 2026-11-06T22:13:30.407792+00:00 | R3 | CRITICAL | demo_workspace/sensitive/client_database.csv |  | Integrity Failure: File hash mismatch detected |
| 2026-11-06T22:13:32.237064+00:00 | R5 | HIGH | demo_workspace/sensitive/server.key |  | Sensitive file deleted |
| 2026-11-06T22:13:54.038716+00:00 | R4 | HIGH |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | Suspicious movement: 200 files transferred to unknown directory |

## Integrity results
| File | Hash before | Hash after | Status |
|---|---|---|---|
| demo_workspace/documents/meeting_notes.txt | 1bbe595a0fb9196c4f7cc842fb4b6cec2890feb2d98ed453c1f11f1f731a0b3a | 1bbe595a0fb9196c4f7cc842fb4b6cec2890feb2d98ed453c1f11f1f731a0b3a | OK |
| demo_workspace/sensitive/employee_salaries.csv | f13515328f40fdebf310e185bb34a91703201566ac0a398f3ca859e50f0f83a2 | f13515328f40fdebf310e185bb34a91703201566ac0a398f3ca859e50f0f83a2 | OK |
| demo_workspace/sensitive/server.key | fb6c4c9eb0f3c9d647d11ab0dca76ac6ecde7ad2bc6e57a0ac26b29b32202a7f | fb6c4c9eb0f3c9d647d11ab0dca76ac6ecde7ad2bc6e57a0ac26b29b32202a7f | OK |
| demo_workspace/sensitive/client_database.csv | 2809cde731a98897ea8226664b5f76682f6fd4c076569ecb095c7f88740cc2fc | 2809cde731a98897ea8226664b5f76682f6fd4c076569ecb095c7f88740cc2fc | OK |
| demo_workspace/sensitive/employee_salaries.csv | f13515328f40fdebf310e185bb34a91703201566ac0a398f3ca859e50f0f83a2 | f13515328f40fdebf310e185bb34a91703201566ac0a398f3ca859e50f0f83a2 | OK |
| demo_workspace/sensitive/passwords_backup.txt | cb9c5202d7f1ce2ab4aa49df81233d95b36bf32b3b5857075b758124a77aac81 | cb9c5202d7f1ce2ab4aa49df81233d95b36bf32b3b5857075b758124a77aac81 | OK |
| demo_workspace/network_share_sim/passwords_backup.txt | cb9c5202d7f1ce2ab4aa49df81233d95b36bf32b3b5857075b758124a77aac81 | f9dec16a36e82ede11988c63715447b73fe2751f19129230a3bd0bae2208062c | MISMATCH |
| demo_workspace/sensitive/client_database.csv | 2809cde731a98897ea8226664b5f76682f6fd4c076569ecb095c7f88740cc2fc | 5b7cc3161b0da9bdc8789763541834af19bbcc2687efa279f02d42533f673d2b | MISMATCH |

## Top users and processes

Users: pc (415)

Processes: unknown (415)

## Full timeline
| Time | Type | User | Process | File | Destination | Severity | Rule | Message |
|---|---|---|---|---|---|---|---|---|
| 2026-11-06T22:13:20.212828+00:00 | MODIFY | pc | unknown | demo_workspace/documents/meeting_notes_copy.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:20.217039+00:00 | COPY | pc | unknown | demo_workspace/documents/meeting_notes.txt | demo_workspace/documents/meeting_notes_copy.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:21.679083+00:00 | MODIFY | pc | unknown | demo_workspace/approved_backup/employee_salaries.csv |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:21.679083+00:00 | COPY | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/approved_backup/employee_salaries.csv | INFO | R0 | Authorized transfer |
| 2026-11-06T22:13:23.139580+00:00 | MODIFY | pc | unknown | demo_workspace/usb_drive_sim/server.key |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:23.139580+00:00 | COPY | pc | unknown | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-06T22:13:24.576297+00:00 | MODIFY | pc | unknown | demo_workspace/cloud_sync_sim/client_database.csv |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:24.578298+00:00 | COPY | pc | unknown | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-06T22:13:26.046867+00:00 | MOVE | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | HIGH | R1 | Sensitive file moved outside approved location |
| 2026-11-06T22:13:27.476853+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:27.476853+00:00 | COPY | pc | unknown | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-06T22:13:28.978324+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-06T22:13:30.407792+00:00 | MODIFY | pc | unknown | demo_workspace/sensitive/client_database.csv |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-06T22:13:32.237064+00:00 | DELETE | pc | unknown | demo_workspace/sensitive/server.key |  | HIGH | R5 | Sensitive file deleted |
| 2026-11-06T22:13:33.829916+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.834725+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.838741+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.838741+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt | demo_workspace/unknown_dir/bulk/tiny_000.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.842066+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.842066+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt | demo_workspace/unknown_dir/bulk/tiny_001.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.842066+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt | demo_workspace/unknown_dir/bulk/tiny_003.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:33.842066+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt | demo_workspace/unknown_dir/bulk/tiny_002.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.247916+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.251680+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.257884+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.257884+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt | demo_workspace/unknown_dir/bulk/tiny_004.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.261286+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt | demo_workspace/unknown_dir/bulk/tiny_005.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.261661+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.265731+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt | demo_workspace/unknown_dir/bulk/tiny_006.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.266731+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt | demo_workspace/unknown_dir/bulk/tiny_007.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.664402+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.670218+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.673223+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt | demo_workspace/unknown_dir/bulk/tiny_008.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.673223+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.673223+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt | demo_workspace/unknown_dir/bulk/tiny_009.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.677872+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.677872+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt | demo_workspace/unknown_dir/bulk/tiny_010.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:34.677872+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt | demo_workspace/unknown_dir/bulk/tiny_011.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.074438+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt | demo_workspace/unknown_dir/bulk/tiny_012.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.074438+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.081034+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.086906+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.086906+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.086906+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt | demo_workspace/unknown_dir/bulk/tiny_013.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.086906+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt | demo_workspace/unknown_dir/bulk/tiny_014.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.086906+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt | demo_workspace/unknown_dir/bulk/tiny_015.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.490302+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.496229+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.502187+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt | demo_workspace/unknown_dir/bulk/tiny_016.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.502187+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.502187+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt | demo_workspace/unknown_dir/bulk/tiny_017.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.502187+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.511237+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt | demo_workspace/unknown_dir/bulk/tiny_018.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.511237+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt | demo_workspace/unknown_dir/bulk/tiny_019.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.903169+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.915578+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.916589+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt | demo_workspace/unknown_dir/bulk/tiny_020.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.916589+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.925767+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.925767+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt | demo_workspace/unknown_dir/bulk/tiny_021.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.925767+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt | demo_workspace/unknown_dir/bulk/tiny_022.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:35.925767+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt | demo_workspace/unknown_dir/bulk/tiny_023.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.313797+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt | demo_workspace/unknown_dir/bulk/tiny_024.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.321147+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.325857+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.325857+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt | demo_workspace/unknown_dir/bulk/tiny_025.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.333942+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.333942+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.333942+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt | demo_workspace/unknown_dir/bulk/tiny_026.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.339239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt | demo_workspace/unknown_dir/bulk/tiny_027.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.727284+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.727284+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt | demo_workspace/unknown_dir/bulk/tiny_028.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.733064+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.733064+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt | demo_workspace/unknown_dir/bulk/tiny_029.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.739412+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt | demo_workspace/unknown_dir/bulk/tiny_030.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.744318+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.746841+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:36.746841+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt | demo_workspace/unknown_dir/bulk/tiny_031.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.148691+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.148691+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.153513+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.153513+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt | demo_workspace/unknown_dir/bulk/tiny_032.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.153513+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.153513+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt | demo_workspace/unknown_dir/bulk/tiny_033.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.153513+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt | demo_workspace/unknown_dir/bulk/tiny_035.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.164501+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt | demo_workspace/unknown_dir/bulk/tiny_034.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.558806+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.559804+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt | demo_workspace/unknown_dir/bulk/tiny_036.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.563183+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.566178+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt | demo_workspace/unknown_dir/bulk/tiny_037.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.573249+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.574249+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.578248+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt | demo_workspace/unknown_dir/bulk/tiny_038.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.578248+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt | demo_workspace/unknown_dir/bulk/tiny_039.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.970131+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.973901+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.978699+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt | demo_workspace/unknown_dir/bulk/tiny_040.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.978699+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt | demo_workspace/unknown_dir/bulk/tiny_041.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.978699+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.978699+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt | demo_workspace/unknown_dir/bulk/tiny_042.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.989886+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:37.989886+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt | demo_workspace/unknown_dir/bulk/tiny_043.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.379443+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.388057+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt | demo_workspace/unknown_dir/bulk/tiny_044.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.388057+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.394765+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.395772+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt | demo_workspace/unknown_dir/bulk/tiny_045.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.395772+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.395772+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt | demo_workspace/unknown_dir/bulk/tiny_046.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.395772+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt | demo_workspace/unknown_dir/bulk/tiny_047.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.793105+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt | demo_workspace/unknown_dir/bulk/tiny_048.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.794109+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.802349+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.802349+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt | demo_workspace/unknown_dir/bulk/tiny_049.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.804872+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.804872+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt | demo_workspace/unknown_dir/bulk/tiny_050.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.809925+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:38.813579+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt | demo_workspace/unknown_dir/bulk/tiny_051.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.201165+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.213950+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt | demo_workspace/unknown_dir/bulk/tiny_052.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.219059+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.219059+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.219059+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt | demo_workspace/unknown_dir/bulk/tiny_054.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.229792+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.229792+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt | demo_workspace/unknown_dir/bulk/tiny_053.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.229792+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt | demo_workspace/unknown_dir/bulk/tiny_055.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.622235+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.626359+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt | demo_workspace/unknown_dir/bulk/tiny_056.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.626359+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt | demo_workspace/unknown_dir/bulk/tiny_057.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.631206+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.634798+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.638045+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt | demo_workspace/unknown_dir/bulk/tiny_058.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.638045+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:39.641000+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt | demo_workspace/unknown_dir/bulk/tiny_059.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.036270+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.041076+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.045609+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.051021+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt | demo_workspace/unknown_dir/bulk/tiny_061.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.051021+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.051021+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt | demo_workspace/unknown_dir/bulk/tiny_063.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.060390+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt | demo_workspace/unknown_dir/bulk/tiny_060.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.060390+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt | demo_workspace/unknown_dir/bulk/tiny_062.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.453953+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.464189+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt | demo_workspace/unknown_dir/bulk/tiny_065.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.467954+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt | demo_workspace/unknown_dir/bulk/tiny_064.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.467954+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.467954+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.467954+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.467954+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt | demo_workspace/unknown_dir/bulk/tiny_066.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.481745+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt | demo_workspace/unknown_dir/bulk/tiny_067.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.875893+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.881598+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.882597+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt | demo_workspace/unknown_dir/bulk/tiny_068.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.888620+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.890160+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt | demo_workspace/unknown_dir/bulk/tiny_069.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.890160+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt | demo_workspace/unknown_dir/bulk/tiny_070.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.890160+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:40.897143+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt | demo_workspace/unknown_dir/bulk/tiny_071.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.290603+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.294106+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt | demo_workspace/unknown_dir/bulk/tiny_072.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.294106+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.300417+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt | demo_workspace/unknown_dir/bulk/tiny_073.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.302432+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.306444+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.306444+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt | demo_workspace/unknown_dir/bulk/tiny_074.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.306444+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt | demo_workspace/unknown_dir/bulk/tiny_075.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.708716+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.710729+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.710729+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt | demo_workspace/unknown_dir/bulk/tiny_076.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.716176+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.720716+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.720716+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt | demo_workspace/unknown_dir/bulk/tiny_077.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.720716+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt | demo_workspace/unknown_dir/bulk/tiny_078.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:41.729453+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt | demo_workspace/unknown_dir/bulk/tiny_079.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.127904+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.130425+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt | demo_workspace/unknown_dir/bulk/tiny_081.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.130425+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.135189+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.135189+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt | demo_workspace/unknown_dir/bulk/tiny_080.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.135189+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.146280+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt | demo_workspace/unknown_dir/bulk/tiny_082.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.149996+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt | demo_workspace/unknown_dir/bulk/tiny_083.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.533800+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt | demo_workspace/unknown_dir/bulk/tiny_084.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.538717+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.545620+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.545620+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt | demo_workspace/unknown_dir/bulk/tiny_085.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.552643+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.556186+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt | demo_workspace/unknown_dir/bulk/tiny_086.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.559187+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.561188+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt | demo_workspace/unknown_dir/bulk/tiny_087.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.943702+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.943702+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt | demo_workspace/unknown_dir/bulk/tiny_088.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.951436+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.951436+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt | demo_workspace/unknown_dir/bulk/tiny_089.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.963052+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.963052+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt | demo_workspace/unknown_dir/bulk/tiny_090.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.966495+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:42.966495+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt | demo_workspace/unknown_dir/bulk/tiny_091.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.351703+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.351703+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt | demo_workspace/unknown_dir/bulk/tiny_092.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.359984+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.359984+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt | demo_workspace/unknown_dir/bulk/tiny_093.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.368837+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.372524+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt | demo_workspace/unknown_dir/bulk/tiny_094.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.374041+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.374041+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt | demo_workspace/unknown_dir/bulk/tiny_095.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.759428+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.759428+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt | demo_workspace/unknown_dir/bulk/tiny_096.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.775189+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.781198+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.782715+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt | demo_workspace/unknown_dir/bulk/tiny_098.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.782715+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt | demo_workspace/unknown_dir/bulk/tiny_097.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.782715+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:43.782715+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt | demo_workspace/unknown_dir/bulk/tiny_099.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.167457+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.171186+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt | demo_workspace/unknown_dir/bulk/tiny_100.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.186601+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.186601+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt | demo_workspace/unknown_dir/bulk/tiny_101.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.193987+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.193987+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.193987+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt | demo_workspace/unknown_dir/bulk/tiny_102.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.193987+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt | demo_workspace/unknown_dir/bulk/tiny_103.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.577737+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.581359+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt | demo_workspace/unknown_dir/bulk/tiny_104.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.595839+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.601012+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt | demo_workspace/unknown_dir/bulk/tiny_105.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.605531+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt | demo_workspace/unknown_dir/bulk/tiny_106.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.605531+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.610943+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.610943+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt | demo_workspace/unknown_dir/bulk/tiny_107.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.989996+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:44.997658+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt | demo_workspace/unknown_dir/bulk/tiny_108.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.008377+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.017880+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.019385+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt | demo_workspace/unknown_dir/bulk/tiny_109.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.022989+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt | demo_workspace/unknown_dir/bulk/tiny_110.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.022989+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.029517+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt | demo_workspace/unknown_dir/bulk/tiny_111.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.403268+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt | demo_workspace/unknown_dir/bulk/tiny_112.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.403268+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.421222+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt | demo_workspace/unknown_dir/bulk/tiny_113.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.421222+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.428885+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt | demo_workspace/unknown_dir/bulk/tiny_114.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.430892+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.435427+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt | demo_workspace/unknown_dir/bulk/tiny_115.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.438558+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.811174+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.815341+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt | demo_workspace/unknown_dir/bulk/tiny_116.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.830681+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.833595+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt | demo_workspace/unknown_dir/bulk/tiny_117.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.835611+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.842393+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt | demo_workspace/unknown_dir/bulk/tiny_118.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.846425+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:45.846425+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt | demo_workspace/unknown_dir/bulk/tiny_119.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.220306+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.220306+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt | demo_workspace/unknown_dir/bulk/tiny_120.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.242115+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.242115+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt | demo_workspace/unknown_dir/bulk/tiny_121.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.249279+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt | demo_workspace/unknown_dir/bulk/tiny_122.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.252442+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.253976+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.260174+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt | demo_workspace/unknown_dir/bulk/tiny_123.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.632536+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.634711+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt | demo_workspace/unknown_dir/bulk/tiny_124.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.648011+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.659359+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt | demo_workspace/unknown_dir/bulk/tiny_125.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.660665+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.665234+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt | demo_workspace/unknown_dir/bulk/tiny_126.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.667234+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:46.670233+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt | demo_workspace/unknown_dir/bulk/tiny_127.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.041119+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.041119+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt | demo_workspace/unknown_dir/bulk/tiny_128.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.060094+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt | demo_workspace/unknown_dir/bulk/tiny_129.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.063585+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.069349+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt | demo_workspace/unknown_dir/bulk/tiny_130.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.069349+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.074564+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.074564+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt | demo_workspace/unknown_dir/bulk/tiny_131.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.453127+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.455141+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt | demo_workspace/unknown_dir/bulk/tiny_132.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.470559+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.470559+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt | demo_workspace/unknown_dir/bulk/tiny_133.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.477085+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.477085+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt | demo_workspace/unknown_dir/bulk/tiny_134.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.483666+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.483666+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt | demo_workspace/unknown_dir/bulk/tiny_135.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.862886+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.862886+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt | demo_workspace/unknown_dir/bulk/tiny_136.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.877956+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.879953+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt | demo_workspace/unknown_dir/bulk/tiny_137.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.885689+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.887689+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt | demo_workspace/unknown_dir/bulk/tiny_138.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.893301+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:47.893301+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt | demo_workspace/unknown_dir/bulk/tiny_139.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.274039+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.274039+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt | demo_workspace/unknown_dir/bulk/tiny_140.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.286324+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.286324+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt | demo_workspace/unknown_dir/bulk/tiny_141.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.291176+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.291176+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt | demo_workspace/unknown_dir/bulk/tiny_142.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.299285+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.302540+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt | demo_workspace/unknown_dir/bulk/tiny_143.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.683423+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt | demo_workspace/unknown_dir/bulk/tiny_144.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.683423+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.693047+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.699562+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt | demo_workspace/unknown_dir/bulk/tiny_145.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.699562+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.704960+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt | demo_workspace/unknown_dir/bulk/tiny_146.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.707985+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:48.707985+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt | demo_workspace/unknown_dir/bulk/tiny_147.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.093782+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.099194+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt | demo_workspace/unknown_dir/bulk/tiny_148.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.105227+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt | demo_workspace/unknown_dir/bulk/tiny_149.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.105227+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.109160+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.109160+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt | demo_workspace/unknown_dir/bulk/tiny_150.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.116620+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.116620+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt | demo_workspace/unknown_dir/bulk/tiny_151.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.507788+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt | demo_workspace/unknown_dir/bulk/tiny_152.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.507788+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.515952+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.517971+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.524122+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt | demo_workspace/unknown_dir/bulk/tiny_153.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.526130+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt | demo_workspace/unknown_dir/bulk/tiny_154.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.526130+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.526130+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt | demo_workspace/unknown_dir/bulk/tiny_155.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.915730+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.922388+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt | demo_workspace/unknown_dir/bulk/tiny_156.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.925915+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.929966+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt | demo_workspace/unknown_dir/bulk/tiny_157.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.935523+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.935523+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt | demo_workspace/unknown_dir/bulk/tiny_158.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.940063+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:49.940063+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt | demo_workspace/unknown_dir/bulk/tiny_159.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.327157+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.327157+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt | demo_workspace/unknown_dir/bulk/tiny_160.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.333928+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.338210+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt | demo_workspace/unknown_dir/bulk/tiny_161.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.344876+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt | demo_workspace/unknown_dir/bulk/tiny_162.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.345922+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.345922+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.345922+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt | demo_workspace/unknown_dir/bulk/tiny_163.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.735029+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.741500+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt | demo_workspace/unknown_dir/bulk/tiny_164.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.743016+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.747790+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt | demo_workspace/unknown_dir/bulk/tiny_165.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.755992+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.755992+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.755992+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt | demo_workspace/unknown_dir/bulk/tiny_166.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:50.755992+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt | demo_workspace/unknown_dir/bulk/tiny_167.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.146540+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.152626+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt | demo_workspace/unknown_dir/bulk/tiny_168.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.156578+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.156578+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt | demo_workspace/unknown_dir/bulk/tiny_169.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.166125+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.166125+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt | demo_workspace/unknown_dir/bulk/tiny_170.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.172491+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.177002+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt | demo_workspace/unknown_dir/bulk/tiny_171.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.559094+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.563633+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt | demo_workspace/unknown_dir/bulk/tiny_172.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.566688+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.570687+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt | demo_workspace/unknown_dir/bulk/tiny_173.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.577194+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.581303+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt | demo_workspace/unknown_dir/bulk/tiny_174.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.582819+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.582819+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt | demo_workspace/unknown_dir/bulk/tiny_175.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.967838+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.974027+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt | demo_workspace/unknown_dir/bulk/tiny_176.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.974027+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.974027+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt | demo_workspace/unknown_dir/bulk/tiny_177.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.989953+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.989953+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt | demo_workspace/unknown_dir/bulk/tiny_178.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.992469+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:51.992469+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt | demo_workspace/unknown_dir/bulk/tiny_179.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.383110+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.387131+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt | demo_workspace/unknown_dir/bulk/tiny_180.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.387131+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.387131+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt | demo_workspace/unknown_dir/bulk/tiny_181.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.399051+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.403089+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt | demo_workspace/unknown_dir/bulk/tiny_182.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.403089+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.403089+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt | demo_workspace/unknown_dir/bulk/tiny_183.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.791365+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.791365+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt | demo_workspace/unknown_dir/bulk/tiny_184.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.795935+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.799839+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt | demo_workspace/unknown_dir/bulk/tiny_185.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.804817+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt | demo_workspace/unknown_dir/bulk/tiny_186.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.810275+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.812790+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:52.812790+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt | demo_workspace/unknown_dir/bulk/tiny_187.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.203550+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.203550+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.212245+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt | demo_workspace/unknown_dir/bulk/tiny_189.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.212245+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt | demo_workspace/unknown_dir/bulk/tiny_188.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.214284+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.214284+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt | demo_workspace/unknown_dir/bulk/tiny_190.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.220504+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.224081+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt | demo_workspace/unknown_dir/bulk/tiny_191.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.614922+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.618912+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt | demo_workspace/unknown_dir/bulk/tiny_192.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.618912+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.626727+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.628239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt | demo_workspace/unknown_dir/bulk/tiny_193.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.628239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt | demo_workspace/unknown_dir/bulk/tiny_194.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.628239+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:53.628239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt | demo_workspace/unknown_dir/bulk/tiny_195.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.027785+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt | demo_workspace/unknown_dir/bulk/tiny_196.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.030564+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.030564+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.030564+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt | demo_workspace/unknown_dir/bulk/tiny_197.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.036206+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.038716+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt | demo_workspace/unknown_dir/bulk/tiny_198.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.038716+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.038716+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt | demo_workspace/unknown_dir/bulk/tiny_199.txt | INFO | R0 | File activity recorded |
| 2026-11-06T22:13:54.038716+00:00 | BULK | pc | unknown |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | HIGH | R4 | Suspicious movement: 200 files transferred to unknown directory |

## Conclusion
The monitor recorded 415 events and 8 rule findings. Review high and critical findings, then retain this report with the JSONL audit log.
