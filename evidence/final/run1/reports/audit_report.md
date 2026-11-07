# Secure File Transfer Monitoring System — Audit Report

Generated: 2026-11-07T07:22:32.397577+00:00
Monitoring period: 2026-11-07T07:21:27.342688+00:00 to 2026-11-07T07:22:32.049174+00:00

## Totals by event type
| Event | Count |
|---|---:|
| BULK | 1 |
| COPY | 5 |
| CREATE | 200 |
| DELETE | 1 |
| MODIFY | 2 |
| MOVE | 1 |

## Totals by severity
| Severity | Count |
|---|---:|
| CRITICAL | 2 |
| HIGH | 6 |
| INFO | 202 |

## Violations
| Time | Rule | Severity | File | Destination | Message |
|---|---|---|---|---|---|
| 2026-11-07T07:21:31.062811+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-07T07:21:32.910476+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-07T07:21:34.786897+00:00 | R1 | HIGH | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | Sensitive file moved outside approved location |
| 2026-11-07T07:21:36.627052+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-07T07:21:38.511656+00:00 | R3 | CRITICAL | demo_workspace/network_share_sim/passwords_backup.txt |  | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:21:40.351478+00:00 | R3 | CRITICAL | demo_workspace/sensitive/client_database.csv |  | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:21:42.150591+00:00 | R5 | HIGH | demo_workspace/sensitive/server.key |  | Sensitive file deleted |
| 2026-11-07T07:22:32.049174+00:00 | R4 | HIGH |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | Suspicious movement: 200 files transferred to unknown directory |

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

Users: pc (210)

Processes: unknown (210)

## Full timeline
| Time | Type | User | Process | File | Destination | Severity | Rule | Message |
|---|---|---|---|---|---|---|---|---|
| 2026-11-07T07:21:27.342688+00:00 | COPY | pc | unknown | demo_workspace/documents/meeting_notes.txt | demo_workspace/documents/meeting_notes_copy.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:29.223840+00:00 | COPY | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/approved_backup/employee_salaries.csv | INFO | R0 | Authorized transfer |
| 2026-11-07T07:21:31.062811+00:00 | COPY | pc | unknown | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-07T07:21:32.910476+00:00 | COPY | pc | unknown | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-07T07:21:34.786897+00:00 | MOVE | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | HIGH | R1 | Sensitive file moved outside approved location |
| 2026-11-07T07:21:36.627052+00:00 | COPY | pc | unknown | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-07T07:21:38.511656+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:21:40.351478+00:00 | MODIFY | pc | unknown | demo_workspace/sensitive/client_database.csv |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:21:42.150591+00:00 | DELETE | pc | unknown | demo_workspace/sensitive/server.key |  | HIGH | R5 | Sensitive file deleted |
| 2026-11-07T07:21:51.341061+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt | demo_workspace/unknown_dir/bulk/tiny_000.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:51.342230+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt | demo_workspace/unknown_dir/bulk/tiny_003.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:51.342230+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt | demo_workspace/unknown_dir/bulk/tiny_002.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:51.345748+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt | demo_workspace/unknown_dir/bulk/tiny_001.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.163042+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt | demo_workspace/unknown_dir/bulk/tiny_006.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.166197+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt | demo_workspace/unknown_dir/bulk/tiny_007.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.168199+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt | demo_workspace/unknown_dir/bulk/tiny_004.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.170198+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt | demo_workspace/unknown_dir/bulk/tiny_005.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.978680+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt | demo_workspace/unknown_dir/bulk/tiny_008.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.981680+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt | demo_workspace/unknown_dir/bulk/tiny_009.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.984821+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt | demo_workspace/unknown_dir/bulk/tiny_011.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:52.985821+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt | demo_workspace/unknown_dir/bulk/tiny_010.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:53.813964+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt | demo_workspace/unknown_dir/bulk/tiny_014.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:53.817595+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt | demo_workspace/unknown_dir/bulk/tiny_015.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:53.820603+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt | demo_workspace/unknown_dir/bulk/tiny_012.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:53.821601+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt | demo_workspace/unknown_dir/bulk/tiny_013.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:54.625477+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt | demo_workspace/unknown_dir/bulk/tiny_016.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:54.635745+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt | demo_workspace/unknown_dir/bulk/tiny_017.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:54.636744+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt | demo_workspace/unknown_dir/bulk/tiny_019.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:54.639744+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt | demo_workspace/unknown_dir/bulk/tiny_018.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:55.443035+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt | demo_workspace/unknown_dir/bulk/tiny_020.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:55.451583+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt | demo_workspace/unknown_dir/bulk/tiny_021.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:55.454093+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt | demo_workspace/unknown_dir/bulk/tiny_022.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:55.456100+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt | demo_workspace/unknown_dir/bulk/tiny_023.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:56.259787+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt | demo_workspace/unknown_dir/bulk/tiny_024.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:56.272424+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt | demo_workspace/unknown_dir/bulk/tiny_026.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:56.274455+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt | demo_workspace/unknown_dir/bulk/tiny_025.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:56.275463+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt | demo_workspace/unknown_dir/bulk/tiny_027.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.070344+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt | demo_workspace/unknown_dir/bulk/tiny_028.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.090015+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt | demo_workspace/unknown_dir/bulk/tiny_029.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.092527+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt | demo_workspace/unknown_dir/bulk/tiny_030.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.094031+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt | demo_workspace/unknown_dir/bulk/tiny_031.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.881143+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt | demo_workspace/unknown_dir/bulk/tiny_032.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.904757+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt | demo_workspace/unknown_dir/bulk/tiny_033.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.907760+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt | demo_workspace/unknown_dir/bulk/tiny_035.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:57.910280+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt | demo_workspace/unknown_dir/bulk/tiny_034.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:58.691106+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt | demo_workspace/unknown_dir/bulk/tiny_036.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:58.718698+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt | demo_workspace/unknown_dir/bulk/tiny_038.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:58.723701+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt | demo_workspace/unknown_dir/bulk/tiny_039.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:58.725213+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt | demo_workspace/unknown_dir/bulk/tiny_037.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:59.501452+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt | demo_workspace/unknown_dir/bulk/tiny_040.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:59.529484+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt | demo_workspace/unknown_dir/bulk/tiny_041.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:59.540113+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt | demo_workspace/unknown_dir/bulk/tiny_043.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:21:59.542634+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt | demo_workspace/unknown_dir/bulk/tiny_042.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:00.310509+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt | demo_workspace/unknown_dir/bulk/tiny_044.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:00.339731+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt | demo_workspace/unknown_dir/bulk/tiny_045.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:00.353747+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt | demo_workspace/unknown_dir/bulk/tiny_046.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:00.356752+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt | demo_workspace/unknown_dir/bulk/tiny_047.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.121834+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt | demo_workspace/unknown_dir/bulk/tiny_048.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.152346+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt | demo_workspace/unknown_dir/bulk/tiny_049.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.163903+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt | demo_workspace/unknown_dir/bulk/tiny_050.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.170197+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt | demo_workspace/unknown_dir/bulk/tiny_051.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.937685+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt | demo_workspace/unknown_dir/bulk/tiny_052.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.973868+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt | demo_workspace/unknown_dir/bulk/tiny_053.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:01.978959+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt | demo_workspace/unknown_dir/bulk/tiny_054.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:02.750395+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt | demo_workspace/unknown_dir/bulk/tiny_055.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:02.751397+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt | demo_workspace/unknown_dir/bulk/tiny_056.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:02.790930+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt | demo_workspace/unknown_dir/bulk/tiny_057.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:02.792938+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt | demo_workspace/unknown_dir/bulk/tiny_058.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:03.566002+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt | demo_workspace/unknown_dir/bulk/tiny_059.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:03.566002+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt | demo_workspace/unknown_dir/bulk/tiny_060.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:03.605826+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt | demo_workspace/unknown_dir/bulk/tiny_061.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:03.605826+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt | demo_workspace/unknown_dir/bulk/tiny_062.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:04.378328+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt | demo_workspace/unknown_dir/bulk/tiny_064.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:04.380329+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt | demo_workspace/unknown_dir/bulk/tiny_063.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:04.420242+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt | demo_workspace/unknown_dir/bulk/tiny_066.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:04.420242+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt | demo_workspace/unknown_dir/bulk/tiny_065.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:05.192941+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt | demo_workspace/unknown_dir/bulk/tiny_067.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:05.193942+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt | demo_workspace/unknown_dir/bulk/tiny_068.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:05.236745+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt | demo_workspace/unknown_dir/bulk/tiny_069.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:05.236745+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt | demo_workspace/unknown_dir/bulk/tiny_070.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.007531+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt | demo_workspace/unknown_dir/bulk/tiny_071.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.007531+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt | demo_workspace/unknown_dir/bulk/tiny_072.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.053961+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt | demo_workspace/unknown_dir/bulk/tiny_074.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.053961+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt | demo_workspace/unknown_dir/bulk/tiny_073.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.821710+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt | demo_workspace/unknown_dir/bulk/tiny_075.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.822710+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt | demo_workspace/unknown_dir/bulk/tiny_076.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.870008+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt | demo_workspace/unknown_dir/bulk/tiny_077.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:06.870008+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt | demo_workspace/unknown_dir/bulk/tiny_078.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:07.638168+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt | demo_workspace/unknown_dir/bulk/tiny_080.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:07.640168+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt | demo_workspace/unknown_dir/bulk/tiny_079.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:07.683007+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt | demo_workspace/unknown_dir/bulk/tiny_081.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:07.684006+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt | demo_workspace/unknown_dir/bulk/tiny_082.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:08.454057+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt | demo_workspace/unknown_dir/bulk/tiny_083.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:08.456133+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt | demo_workspace/unknown_dir/bulk/tiny_084.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:08.496350+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt | demo_workspace/unknown_dir/bulk/tiny_086.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:08.498402+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt | demo_workspace/unknown_dir/bulk/tiny_085.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:09.265699+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt | demo_workspace/unknown_dir/bulk/tiny_087.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:09.271208+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt | demo_workspace/unknown_dir/bulk/tiny_088.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:09.310867+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt | demo_workspace/unknown_dir/bulk/tiny_090.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:09.310867+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt | demo_workspace/unknown_dir/bulk/tiny_089.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.078328+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt | demo_workspace/unknown_dir/bulk/tiny_091.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.082334+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt | demo_workspace/unknown_dir/bulk/tiny_092.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.122214+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt | demo_workspace/unknown_dir/bulk/tiny_094.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.126248+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt | demo_workspace/unknown_dir/bulk/tiny_093.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.887862+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt | demo_workspace/unknown_dir/bulk/tiny_095.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.892881+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt | demo_workspace/unknown_dir/bulk/tiny_096.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.938832+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt | demo_workspace/unknown_dir/bulk/tiny_097.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:10.941339+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt | demo_workspace/unknown_dir/bulk/tiny_098.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:11.702921+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt | demo_workspace/unknown_dir/bulk/tiny_099.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:11.705308+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt | demo_workspace/unknown_dir/bulk/tiny_100.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:11.755998+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt | demo_workspace/unknown_dir/bulk/tiny_101.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:11.757503+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt | demo_workspace/unknown_dir/bulk/tiny_102.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:12.517746+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt | demo_workspace/unknown_dir/bulk/tiny_103.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:12.519749+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt | demo_workspace/unknown_dir/bulk/tiny_104.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:12.569095+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt | demo_workspace/unknown_dir/bulk/tiny_105.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:12.570097+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt | demo_workspace/unknown_dir/bulk/tiny_106.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:13.333684+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt | demo_workspace/unknown_dir/bulk/tiny_107.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:13.334691+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt | demo_workspace/unknown_dir/bulk/tiny_108.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:13.384740+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt | demo_workspace/unknown_dir/bulk/tiny_109.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:13.385742+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt | demo_workspace/unknown_dir/bulk/tiny_110.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:14.149516+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt | demo_workspace/unknown_dir/bulk/tiny_112.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:14.152519+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt | demo_workspace/unknown_dir/bulk/tiny_111.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:14.199175+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt | demo_workspace/unknown_dir/bulk/tiny_114.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:14.199175+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt | demo_workspace/unknown_dir/bulk/tiny_113.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:14.961986+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt | demo_workspace/unknown_dir/bulk/tiny_115.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:14.963987+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt | demo_workspace/unknown_dir/bulk/tiny_116.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:15.010917+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt | demo_workspace/unknown_dir/bulk/tiny_117.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:15.011916+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt | demo_workspace/unknown_dir/bulk/tiny_118.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:15.775288+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt | demo_workspace/unknown_dir/bulk/tiny_119.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:15.777288+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt | demo_workspace/unknown_dir/bulk/tiny_120.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:15.825164+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt | demo_workspace/unknown_dir/bulk/tiny_122.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:15.825164+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt | demo_workspace/unknown_dir/bulk/tiny_121.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:16.589254+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt | demo_workspace/unknown_dir/bulk/tiny_123.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:16.590253+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt | demo_workspace/unknown_dir/bulk/tiny_124.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:16.638897+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt | demo_workspace/unknown_dir/bulk/tiny_126.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:16.638897+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt | demo_workspace/unknown_dir/bulk/tiny_125.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:17.403826+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt | demo_workspace/unknown_dir/bulk/tiny_128.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:17.404895+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt | demo_workspace/unknown_dir/bulk/tiny_127.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:17.450025+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt | demo_workspace/unknown_dir/bulk/tiny_130.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:17.457553+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt | demo_workspace/unknown_dir/bulk/tiny_129.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:18.219760+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt | demo_workspace/unknown_dir/bulk/tiny_131.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:18.220759+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt | demo_workspace/unknown_dir/bulk/tiny_132.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:18.261787+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt | demo_workspace/unknown_dir/bulk/tiny_133.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:18.273833+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt | demo_workspace/unknown_dir/bulk/tiny_134.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:19.031705+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt | demo_workspace/unknown_dir/bulk/tiny_135.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:19.037730+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt | demo_workspace/unknown_dir/bulk/tiny_136.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:19.071905+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt | demo_workspace/unknown_dir/bulk/tiny_137.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:19.089450+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt | demo_workspace/unknown_dir/bulk/tiny_138.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:19.843685+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt | demo_workspace/unknown_dir/bulk/tiny_139.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:19.849721+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt | demo_workspace/unknown_dir/bulk/tiny_140.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:20.020619+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt | demo_workspace/unknown_dir/bulk/tiny_141.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:20.020619+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt | demo_workspace/unknown_dir/bulk/tiny_142.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:20.661969+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt | demo_workspace/unknown_dir/bulk/tiny_144.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:20.661969+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt | demo_workspace/unknown_dir/bulk/tiny_143.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:20.833988+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt | demo_workspace/unknown_dir/bulk/tiny_146.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:20.837207+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt | demo_workspace/unknown_dir/bulk/tiny_145.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:21.475347+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt | demo_workspace/unknown_dir/bulk/tiny_147.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:21.481352+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt | demo_workspace/unknown_dir/bulk/tiny_148.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:21.649493+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt | demo_workspace/unknown_dir/bulk/tiny_149.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:21.652491+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt | demo_workspace/unknown_dir/bulk/tiny_150.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:22.289668+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt | demo_workspace/unknown_dir/bulk/tiny_151.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:22.295189+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt | demo_workspace/unknown_dir/bulk/tiny_152.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:22.466069+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt | demo_workspace/unknown_dir/bulk/tiny_154.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:22.468579+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt | demo_workspace/unknown_dir/bulk/tiny_153.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:23.103875+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt | demo_workspace/unknown_dir/bulk/tiny_155.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:23.111090+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt | demo_workspace/unknown_dir/bulk/tiny_156.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:23.281127+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt | demo_workspace/unknown_dir/bulk/tiny_157.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:23.282127+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt | demo_workspace/unknown_dir/bulk/tiny_158.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:23.917279+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt | demo_workspace/unknown_dir/bulk/tiny_159.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:23.922351+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt | demo_workspace/unknown_dir/bulk/tiny_160.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:24.095493+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt | demo_workspace/unknown_dir/bulk/tiny_161.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:24.097494+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt | demo_workspace/unknown_dir/bulk/tiny_162.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:24.732245+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt | demo_workspace/unknown_dir/bulk/tiny_163.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:24.738267+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt | demo_workspace/unknown_dir/bulk/tiny_164.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:24.909770+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt | demo_workspace/unknown_dir/bulk/tiny_166.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:24.910770+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt | demo_workspace/unknown_dir/bulk/tiny_165.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:25.550219+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt | demo_workspace/unknown_dir/bulk/tiny_167.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:25.722896+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt | demo_workspace/unknown_dir/bulk/tiny_168.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:25.727404+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt | demo_workspace/unknown_dir/bulk/tiny_169.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:25.728404+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt | demo_workspace/unknown_dir/bulk/tiny_170.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:26.361297+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt | demo_workspace/unknown_dir/bulk/tiny_171.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:26.536739+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt | demo_workspace/unknown_dir/bulk/tiny_172.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:26.542286+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt | demo_workspace/unknown_dir/bulk/tiny_173.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:26.547384+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt | demo_workspace/unknown_dir/bulk/tiny_174.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:27.173063+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt | demo_workspace/unknown_dir/bulk/tiny_175.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:27.349491+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt | demo_workspace/unknown_dir/bulk/tiny_176.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:27.356040+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt | demo_workspace/unknown_dir/bulk/tiny_177.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:27.358552+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt | demo_workspace/unknown_dir/bulk/tiny_178.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:27.988239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt | demo_workspace/unknown_dir/bulk/tiny_179.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.163807+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt | demo_workspace/unknown_dir/bulk/tiny_180.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.168616+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt | demo_workspace/unknown_dir/bulk/tiny_181.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.170619+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt | demo_workspace/unknown_dir/bulk/tiny_182.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.800476+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt | demo_workspace/unknown_dir/bulk/tiny_183.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.974292+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt | demo_workspace/unknown_dir/bulk/tiny_184.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.981890+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt | demo_workspace/unknown_dir/bulk/tiny_185.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:28.984913+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt | demo_workspace/unknown_dir/bulk/tiny_186.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:29.612523+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt | demo_workspace/unknown_dir/bulk/tiny_187.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:29.789100+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt | demo_workspace/unknown_dir/bulk/tiny_188.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:29.800148+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt | demo_workspace/unknown_dir/bulk/tiny_189.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:29.802149+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt | demo_workspace/unknown_dir/bulk/tiny_190.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:30.425804+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt | demo_workspace/unknown_dir/bulk/tiny_191.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:30.601203+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt | demo_workspace/unknown_dir/bulk/tiny_192.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:30.610898+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt | demo_workspace/unknown_dir/bulk/tiny_193.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:30.614932+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt | demo_workspace/unknown_dir/bulk/tiny_194.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:31.238302+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt | demo_workspace/unknown_dir/bulk/tiny_195.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:31.410724+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt | demo_workspace/unknown_dir/bulk/tiny_196.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:31.426606+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt | demo_workspace/unknown_dir/bulk/tiny_198.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:31.432119+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt | demo_workspace/unknown_dir/bulk/tiny_197.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:32.049174+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt | demo_workspace/unknown_dir/bulk/tiny_199.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:32.049174+00:00 | BULK | pc | unknown |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | HIGH | R4 | Suspicious movement: 200 files transferred to unknown directory |

## Conclusion
The monitor recorded 210 events and 8 rule findings. Review high and critical findings, then retain this report with the JSONL audit log.
