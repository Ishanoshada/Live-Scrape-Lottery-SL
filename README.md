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

> **Last Updated (Sri Lanka Time):** `2026-09-10 01:26:29 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 328 Rows | 15.75 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 336 Rows | 14.35 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 335 Rows | 14.12 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 335 Rows | 13.76 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 335 Rows | 14.18 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 335 Rows | 15.08 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 326 Rows | 12.68 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 335 Rows | 15.39 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1854 Rows | 70.91 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1742 Rows | 71.19 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1861 Rows | 69.36 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1039 Rows | 34.44 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1855 Rows | 70.94 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1013 Rows | 37.67 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-10 01:26:29 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (121/328)<br>**2** (119/328)<br>**6** (114/328)<br>**8** (113/328)<br>**4** (113/328) | **D** (19/328)<br>**J** (19/328)<br>**G** (18/328)<br>**W** (18/328)<br>**N** (17/328) |
| **Dhana Nidhanaya** | **9** (32/336)<br>**4** (30/336)<br>**7** (28/336)<br>**28** (26/336)<br>**3** (26/336) | **U** (20/336)<br>**F** (18/336)<br>**W** (18/336)<br>**M** (18/336)<br>**Z** (17/336) |
| **Govisetha** | **55** (27/335)<br>**10** (26/335)<br>**44** (25/335)<br>**29** (24/335)<br>**33** (24/335) | **P** (19/335)<br>**C** (18/335)<br>**X** (17/335)<br>**K** (16/335)<br>**W** (15/335) |
| **Handahana** | **58** (32/335)<br>**11** (31/335)<br>**55** (31/335)<br>**6** (30/335)<br>**21** (29/335) | N/A |
| **Mahajana Sampatha** | **5** (167/335)<br>**1** (166/335)<br>**2** (165/335)<br>**7** (162/335)<br>**4** (161/335) | **D** (19/335)<br>**J** (19/335)<br>**W** (19/335)<br>**G** (18/335)<br>**Q** (17/335) |
| **Mega Power** | **11** (39/335)<br>**26** (37/335)<br>**3** (36/335)<br>**13** (35/335)<br>**6** (34/335) | **T** (22/335)<br>**V** (22/335)<br>**U** (20/335)<br>**K** (18/335)<br>**J** (17/335) |
| **Nlb Jaya** | **5** (141/326)<br>**0** (128/326)<br>**3** (126/326)<br>**2** (125/326)<br>**7** (118/326) | **I** (18/326)<br>**T** (18/326)<br>**G** (17/326)<br>**O** (17/326)<br>**H** (16/326) |
| **Suba Dawasak** | **3** (135/335)<br>**4** (135/335)<br>**9** (127/335)<br>**1** (126/335)<br>**8** (126/335) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1854)<br>**20** (121/1854)<br>**57** (121/1854)<br>**38** (118/1854)<br>**75** (114/1854) | **B** (88/1854)<br>**R** (84/1854)<br>**M** (82/1854)<br>**P** (80/1854)<br>**N** (79/1854) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1742)<br>**10** (147/1742)<br>**6** (144/1742)<br>**29** (144/1742)<br>**21** (143/1742) | **H** (89/1742)<br>**U** (80/1742)<br>**M** (78/1742)<br>**G** (76/1742)<br>**D** (75/1742) |
| **Lagna Wasana** | **5** (142/1861)<br>**23** (140/1861)<br>**39** (138/1861)<br>**36** (138/1861)<br>**28** (138/1861) | N/A |
| **Sasiri** | **9** (80/1039)<br>**22** (78/1039)<br>**20** (77/1039)<br>**26** (77/1039)<br>**19** (74/1039) | N/A |
| **Super Ball** | **52** (112/1855)<br>**9** (112/1855)<br>**45** (112/1855)<br>**29** (112/1855)<br>**62** (110/1855) | **I** (93/1855)<br>**V** (83/1855)<br>**T** (83/1855)<br>**D** (82/1855)<br>**A** (81/1855) |
| **Supiri Dhana Sampatha** | **0** (509/1013)<br>**2** (508/1013)<br>**3** (501/1013)<br>**7** (500/1013)<br>**5** (483/1013) | **V** (54/1013)<br>**K** (47/1013)<br>**S** (46/1013)<br>**G** (46/1013)<br>**T** (46/1013) |

