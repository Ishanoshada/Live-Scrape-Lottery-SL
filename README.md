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

> **Last Updated (Sri Lanka Time):** `2026-09-07 12:54:08 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 325 Rows | 15.60 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 333 Rows | 14.21 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 332 Rows | 13.98 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 332 Rows | 13.63 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 332 Rows | 14.04 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 332 Rows | 14.94 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 323 Rows | 12.55 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 332 Rows | 15.24 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1851 Rows | 70.79 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1739 Rows | 71.06 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1858 Rows | 69.24 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1036 Rows | 34.33 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1852 Rows | 70.83 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1010 Rows | 37.56 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-07 12:54:08 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (120/325)<br>**2** (118/325)<br>**6** (113/325)<br>**3** (112/325)<br>**8** (112/325) | **D** (19/325)<br>**J** (19/325)<br>**G** (18/325)<br>**W** (18/325)<br>**N** (17/325) |
| **Dhana Nidhanaya** | **9** (32/333)<br>**4** (30/333)<br>**7** (28/333)<br>**28** (26/333)<br>**3** (26/333) | **U** (20/333)<br>**F** (18/333)<br>**W** (18/333)<br>**M** (18/333)<br>**Z** (17/333) |
| **Govisetha** | **55** (27/332)<br>**10** (26/332)<br>**44** (24/332)<br>**29** (24/332)<br>**23** (23/332) | **P** (18/332)<br>**C** (18/332)<br>**X** (17/332)<br>**K** (16/332)<br>**W** (15/332) |
| **Handahana** | **58** (32/332)<br>**11** (31/332)<br>**55** (30/332)<br>**21** (29/332)<br>**6** (29/332) | N/A |
| **Mahajana Sampatha** | **5** (166/332)<br>**2** (164/332)<br>**1** (164/332)<br>**7** (161/332)<br>**3** (160/332) | **D** (19/332)<br>**J** (19/332)<br>**W** (19/332)<br>**G** (18/332)<br>**Q** (17/332) |
| **Mega Power** | **11** (39/332)<br>**26** (37/332)<br>**3** (36/332)<br>**13** (35/332)<br>**6** (34/332) | **T** (22/332)<br>**V** (22/332)<br>**U** (20/332)<br>**K** (18/332)<br>**J** (17/332) |
| **Nlb Jaya** | **5** (139/323)<br>**0** (127/323)<br>**3** (125/323)<br>**2** (124/323)<br>**7** (117/323) | **I** (18/323)<br>**T** (18/323)<br>**G** (17/323)<br>**O** (17/323)<br>**H** (16/323) |
| **Suba Dawasak** | **3** (135/332)<br>**4** (134/332)<br>**1** (126/332)<br>**9** (125/332)<br>**8** (124/332) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1851)<br>**20** (121/1851)<br>**57** (120/1851)<br>**38** (117/1851)<br>**75** (114/1851) | **B** (88/1851)<br>**R** (84/1851)<br>**M** (82/1851)<br>**P** (80/1851)<br>**N** (79/1851) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1739)<br>**10** (147/1739)<br>**6** (143/1739)<br>**29** (143/1739)<br>**15** (143/1739) | **H** (89/1739)<br>**U** (80/1739)<br>**M** (77/1739)<br>**D** (75/1739)<br>**G** (75/1739) |
| **Lagna Wasana** | **5** (142/1858)<br>**23** (140/1858)<br>**39** (138/1858)<br>**36** (138/1858)<br>**28** (138/1858) | N/A |
| **Sasiri** | **9** (80/1036)<br>**22** (77/1036)<br>**20** (77/1036)<br>**26** (76/1036)<br>**19** (74/1036) | N/A |
| **Super Ball** | **52** (112/1852)<br>**9** (112/1852)<br>**45** (112/1852)<br>**29** (112/1852)<br>**62** (109/1852) | **I** (93/1852)<br>**V** (83/1852)<br>**T** (82/1852)<br>**D** (82/1852)<br>**A** (81/1852) |
| **Supiri Dhana Sampatha** | **0** (508/1010)<br>**2** (507/1010)<br>**3** (500/1010)<br>**7** (497/1010)<br>**5** (482/1010) | **V** (53/1010)<br>**K** (47/1010)<br>**S** (46/1010)<br>**G** (46/1010)<br>**T** (46/1010) |

