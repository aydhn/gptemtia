*** WARNING / UYARI ***
Bu rapor offline scenario regression/deterministic replay çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler veya yatırım tavsiyesi değildir.
Golden outputlar gerçek piyasa performansı referansı değildir.
Snapshot diffler yatırım sinyali değildir.
Demo acceptance production acceptance değildir.
***

# Demo Acceptance Report

Score: 0.9230769230769231
Label: demo_accepted_offline

|    | checklist_item                                      | passed   |
|---:|:----------------------------------------------------|:---------|
|  0 | scenario registry mevcut                            | True     |
|  1 | synthetic sample data mevcut                        | True     |
|  2 | fixtures synthetic                                  | True     |
|  3 | expected outputs tanımlı                            | True     |
|  4 | golden outputs mevcut                               | True     |
|  5 | snapshots capture edildi                            | True     |
|  6 | deterministic replay çalıştı veya dry-run validated | False    |
|  7 | output contracts validated                          | True     |
|  8 | demo workflows safe                                 | True     |
|  9 | no live/broker/deploy/daemon commands               | True     |
| 10 | no investment advice language                       | True     |
| 11 | scenario reports saved                              | True     |
| 12 | quality report produced                             | True     |
