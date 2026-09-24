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

> **Last Updated (Sri Lanka Time):** `2026-09-25 02:08:51 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 343 Rows | 16.52 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 351 Rows | 15.03 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 350 Rows | 14.79 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 350 Rows | 14.42 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 350 Rows | 14.85 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 350 Rows | 15.80 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 341 Rows | 13.29 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 350 Rows | 16.12 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1869 Rows | 71.48 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1757 Rows | 71.80 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1876 Rows | 69.92 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1054 Rows | 34.95 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1870 Rows | 71.52 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1028 Rows | 38.25 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-25 02:08:51 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (125/343)<br>**5** (124/343)<br>**6** (120/343)<br>**3** (117/343)<br>**4** (117/343) | **D** (22/343)<br>**Q** (20/343)<br>**J** (20/343)<br>**G** (19/343)<br>**N** (18/343) |
| **Dhana Nidhanaya** | **9** (32/351)<br>**4** (30/351)<br>**7** (29/351)<br>**3** (27/351)<br>**28** (26/351) | **U** (20/351)<br>**W** (19/351)<br>**Z** (18/351)<br>**F** (18/351)<br>**M** (18/351) |
| **Govisetha** | **55** (28/350)<br>**10** (26/350)<br>**44** (26/350)<br>**33** (25/350)<br>**29** (24/350) | **P** (19/350)<br>**I** (18/350)<br>**C** (18/350)<br>**X** (17/350)<br>**W** (16/350) |
| **Handahana** | **58** (32/350)<br>**11** (31/350)<br>**55** (31/350)<br>**60** (30/350)<br>**21** (30/350) | N/A |
| **Mahajana Sampatha** | **1** (175/350)<br>**2** (173/350)<br>**5** (172/350)<br>**3** (168/350)<br>**9** (167/350) | **D** (22/350)<br>**Q** (20/350)<br>**J** (20/350)<br>**G** (19/350)<br>**W** (19/350) |
| **Mega Power** | **11** (40/350)<br>**3** (38/350)<br>**26** (38/350)<br>**13** (37/350)<br>**22** (35/350) | **T** (22/350)<br>**V** (22/350)<br>**U** (22/350)<br>**K** (19/350)<br>**J** (17/350) |
| **Nlb Jaya** | **5** (142/341)<br>**0** (132/341)<br>**3** (130/341)<br>**2** (129/341)<br>**7** (128/341) | **T** (21/341)<br>**I** (19/341)<br>**G** (18/341)<br>**P** (17/341)<br>**O** (17/341) |
| **Suba Dawasak** | **4** (143/350)<br>**3** (140/350)<br>**9** (133/350)<br>**2** (133/350)<br>**1** (132/350) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1869)<br>**20** (122/1869)<br>**57** (121/1869)<br>**38** (118/1869)<br>**29** (114/1869) | **B** (88/1869)<br>**R** (85/1869)<br>**M** (84/1869)<br>**P** (81/1869)<br>**N** (81/1869) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1757)<br>**10** (149/1757)<br>**21** (147/1757)<br>**6** (145/1757)<br>**15** (145/1757) | **H** (89/1757)<br>**U** (81/1757)<br>**M** (78/1757)<br>**G** (76/1757)<br>**D** (75/1757) |
| **Lagna Wasana** | **5** (143/1876)<br>**23** (142/1876)<br>**39** (139/1876)<br>**36** (139/1876)<br>**25** (139/1876) | N/A |
| **Sasiri** | **9** (82/1054)<br>**20** (79/1054)<br>**22** (78/1054)<br>**26** (78/1054)<br>**21** (77/1054) | N/A |
| **Super Ball** | **45** (113/1870)<br>**52** (112/1870)<br>**9** (112/1870)<br>**29** (112/1870)<br>**43** (111/1870) | **I** (93/1870)<br>**V** (84/1870)<br>**T** (84/1870)<br>**D** (82/1870)<br>**A** (82/1870) |
| **Supiri Dhana Sampatha** | **0** (517/1028)<br>**2** (514/1028)<br>**3** (508/1028)<br>**7** (507/1028)<br>**8** (492/1028) | **V** (55/1028)<br>**K** (49/1028)<br>**S** (48/1028)<br>**T** (47/1028)<br>**G** (46/1028) |

