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

> **Last Updated (Sri Lanka Time):** `2026-08-11 11:54:05 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 299 Rows | 14.33 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 307 Rows | 13.08 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 306 Rows | 12.87 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 306 Rows | 12.54 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 306 Rows | 12.92 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 306 Rows | 13.75 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 297 Rows | 11.51 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 306 Rows | 14.03 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1825 Rows | 69.79 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1713 Rows | 69.99 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1832 Rows | 68.27 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1010 Rows | 33.44 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1826 Rows | 69.83 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 984 Rows | 36.58 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-11 11:54:05 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (112/299)<br>**2** (108/299)<br>**3** (104/299)<br>**6** (104/299)<br>**8** (103/299) | **D** (19/299)<br>**J** (18/299)<br>**Q** (17/299)<br>**N** (16/299)<br>**G** (16/299) |
| **Dhana Nidhanaya** | **9** (28/307)<br>**4** (27/307)<br>**7** (27/307)<br>**28** (25/307)<br>**80** (24/307) | **U** (20/307)<br>**Z** (16/307)<br>**F** (16/307)<br>**W** (16/307)<br>**M** (16/307) |
| **Govisetha** | **55** (25/306)<br>**10** (23/306)<br>**44** (23/306)<br>**33** (23/306)<br>**23** (22/306) | **C** (17/306)<br>**P** (16/306)<br>**K** (16/306)<br>**X** (16/306)<br>**O** (14/306) |
| **Handahana** | **58** (31/306)<br>**11** (29/306)<br>**55** (28/306)<br>**6** (28/306)<br>**21** (27/306) | N/A |
| **Mahajana Sampatha** | **5** (152/306)<br>**2** (151/306)<br>**1** (151/306)<br>**7** (150/306)<br>**4** (148/306) | **D** (19/306)<br>**J** (18/306)<br>**Q** (17/306)<br>**G** (16/306)<br>**N** (15/306) |
| **Mega Power** | **11** (37/306)<br>**26** (34/306)<br>**13** (34/306)<br>**6** (32/306)<br>**22** (32/306) | **T** (21/306)<br>**V** (20/306)<br>**U** (20/306)<br>**K** (17/306)<br>**J** (16/306) |
| **Nlb Jaya** | **5** (133/297)<br>**0** (116/297)<br>**3** (113/297)<br>**2** (113/297)<br>**7** (107/297) | **I** (18/297)<br>**T** (18/297)<br>**G** (16/297)<br>**P** (15/297)<br>**Y** (15/297) |
| **Suba Dawasak** | **3** (127/306)<br>**4** (124/306)<br>**1** (118/306)<br>**8** (114/306)<br>**9** (112/306) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1825)<br>**20** (120/1825)<br>**57** (117/1825)<br>**38** (115/1825)<br>**75** (112/1825) | **B** (85/1825)<br>**R** (83/1825)<br>**P** (80/1825)<br>**M** (80/1825)<br>**N** (78/1825) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (159/1713)<br>**10** (146/1713)<br>**6** (141/1713)<br>**21** (141/1713)<br>**15** (141/1713) | **H** (89/1713)<br>**U** (78/1713)<br>**M** (75/1713)<br>**D** (73/1713)<br>**G** (73/1713) |
| **Lagna Wasana** | **5** (140/1832)<br>**36** (136/1832)<br>**25** (136/1832)<br>**28** (136/1832)<br>**23** (135/1832) | N/A |
| **Sasiri** | **9** (76/1010)<br>**22** (74/1010)<br>**20** (74/1010)<br>**19** (73/1010)<br>**26** (73/1010) | N/A |
| **Super Ball** | **52** (111/1826)<br>**45** (111/1826)<br>**29** (111/1826)<br>**9** (109/1826)<br>**3** (108/1826) | **I** (92/1826)<br>**V** (82/1826)<br>**T** (82/1826)<br>**D** (82/1826)<br>**A** (79/1826) |
| **Supiri Dhana Sampatha** | **2** (497/984)<br>**0** (492/984)<br>**3** (487/984)<br>**7** (482/984)<br>**5** (471/984) | **V** (52/984)<br>**K** (46/984)<br>**T** (45/984)<br>**S** (44/984)<br>**J** (44/984) |

