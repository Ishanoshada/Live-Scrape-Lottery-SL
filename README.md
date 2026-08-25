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

> **Last Updated (Sri Lanka Time):** `2026-08-25 11:25:22 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 313 Rows | 15.01 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 321 Rows | 13.68 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 320 Rows | 13.45 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 320 Rows | 13.11 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 320 Rows | 13.51 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 320 Rows | 14.38 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 311 Rows | 12.07 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 320 Rows | 14.67 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1839 Rows | 70.33 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1727 Rows | 70.57 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1846 Rows | 68.80 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1024 Rows | 33.92 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1840 Rows | 70.37 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 998 Rows | 37.10 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-25 11:25:22 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (116/313)<br>**2** (114/313)<br>**6** (108/313)<br>**3** (108/313)<br>**7** (108/313) | **D** (19/313)<br>**J** (19/313)<br>**N** (17/313)<br>**Q** (17/313)<br>**G** (16/313) |
| **Dhana Nidhanaya** | **9** (31/321)<br>**4** (28/321)<br>**7** (28/321)<br>**28** (25/321)<br>**80** (24/321) | **U** (20/321)<br>**W** (18/321)<br>**M** (17/321)<br>**Z** (16/321)<br>**F** (16/321) |
| **Govisetha** | **55** (25/320)<br>**44** (24/320)<br>**29** (24/320)<br>**10** (23/320)<br>**33** (23/320) | **P** (18/320)<br>**C** (17/320)<br>**X** (17/320)<br>**K** (16/320)<br>**A** (14/320) |
| **Handahana** | **58** (32/320)<br>**11** (30/320)<br>**55** (29/320)<br>**21** (28/320)<br>**6** (28/320) | N/A |
| **Mahajana Sampatha** | **2** (159/320)<br>**5** (159/320)<br>**1** (158/320)<br>**7** (157/320)<br>**4** (154/320) | **D** (19/320)<br>**J** (19/320)<br>**Q** (17/320)<br>**N** (16/320)<br>**G** (16/320) |
| **Mega Power** | **11** (37/320)<br>**26** (35/320)<br>**13** (35/320)<br>**3** (34/320)<br>**22** (32/320) | **T** (22/320)<br>**V** (20/320)<br>**U** (20/320)<br>**K** (18/320)<br>**J** (17/320) |
| **Nlb Jaya** | **5** (136/311)<br>**2** (121/311)<br>**0** (120/311)<br>**3** (119/311)<br>**7** (111/311) | **I** (18/311)<br>**T** (18/311)<br>**G** (17/311)<br>**H** (16/311)<br>**O** (16/311) |
| **Suba Dawasak** | **3** (131/320)<br>**4** (129/320)<br>**1** (123/320)<br>**8** (120/320)<br>**9** (119/320) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1839)<br>**20** (121/1839)<br>**57** (118/1839)<br>**38** (116/1839)<br>**75** (112/1839) | **B** (86/1839)<br>**R** (84/1839)<br>**M** (81/1839)<br>**P** (80/1839)<br>**N** (79/1839) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1727)<br>**10** (146/1727)<br>**6** (142/1727)<br>**29** (142/1727)<br>**15** (142/1727) | **H** (89/1727)<br>**U** (78/1727)<br>**M** (76/1727)<br>**D** (74/1727)<br>**G** (74/1727) |
| **Lagna Wasana** | **5** (140/1846)<br>**23** (138/1846)<br>**36** (137/1846)<br>**28** (137/1846)<br>**25** (136/1846) | N/A |
| **Sasiri** | **9** (79/1024)<br>**22** (77/1024)<br>**26** (76/1024)<br>**20** (75/1024)<br>**19** (74/1024) | N/A |
| **Super Ball** | **52** (111/1840)<br>**45** (111/1840)<br>**29** (111/1840)<br>**9** (110/1840)<br>**74** (109/1840) | **I** (92/1840)<br>**V** (82/1840)<br>**T** (82/1840)<br>**D** (82/1840)<br>**A** (81/1840) |
| **Supiri Dhana Sampatha** | **0** (501/998)<br>**2** (500/998)<br>**3** (495/998)<br>**7** (491/998)<br>**5** (476/998) | **V** (53/998)<br>**K** (47/998)<br>**G** (45/998)<br>**T** (45/998)<br>**S** (44/998) |

