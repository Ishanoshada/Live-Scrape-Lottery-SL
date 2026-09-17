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

> **Last Updated (Sri Lanka Time):** `2026-09-18 01:58:32 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 336 Rows | 16.16 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 344 Rows | 14.71 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 343 Rows | 14.47 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 343 Rows | 14.11 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 343 Rows | 14.54 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 343 Rows | 15.46 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 334 Rows | 13.01 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 343 Rows | 15.78 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1862 Rows | 71.21 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1750 Rows | 71.52 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1869 Rows | 69.66 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1047 Rows | 34.71 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1863 Rows | 71.25 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1021 Rows | 37.98 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-18 01:58:32 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/336)<br>**2** (122/336)<br>**6** (117/336)<br>**4** (116/336)<br>**8** (114/336) | **D** (22/336)<br>**J** (19/336)<br>**N** (18/336)<br>**Q** (18/336)<br>**G** (18/336) |
| **Dhana Nidhanaya** | **9** (32/344)<br>**4** (30/344)<br>**7** (28/344)<br>**3** (27/344)<br>**28** (26/344) | **U** (20/344)<br>**W** (19/344)<br>**Z** (18/344)<br>**F** (18/344)<br>**M** (18/344) |
| **Govisetha** | **55** (28/343)<br>**10** (26/343)<br>**44** (25/343)<br>**29** (24/343)<br>**33** (24/343) | **P** (19/343)<br>**C** (18/343)<br>**X** (17/343)<br>**K** (16/343)<br>**I** (16/343) |
| **Handahana** | **58** (32/343)<br>**11** (31/343)<br>**55** (31/343)<br>**6** (30/343)<br>**60** (29/343) | N/A |
| **Mahajana Sampatha** | **5** (171/343)<br>**2** (170/343)<br>**1** (170/343)<br>**9** (165/343)<br>**4** (164/343) | **D** (22/343)<br>**J** (19/343)<br>**W** (19/343)<br>**Q** (18/343)<br>**G** (18/343) |
| **Mega Power** | **11** (40/343)<br>**3** (37/343)<br>**26** (37/343)<br>**13** (35/343)<br>**22** (34/343) | **T** (22/343)<br>**V** (22/343)<br>**U** (20/343)<br>**K** (18/343)<br>**J** (17/343) |
| **Nlb Jaya** | **5** (142/334)<br>**0** (130/334)<br>**3** (127/334)<br>**2** (127/334)<br>**7** (123/334) | **T** (20/334)<br>**I** (19/334)<br>**G** (18/334)<br>**O** (17/334)<br>**P** (16/334) |
| **Suba Dawasak** | **4** (140/343)<br>**3** (138/343)<br>**1** (130/343)<br>**8** (130/343)<br>**9** (130/343) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1862)<br>**20** (122/1862)<br>**57** (121/1862)<br>**38** (118/1862)<br>**75** (114/1862) | **B** (88/1862)<br>**R** (85/1862)<br>**M** (82/1862)<br>**P** (80/1862)<br>**N** (80/1862) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1750)<br>**10** (148/1750)<br>**6** (144/1750)<br>**29** (144/1750)<br>**21** (144/1750) | **H** (89/1750)<br>**U** (80/1750)<br>**M** (78/1750)<br>**G** (76/1750)<br>**D** (75/1750) |
| **Lagna Wasana** | **5** (143/1869)<br>**23** (141/1869)<br>**39** (138/1869)<br>**36** (138/1869)<br>**25** (138/1869) | N/A |
| **Sasiri** | **9** (81/1047)<br>**20** (79/1047)<br>**22** (78/1047)<br>**26** (77/1047)<br>**21** (75/1047) | N/A |
| **Super Ball** | **52** (112/1863)<br>**9** (112/1863)<br>**45** (112/1863)<br>**29** (112/1863)<br>**62** (110/1863) | **I** (93/1863)<br>**V** (83/1863)<br>**T** (83/1863)<br>**D** (82/1863)<br>**A** (81/1863) |
| **Supiri Dhana Sampatha** | **0** (514/1021)<br>**2** (510/1021)<br>**3** (506/1021)<br>**7** (501/1021)<br>**8** (486/1021) | **V** (55/1021)<br>**K** (48/1021)<br>**S** (47/1021)<br>**T** (47/1021)<br>**G** (46/1021) |

