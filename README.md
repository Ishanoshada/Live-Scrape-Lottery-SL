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

> **Last Updated (Sri Lanka Time):** `2026-07-18 11:56:27 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 275 Rows | 13.21 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 283 Rows | 12.07 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 282 Rows | 11.88 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 282 Rows | 11.59 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 282 Rows | 11.94 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 282 Rows | 12.71 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 273 Rows | 10.59 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 282 Rows | 12.95 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1801 Rows | 68.88 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1689 Rows | 69.00 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1808 Rows | 67.38 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 986 Rows | 32.62 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1802 Rows | 68.92 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 960 Rows | 35.69 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-18 11:56:27 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (103/275)<br>**6** (99/275)<br>**2** (97/275)<br>**7** (97/275)<br>**3** (94/275) | **Q** (17/275)<br>**D** (17/275)<br>**N** (16/275)<br>**J** (16/275)<br>**G** (16/275) |
| **Dhana Nidhanaya** | **9** (26/283)<br>**28** (25/283)<br>**7** (25/283)<br>**4** (23/283)<br>**6** (23/283) | **U** (17/283)<br>**F** (15/283)<br>**W** (15/283)<br>**Z** (14/283)<br>**T** (14/283) |
| **Govisetha** | **55** (23/282)<br>**10** (21/282)<br>**44** (21/282)<br>**33** (21/282)<br>**23** (20/282) | **P** (16/282)<br>**C** (15/282)<br>**K** (14/282)<br>**D** (13/282)<br>**A** (13/282) |
| **Handahana** | **58** (30/282)<br>**11** (27/282)<br>**21** (27/282)<br>**6** (27/282)<br>**55** (25/282) | N/A |
| **Mahajana Sampatha** | **5** (140/282)<br>**4** (138/282)<br>**7** (138/282)<br>**2** (138/282)<br>**6** (138/282) | **Q** (17/282)<br>**D** (17/282)<br>**J** (16/282)<br>**G** (16/282)<br>**N** (15/282) |
| **Mega Power** | **11** (36/282)<br>**6** (31/282)<br>**3** (31/282)<br>**22** (30/282)<br>**19** (30/282) | **T** (19/282)<br>**V** (19/282)<br>**U** (19/282)<br>**K** (16/282)<br>**J** (16/282) |
| **Nlb Jaya** | **5** (122/273)<br>**3** (104/273)<br>**0** (104/273)<br>**2** (103/273)<br>**7** (97/273) | **T** (18/273)<br>**I** (16/273)<br>**G** (16/273)<br>**M** (14/273)<br>**P** (14/273) |
| **Suba Dawasak** | **3** (116/282)<br>**4** (115/282)<br>**1** (110/282)<br>**8** (105/282)<br>**5** (102/282) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (122/1801)<br>**20** (119/1801)<br>**57** (116/1801)<br>**75** (111/1801)<br>**38** (111/1801) | **B** (82/1801)<br>**R** (81/1801)<br>**P** (80/1801)<br>**M** (80/1801)<br>**I** (77/1801) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1689)<br>**10** (145/1689)<br>**6** (138/1689)<br>**29** (138/1689)<br>**27** (138/1689) | **H** (88/1689)<br>**U** (77/1689)<br>**M** (73/1689)<br>**X** (73/1689)<br>**W** (72/1689) |
| **Lagna Wasana** | **5** (139/1808)<br>**28** (136/1808)<br>**36** (135/1808)<br>**25** (135/1808)<br>**39** (132/1808) | N/A |
| **Sasiri** | **9** (74/986)<br>**20** (73/986)<br>**22** (71/986)<br>**26** (71/986)<br>**5** (69/986) | N/A |
| **Super Ball** | **52** (110/1802)<br>**45** (110/1802)<br>**29** (110/1802)<br>**3** (107/1802)<br>**74** (107/1802) | **I** (90/1802)<br>**V** (81/1802)<br>**T** (81/1802)<br>**D** (81/1802)<br>**A** (79/1802) |
| **Supiri Dhana Sampatha** | **2** (485/960)<br>**0** (481/960)<br>**3** (479/960)<br>**7** (473/960)<br>**5** (458/960) | **V** (50/960)<br>**K** (46/960)<br>**S** (44/960)<br>**J** (44/960)<br>**T** (44/960) |

