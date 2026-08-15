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

> **Last Updated (Sri Lanka Time):** `2026-08-15 11:14:52 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 303 Rows | 14.53 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 311 Rows | 13.25 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 310 Rows | 13.04 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 310 Rows | 12.71 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 310 Rows | 13.10 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 310 Rows | 13.94 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 301 Rows | 11.67 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 310 Rows | 14.21 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1829 Rows | 69.95 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1717 Rows | 70.16 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1836 Rows | 68.43 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1014 Rows | 33.58 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1830 Rows | 69.99 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 988 Rows | 36.73 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-15 11:14:52 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (113/303)<br>**2** (109/303)<br>**3** (106/303)<br>**6** (105/303)<br>**7** (105/303) | **D** (19/303)<br>**J** (18/303)<br>**N** (17/303)<br>**Q** (17/303)<br>**G** (16/303) |
| **Dhana Nidhanaya** | **9** (29/311)<br>**4** (27/311)<br>**7** (27/311)<br>**28** (25/311)<br>**80** (24/311) | **U** (20/311)<br>**W** (17/311)<br>**M** (17/311)<br>**Z** (16/311)<br>**F** (16/311) |
| **Govisetha** | **55** (25/310)<br>**44** (24/310)<br>**29** (24/310)<br>**10** (23/310)<br>**33** (23/310) | **C** (17/310)<br>**P** (16/310)<br>**K** (16/310)<br>**X** (16/310)<br>**W** (14/310) |
| **Handahana** | **58** (31/310)<br>**11** (30/310)<br>**55** (29/310)<br>**21** (28/310)<br>**6** (28/310) | N/A |
| **Mahajana Sampatha** | **1** (154/310)<br>**5** (153/310)<br>**2** (153/310)<br>**7** (152/310)<br>**4** (150/310) | **D** (19/310)<br>**J** (18/310)<br>**Q** (17/310)<br>**N** (16/310)<br>**G** (16/310) |
| **Mega Power** | **11** (37/310)<br>**26** (34/310)<br>**13** (34/310)<br>**22** (32/310)<br>**6** (32/310) | **T** (21/310)<br>**V** (20/310)<br>**U** (20/310)<br>**K** (17/310)<br>**J** (16/310) |
| **Nlb Jaya** | **5** (133/301)<br>**0** (117/301)<br>**3** (116/301)<br>**2** (114/301)<br>**7** (109/301) | **I** (18/301)<br>**T** (18/301)<br>**G** (16/301)<br>**P** (15/301)<br>**H** (15/301) |
| **Suba Dawasak** | **3** (127/310)<br>**4** (126/310)<br>**1** (120/310)<br>**8** (117/310)<br>**2** (114/310) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1829)<br>**20** (120/1829)<br>**57** (117/1829)<br>**38** (115/1829)<br>**75** (112/1829) | **B** (85/1829)<br>**R** (83/1829)<br>**P** (80/1829)<br>**M** (80/1829)<br>**N** (78/1829) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (161/1717)<br>**10** (146/1717)<br>**6** (142/1717)<br>**21** (141/1717)<br>**15** (141/1717) | **H** (89/1717)<br>**U** (78/1717)<br>**M** (75/1717)<br>**D** (74/1717)<br>**G** (73/1717) |
| **Lagna Wasana** | **5** (140/1836)<br>**36** (137/1836)<br>**23** (136/1836)<br>**25** (136/1836)<br>**28** (136/1836) | N/A |
| **Sasiri** | **9** (76/1014)<br>**22** (74/1014)<br>**20** (74/1014)<br>**19** (74/1014)<br>**26** (74/1014) | N/A |
| **Super Ball** | **52** (111/1830)<br>**45** (111/1830)<br>**29** (111/1830)<br>**9** (109/1830)<br>**3** (108/1830) | **I** (92/1830)<br>**V** (82/1830)<br>**T** (82/1830)<br>**D** (82/1830)<br>**A** (80/1830) |
| **Supiri Dhana Sampatha** | **2** (498/988)<br>**0** (496/988)<br>**3** (489/988)<br>**7** (485/988)<br>**5** (472/988) | **V** (53/988)<br>**K** (46/988)<br>**T** (45/988)<br>**S** (44/988)<br>**J** (44/988) |

