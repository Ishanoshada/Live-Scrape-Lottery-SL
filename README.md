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

> **Last Updated (Sri Lanka Time):** `2026-09-04 01:31:14 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 322 Rows | 15.45 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 330 Rows | 14.08 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 329 Rows | 13.85 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 329 Rows | 13.50 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 328 Rows | 13.86 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 328 Rows | 14.75 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 319 Rows | 12.39 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 328 Rows | 15.04 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1848 Rows | 70.68 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1736 Rows | 70.94 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1855 Rows | 69.13 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1033 Rows | 34.23 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1849 Rows | 70.71 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1007 Rows | 37.45 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-04 01:31:14 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (120/322)<br>**2** (116/322)<br>**3** (112/322)<br>**6** (111/322)<br>**8** (111/322) | **D** (19/322)<br>**J** (19/322)<br>**G** (18/322)<br>**W** (18/322)<br>**N** (17/322) |
| **Dhana Nidhanaya** | **9** (32/330)<br>**4** (30/330)<br>**7** (28/330)<br>**28** (26/330)<br>**3** (26/330) | **U** (20/330)<br>**F** (18/330)<br>**W** (18/330)<br>**M** (18/330)<br>**Z** (16/330) |
| **Govisetha** | **55** (27/329)<br>**10** (25/329)<br>**44** (24/329)<br>**29** (24/329)<br>**23** (23/329) | **P** (18/329)<br>**C** (18/329)<br>**X** (17/329)<br>**K** (16/329)<br>**W** (15/329) |
| **Handahana** | **58** (32/329)<br>**11** (31/329)<br>**55** (29/329)<br>**6** (29/329)<br>**16** (28/329) | N/A |
| **Mahajana Sampatha** | **5** (164/328)<br>**2** (162/328)<br>**7** (161/328)<br>**1** (160/328)<br>**3** (158/328) | **D** (19/328)<br>**J** (19/328)<br>**G** (18/328)<br>**W** (18/328)<br>**Q** (17/328) |
| **Mega Power** | **11** (38/328)<br>**26** (37/328)<br>**3** (36/328)<br>**13** (35/328)<br>**6** (33/328) | **T** (22/328)<br>**V** (21/328)<br>**U** (20/328)<br>**K** (18/328)<br>**J** (17/328) |
| **Nlb Jaya** | **5** (139/319)<br>**0** (125/319)<br>**3** (123/319)<br>**2** (123/319)<br>**7** (114/319) | **I** (18/319)<br>**T** (18/319)<br>**G** (17/319)<br>**O** (17/319)<br>**H** (16/319) |
| **Suba Dawasak** | **3** (134/328)<br>**4** (132/328)<br>**1** (124/328)<br>**9** (124/328)<br>**8** (123/328) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1848)<br>**20** (121/1848)<br>**57** (119/1848)<br>**38** (116/1848)<br>**75** (114/1848) | **B** (87/1848)<br>**R** (84/1848)<br>**M** (81/1848)<br>**P** (80/1848)<br>**N** (79/1848) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1736)<br>**10** (146/1736)<br>**6** (143/1736)<br>**29** (143/1736)<br>**15** (143/1736) | **H** (89/1736)<br>**U** (79/1736)<br>**M** (77/1736)<br>**D** (75/1736)<br>**G** (75/1736) |
| **Lagna Wasana** | **5** (142/1855)<br>**23** (139/1855)<br>**39** (138/1855)<br>**36** (138/1855)<br>**28** (138/1855) | N/A |
| **Sasiri** | **9** (80/1033)<br>**22** (77/1033)<br>**20** (77/1033)<br>**26** (76/1033)<br>**19** (74/1033) | N/A |
| **Super Ball** | **9** (112/1849)<br>**45** (112/1849)<br>**29** (112/1849)<br>**52** (111/1849)<br>**74** (109/1849) | **I** (93/1849)<br>**V** (82/1849)<br>**T** (82/1849)<br>**D** (82/1849)<br>**A** (81/1849) |
| **Supiri Dhana Sampatha** | **2** (505/1007)<br>**0** (505/1007)<br>**3** (498/1007)<br>**7** (496/1007)<br>**5** (482/1007) | **V** (53/1007)<br>**K** (47/1007)<br>**S** (46/1007)<br>**G** (46/1007)<br>**T** (46/1007) |

