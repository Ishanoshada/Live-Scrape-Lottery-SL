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

> **Last Updated (Sri Lanka Time):** `2026-09-11 01:26:15 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 329 Rows | 15.81 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 337 Rows | 14.40 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 336 Rows | 14.16 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 336 Rows | 13.80 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 336 Rows | 14.22 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 336 Rows | 15.13 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 327 Rows | 12.72 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 336 Rows | 15.44 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1855 Rows | 70.94 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1743 Rows | 71.23 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1862 Rows | 69.39 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1040 Rows | 34.47 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1856 Rows | 70.98 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1014 Rows | 37.71 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-11 01:26:15 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (121/329)<br>**2** (119/329)<br>**6** (115/329)<br>**8** (113/329)<br>**4** (113/329) | **D** (19/329)<br>**J** (19/329)<br>**Q** (18/329)<br>**G** (18/329)<br>**W** (18/329) |
| **Dhana Nidhanaya** | **9** (32/337)<br>**4** (30/337)<br>**7** (28/337)<br>**28** (26/337)<br>**3** (26/337) | **U** (20/337)<br>**F** (18/337)<br>**W** (18/337)<br>**M** (18/337)<br>**Z** (17/337) |
| **Govisetha** | **55** (27/336)<br>**10** (26/336)<br>**44** (25/336)<br>**29** (24/336)<br>**33** (24/336) | **P** (19/336)<br>**C** (18/336)<br>**X** (17/336)<br>**K** (16/336)<br>**W** (15/336) |
| **Handahana** | **58** (32/336)<br>**11** (31/336)<br>**55** (31/336)<br>**6** (30/336)<br>**21** (29/336) | N/A |
| **Mahajana Sampatha** | **5** (167/336)<br>**1** (166/336)<br>**2** (165/336)<br>**9** (162/336)<br>**7** (162/336) | **D** (19/336)<br>**J** (19/336)<br>**W** (19/336)<br>**Q** (18/336)<br>**G** (18/336) |
| **Mega Power** | **11** (40/336)<br>**26** (37/336)<br>**3** (36/336)<br>**13** (35/336)<br>**22** (34/336) | **T** (22/336)<br>**V** (22/336)<br>**U** (20/336)<br>**K** (18/336)<br>**J** (17/336) |
| **Nlb Jaya** | **5** (141/327)<br>**0** (128/327)<br>**3** (127/327)<br>**2** (126/327)<br>**7** (118/327) | **I** (18/327)<br>**T** (18/327)<br>**G** (17/327)<br>**O** (17/327)<br>**H** (16/327) |
| **Suba Dawasak** | **3** (135/336)<br>**4** (135/336)<br>**1** (127/336)<br>**9** (127/336)<br>**2** (127/336) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1855)<br>**20** (122/1855)<br>**57** (121/1855)<br>**38** (118/1855)<br>**75** (114/1855) | **B** (88/1855)<br>**R** (84/1855)<br>**M** (82/1855)<br>**P** (80/1855)<br>**N** (79/1855) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1743)<br>**10** (147/1743)<br>**6** (144/1743)<br>**29** (144/1743)<br>**21** (143/1743) | **H** (89/1743)<br>**U** (80/1743)<br>**M** (78/1743)<br>**G** (76/1743)<br>**D** (75/1743) |
| **Lagna Wasana** | **5** (142/1862)<br>**23** (140/1862)<br>**39** (138/1862)<br>**36** (138/1862)<br>**28** (138/1862) | N/A |
| **Sasiri** | **9** (80/1040)<br>**22** (78/1040)<br>**20** (77/1040)<br>**26** (77/1040)<br>**19** (74/1040) | N/A |
| **Super Ball** | **52** (112/1856)<br>**9** (112/1856)<br>**45** (112/1856)<br>**29** (112/1856)<br>**62** (110/1856) | **I** (93/1856)<br>**V** (83/1856)<br>**T** (83/1856)<br>**D** (82/1856)<br>**A** (81/1856) |
| **Supiri Dhana Sampatha** | **0** (509/1014)<br>**2** (508/1014)<br>**3** (502/1014)<br>**7** (500/1014)<br>**5** (484/1014) | **V** (54/1014)<br>**K** (47/1014)<br>**S** (46/1014)<br>**G** (46/1014)<br>**T** (46/1014) |

