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

> **Last Updated (Sri Lanka Time):** `2026-09-13 01:03:15 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 331 Rows | 15.91 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 339 Rows | 14.49 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 338 Rows | 14.25 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 338 Rows | 13.89 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 338 Rows | 14.31 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 338 Rows | 15.23 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 329 Rows | 12.80 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 338 Rows | 15.54 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1857 Rows | 71.02 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1745 Rows | 71.31 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1864 Rows | 69.47 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1042 Rows | 34.54 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1858 Rows | 71.06 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1016 Rows | 37.79 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-13 01:03:15 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (123/331)<br>**2** (120/331)<br>**6** (115/331)<br>**1** (114/331)<br>**8** (113/331) | **D** (19/331)<br>**J** (19/331)<br>**Q** (18/331)<br>**G** (18/331)<br>**W** (18/331) |
| **Dhana Nidhanaya** | **9** (32/339)<br>**4** (30/339)<br>**7** (28/339)<br>**28** (26/339)<br>**3** (26/339) | **U** (20/339)<br>**Z** (18/339)<br>**F** (18/339)<br>**W** (18/339)<br>**M** (18/339) |
| **Govisetha** | **55** (27/338)<br>**10** (26/338)<br>**44** (25/338)<br>**29** (24/338)<br>**33** (24/338) | **P** (19/338)<br>**C** (18/338)<br>**X** (17/338)<br>**K** (16/338)<br>**W** (15/338) |
| **Handahana** | **58** (32/338)<br>**11** (31/338)<br>**55** (31/338)<br>**6** (30/338)<br>**21** (29/338) | N/A |
| **Mahajana Sampatha** | **5** (169/338)<br>**1** (168/338)<br>**2** (166/338)<br>**9** (164/338)<br>**7** (163/338) | **D** (19/338)<br>**J** (19/338)<br>**W** (19/338)<br>**Q** (18/338)<br>**G** (18/338) |
| **Mega Power** | **11** (40/338)<br>**26** (37/338)<br>**3** (36/338)<br>**13** (35/338)<br>**22** (34/338) | **T** (22/338)<br>**V** (22/338)<br>**U** (20/338)<br>**K** (18/338)<br>**J** (17/338) |
| **Nlb Jaya** | **5** (142/329)<br>**0** (129/329)<br>**3** (127/329)<br>**2** (127/329)<br>**7** (119/329) | **I** (18/329)<br>**T** (18/329)<br>**G** (17/329)<br>**O** (17/329)<br>**P** (16/329) |
| **Suba Dawasak** | **3** (137/338)<br>**4** (137/338)<br>**1** (129/338)<br>**8** (128/338)<br>**9** (127/338) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1857)<br>**20** (122/1857)<br>**57** (121/1857)<br>**38** (118/1857)<br>**75** (114/1857) | **B** (88/1857)<br>**R** (84/1857)<br>**M** (82/1857)<br>**P** (80/1857)<br>**N** (80/1857) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1745)<br>**10** (147/1745)<br>**6** (144/1745)<br>**29** (144/1745)<br>**21** (143/1745) | **H** (89/1745)<br>**U** (80/1745)<br>**M** (78/1745)<br>**G** (76/1745)<br>**D** (75/1745) |
| **Lagna Wasana** | **5** (142/1864)<br>**23** (141/1864)<br>**39** (138/1864)<br>**36** (138/1864)<br>**28** (138/1864) | N/A |
| **Sasiri** | **9** (80/1042)<br>**22** (78/1042)<br>**20** (77/1042)<br>**26** (77/1042)<br>**19** (74/1042) | N/A |
| **Super Ball** | **52** (112/1858)<br>**9** (112/1858)<br>**45** (112/1858)<br>**29** (112/1858)<br>**62** (110/1858) | **I** (93/1858)<br>**V** (83/1858)<br>**T** (83/1858)<br>**D** (82/1858)<br>**A** (81/1858) |
| **Supiri Dhana Sampatha** | **0** (511/1016)<br>**2** (509/1016)<br>**3** (502/1016)<br>**7** (501/1016)<br>**5** (484/1016) | **V** (54/1016)<br>**K** (47/1016)<br>**T** (47/1016)<br>**S** (46/1016)<br>**G** (46/1016) |

