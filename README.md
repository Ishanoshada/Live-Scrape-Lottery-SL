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

> **Last Updated (Sri Lanka Time):** `2026-09-03 01:29:40 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 321 Rows | 15.40 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 329 Rows | 14.03 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 328 Rows | 13.80 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 328 Rows | 13.45 KB |
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
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1847 Rows | 70.64 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1735 Rows | 70.90 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1854 Rows | 69.10 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1032 Rows | 34.20 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1848 Rows | 70.67 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1006 Rows | 37.41 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-03 01:29:40 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (119/321)<br>**2** (116/321)<br>**3** (112/321)<br>**6** (111/321)<br>**7** (111/321) | **D** (19/321)<br>**J** (19/321)<br>**G** (18/321)<br>**N** (17/321)<br>**Q** (17/321) |
| **Dhana Nidhanaya** | **9** (32/329)<br>**4** (30/329)<br>**7** (28/329)<br>**28** (26/329)<br>**3** (26/329) | **U** (20/329)<br>**F** (18/329)<br>**W** (18/329)<br>**M** (18/329)<br>**Z** (16/329) |
| **Govisetha** | **55** (27/328)<br>**10** (25/328)<br>**44** (24/328)<br>**29** (24/328)<br>**23** (23/328) | **P** (18/328)<br>**C** (18/328)<br>**X** (17/328)<br>**K** (16/328)<br>**D** (14/328) |
| **Handahana** | **58** (32/328)<br>**11** (31/328)<br>**55** (29/328)<br>**6** (29/328)<br>**16** (28/328) | N/A |
| **Mahajana Sampatha** | **5** (164/328)<br>**2** (162/328)<br>**7** (161/328)<br>**1** (160/328)<br>**4** (158/328) | **D** (19/328)<br>**J** (19/328)<br>**G** (18/328)<br>**W** (18/328)<br>**Q** (17/328) |
| **Mega Power** | **11** (38/328)<br>**26** (37/328)<br>**3** (36/328)<br>**13** (35/328)<br>**6** (33/328) | **T** (22/328)<br>**V** (21/328)<br>**U** (20/328)<br>**K** (18/328)<br>**J** (17/328) |
| **Nlb Jaya** | **5** (139/319)<br>**0** (125/319)<br>**3** (123/319)<br>**2** (123/319)<br>**7** (114/319) | **I** (18/319)<br>**T** (18/319)<br>**G** (17/319)<br>**O** (17/319)<br>**H** (16/319) |
| **Suba Dawasak** | **3** (134/328)<br>**4** (132/328)<br>**1** (124/328)<br>**9** (124/328)<br>**8** (123/328) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1847)<br>**20** (121/1847)<br>**57** (119/1847)<br>**38** (116/1847)<br>**75** (114/1847) | **B** (87/1847)<br>**R** (84/1847)<br>**M** (81/1847)<br>**P** (80/1847)<br>**N** (79/1847) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1735)<br>**10** (146/1735)<br>**29** (143/1735)<br>**15** (143/1735)<br>**6** (142/1735) | **H** (89/1735)<br>**U** (79/1735)<br>**M** (77/1735)<br>**D** (75/1735)<br>**G** (75/1735) |
| **Lagna Wasana** | **5** (142/1854)<br>**23** (139/1854)<br>**39** (138/1854)<br>**36** (137/1854)<br>**28** (137/1854) | N/A |
| **Sasiri** | **9** (80/1032)<br>**22** (77/1032)<br>**20** (77/1032)<br>**26** (76/1032)<br>**19** (74/1032) | N/A |
| **Super Ball** | **9** (112/1848)<br>**52** (111/1848)<br>**45** (111/1848)<br>**29** (111/1848)<br>**74** (109/1848) | **I** (93/1848)<br>**V** (82/1848)<br>**T** (82/1848)<br>**D** (82/1848)<br>**A** (81/1848) |
| **Supiri Dhana Sampatha** | **2** (505/1006)<br>**0** (504/1006)<br>**3** (498/1006)<br>**7** (495/1006)<br>**5** (481/1006) | **V** (53/1006)<br>**K** (47/1006)<br>**S** (46/1006)<br>**G** (46/1006)<br>**T** (45/1006) |

