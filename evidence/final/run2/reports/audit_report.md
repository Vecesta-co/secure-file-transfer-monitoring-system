# Secure File Transfer Monitoring System — Audit Report

Generated: 2026-11-07T07:23:35.204149+00:00
Monitoring period: 2026-11-07T07:22:37.252255+00:00 to 2026-11-07T07:23:34.722998+00:00

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
| 2026-11-07T07:22:40.922625+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-07T07:22:42.761323+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-07T07:22:44.612045+00:00 | R1 | HIGH | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | Sensitive file moved outside approved location |
| 2026-11-07T07:22:46.446494+00:00 | R1,R2 | HIGH | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-07T07:22:48.308197+00:00 | R3 | CRITICAL | demo_workspace/network_share_sim/passwords_backup.txt |  | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:22:50.160060+00:00 | R3 | CRITICAL | demo_workspace/sensitive/client_database.csv |  | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:22:51.962515+00:00 | R5 | HIGH | demo_workspace/sensitive/server.key |  | Sensitive file deleted |
| 2026-11-07T07:23:34.722998+00:00 | R4 | HIGH |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | Suspicious movement: 200 files transferred to unknown directory |

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
| 2026-11-07T07:22:37.252255+00:00 | COPY | pc | unknown | demo_workspace/documents/meeting_notes.txt | demo_workspace/documents/meeting_notes_copy.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:39.078639+00:00 | COPY | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/approved_backup/employee_salaries.csv | INFO | R0 | Authorized transfer |
| 2026-11-07T07:22:40.922625+00:00 | COPY | pc | unknown | demo_workspace/sensitive/server.key | demo_workspace/usb_drive_sim/server.key | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to USB drive |
| 2026-11-07T07:22:42.761323+00:00 | COPY | pc | unknown | demo_workspace/sensitive/client_database.csv | demo_workspace/cloud_sync_sim/client_database.csv | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to cloud folder |
| 2026-11-07T07:22:44.612045+00:00 | MOVE | pc | unknown | demo_workspace/sensitive/employee_salaries.csv | demo_workspace/unknown_dir/employee_salaries.csv | HIGH | R1 | Sensitive file moved outside approved location |
| 2026-11-07T07:22:46.446494+00:00 | COPY | pc | unknown | demo_workspace/sensitive/passwords_backup.txt | demo_workspace/network_share_sim/passwords_backup.txt | HIGH | R1,R2 | Sensitive file moved outside approved location; Sensitive file copied to network share |
| 2026-11-07T07:22:48.308197+00:00 | MODIFY | pc | unknown | demo_workspace/network_share_sim/passwords_backup.txt |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:22:50.160060+00:00 | MODIFY | pc | unknown | demo_workspace/sensitive/client_database.csv |  | CRITICAL | R3 | Integrity Failure: File hash mismatch detected |
| 2026-11-07T07:22:51.962515+00:00 | DELETE | pc | unknown | demo_workspace/sensitive/server.key |  | HIGH | R5 | Sensitive file deleted |
| 2026-11-07T07:22:53.952896+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_000.txt | demo_workspace/unknown_dir/bulk/tiny_000.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:53.953897+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_002.txt | demo_workspace/unknown_dir/bulk/tiny_002.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:53.955932+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_001.txt | demo_workspace/unknown_dir/bulk/tiny_001.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:53.957956+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_003.txt | demo_workspace/unknown_dir/bulk/tiny_003.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:54.770401+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_004.txt | demo_workspace/unknown_dir/bulk/tiny_004.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:54.772468+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_005.txt | demo_workspace/unknown_dir/bulk/tiny_005.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:54.775500+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_007.txt | demo_workspace/unknown_dir/bulk/tiny_007.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:54.777508+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_006.txt | demo_workspace/unknown_dir/bulk/tiny_006.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:55.583805+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_008.txt | demo_workspace/unknown_dir/bulk/tiny_008.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:55.586326+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_009.txt | demo_workspace/unknown_dir/bulk/tiny_009.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:55.590326+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_010.txt | demo_workspace/unknown_dir/bulk/tiny_010.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:55.591330+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_011.txt | demo_workspace/unknown_dir/bulk/tiny_011.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:56.402065+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_012.txt | demo_workspace/unknown_dir/bulk/tiny_012.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:56.404065+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_013.txt | demo_workspace/unknown_dir/bulk/tiny_013.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:56.409915+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_014.txt | demo_workspace/unknown_dir/bulk/tiny_014.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:56.411913+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_015.txt | demo_workspace/unknown_dir/bulk/tiny_015.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:57.215738+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_016.txt | demo_workspace/unknown_dir/bulk/tiny_016.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:57.222758+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_017.txt | demo_workspace/unknown_dir/bulk/tiny_017.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:57.227269+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_019.txt | demo_workspace/unknown_dir/bulk/tiny_019.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:57.229779+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_018.txt | demo_workspace/unknown_dir/bulk/tiny_018.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.033982+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_020.txt | demo_workspace/unknown_dir/bulk/tiny_020.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.038169+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_021.txt | demo_workspace/unknown_dir/bulk/tiny_021.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.041168+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_022.txt | demo_workspace/unknown_dir/bulk/tiny_022.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.041675+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_023.txt | demo_workspace/unknown_dir/bulk/tiny_023.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.850274+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_025.txt | demo_workspace/unknown_dir/bulk/tiny_025.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.856869+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_026.txt | demo_workspace/unknown_dir/bulk/tiny_026.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.858387+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_024.txt | demo_workspace/unknown_dir/bulk/tiny_024.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:58.860397+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_027.txt | demo_workspace/unknown_dir/bulk/tiny_027.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:59.662201+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_028.txt | demo_workspace/unknown_dir/bulk/tiny_028.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:59.674868+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_030.txt | demo_workspace/unknown_dir/bulk/tiny_030.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:59.675870+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_029.txt | demo_workspace/unknown_dir/bulk/tiny_029.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:22:59.678381+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_031.txt | demo_workspace/unknown_dir/bulk/tiny_031.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:00.477193+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_032.txt | demo_workspace/unknown_dir/bulk/tiny_032.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:00.492282+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_033.txt | demo_workspace/unknown_dir/bulk/tiny_033.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:00.498747+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_035.txt | demo_workspace/unknown_dir/bulk/tiny_035.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:00.505766+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_034.txt | demo_workspace/unknown_dir/bulk/tiny_034.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:01.292352+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_036.txt | demo_workspace/unknown_dir/bulk/tiny_036.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:01.306932+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_037.txt | demo_workspace/unknown_dir/bulk/tiny_037.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:01.309940+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_038.txt | demo_workspace/unknown_dir/bulk/tiny_038.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:01.315772+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_039.txt | demo_workspace/unknown_dir/bulk/tiny_039.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.106111+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_040.txt | demo_workspace/unknown_dir/bulk/tiny_040.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.117994+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_041.txt | demo_workspace/unknown_dir/bulk/tiny_041.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.120993+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_042.txt | demo_workspace/unknown_dir/bulk/tiny_042.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.126791+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_043.txt | demo_workspace/unknown_dir/bulk/tiny_043.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.921084+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_044.txt | demo_workspace/unknown_dir/bulk/tiny_044.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.929286+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_045.txt | demo_workspace/unknown_dir/bulk/tiny_045.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.934296+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_046.txt | demo_workspace/unknown_dir/bulk/tiny_046.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:02.937804+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_047.txt | demo_workspace/unknown_dir/bulk/tiny_047.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:03.732326+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_048.txt | demo_workspace/unknown_dir/bulk/tiny_048.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:03.743126+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_049.txt | demo_workspace/unknown_dir/bulk/tiny_049.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:03.749674+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_050.txt | demo_workspace/unknown_dir/bulk/tiny_050.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:03.751925+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_051.txt | demo_workspace/unknown_dir/bulk/tiny_051.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:04.547502+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_052.txt | demo_workspace/unknown_dir/bulk/tiny_052.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:04.553024+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_053.txt | demo_workspace/unknown_dir/bulk/tiny_053.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:04.561607+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_054.txt | demo_workspace/unknown_dir/bulk/tiny_054.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:04.562609+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_055.txt | demo_workspace/unknown_dir/bulk/tiny_055.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:05.358376+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_056.txt | demo_workspace/unknown_dir/bulk/tiny_056.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:05.363827+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_057.txt | demo_workspace/unknown_dir/bulk/tiny_057.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:05.374933+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_058.txt | demo_workspace/unknown_dir/bulk/tiny_058.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:05.375938+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_059.txt | demo_workspace/unknown_dir/bulk/tiny_059.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:06.169287+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_060.txt | demo_workspace/unknown_dir/bulk/tiny_060.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:06.174803+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_061.txt | demo_workspace/unknown_dir/bulk/tiny_061.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:06.194987+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_062.txt | demo_workspace/unknown_dir/bulk/tiny_062.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:06.194987+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_063.txt | demo_workspace/unknown_dir/bulk/tiny_063.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:06.989643+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_064.txt | demo_workspace/unknown_dir/bulk/tiny_064.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:06.991643+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_065.txt | demo_workspace/unknown_dir/bulk/tiny_065.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:07.010390+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_066.txt | demo_workspace/unknown_dir/bulk/tiny_066.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:07.011389+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_067.txt | demo_workspace/unknown_dir/bulk/tiny_067.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:07.801594+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_068.txt | demo_workspace/unknown_dir/bulk/tiny_068.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:07.802594+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_069.txt | demo_workspace/unknown_dir/bulk/tiny_069.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:07.823644+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_070.txt | demo_workspace/unknown_dir/bulk/tiny_070.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:07.823644+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_071.txt | demo_workspace/unknown_dir/bulk/tiny_071.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:08.612214+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_072.txt | demo_workspace/unknown_dir/bulk/tiny_072.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:08.615244+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_073.txt | demo_workspace/unknown_dir/bulk/tiny_073.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:08.637171+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_075.txt | demo_workspace/unknown_dir/bulk/tiny_075.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:08.638200+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_074.txt | demo_workspace/unknown_dir/bulk/tiny_074.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:09.430726+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_076.txt | demo_workspace/unknown_dir/bulk/tiny_076.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:09.430726+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_077.txt | demo_workspace/unknown_dir/bulk/tiny_077.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:09.448944+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_078.txt | demo_workspace/unknown_dir/bulk/tiny_078.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:09.448944+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_079.txt | demo_workspace/unknown_dir/bulk/tiny_079.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:10.240955+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_080.txt | demo_workspace/unknown_dir/bulk/tiny_080.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:10.264827+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_081.txt | demo_workspace/unknown_dir/bulk/tiny_081.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:10.268331+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_083.txt | demo_workspace/unknown_dir/bulk/tiny_083.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:10.268331+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_082.txt | demo_workspace/unknown_dir/bulk/tiny_082.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.052566+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_084.txt | demo_workspace/unknown_dir/bulk/tiny_084.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.077371+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_085.txt | demo_workspace/unknown_dir/bulk/tiny_085.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.080876+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_086.txt | demo_workspace/unknown_dir/bulk/tiny_086.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.082881+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_087.txt | demo_workspace/unknown_dir/bulk/tiny_087.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.868214+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_088.txt | demo_workspace/unknown_dir/bulk/tiny_088.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.892334+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_089.txt | demo_workspace/unknown_dir/bulk/tiny_089.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.895842+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_090.txt | demo_workspace/unknown_dir/bulk/tiny_090.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:11.900353+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_091.txt | demo_workspace/unknown_dir/bulk/tiny_091.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:12.678771+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_092.txt | demo_workspace/unknown_dir/bulk/tiny_092.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:12.705619+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_093.txt | demo_workspace/unknown_dir/bulk/tiny_093.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:12.712646+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_094.txt | demo_workspace/unknown_dir/bulk/tiny_094.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:12.715159+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_095.txt | demo_workspace/unknown_dir/bulk/tiny_095.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:13.490216+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_096.txt | demo_workspace/unknown_dir/bulk/tiny_096.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:13.518635+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_097.txt | demo_workspace/unknown_dir/bulk/tiny_097.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:13.527682+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_098.txt | demo_workspace/unknown_dir/bulk/tiny_098.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:13.528678+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_099.txt | demo_workspace/unknown_dir/bulk/tiny_099.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:14.301962+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_100.txt | demo_workspace/unknown_dir/bulk/tiny_100.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:14.328202+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_101.txt | demo_workspace/unknown_dir/bulk/tiny_101.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:14.344973+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_102.txt | demo_workspace/unknown_dir/bulk/tiny_102.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:14.344973+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_103.txt | demo_workspace/unknown_dir/bulk/tiny_103.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:15.112183+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_104.txt | demo_workspace/unknown_dir/bulk/tiny_104.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:15.138501+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_105.txt | demo_workspace/unknown_dir/bulk/tiny_105.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:15.161594+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_106.txt | demo_workspace/unknown_dir/bulk/tiny_106.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:15.926338+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_108.txt | demo_workspace/unknown_dir/bulk/tiny_108.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:15.927842+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_107.txt | demo_workspace/unknown_dir/bulk/tiny_107.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:15.947907+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_109.txt | demo_workspace/unknown_dir/bulk/tiny_109.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:16.738444+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_110.txt | demo_workspace/unknown_dir/bulk/tiny_110.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:16.739445+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_111.txt | demo_workspace/unknown_dir/bulk/tiny_111.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:16.762465+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_113.txt | demo_workspace/unknown_dir/bulk/tiny_113.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:16.762465+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_112.txt | demo_workspace/unknown_dir/bulk/tiny_112.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:17.552750+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_114.txt | demo_workspace/unknown_dir/bulk/tiny_114.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:17.552750+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_115.txt | demo_workspace/unknown_dir/bulk/tiny_115.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:17.575275+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_116.txt | demo_workspace/unknown_dir/bulk/tiny_116.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:18.366208+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_118.txt | demo_workspace/unknown_dir/bulk/tiny_118.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:18.366208+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_117.txt | demo_workspace/unknown_dir/bulk/tiny_117.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:18.388566+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_119.txt | demo_workspace/unknown_dir/bulk/tiny_119.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:18.388566+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_120.txt | demo_workspace/unknown_dir/bulk/tiny_120.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:19.180549+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_122.txt | demo_workspace/unknown_dir/bulk/tiny_122.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:19.181554+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_121.txt | demo_workspace/unknown_dir/bulk/tiny_121.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:19.201539+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_123.txt | demo_workspace/unknown_dir/bulk/tiny_123.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:19.202540+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_124.txt | demo_workspace/unknown_dir/bulk/tiny_124.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:19.997315+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_125.txt | demo_workspace/unknown_dir/bulk/tiny_125.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:19.999321+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_126.txt | demo_workspace/unknown_dir/bulk/tiny_126.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:20.014861+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_128.txt | demo_workspace/unknown_dir/bulk/tiny_128.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:20.015862+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_127.txt | demo_workspace/unknown_dir/bulk/tiny_127.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:20.812525+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_129.txt | demo_workspace/unknown_dir/bulk/tiny_129.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:20.831699+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_130.txt | demo_workspace/unknown_dir/bulk/tiny_130.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:20.833701+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_131.txt | demo_workspace/unknown_dir/bulk/tiny_131.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:20.834854+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_132.txt | demo_workspace/unknown_dir/bulk/tiny_132.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:21.626534+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_133.txt | demo_workspace/unknown_dir/bulk/tiny_133.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:21.646075+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_135.txt | demo_workspace/unknown_dir/bulk/tiny_135.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:21.653986+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_134.txt | demo_workspace/unknown_dir/bulk/tiny_134.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:21.655183+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_136.txt | demo_workspace/unknown_dir/bulk/tiny_136.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:22.437750+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_137.txt | demo_workspace/unknown_dir/bulk/tiny_137.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:22.461945+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_138.txt | demo_workspace/unknown_dir/bulk/tiny_138.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:22.470103+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_139.txt | demo_workspace/unknown_dir/bulk/tiny_139.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:22.471103+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_140.txt | demo_workspace/unknown_dir/bulk/tiny_140.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:23.249310+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_141.txt | demo_workspace/unknown_dir/bulk/tiny_141.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:23.277057+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_142.txt | demo_workspace/unknown_dir/bulk/tiny_142.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:23.287747+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_144.txt | demo_workspace/unknown_dir/bulk/tiny_144.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:23.290747+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_143.txt | demo_workspace/unknown_dir/bulk/tiny_143.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.067991+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_145.txt | demo_workspace/unknown_dir/bulk/tiny_145.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.091117+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_146.txt | demo_workspace/unknown_dir/bulk/tiny_146.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.102146+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_147.txt | demo_workspace/unknown_dir/bulk/tiny_147.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.104146+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_148.txt | demo_workspace/unknown_dir/bulk/tiny_148.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.879782+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_149.txt | demo_workspace/unknown_dir/bulk/tiny_149.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.903889+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_150.txt | demo_workspace/unknown_dir/bulk/tiny_150.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.918922+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_151.txt | demo_workspace/unknown_dir/bulk/tiny_151.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:24.921922+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_152.txt | demo_workspace/unknown_dir/bulk/tiny_152.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:25.694327+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_153.txt | demo_workspace/unknown_dir/bulk/tiny_153.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:25.719634+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_154.txt | demo_workspace/unknown_dir/bulk/tiny_154.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:25.734957+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_155.txt | demo_workspace/unknown_dir/bulk/tiny_155.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:25.736961+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_156.txt | demo_workspace/unknown_dir/bulk/tiny_156.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:26.519448+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_157.txt | demo_workspace/unknown_dir/bulk/tiny_157.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:26.536974+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_158.txt | demo_workspace/unknown_dir/bulk/tiny_158.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:26.557488+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_160.txt | demo_workspace/unknown_dir/bulk/tiny_160.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:26.558745+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_159.txt | demo_workspace/unknown_dir/bulk/tiny_159.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:27.338122+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_161.txt | demo_workspace/unknown_dir/bulk/tiny_161.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:27.348629+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_162.txt | demo_workspace/unknown_dir/bulk/tiny_162.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:27.370006+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_163.txt | demo_workspace/unknown_dir/bulk/tiny_163.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:27.371007+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_164.txt | demo_workspace/unknown_dir/bulk/tiny_164.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.151777+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_165.txt | demo_workspace/unknown_dir/bulk/tiny_165.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.158897+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_166.txt | demo_workspace/unknown_dir/bulk/tiny_166.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.182314+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_167.txt | demo_workspace/unknown_dir/bulk/tiny_167.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.183314+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_168.txt | demo_workspace/unknown_dir/bulk/tiny_168.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.963313+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_169.txt | demo_workspace/unknown_dir/bulk/tiny_169.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.969852+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_170.txt | demo_workspace/unknown_dir/bulk/tiny_170.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:28.999574+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_171.txt | demo_workspace/unknown_dir/bulk/tiny_171.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:29.001576+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_172.txt | demo_workspace/unknown_dir/bulk/tiny_172.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:29.777170+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_173.txt | demo_workspace/unknown_dir/bulk/tiny_173.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:29.792693+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_174.txt | demo_workspace/unknown_dir/bulk/tiny_174.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:29.812249+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_175.txt | demo_workspace/unknown_dir/bulk/tiny_175.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:29.815250+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_176.txt | demo_workspace/unknown_dir/bulk/tiny_176.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:30.589705+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_177.txt | demo_workspace/unknown_dir/bulk/tiny_177.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:30.610855+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_178.txt | demo_workspace/unknown_dir/bulk/tiny_178.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:30.637890+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_179.txt | demo_workspace/unknown_dir/bulk/tiny_179.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:30.639890+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_180.txt | demo_workspace/unknown_dir/bulk/tiny_180.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:31.399489+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_181.txt | demo_workspace/unknown_dir/bulk/tiny_181.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:31.427378+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_182.txt | demo_workspace/unknown_dir/bulk/tiny_182.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:31.454936+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_183.txt | demo_workspace/unknown_dir/bulk/tiny_183.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:31.455935+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_184.txt | demo_workspace/unknown_dir/bulk/tiny_184.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:32.214390+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_185.txt | demo_workspace/unknown_dir/bulk/tiny_185.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:32.241390+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_186.txt | demo_workspace/unknown_dir/bulk/tiny_186.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:32.269120+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_187.txt | demo_workspace/unknown_dir/bulk/tiny_187.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:32.272128+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_188.txt | demo_workspace/unknown_dir/bulk/tiny_188.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.026262+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_189.txt | demo_workspace/unknown_dir/bulk/tiny_189.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.054277+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_190.txt | demo_workspace/unknown_dir/bulk/tiny_190.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.093308+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_191.txt | demo_workspace/unknown_dir/bulk/tiny_191.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.094306+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_192.txt | demo_workspace/unknown_dir/bulk/tiny_192.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.838808+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_193.txt | demo_workspace/unknown_dir/bulk/tiny_193.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.866845+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_194.txt | demo_workspace/unknown_dir/bulk/tiny_194.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.912511+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_195.txt | demo_workspace/unknown_dir/bulk/tiny_195.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:33.913511+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_196.txt | demo_workspace/unknown_dir/bulk/tiny_196.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:34.662935+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_197.txt | demo_workspace/unknown_dir/bulk/tiny_197.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:34.679949+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_198.txt | demo_workspace/unknown_dir/bulk/tiny_198.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:34.722998+00:00 | CREATE | pc | unknown | demo_workspace/unknown_dir/bulk/tiny_199.txt | demo_workspace/unknown_dir/bulk/tiny_199.txt | INFO | R0 | File activity recorded |
| 2026-11-07T07:23:34.722998+00:00 | BULK | pc | unknown |  | demo_workspace/unknown_dir/bulk/tiny_199.txt | HIGH | R4 | Suspicious movement: 200 files transferred to unknown directory |

## Conclusion
The monitor recorded 210 events and 8 rule findings. Review high and critical findings, then retain this report with the JSONL audit log.
