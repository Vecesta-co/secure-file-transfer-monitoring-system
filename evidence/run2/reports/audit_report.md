# Secure File Transfer Monitoring System — Audit Report

Generated: 2026-11-06T20:22:28.914762+00:00
Monitoring period: 2026-11-06T20:21:53.760276+00:00 to 2026-11-06T20:22:27.740474+00:00

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
| 2026-11-06T20:21:56.713142+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-06T20:21:58.165594+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-06T20:21:59.605675+00:00 | R1 | HIGH | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | Sensitive file moved outside approved location |
| 2026-11-06T20:22:01.052375+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-06T20:22:02.489156+00:00 | R3 | CRITICAL | demo_workspace/network_share_sim/passwords_backup.txt |  | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:22:03.914908+00:00 | R3 | CRITICAL | demo_workspace/sensitive/client_database.csv |  | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:22:05.854686+00:00 | R5 | HIGH | demo_workspace/sensitive/server.key |  | Sensitive file deleted |
| 2026-11-06T20:22:27.740474+00:00 | R4 | HIGH |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | Suspicious movement: 200 files transferred to unknown directory |

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
| 2026-11-06T20:21:53.760276+00:00 | MODIFY | pc | unknown | demo_workspace/documents/meeting_notes_copy.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:53.764287+00:00 | COPY | pc | unknown | demo_workspace/documents/meeting_notes.txt | demo_workspace/documents/meeting_notes_copy.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:55.236103+00:00 | MODIFY | pc | unknown | demo_workspace/approved_backup/employee_salaries.csv |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:55.236103+00:00 | COPY | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/approved_backup/employee_salaries.csv | INFO | R0 | Authorized transfer |
| 2026-11-06T20:21:56.713142+00:00 | MODIFY | pc | unknown | demo_workspace/usb_drive_sim/server.key |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:56.713142+00:00 | COPY | pc | unknown | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-06T20:21:58.165594+00:00 | MODIFY | pc | unknown | demo_workspace/cloud_sync_sim/client_database.csv |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:21:58.165594+00:00 | COPY | pc | unknown | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-06T20:21:59.605675+00:00 | MOVE | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | HIGH | R1 | Sensitive file moved outside approved location |
| 2026-11-06T20:22:01.046549+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:01.052375+00:00 | COPY | pc | unknown | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-06T20:22:02.489156+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:22:03.914908+00:00 | MODIFY | pc | unknown | demo_workspace/sensitive/client_database.csv |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-06T20:22:05.854686+00:00 | DELETE | pc | unknown | demo_workspace/sensitive/server.key |  | HIGH | R5 | Sensitive file deleted |
| 2026-11-06T20:22:07.409080+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.412471+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.412471+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.412471+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.412471+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt | demo_workspace/unknown_dir/bulk/tiny_000.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.422997+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt | demo_workspace/unknown_dir/bulk/tiny_001.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.422997+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt | demo_workspace/unknown_dir/bulk/tiny_003.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.422997+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt | demo_workspace/unknown_dir/bulk/tiny_002.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.830817+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt | demo_workspace/unknown_dir/bulk/tiny_004.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt | demo_workspace/unknown_dir/bulk/tiny_007.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt | demo_workspace/unknown_dir/bulk/tiny_006.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:07.834352+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt | demo_workspace/unknown_dir/bulk/tiny_005.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.250677+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.250677+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.250677+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.250677+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.263272+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt | demo_workspace/unknown_dir/bulk/tiny_010.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.263272+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt | demo_workspace/unknown_dir/bulk/tiny_009.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.263272+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt | demo_workspace/unknown_dir/bulk/tiny_011.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.263272+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt | demo_workspace/unknown_dir/bulk/tiny_008.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.661005+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.664709+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt | demo_workspace/unknown_dir/bulk/tiny_012.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.664709+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.669979+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt | demo_workspace/unknown_dir/bulk/tiny_013.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.673122+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.673122+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.676788+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt | demo_workspace/unknown_dir/bulk/tiny_014.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:08.680679+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt | demo_workspace/unknown_dir/bulk/tiny_015.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.077862+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.082883+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.086411+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt | demo_workspace/unknown_dir/bulk/tiny_016.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.086411+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.086411+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt | demo_workspace/unknown_dir/bulk/tiny_017.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.090785+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.090785+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt | demo_workspace/unknown_dir/bulk/tiny_018.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.090785+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt | demo_workspace/unknown_dir/bulk/tiny_019.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.495572+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.495572+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.500618+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt | demo_workspace/unknown_dir/bulk/tiny_020.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.500618+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.505391+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.505391+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt | demo_workspace/unknown_dir/bulk/tiny_021.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.508650+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt | demo_workspace/unknown_dir/bulk/tiny_022.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.508650+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt | demo_workspace/unknown_dir/bulk/tiny_023.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.908810+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.913086+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.913086+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt | demo_workspace/unknown_dir/bulk/tiny_024.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.916055+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.916055+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt | demo_workspace/unknown_dir/bulk/tiny_025.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.916055+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.916055+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt | demo_workspace/unknown_dir/bulk/tiny_026.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:09.916055+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt | demo_workspace/unknown_dir/bulk/tiny_027.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.331074+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.331074+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.331074+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.331074+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt | demo_workspace/unknown_dir/bulk/tiny_029.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.343563+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.343563+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt | demo_workspace/unknown_dir/bulk/tiny_030.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.343563+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt | demo_workspace/unknown_dir/bulk/tiny_031.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.343563+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt | demo_workspace/unknown_dir/bulk/tiny_028.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.749840+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.749840+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.755686+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt | demo_workspace/unknown_dir/bulk/tiny_032.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.755686+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.762484+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.762484+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt | demo_workspace/unknown_dir/bulk/tiny_033.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.764490+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt | demo_workspace/unknown_dir/bulk/tiny_034.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:10.764490+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt | demo_workspace/unknown_dir/bulk/tiny_035.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.167556+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.167556+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.167556+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt | demo_workspace/unknown_dir/bulk/tiny_036.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.175657+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt | demo_workspace/unknown_dir/bulk/tiny_037.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.175657+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.175657+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.187892+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt | demo_workspace/unknown_dir/bulk/tiny_038.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.187892+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt | demo_workspace/unknown_dir/bulk/tiny_039.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.585235+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.592853+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.592853+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt | demo_workspace/unknown_dir/bulk/tiny_041.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.596863+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.596863+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt | demo_workspace/unknown_dir/bulk/tiny_042.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.596863+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt | demo_workspace/unknown_dir/bulk/tiny_040.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.596863+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:11.596863+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt | demo_workspace/unknown_dir/bulk/tiny_043.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.010604+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.010604+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.010604+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt | demo_workspace/unknown_dir/bulk/tiny_044.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.018657+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.018657+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.018657+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt | demo_workspace/unknown_dir/bulk/tiny_045.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.026354+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt | demo_workspace/unknown_dir/bulk/tiny_047.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.026354+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt | demo_workspace/unknown_dir/bulk/tiny_046.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.422916+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.422916+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.422916+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt | demo_workspace/unknown_dir/bulk/tiny_048.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.434881+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt | demo_workspace/unknown_dir/bulk/tiny_049.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.434881+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.441127+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt | demo_workspace/unknown_dir/bulk/tiny_050.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.441127+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.447793+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt | demo_workspace/unknown_dir/bulk/tiny_051.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.838826+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.848883+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.851405+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt | demo_workspace/unknown_dir/bulk/tiny_052.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.853151+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt | demo_workspace/unknown_dir/bulk/tiny_053.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.853151+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.853151+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.853151+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt | demo_workspace/unknown_dir/bulk/tiny_054.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:12.853151+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt | demo_workspace/unknown_dir/bulk/tiny_055.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.250514+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt | demo_workspace/unknown_dir/bulk/tiny_056.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.254288+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.257253+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt | demo_workspace/unknown_dir/bulk/tiny_057.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.263328+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.266362+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.267366+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt | demo_workspace/unknown_dir/bulk/tiny_058.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.267366+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.267366+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt | demo_workspace/unknown_dir/bulk/tiny_059.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.661398+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.667061+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt | demo_workspace/unknown_dir/bulk/tiny_060.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.667061+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.678318+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt | demo_workspace/unknown_dir/bulk/tiny_061.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.678318+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.678318+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt | demo_workspace/unknown_dir/bulk/tiny_062.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.678318+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:13.688048+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt | demo_workspace/unknown_dir/bulk/tiny_063.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.091314+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.091314+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.091314+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.091314+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt | demo_workspace/unknown_dir/bulk/tiny_064.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.091314+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.091314+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt | demo_workspace/unknown_dir/bulk/tiny_067.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.105440+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt | demo_workspace/unknown_dir/bulk/tiny_066.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.105440+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt | demo_workspace/unknown_dir/bulk/tiny_065.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.515518+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.517263+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.517263+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.517263+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt | demo_workspace/unknown_dir/bulk/tiny_068.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.517263+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt | demo_workspace/unknown_dir/bulk/tiny_070.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.517263+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.533075+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt | demo_workspace/unknown_dir/bulk/tiny_071.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.535084+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt | demo_workspace/unknown_dir/bulk/tiny_069.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.927664+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.929178+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt | demo_workspace/unknown_dir/bulk/tiny_072.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.929178+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.939612+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt | demo_workspace/unknown_dir/bulk/tiny_073.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.939612+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.945270+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.945270+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt | demo_workspace/unknown_dir/bulk/tiny_074.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:14.945270+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt | demo_workspace/unknown_dir/bulk/tiny_075.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.351373+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.356558+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.356558+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt | demo_workspace/unknown_dir/bulk/tiny_076.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.356558+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt | demo_workspace/unknown_dir/bulk/tiny_077.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.356558+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.356558+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.356558+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt | demo_workspace/unknown_dir/bulk/tiny_078.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.372205+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt | demo_workspace/unknown_dir/bulk/tiny_079.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt | demo_workspace/unknown_dir/bulk/tiny_081.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt | demo_workspace/unknown_dir/bulk/tiny_080.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.783769+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt | demo_workspace/unknown_dir/bulk/tiny_082.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:15.799485+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt | demo_workspace/unknown_dir/bulk/tiny_083.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.196565+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.197580+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt | demo_workspace/unknown_dir/bulk/tiny_084.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.202636+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.211344+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.211344+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt | demo_workspace/unknown_dir/bulk/tiny_085.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.211344+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.211344+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt | demo_workspace/unknown_dir/bulk/tiny_086.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.211344+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt | demo_workspace/unknown_dir/bulk/tiny_087.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.618403+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.625241+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.625241+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt | demo_workspace/unknown_dir/bulk/tiny_088.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.625241+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.625241+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt | demo_workspace/unknown_dir/bulk/tiny_089.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.625241+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.638122+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt | demo_workspace/unknown_dir/bulk/tiny_090.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:16.638122+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt | demo_workspace/unknown_dir/bulk/tiny_091.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.034415+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.034415+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt | demo_workspace/unknown_dir/bulk/tiny_092.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.046967+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.050480+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.050480+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.050480+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt | demo_workspace/unknown_dir/bulk/tiny_094.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.050480+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt | demo_workspace/unknown_dir/bulk/tiny_093.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.050480+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt | demo_workspace/unknown_dir/bulk/tiny_095.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.444735+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.448195+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt | demo_workspace/unknown_dir/bulk/tiny_096.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.461710+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.465768+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.470287+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt | demo_workspace/unknown_dir/bulk/tiny_097.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.475909+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.475909+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt | demo_workspace/unknown_dir/bulk/tiny_098.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.475909+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt | demo_workspace/unknown_dir/bulk/tiny_099.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.853609+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt | demo_workspace/unknown_dir/bulk/tiny_100.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.856331+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.871967+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt | demo_workspace/unknown_dir/bulk/tiny_101.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.874049+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.881639+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt | demo_workspace/unknown_dir/bulk/tiny_102.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.881639+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.888080+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:17.888080+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt | demo_workspace/unknown_dir/bulk/tiny_103.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.264825+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt | demo_workspace/unknown_dir/bulk/tiny_104.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.264825+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.278204+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.278204+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt | demo_workspace/unknown_dir/bulk/tiny_105.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.290358+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.294389+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.294389+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt | demo_workspace/unknown_dir/bulk/tiny_106.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.294389+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt | demo_workspace/unknown_dir/bulk/tiny_107.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.671637+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.671637+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt | demo_workspace/unknown_dir/bulk/tiny_108.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.686000+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.686000+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt | demo_workspace/unknown_dir/bulk/tiny_109.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.698651+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt | demo_workspace/unknown_dir/bulk/tiny_110.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.700655+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.707057+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:18.707057+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt | demo_workspace/unknown_dir/bulk/tiny_111.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.085343+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.092237+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt | demo_workspace/unknown_dir/bulk/tiny_112.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.094772+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.094772+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt | demo_workspace/unknown_dir/bulk/tiny_113.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.104904+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.110441+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt | demo_workspace/unknown_dir/bulk/tiny_114.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.115904+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.115904+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt | demo_workspace/unknown_dir/bulk/tiny_115.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.498135+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt | demo_workspace/unknown_dir/bulk/tiny_116.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.498135+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.505242+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.507663+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt | demo_workspace/unknown_dir/bulk/tiny_117.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.515391+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt | demo_workspace/unknown_dir/bulk/tiny_118.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.516897+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.525150+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.525150+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt | demo_workspace/unknown_dir/bulk/tiny_119.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.906628+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.919165+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.921721+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt | demo_workspace/unknown_dir/bulk/tiny_120.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.922234+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt | demo_workspace/unknown_dir/bulk/tiny_121.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.922234+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.922234+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt | demo_workspace/unknown_dir/bulk/tiny_122.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.934905+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:19.934905+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt | demo_workspace/unknown_dir/bulk/tiny_123.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.318191+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt | demo_workspace/unknown_dir/bulk/tiny_124.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.323234+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.329888+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt | demo_workspace/unknown_dir/bulk/tiny_125.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.333924+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.333924+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt | demo_workspace/unknown_dir/bulk/tiny_126.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.333924+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.343886+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.343886+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt | demo_workspace/unknown_dir/bulk/tiny_127.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.727342+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt | demo_workspace/unknown_dir/bulk/tiny_128.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.727342+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.737389+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt | demo_workspace/unknown_dir/bulk/tiny_129.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.737389+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.745461+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.752433+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.752433+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt | demo_workspace/unknown_dir/bulk/tiny_130.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:20.760284+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt | demo_workspace/unknown_dir/bulk/tiny_131.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.134847+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.134847+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt | demo_workspace/unknown_dir/bulk/tiny_132.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.147367+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.150507+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt | demo_workspace/unknown_dir/bulk/tiny_133.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.158986+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt | demo_workspace/unknown_dir/bulk/tiny_134.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.158986+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.164929+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.164929+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt | demo_workspace/unknown_dir/bulk/tiny_135.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.542511+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.542511+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt | demo_workspace/unknown_dir/bulk/tiny_136.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.555018+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.559460+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt | demo_workspace/unknown_dir/bulk/tiny_137.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.565552+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.570314+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt | demo_workspace/unknown_dir/bulk/tiny_138.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.573832+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.573832+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt | demo_workspace/unknown_dir/bulk/tiny_139.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.953078+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.953078+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt | demo_workspace/unknown_dir/bulk/tiny_140.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.963233+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt | demo_workspace/unknown_dir/bulk/tiny_141.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.965740+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.974294+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.974294+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt | demo_workspace/unknown_dir/bulk/tiny_142.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.983562+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:21.983562+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt | demo_workspace/unknown_dir/bulk/tiny_143.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.371529+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.371529+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.382029+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt | demo_workspace/unknown_dir/bulk/tiny_144.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.382029+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt | demo_workspace/unknown_dir/bulk/tiny_145.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.382029+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.389455+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.395862+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt | demo_workspace/unknown_dir/bulk/tiny_146.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.395862+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt | demo_workspace/unknown_dir/bulk/tiny_147.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.780833+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.780833+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt | demo_workspace/unknown_dir/bulk/tiny_148.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.794231+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.795248+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt | demo_workspace/unknown_dir/bulk/tiny_149.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.798612+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt | demo_workspace/unknown_dir/bulk/tiny_150.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.798612+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.803855+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt | demo_workspace/unknown_dir/bulk/tiny_151.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:22.803855+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.195257+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.195257+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt | demo_workspace/unknown_dir/bulk/tiny_152.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.203080+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.205110+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt | demo_workspace/unknown_dir/bulk/tiny_153.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.205110+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.211611+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt | demo_workspace/unknown_dir/bulk/tiny_154.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.211611+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.211611+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt | demo_workspace/unknown_dir/bulk/tiny_155.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.604678+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.608871+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt | demo_workspace/unknown_dir/bulk/tiny_156.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.613829+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt | demo_workspace/unknown_dir/bulk/tiny_157.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.616337+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.616337+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.620940+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.624438+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt | demo_workspace/unknown_dir/bulk/tiny_158.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:23.626672+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt | demo_workspace/unknown_dir/bulk/tiny_159.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.016850+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.016850+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt | demo_workspace/unknown_dir/bulk/tiny_160.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.022288+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.027370+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt | demo_workspace/unknown_dir/bulk/tiny_161.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.030407+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.030407+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.030407+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt | demo_workspace/unknown_dir/bulk/tiny_163.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.030407+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt | demo_workspace/unknown_dir/bulk/tiny_162.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.432324+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.432324+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.437913+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt | demo_workspace/unknown_dir/bulk/tiny_165.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.441350+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt | demo_workspace/unknown_dir/bulk/tiny_164.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.441350+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.448065+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.448065+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt | demo_workspace/unknown_dir/bulk/tiny_166.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.453549+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt | demo_workspace/unknown_dir/bulk/tiny_167.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.841222+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.841222+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt | demo_workspace/unknown_dir/bulk/tiny_168.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.851213+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.851213+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt | demo_workspace/unknown_dir/bulk/tiny_169.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.858213+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt | demo_workspace/unknown_dir/bulk/tiny_170.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.858213+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.861634+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:24.865327+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt | demo_workspace/unknown_dir/bulk/tiny_171.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.249884+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.257149+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt | demo_workspace/unknown_dir/bulk/tiny_172.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.258665+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.261971+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt | demo_workspace/unknown_dir/bulk/tiny_173.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.265385+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.271918+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt | demo_workspace/unknown_dir/bulk/tiny_174.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.271918+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.271918+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt | demo_workspace/unknown_dir/bulk/tiny_175.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.662148+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.662148+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt | demo_workspace/unknown_dir/bulk/tiny_176.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.667304+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.672051+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt | demo_workspace/unknown_dir/bulk/tiny_177.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.674513+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt | demo_workspace/unknown_dir/bulk/tiny_178.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.678037+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.680051+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:25.680051+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt | demo_workspace/unknown_dir/bulk/tiny_179.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.074375+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.076896+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt | demo_workspace/unknown_dir/bulk/tiny_180.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.076896+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.082795+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt | demo_workspace/unknown_dir/bulk/tiny_181.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.082795+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.082795+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt | demo_workspace/unknown_dir/bulk/tiny_182.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.090238+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.090238+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt | demo_workspace/unknown_dir/bulk/tiny_183.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.482643+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.482643+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt | demo_workspace/unknown_dir/bulk/tiny_184.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.497222+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.497222+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.497222+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt | demo_workspace/unknown_dir/bulk/tiny_185.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.503502+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt | demo_workspace/unknown_dir/bulk/tiny_186.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.503502+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.503502+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt | demo_workspace/unknown_dir/bulk/tiny_187.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.890779+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.895257+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt | demo_workspace/unknown_dir/bulk/tiny_188.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.904486+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.910905+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt | demo_workspace/unknown_dir/bulk/tiny_189.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.910905+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.915128+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.915128+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt | demo_workspace/unknown_dir/bulk/tiny_191.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:26.915128+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt | demo_workspace/unknown_dir/bulk/tiny_190.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.302116+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.302116+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt | demo_workspace/unknown_dir/bulk/tiny_192.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.316545+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt | demo_workspace/unknown_dir/bulk/tiny_193.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.316545+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.320244+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.320244+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt | demo_workspace/unknown_dir/bulk/tiny_194.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.328085+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.331119+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt | demo_workspace/unknown_dir/bulk/tiny_195.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.715706+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.715706+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt | demo_workspace/unknown_dir/bulk/tiny_196.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.726815+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.732225+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.733741+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt | demo_workspace/unknown_dir/bulk/tiny_197.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.740474+00:00 | MODIFY | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt |  | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.740474+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt | demo_workspace/unknown_dir/bulk/tiny_198.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.740474+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt | demo_workspace/unknown_dir/bulk/tiny_199.txt | INFO | R0 | File activity recorded |
| 2026-11-06T20:22:27.740474+00:00 | BULK | pc | unknown |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | HIGH | R4 | Suspicious movement: 200 files transferred to unknown directory |

## Conclusion
The monitor recorded 415 events and 8 rule findings. Review high and critical findings, then retain this report with the JSONL audit log.
