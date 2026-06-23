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

> **Last Updated (Sri Lanka Time):** `2026-06-24 12:56:05 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 250 Rows | 12.06 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 258 Rows | 11.04 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 257 Rows | 10.88 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 257 Rows | 10.61 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 257 Rows | 10.93 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 257 Rows | 11.63 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 248 Rows | 9.66 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 257 Rows | 11.85 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1776 Rows | 67.92 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1664 Rows | 67.97 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1783 Rows | 66.45 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 961 Rows | 31.76 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1777 Rows | 67.96 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 935 Rows | 34.75 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-24 12:56:05 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (95/250)<br>**6** (93/250)<br>**0** (90/250)<br>**2** (89/250)<br>**7** (88/250) | **N** (15/250)<br>**Q** (15/250)<br>**J** (15/250)<br>**D** (14/250)<br>**Y** (13/250) |
| **Dhana Nidhanaya** | **9** (25/258)<br>**28** (24/258)<br>**6** (21/258)<br>**7** (21/258)<br>**4** (20/258) | **U** (17/258)<br>**F** (14/258)<br>**W** (13/258)<br>**Z** (12/258)<br>**T** (12/258) |
| **Govisetha** | **55** (21/257)<br>**10** (20/257)<br>**23** (20/257)<br>**44** (19/257)<br>**29** (19/257) | **P** (15/257)<br>**C** (14/257)<br>**D** (12/257)<br>**O** (12/257)<br>**M** (12/257) |
| **Handahana** | **58** (26/257)<br>**21** (25/257)<br>**6** (25/257)<br>**11** (23/257)<br>**55** (23/257) | N/A |
| **Mahajana Sampatha** | **2** (127/257)<br>**1** (127/257)<br>**5** (126/257)<br>**6** (126/257)<br>**4** (123/257) | **Q** (15/257)<br>**J** (15/257)<br>**N** (14/257)<br>**D** (14/257)<br>**Y** (13/257) |
| **Mega Power** | **11** (35/257)<br>**3** (30/257)<br>**13** (29/257)<br>**22** (28/257)<br>**19** (28/257) | **V** (18/257)<br>**T** (16/257)<br>**U** (16/257)<br>**K** (15/257)<br>**J** (14/257) |
| **Nlb Jaya** | **5** (110/248)<br>**3** (96/248)<br>**0** (95/248)<br>**2** (93/248)<br>**1** (88/248) | **T** (15/248)<br>**G** (15/248)<br>**P** (14/248)<br>**I** (14/248)<br>**Y** (14/248) |
| **Suba Dawasak** | **3** (107/257)<br>**4** (104/257)<br>**1** (102/257)<br>**9** (95/257)<br>**5** (92/257) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1776)<br>**20** (117/1776)<br>**57** (116/1776)<br>**75** (110/1776)<br>**38** (109/1776) | **B** (82/1776)<br>**R** (79/1776)<br>**P** (79/1776)<br>**M** (79/1776)<br>**I** (76/1776) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1664)<br>**10** (142/1664)<br>**27** (137/1664)<br>**29** (136/1664)<br>**21** (136/1664) | **H** (88/1664)<br>**U** (77/1664)<br>**M** (72/1664)<br>**X** (72/1664)<br>**W** (72/1664) |
| **Lagna Wasana** | **28** (136/1783)<br>**5** (135/1783)<br>**36** (133/1783)<br>**23** (132/1783)<br>**2** (131/1783) | N/A |
| **Sasiri** | **9** (73/961)<br>**20** (71/961)<br>**26** (71/961)<br>**22** (70/961)<br>**5** (67/961) | N/A |
| **Super Ball** | **45** (110/1777)<br>**52** (108/1777)<br>**74** (107/1777)<br>**3** (106/1777)<br>**57** (106/1777) | **I** (90/1777)<br>**D** (81/1777)<br>**V** (80/1777)<br>**T** (79/1777)<br>**A** (79/1777) |
| **Supiri Dhana Sampatha** | **2** (472/935)<br>**0** (471/935)<br>**3** (468/935)<br>**7** (458/935)<br>**5** (448/935) | **K** (46/935)<br>**V** (46/935)<br>**S** (43/935)<br>**M** (43/935)<br>**T** (43/935) |

