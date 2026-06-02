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

> **Last Updated (Sri Lanka Time):** `2026-06-03 01:55:13 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 229 Rows | 11.09 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 237 Rows | 10.17 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 236 Rows | 10.04 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 236 Rows | 9.79 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 236 Rows | 10.09 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 236 Rows | 10.73 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 227 Rows | 8.88 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 236 Rows | 10.93 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1755 Rows | 67.12 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1643 Rows | 67.11 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1762 Rows | 65.67 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 940 Rows | 31.04 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1756 Rows | 67.16 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 914 Rows | 33.97 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-03 01:55:13 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (88/229)<br>**5** (84/229)<br>**2** (81/229)<br>**7** (80/229)<br>**4** (79/229) | **N** (14/229)<br>**D** (14/229)<br>**J** (14/229)<br>**Q** (13/229)<br>**Y** (12/229) |
| **Dhana Nidhanaya** | **28** (23/237)<br>**9** (23/237)<br>**6** (20/237)<br>**7** (19/237)<br>**16** (18/237) | **U** (15/237)<br>**W** (13/237)<br>**Z** (12/237)<br>**T** (12/237)<br>**M** (12/237) |
| **Govisetha** | **10** (20/236)<br>**44** (19/236)<br>**55** (18/236)<br>**33** (18/236)<br>**19** (17/236) | **P** (14/236)<br>**O** (12/236)<br>**D** (11/236)<br>**W** (11/236)<br>**K** (11/236) |
| **Handahana** | **58** (22/236)<br>**61** (22/236)<br>**21** (22/236)<br>**55** (22/236)<br>**6** (22/236) | N/A |
| **Mahajana Sampatha** | **1** (118/236)<br>**6** (117/236)<br>**2** (116/236)<br>**5** (115/236)<br>**4** (114/236) | **D** (14/236)<br>**J** (14/236)<br>**N** (13/236)<br>**Q** (13/236)<br>**Y** (12/236) |
| **Mega Power** | **11** (30/236)<br>**3** (28/236)<br>**22** (27/236)<br>**13** (27/236)<br>**6** (26/236) | **V** (17/236)<br>**T** (14/236)<br>**K** (14/236)<br>**U** (13/236)<br>**J** (12/236) |
| **Nlb Jaya** | **5** (99/227)<br>**0** (89/227)<br>**3** (88/227)<br>**2** (85/227)<br>**1** (81/227) | **P** (14/227)<br>**I** (14/227)<br>**T** (14/227)<br>**M** (13/227)<br>**G** (13/227) |
| **Suba Dawasak** | **3** (98/236)<br>**1** (94/236)<br>**4** (92/236)<br>**9** (88/236)<br>**5** (87/236) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (117/1755)<br>**57** (115/1755)<br>**20** (114/1755)<br>**13** (109/1755)<br>**75** (108/1755) | **B** (82/1755)<br>**M** (79/1755)<br>**R** (78/1755)<br>**P** (78/1755)<br>**I** (75/1755) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1643)<br>**10** (142/1643)<br>**29** (134/1643)<br>**21** (134/1643)<br>**22** (133/1643) | **H** (88/1643)<br>**U** (76/1643)<br>**W** (72/1643)<br>**G** (70/1643)<br>**X** (70/1643) |
| **Lagna Wasana** | **5** (135/1762)<br>**28** (134/1762)<br>**36** (131/1762)<br>**23** (130/1762)<br>**25** (130/1762) | N/A |
| **Sasiri** | **9** (72/940)<br>**20** (70/940)<br>**22** (68/940)<br>**26** (68/940)<br>**19** (67/940) | N/A |
| **Super Ball** | **45** (109/1756)<br>**74** (107/1756)<br>**52** (106/1756)<br>**29** (106/1756)<br>**43** (106/1756) | **I** (87/1756)<br>**D** (81/1756)<br>**T** (79/1756)<br>**V** (77/1756)<br>**A** (77/1756) |
| **Supiri Dhana Sampatha** | **0** (463/914)<br>**2** (460/914)<br>**3** (458/914)<br>**7** (450/914)<br>**5** (437/914) | **K** (44/914)<br>**V** (44/914)<br>**S** (43/914)<br>**M** (43/914)<br>**T** (43/914) |

