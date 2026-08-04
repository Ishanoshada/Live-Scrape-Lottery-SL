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

> **Last Updated (Sri Lanka Time):** `2026-08-05 12:36:47 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 292 Rows | 14.00 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 300 Rows | 12.78 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 299 Rows | 12.57 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 299 Rows | 12.25 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 299 Rows | 12.63 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 299 Rows | 13.44 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 290 Rows | 11.24 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 299 Rows | 13.70 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1818 Rows | 69.53 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1706 Rows | 69.70 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1825 Rows | 68.01 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1003 Rows | 33.20 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1819 Rows | 69.56 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 977 Rows | 36.32 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-05 12:36:47 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (108/292)<br>**2** (105/292)<br>**6** (103/292)<br>**3** (103/292)<br>**7** (101/292) | **D** (19/292)<br>**Q** (17/292)<br>**J** (17/292)<br>**N** (16/292)<br>**G** (16/292) |
| **Dhana Nidhanaya** | **9** (27/300)<br>**7** (26/300)<br>**4** (25/300)<br>**28** (25/300)<br>**6** (23/300) | **U** (20/300)<br>**F** (16/300)<br>**W** (16/300)<br>**Z** (15/300)<br>**T** (15/300) |
| **Govisetha** | **55** (25/299)<br>**10** (23/299)<br>**33** (23/299)<br>**23** (22/299)<br>**44** (22/299) | **P** (16/299)<br>**K** (16/299)<br>**C** (16/299)<br>**O** (14/299)<br>**Y** (14/299) |
| **Handahana** | **58** (31/299)<br>**11** (29/299)<br>**55** (28/299)<br>**6** (28/299)<br>**21** (27/299) | N/A |
| **Mahajana Sampatha** | **2** (148/299)<br>**5** (147/299)<br>**7** (146/299)<br>**4** (145/299)<br>**3** (145/299) | **D** (19/299)<br>**Q** (17/299)<br>**J** (17/299)<br>**G** (16/299)<br>**N** (15/299) |
| **Mega Power** | **11** (36/299)<br>**13** (33/299)<br>**6** (32/299)<br>**22** (32/299)<br>**3** (32/299) | **T** (21/299)<br>**V** (20/299)<br>**U** (19/299)<br>**K** (17/299)<br>**J** (16/299) |
| **Nlb Jaya** | **5** (131/290)<br>**2** (111/290)<br>**0** (111/290)<br>**3** (110/290)<br>**7** (105/290) | **I** (18/290)<br>**T** (18/290)<br>**G** (16/290)<br>**Y** (15/290)<br>**M** (14/290) |
| **Suba Dawasak** | **3** (122/299)<br>**4** (121/299)<br>**1** (117/299)<br>**9** (111/299)<br>**8** (110/299) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1818)<br>**20** (120/1818)<br>**57** (117/1818)<br>**38** (114/1818)<br>**75** (112/1818) | **R** (83/1818)<br>**B** (82/1818)<br>**P** (80/1818)<br>**M** (80/1818)<br>**N** (78/1818) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (158/1706)<br>**10** (145/1706)<br>**6** (141/1706)<br>**15** (141/1706)<br>**29** (140/1706) | **H** (88/1706)<br>**U** (78/1706)<br>**G** (73/1706)<br>**M** (73/1706)<br>**X** (73/1706) |
| **Lagna Wasana** | **5** (140/1825)<br>**25** (136/1825)<br>**28** (136/1825)<br>**36** (135/1825)<br>**23** (135/1825) | N/A |
| **Sasiri** | **9** (75/1003)<br>**22** (74/1003)<br>**20** (74/1003)<br>**19** (72/1003)<br>**26** (71/1003) | N/A |
| **Super Ball** | **45** (111/1819)<br>**29** (111/1819)<br>**52** (110/1819)<br>**9** (109/1819)<br>**3** (107/1819) | **I** (92/1819)<br>**T** (82/1819)<br>**D** (82/1819)<br>**V** (81/1819)<br>**A** (79/1819) |
| **Supiri Dhana Sampatha** | **2** (494/977)<br>**0** (490/977)<br>**3** (484/977)<br>**7** (480/977)<br>**5** (465/977) | **V** (51/977)<br>**K** (46/977)<br>**T** (45/977)<br>**S** (44/977)<br>**J** (44/977) |

