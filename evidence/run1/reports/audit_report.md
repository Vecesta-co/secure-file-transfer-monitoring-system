# Secure File Transfer Monitoring System — Audit Report

Generated: 2026-11-06T20:21:45.000455+00:00
Monitoring period: 2026-11-06T20:21:09.688773+00:00 to 2026-11-06T20:21:43.567800+00:00

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
| 2026-11-06T20:21:12.652892+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-06T20:21:14.100667+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-06T20:21:15.563199+00:00 | R1 | HIGH | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | Sensitive file moved outside approved location |
| 2026-11-06T20:21:17.004712+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-06T20:21:18.488147+00:00 | R3 | CRITICAL | demo_workspace/network_share_sim/passwords_backup.txt |  | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:21:19.928332+00:00 | R3 | CRITICAL | demo_workspace/sensitive/client_database.csv |  | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:21:21.743498+00:00 | R5 | HIGH | demo_workspace/sensitive/server.key |  | Sensitive file deleted |
| 2026-11-06T20:21:43.567800+00:00 | R4 | HIGH |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | Suspicious movement: 200 files transferred to unknown directory |

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
| 2026-11-06T20:21:09.688773+00:00 | MODIFY | pc | unknown | demo_workspace/documents/meeting_notes_copy.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:09.693282+00:00 | COPY | pc | unknown | demo_workspace/documents/meeting_notes.txt | demo_workspace/documents/meeting_notes_copy.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:11.173488+00:00 | MODIFY | pc | unknown | demo_workspace/approved_backup/employee_salaries.csv |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:11.173488+00:00 | COPY | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/approved_backup/employee_salaries.csv | INFO | R0 | Authorized transfer |
| 2026-11-06T20:21:12.652892+00:00 | MODIFY | pc | unknown | demo_workspace/usb_drive_sim/server.key |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:12.652892+00:00 | COPY | pc | unknown | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-06T20:21:14.100667+00:00 | MODIFY | pc | unknown | demo_workspace/cloud_sync_sim/client_database.csv |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:14.100667+00:00 | COPY | pc | unknown | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-06T20:21:15.563199+00:00 | MOVE | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | HIGH | R1 | Sensitive file moved outside approved location |
| 2026-11-06T20:21:17.004712+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:17.004712+00:00 | COPY | pc | unknown | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-06T20:21:18.488147+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:21:19.928332+00:00 | MODIFY | pc | unknown | demo_workspace/sensitive/client_database.csv |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:21:21.743498+00:00 | DELETE | pc | unknown | demo_workspace/sensitive/server.key |  | HIGH | R5 | Sensitive file deleted |
| 2026-11-06T20:21:23.317488+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.319150+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.323620+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.323620+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt | demo_workspace/unknown_dir/bulk/tiny_000.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.329566+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.329566+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt | demo_workspace/unknown_dir/bulk/tiny_003.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.329566+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt | demo_workspace/unknown_dir/bulk/tiny_002.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.329566+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt | demo_workspace/unknown_dir/bulk/tiny_001.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.739095+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.739095+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.744634+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt | demo_workspace/unknown_dir/bulk/tiny_004.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.744634+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.744634+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.744634+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt | demo_workspace/unknown_dir/bulk/tiny_007.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.744634+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt | demo_workspace/unknown_dir/bulk/tiny_005.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:23.744634+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt | demo_workspace/unknown_dir/bulk/tiny_006.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.156950+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.156950+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt | demo_workspace/unknown_dir/bulk/tiny_008.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.167986+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt | demo_workspace/unknown_dir/bulk/tiny_011.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.167986+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.167986+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt | demo_workspace/unknown_dir/bulk/tiny_010.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.167986+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.167986+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.167986+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt | demo_workspace/unknown_dir/bulk/tiny_009.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.569921+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt | demo_workspace/unknown_dir/bulk/tiny_012.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.571925+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.581058+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.581058+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.581058+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt | demo_workspace/unknown_dir/bulk/tiny_013.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.581058+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.581058+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt | demo_workspace/unknown_dir/bulk/tiny_014.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.581058+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt | demo_workspace/unknown_dir/bulk/tiny_015.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.985349+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.992165+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt | demo_workspace/unknown_dir/bulk/tiny_016.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.993670+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.997336+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.997336+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt | demo_workspace/unknown_dir/bulk/tiny_017.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.997336+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.997336+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt | demo_workspace/unknown_dir/bulk/tiny_018.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:24.997336+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt | demo_workspace/unknown_dir/bulk/tiny_019.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.405205+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.409472+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.409472+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt | demo_workspace/unknown_dir/bulk/tiny_020.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.409472+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.409472+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt | demo_workspace/unknown_dir/bulk/tiny_021.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.409472+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.409472+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt | demo_workspace/unknown_dir/bulk/tiny_022.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.420045+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt | demo_workspace/unknown_dir/bulk/tiny_023.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.819495+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.822038+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt | demo_workspace/unknown_dir/bulk/tiny_024.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.825329+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.825329+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.832172+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt | demo_workspace/unknown_dir/bulk/tiny_025.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.832172+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.832172+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt | demo_workspace/unknown_dir/bulk/tiny_026.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:25.832172+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt | demo_workspace/unknown_dir/bulk/tiny_027.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.245232+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.245232+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.245232+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.245232+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.245232+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt | demo_workspace/unknown_dir/bulk/tiny_029.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.257372+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt | demo_workspace/unknown_dir/bulk/tiny_030.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.257372+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt | demo_workspace/unknown_dir/bulk/tiny_028.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.257372+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt | demo_workspace/unknown_dir/bulk/tiny_031.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.659592+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.662792+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.663806+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.663806+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt | demo_workspace/unknown_dir/bulk/tiny_032.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.663806+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt | demo_workspace/unknown_dir/bulk/tiny_033.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.663806+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.675360+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt | demo_workspace/unknown_dir/bulk/tiny_035.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:26.675360+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt | demo_workspace/unknown_dir/bulk/tiny_034.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.074204+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt | demo_workspace/unknown_dir/bulk/tiny_036.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.074204+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.074204+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.074204+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt | demo_workspace/unknown_dir/bulk/tiny_037.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.083489+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.083489+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.092622+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt | demo_workspace/unknown_dir/bulk/tiny_039.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.092622+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt | demo_workspace/unknown_dir/bulk/tiny_038.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.493435+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.494448+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.494448+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.494448+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt | demo_workspace/unknown_dir/bulk/tiny_040.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.502548+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt | demo_workspace/unknown_dir/bulk/tiny_042.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.504068+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt | demo_workspace/unknown_dir/bulk/tiny_041.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.504068+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.504068+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt | demo_workspace/unknown_dir/bulk/tiny_043.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.904401+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.913420+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.915968+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt | demo_workspace/unknown_dir/bulk/tiny_044.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.915968+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt | demo_workspace/unknown_dir/bulk/tiny_045.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.921383+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.921383+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt | demo_workspace/unknown_dir/bulk/tiny_046.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.923887+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:27.923887+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt | demo_workspace/unknown_dir/bulk/tiny_047.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.314748+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt | demo_workspace/unknown_dir/bulk/tiny_048.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.320827+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.328442+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.328442+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt | demo_workspace/unknown_dir/bulk/tiny_049.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.330461+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.335530+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.335530+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt | demo_workspace/unknown_dir/bulk/tiny_050.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.335530+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt | demo_workspace/unknown_dir/bulk/tiny_051.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.725361+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt | demo_workspace/unknown_dir/bulk/tiny_052.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.725361+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.734640+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.744062+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.744062+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt | demo_workspace/unknown_dir/bulk/tiny_053.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.744062+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.744062+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt | demo_workspace/unknown_dir/bulk/tiny_054.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:28.756681+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt | demo_workspace/unknown_dir/bulk/tiny_055.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.139887+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.139887+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt | demo_workspace/unknown_dir/bulk/tiny_056.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.145891+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt | demo_workspace/unknown_dir/bulk/tiny_057.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.148902+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.158969+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.160487+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.160487+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt | demo_workspace/unknown_dir/bulk/tiny_058.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.160487+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt | demo_workspace/unknown_dir/bulk/tiny_059.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.546031+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.546031+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt | demo_workspace/unknown_dir/bulk/tiny_060.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.553184+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.553184+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt | demo_workspace/unknown_dir/bulk/tiny_061.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.569378+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt | demo_workspace/unknown_dir/bulk/tiny_062.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.569378+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.569378+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.569378+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt | demo_workspace/unknown_dir/bulk/tiny_063.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.954044+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.963839+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.963839+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt | demo_workspace/unknown_dir/bulk/tiny_064.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.963839+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt | demo_workspace/unknown_dir/bulk/tiny_065.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.980810+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.984892+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt | demo_workspace/unknown_dir/bulk/tiny_066.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.984892+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:29.984892+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt | demo_workspace/unknown_dir/bulk/tiny_067.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.363252+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt | demo_workspace/unknown_dir/bulk/tiny_068.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.372603+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.374660+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.376989+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt | demo_workspace/unknown_dir/bulk/tiny_069.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.386852+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt | demo_workspace/unknown_dir/bulk/tiny_070.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.388358+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.394255+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.396262+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt | demo_workspace/unknown_dir/bulk/tiny_071.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.781155+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.781669+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt | demo_workspace/unknown_dir/bulk/tiny_072.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.781669+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.789102+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt | demo_workspace/unknown_dir/bulk/tiny_073.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.793692+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.800470+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt | demo_workspace/unknown_dir/bulk/tiny_074.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.800470+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:30.806744+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt | demo_workspace/unknown_dir/bulk/tiny_075.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.194774+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.200975+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.202990+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt | demo_workspace/unknown_dir/bulk/tiny_076.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.209649+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt | demo_workspace/unknown_dir/bulk/tiny_077.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.209649+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt | demo_workspace/unknown_dir/bulk/tiny_078.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.209649+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.209649+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.218701+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt | demo_workspace/unknown_dir/bulk/tiny_079.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.615437+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.620516+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.622029+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.622029+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt | demo_workspace/unknown_dir/bulk/tiny_080.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.631078+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt | demo_workspace/unknown_dir/bulk/tiny_081.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.631078+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.631078+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt | demo_workspace/unknown_dir/bulk/tiny_082.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:31.631078+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt | demo_workspace/unknown_dir/bulk/tiny_083.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.025182+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt | demo_workspace/unknown_dir/bulk/tiny_084.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.027208+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.038392+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.044958+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt | demo_workspace/unknown_dir/bulk/tiny_085.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.047494+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.047494+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.058185+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt | demo_workspace/unknown_dir/bulk/tiny_086.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.058185+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt | demo_workspace/unknown_dir/bulk/tiny_087.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.433468+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.438977+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt | demo_workspace/unknown_dir/bulk/tiny_088.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.442207+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt | demo_workspace/unknown_dir/bulk/tiny_089.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.451320+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.458562+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.464344+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt | demo_workspace/unknown_dir/bulk/tiny_090.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.464344+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.470141+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt | demo_workspace/unknown_dir/bulk/tiny_091.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.843333+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.843333+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt | demo_workspace/unknown_dir/bulk/tiny_092.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.851291+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt | demo_workspace/unknown_dir/bulk/tiny_093.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.855857+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.868907+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt | demo_workspace/unknown_dir/bulk/tiny_094.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.872950+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.874469+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:32.874469+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt | demo_workspace/unknown_dir/bulk/tiny_095.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.250847+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.250847+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt | demo_workspace/unknown_dir/bulk/tiny_096.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.264062+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.264062+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt | demo_workspace/unknown_dir/bulk/tiny_097.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.277241+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.283124+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt | demo_workspace/unknown_dir/bulk/tiny_098.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.286649+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.286649+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt | demo_workspace/unknown_dir/bulk/tiny_099.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.660477+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.660477+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt | demo_workspace/unknown_dir/bulk/tiny_100.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.671364+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt | demo_workspace/unknown_dir/bulk/tiny_101.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.671364+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.683488+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt | demo_workspace/unknown_dir/bulk/tiny_102.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.689460+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.699302+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt | demo_workspace/unknown_dir/bulk/tiny_103.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:33.702219+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.067289+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.067289+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt | demo_workspace/unknown_dir/bulk/tiny_104.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.077848+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.083377+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt | demo_workspace/unknown_dir/bulk/tiny_105.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.093770+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.093770+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt | demo_workspace/unknown_dir/bulk/tiny_106.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.108739+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt | demo_workspace/unknown_dir/bulk/tiny_107.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.108739+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.475633+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.475633+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt | demo_workspace/unknown_dir/bulk/tiny_108.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.487024+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.487024+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt | demo_workspace/unknown_dir/bulk/tiny_109.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.501721+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.506615+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt | demo_workspace/unknown_dir/bulk/tiny_110.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.522633+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.526650+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt | demo_workspace/unknown_dir/bulk/tiny_111.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.884601+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.898199+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.898199+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt | demo_workspace/unknown_dir/bulk/tiny_112.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.898199+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt | demo_workspace/unknown_dir/bulk/tiny_113.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.909530+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.913895+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt | demo_workspace/unknown_dir/bulk/tiny_114.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.929628+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt | demo_workspace/unknown_dir/bulk/tiny_115.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:34.933149+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.306532+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt | demo_workspace/unknown_dir/bulk/tiny_116.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.308615+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.308615+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.308615+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt | demo_workspace/unknown_dir/bulk/tiny_117.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.318745+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.318745+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt | demo_workspace/unknown_dir/bulk/tiny_118.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.338968+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.342436+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt | demo_workspace/unknown_dir/bulk/tiny_119.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.719039+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.719039+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.719039+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt | demo_workspace/unknown_dir/bulk/tiny_120.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.719039+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt | demo_workspace/unknown_dir/bulk/tiny_121.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.729202+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.729202+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt | demo_workspace/unknown_dir/bulk/tiny_122.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.745991+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:35.745991+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt | demo_workspace/unknown_dir/bulk/tiny_123.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.137221+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.146223+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.147239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt | demo_workspace/unknown_dir/bulk/tiny_124.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.147239+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.147239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt | demo_workspace/unknown_dir/bulk/tiny_126.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.147239+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt | demo_workspace/unknown_dir/bulk/tiny_125.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.153969+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.160231+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt | demo_workspace/unknown_dir/bulk/tiny_127.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.552560+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt | demo_workspace/unknown_dir/bulk/tiny_128.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.552560+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.559176+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.564485+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.564485+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt | demo_workspace/unknown_dir/bulk/tiny_129.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.564485+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.564485+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt | demo_workspace/unknown_dir/bulk/tiny_130.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.573382+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt | demo_workspace/unknown_dir/bulk/tiny_131.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.959023+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.967031+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt | demo_workspace/unknown_dir/bulk/tiny_132.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.971497+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt | demo_workspace/unknown_dir/bulk/tiny_133.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.971497+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.979264+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.979264+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.985674+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt | demo_workspace/unknown_dir/bulk/tiny_134.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:36.990791+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt | demo_workspace/unknown_dir/bulk/tiny_135.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.370773+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.370773+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt | demo_workspace/unknown_dir/bulk/tiny_136.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.381520+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.385524+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt | demo_workspace/unknown_dir/bulk/tiny_137.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.389476+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt | demo_workspace/unknown_dir/bulk/tiny_138.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.391492+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.394339+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt | demo_workspace/unknown_dir/bulk/tiny_139.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.394339+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.779747+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.786041+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt | demo_workspace/unknown_dir/bulk/tiny_140.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.790036+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt | demo_workspace/unknown_dir/bulk/tiny_141.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.790036+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.796330+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.802300+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt | demo_workspace/unknown_dir/bulk/tiny_142.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.802300+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:37.809602+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt | demo_workspace/unknown_dir/bulk/tiny_143.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.192885+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.197720+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt | demo_workspace/unknown_dir/bulk/tiny_144.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.203453+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.211600+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt | demo_workspace/unknown_dir/bulk/tiny_145.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.213616+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.213616+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt | demo_workspace/unknown_dir/bulk/tiny_146.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.213616+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.220844+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt | demo_workspace/unknown_dir/bulk/tiny_147.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.604524+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.608242+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt | demo_workspace/unknown_dir/bulk/tiny_148.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.616700+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt | demo_workspace/unknown_dir/bulk/tiny_149.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.621232+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.623745+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.626259+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.626259+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt | demo_workspace/unknown_dir/bulk/tiny_150.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:38.632337+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt | demo_workspace/unknown_dir/bulk/tiny_151.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.017292+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.017292+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt | demo_workspace/unknown_dir/bulk/tiny_152.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.027199+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.030326+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt | demo_workspace/unknown_dir/bulk/tiny_153.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.030326+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt | demo_workspace/unknown_dir/bulk/tiny_154.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.036723+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.042645+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt | demo_workspace/unknown_dir/bulk/tiny_155.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.042645+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.426097+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.426097+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt | demo_workspace/unknown_dir/bulk/tiny_156.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.434449+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.434449+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt | demo_workspace/unknown_dir/bulk/tiny_157.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.443470+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.443470+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt | demo_workspace/unknown_dir/bulk/tiny_158.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.450370+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.454974+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt | demo_workspace/unknown_dir/bulk/tiny_159.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.842684+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.842684+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt | demo_workspace/unknown_dir/bulk/tiny_160.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.847433+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.848449+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt | demo_workspace/unknown_dir/bulk/tiny_161.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.851753+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.857474+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt | demo_workspace/unknown_dir/bulk/tiny_162.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.861505+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt | demo_workspace/unknown_dir/bulk/tiny_163.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:39.861505+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.255024+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.259645+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.261661+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt | demo_workspace/unknown_dir/bulk/tiny_164.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.265267+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt | demo_workspace/unknown_dir/bulk/tiny_165.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.267276+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.267792+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.267792+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt | demo_workspace/unknown_dir/bulk/tiny_166.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.267792+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt | demo_workspace/unknown_dir/bulk/tiny_167.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.671442+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.676488+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.679009+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt | demo_workspace/unknown_dir/bulk/tiny_168.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.679009+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.679009+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.679009+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt | demo_workspace/unknown_dir/bulk/tiny_169.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.692329+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt | demo_workspace/unknown_dir/bulk/tiny_170.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:40.692329+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt | demo_workspace/unknown_dir/bulk/tiny_171.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.084129+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.084129+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt | demo_workspace/unknown_dir/bulk/tiny_172.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.091194+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.098715+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt | demo_workspace/unknown_dir/bulk/tiny_173.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.101354+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.103099+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.103099+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt | demo_workspace/unknown_dir/bulk/tiny_174.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.103099+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt | demo_workspace/unknown_dir/bulk/tiny_175.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.491006+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.491006+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt | demo_workspace/unknown_dir/bulk/tiny_176.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.499879+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt | demo_workspace/unknown_dir/bulk/tiny_177.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.503112+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.506580+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt | demo_workspace/unknown_dir/bulk/tiny_178.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.510019+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.516085+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.516085+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt | demo_workspace/unknown_dir/bulk/tiny_179.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.900464+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.905750+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt | demo_workspace/unknown_dir/bulk/tiny_180.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.909774+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.909774+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt | demo_workspace/unknown_dir/bulk/tiny_181.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.915663+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.915663+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt | demo_workspace/unknown_dir/bulk/tiny_182.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.923118+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:41.925628+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt | demo_workspace/unknown_dir/bulk/tiny_183.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.314189+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.317688+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.321457+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt | demo_workspace/unknown_dir/bulk/tiny_184.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.324480+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt | demo_workspace/unknown_dir/bulk/tiny_185.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.324480+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.324480+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt | demo_workspace/unknown_dir/bulk/tiny_186.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.329975+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.329975+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt | demo_workspace/unknown_dir/bulk/tiny_187.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.724441+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt | demo_workspace/unknown_dir/bulk/tiny_188.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.724441+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.731562+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.733076+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt | demo_workspace/unknown_dir/bulk/tiny_189.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.736523+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.738039+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.738039+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt | demo_workspace/unknown_dir/bulk/tiny_190.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:42.738039+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt | demo_workspace/unknown_dir/bulk/tiny_191.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.131595+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.140905+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt | demo_workspace/unknown_dir/bulk/tiny_192.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.145214+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.145214+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt | demo_workspace/unknown_dir/bulk/tiny_193.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.150124+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.150124+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.150124+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt | demo_workspace/unknown_dir/bulk/tiny_194.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.150124+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt | demo_workspace/unknown_dir/bulk/tiny_195.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.545292+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt | demo_workspace/unknown_dir/bulk/tiny_196.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.545292+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.555659+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.560724+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt | demo_workspace/unknown_dir/bulk/tiny_197.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.560724+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.560724+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.560724+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt | demo_workspace/unknown_dir/bulk/tiny_198.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.567800+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt | demo_workspace/unknown_dir/bulk/tiny_199.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:43.567800+00:00 | BULK | pc | unknown |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | HIGH | R4 | Suspicious movement: 200 files transferred to unknown directory |

## Conclusion
The monitor recorded 415 events and 8 rule findings. Review high and critical findings, then retain this report with the JSONL audit log.
