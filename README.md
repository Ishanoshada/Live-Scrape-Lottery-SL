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

> **Last Updated (Sri Lanka Time):** `2026-09-16 01:51:38 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 334 Rows | 16.06 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 342 Rows | 14.62 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 341 Rows | 14.38 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 341 Rows | 14.02 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 341 Rows | 14.45 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 341 Rows | 15.37 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 332 Rows | 12.92 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 341 Rows | 15.68 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1860 Rows | 71.13 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1748 Rows | 71.43 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1867 Rows | 69.58 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1045 Rows | 34.64 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1861 Rows | 71.17 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1019 Rows | 37.90 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-16 01:51:38 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/334)<br>**2** (121/334)<br>**6** (117/334)<br>**4** (115/334)<br>**1** (114/334) | **D** (21/334)<br>**J** (19/334)<br>**N** (18/334)<br>**Q** (18/334)<br>**G** (18/334) |
| **Dhana Nidhanaya** | **9** (32/342)<br>**4** (30/342)<br>**7** (28/342)<br>**3** (27/342)<br>**28** (26/342) | **U** (20/342)<br>**W** (19/342)<br>**Z** (18/342)<br>**F** (18/342)<br>**M** (18/342) |
| **Govisetha** | **55** (27/341)<br>**10** (26/341)<br>**44** (25/341)<br>**29** (24/341)<br>**33** (24/341) | **P** (19/341)<br>**C** (18/341)<br>**X** (17/341)<br>**K** (16/341)<br>**I** (16/341) |
| **Handahana** | **58** (32/341)<br>**11** (31/341)<br>**55** (31/341)<br>**6** (30/341)<br>**60** (29/341) | N/A |
| **Mahajana Sampatha** | **5** (171/341)<br>**1** (169/341)<br>**2** (168/341)<br>**7** (164/341)<br>**9** (164/341) | **D** (21/341)<br>**J** (19/341)<br>**W** (19/341)<br>**Q** (18/341)<br>**G** (18/341) |
| **Mega Power** | **11** (40/341)<br>**3** (37/341)<br>**26** (37/341)<br>**13** (35/341)<br>**22** (34/341) | **T** (22/341)<br>**V** (22/341)<br>**U** (20/341)<br>**K** (18/341)<br>**J** (17/341) |
| **Nlb Jaya** | **5** (142/332)<br>**0** (130/332)<br>**3** (127/332)<br>**2** (127/332)<br>**7** (122/332) | **T** (20/332)<br>**I** (18/332)<br>**G** (18/332)<br>**O** (17/332)<br>**P** (16/332) |
| **Suba Dawasak** | **4** (140/341)<br>**3** (137/341)<br>**1** (130/341)<br>**9** (128/341)<br>**8** (128/341) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1860)<br>**20** (122/1860)<br>**57** (121/1860)<br>**38** (118/1860)<br>**75** (114/1860) | **B** (88/1860)<br>**R** (85/1860)<br>**M** (82/1860)<br>**P** (80/1860)<br>**N** (80/1860) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1748)<br>**10** (147/1748)<br>**6** (144/1748)<br>**29** (144/1748)<br>**21** (144/1748) | **H** (89/1748)<br>**U** (80/1748)<br>**M** (78/1748)<br>**G** (76/1748)<br>**D** (75/1748) |
| **Lagna Wasana** | **5** (143/1867)<br>**23** (141/1867)<br>**39** (138/1867)<br>**36** (138/1867)<br>**25** (138/1867) | N/A |
| **Sasiri** | **9** (80/1045)<br>**22** (78/1045)<br>**20** (78/1045)<br>**26** (77/1045)<br>**19** (74/1045) | N/A |
| **Super Ball** | **52** (112/1861)<br>**9** (112/1861)<br>**45** (112/1861)<br>**29** (112/1861)<br>**62** (110/1861) | **I** (93/1861)<br>**V** (83/1861)<br>**T** (83/1861)<br>**D** (82/1861)<br>**A** (81/1861) |
| **Supiri Dhana Sampatha** | **0** (514/1019)<br>**2** (509/1019)<br>**3** (505/1019)<br>**7** (501/1019)<br>**5** (485/1019) | **V** (54/1019)<br>**K** (47/1019)<br>**S** (47/1019)<br>**T** (47/1019)<br>**G** (46/1019) |

