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

> **Last Updated (Sri Lanka Time):** `2026-08-13 11:56:24 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 301 Rows | 14.43 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 309 Rows | 13.17 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 308 Rows | 12.95 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 308 Rows | 12.63 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 308 Rows | 13.01 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 308 Rows | 13.85 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 299 Rows | 11.59 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 308 Rows | 14.12 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1827 Rows | 69.87 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1715 Rows | 70.08 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1834 Rows | 68.35 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1012 Rows | 33.51 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1828 Rows | 69.91 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 986 Rows | 36.66 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-13 11:56:24 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (113/301)<br>**2** (108/301)<br>**6** (105/301)<br>**3** (105/301)<br>**7** (105/301) | **D** (19/301)<br>**J** (18/301)<br>**Q** (17/301)<br>**N** (16/301)<br>**G** (16/301) |
| **Dhana Nidhanaya** | **9** (29/309)<br>**4** (27/309)<br>**7** (27/309)<br>**28** (25/309)<br>**80** (24/309) | **U** (20/309)<br>**W** (17/309)<br>**Z** (16/309)<br>**F** (16/309)<br>**M** (16/309) |
| **Govisetha** | **55** (25/308)<br>**44** (24/308)<br>**10** (23/308)<br>**29** (23/308)<br>**33** (23/308) | **C** (17/308)<br>**P** (16/308)<br>**K** (16/308)<br>**X** (16/308)<br>**O** (14/308) |
| **Handahana** | **58** (31/308)<br>**11** (29/308)<br>**21** (28/308)<br>**55** (28/308)<br>**6** (28/308) | N/A |
| **Mahajana Sampatha** | **5** (153/308)<br>**1** (153/308)<br>**2** (152/308)<br>**7** (152/308)<br>**4** (149/308) | **D** (19/308)<br>**J** (18/308)<br>**Q** (17/308)<br>**G** (16/308)<br>**N** (15/308) |
| **Mega Power** | **11** (37/308)<br>**26** (34/308)<br>**13** (34/308)<br>**6** (32/308)<br>**22** (32/308) | **T** (21/308)<br>**V** (20/308)<br>**U** (20/308)<br>**K** (17/308)<br>**J** (16/308) |
| **Nlb Jaya** | **5** (133/299)<br>**0** (116/299)<br>**3** (115/299)<br>**2** (113/299)<br>**7** (108/299) | **I** (18/299)<br>**T** (18/299)<br>**G** (16/299)<br>**P** (15/299)<br>**H** (15/299) |
| **Suba Dawasak** | **3** (127/308)<br>**4** (125/308)<br>**1** (119/308)<br>**8** (115/308)<br>**9** (112/308) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1827)<br>**20** (120/1827)<br>**57** (117/1827)<br>**38** (115/1827)<br>**75** (112/1827) | **B** (85/1827)<br>**R** (83/1827)<br>**P** (80/1827)<br>**M** (80/1827)<br>**N** (78/1827) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (161/1715)<br>**10** (146/1715)<br>**6** (142/1715)<br>**21** (141/1715)<br>**15** (141/1715) | **H** (89/1715)<br>**U** (78/1715)<br>**M** (75/1715)<br>**D** (73/1715)<br>**G** (73/1715) |
| **Lagna Wasana** | **5** (140/1834)<br>**36** (136/1834)<br>**25** (136/1834)<br>**28** (136/1834)<br>**23** (135/1834) | N/A |
| **Sasiri** | **9** (76/1012)<br>**22** (74/1012)<br>**20** (74/1012)<br>**19** (74/1012)<br>**26** (73/1012) | N/A |
| **Super Ball** | **52** (111/1828)<br>**45** (111/1828)<br>**29** (111/1828)<br>**9** (109/1828)<br>**3** (108/1828) | **I** (92/1828)<br>**V** (82/1828)<br>**T** (82/1828)<br>**D** (82/1828)<br>**Y** (79/1828) |
| **Supiri Dhana Sampatha** | **2** (498/986)<br>**0** (494/986)<br>**3** (488/986)<br>**7** (483/986)<br>**5** (472/986) | **V** (53/986)<br>**K** (46/986)<br>**T** (45/986)<br>**S** (44/986)<br>**J** (44/986) |

