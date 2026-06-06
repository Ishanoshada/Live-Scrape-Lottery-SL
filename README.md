# 🎰 Sri Lanka Lottery Results Archive (Automated)

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This repository provides a fully automated, up-to-date, and clean archive of lottery results from the **National Lottery Board (NLB)** and the **Development Lottery Board (DLB)** of Sri Lanka. 

All data extraction is powered by the official [srilanka-lottery](https://pypi.org/project/srilanka-lottery/) Python package.

---

## 📑 Table of Contents
* [🚀 Features & How It Works](#-features--how-it-works)
* [📁 Data Structure](#-data-structure)
* [🛠 Usage for Developers](#-usage-for-developers)
* [⚖️ License](#️-license)
* [👨‍💻 Author](#-author)
* [📊 Data Summary](#-data-summary)
* [📈 Lottery Data Analytic Report](#-lottery-data-analytic-report)

---

## 🚀 Features & How It Works

This repository is more than just a storage folder; it is a live, self-updating data pipeline.

1. **Scheduled Automation:** A GitHub Action is configured to run automatically every few hours to check for the latest lottery draw results from the official websites.
2. **Robust Extraction:** Data is scraped securely using the `srilanka-lottery` package, handling sessions and cookies automatically.
3. **Data Deduplication:** The scripts utilize set-based logic to ensure that no duplicate draws are ever recorded. The data remains clean and perfectly sorted by draw number.
4. **Live Analytics:** Every time new results are fetched, a secondary script analyzes the entire historical dataset to calculate the most frequently drawn numbers and letters (Frequency Analysis).
5. **Text-Based Storage:** Results are stored in lightweight `.txt` files, making it incredibly fast to read and process for data scientists and developers.

---

## 📁 Data Structure

The results are saved in a Comma-Separated Values (CSV) compatible text format. You can easily import these files into Excel, Pandas, or any database.

**Format:**
`Draw_Number, Date, Winning_Letter, Numbers...`

**Directory Layout:**
* `/nlb_txt`: Contains results for NLB lotteries (e.g., Mega Power, Mahajana Sampatha, Govisetha, Dhana Nidhanaya).
* `/dlb_txt`: Contains results for DLB lotteries (e.g., Ada Kotipathi, Jayoda, Lagna Wasana, Kapruka).

---

## 🛠 Usage for Developers

If you want to use this data in your own projects, you can fetch the raw text files directly from this repository via GitHub Raw URLs.

Alternatively, if you want to scrape live data directly in your own Python projects, install the core scraping package:

```bash
pip install srilanka-lottery
```

### Basic Example using the Package
```python
from srilanka_lottery import scrape_dlb_latest_results

results = scrape_dlb_latest_results("Ada Kotipathi", limit=5)
print(results)
```

---

## ⚖️ License
This project is licensed under the **MIT License** - meaning you are free to use, modify, and distribute this data and software for personal or commercial projects.

## 👨‍💻 Author
Developed and maintained by **Ishan Oshada**.
* **GitHub:** [@Ishanoshada](https://github.com/Ishanoshada)
* **PyPI Package:** [srilanka-lottery](https://pypi.org/project/srilanka-lottery/)




![Views](https://dynamic-repo-badges.vercel.app/svg/count/7/Repository%20Views/lotterylive2)



## 📊 Data Summary

> **Last Updated (Sri Lanka Time):** `2026-06-07 12:17:47 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 233 Rows | 11.28 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 241 Rows | 10.33 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 240 Rows | 10.20 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 240 Rows | 9.95 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 240 Rows | 10.25 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 240 Rows | 10.91 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 231 Rows | 9.02 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 240 Rows | 11.10 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1759 Rows | 67.27 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1647 Rows | 67.28 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1766 Rows | 65.82 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 944 Rows | 31.18 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1760 Rows | 67.31 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 918 Rows | 34.12 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-07 12:17:47 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (90/233)<br>**5** (86/233)<br>**7** (83/233)<br>**0** (82/233)<br>**2** (81/233) | **J** (15/233)<br>**N** (14/233)<br>**D** (14/233)<br>**Q** (13/233)<br>**Y** (12/233) |
| **Dhana Nidhanaya** | **28** (23/241)<br>**9** (23/241)<br>**6** (20/241)<br>**16** (20/241)<br>**7** (19/241) | **U** (15/241)<br>**W** (13/241)<br>**Z** (12/241)<br>**T** (12/241)<br>**M** (12/241) |
| **Govisetha** | **10** (20/240)<br>**44** (19/240)<br>**55** (19/240)<br>**33** (18/240)<br>**19** (17/240) | **P** (15/240)<br>**D** (12/240)<br>**O** (12/240)<br>**C** (12/240)<br>**W** (11/240) |
| **Handahana** | **6** (24/240)<br>**55** (23/240)<br>**11** (22/240)<br>**58** (22/240)<br>**61** (22/240) | N/A |
| **Mahajana Sampatha** | **1** (120/240)<br>**6** (119/240)<br>**5** (117/240)<br>**7** (116/240)<br>**2** (116/240) | **J** (15/240)<br>**D** (14/240)<br>**N** (13/240)<br>**Q** (13/240)<br>**Y** (12/240) |
| **Mega Power** | **11** (30/240)<br>**3** (28/240)<br>**22** (27/240)<br>**13** (27/240)<br>**6** (26/240) | **V** (18/240)<br>**T** (14/240)<br>**K** (14/240)<br>**J** (13/240)<br>**U** (13/240) |
| **Nlb Jaya** | **5** (99/231)<br>**0** (91/231)<br>**3** (90/231)<br>**2** (86/231)<br>**1** (83/231) | **P** (14/231)<br>**I** (14/231)<br>**T** (14/231)<br>**M** (13/231)<br>**G** (13/231) |
| **Suba Dawasak** | **3** (100/240)<br>**4** (96/240)<br>**1** (95/240)<br>**9** (91/240)<br>**5** (90/240) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (118/1759)<br>**20** (115/1759)<br>**57** (115/1759)<br>**13** (109/1759)<br>**75** (108/1759) | **B** (82/1759)<br>**M** (79/1759)<br>**R** (78/1759)<br>**P** (78/1759)<br>**I** (75/1759) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1647)<br>**10** (142/1647)<br>**29** (134/1647)<br>**21** (134/1647)<br>**27** (134/1647) | **H** (88/1647)<br>**U** (76/1647)<br>**W** (72/1647)<br>**G** (71/1647)<br>**X** (71/1647) |
| **Lagna Wasana** | **28** (135/1766)<br>**5** (135/1766)<br>**36** (132/1766)<br>**23** (130/1766)<br>**25** (130/1766) | N/A |
| **Sasiri** | **9** (72/944)<br>**20** (70/944)<br>**22** (68/944)<br>**26** (68/944)<br>**19** (67/944) | N/A |
| **Super Ball** | **45** (109/1760)<br>**52** (107/1760)<br>**74** (107/1760)<br>**29** (106/1760)<br>**43** (106/1760) | **I** (87/1760)<br>**D** (81/1760)<br>**T** (79/1760)<br>**A** (78/1760)<br>**V** (77/1760) |
| **Supiri Dhana Sampatha** | **0** (467/918)<br>**2** (462/918)<br>**3** (460/918)<br>**7** (452/918)<br>**5** (437/918) | **K** (44/918)<br>**V** (44/918)<br>**S** (43/918)<br>**M** (43/918)<br>**T** (43/918) |

