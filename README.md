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

> **Last Updated (Sri Lanka Time):** `2026-08-24 11:27:13 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 312 Rows | 14.96 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 320 Rows | 13.64 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 319 Rows | 13.41 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 319 Rows | 13.07 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 319 Rows | 13.47 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 319 Rows | 14.33 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 310 Rows | 12.03 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 319 Rows | 14.62 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1838 Rows | 70.29 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1726 Rows | 70.53 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1845 Rows | 68.76 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1023 Rows | 33.89 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1839 Rows | 70.33 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 997 Rows | 37.06 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-24 11:27:13 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (116/312)<br>**2** (113/312)<br>**7** (108/312)<br>**6** (107/312)<br>**3** (107/312) | **D** (19/312)<br>**J** (19/312)<br>**N** (17/312)<br>**Q** (17/312)<br>**G** (16/312) |
| **Dhana Nidhanaya** | **9** (31/320)<br>**4** (28/320)<br>**7** (28/320)<br>**28** (25/320)<br>**80** (24/320) | **U** (20/320)<br>**W** (18/320)<br>**M** (17/320)<br>**Z** (16/320)<br>**F** (16/320) |
| **Govisetha** | **55** (25/319)<br>**44** (24/319)<br>**29** (24/319)<br>**10** (23/319)<br>**33** (23/319) | **P** (18/319)<br>**C** (17/319)<br>**X** (17/319)<br>**K** (16/319)<br>**A** (14/319) |
| **Handahana** | **58** (32/319)<br>**11** (30/319)<br>**55** (29/319)<br>**21** (28/319)<br>**6** (28/319) | N/A |
| **Mahajana Sampatha** | **5** (159/319)<br>**2** (158/319)<br>**1** (158/319)<br>**7** (156/319)<br>**4** (154/319) | **D** (19/319)<br>**J** (19/319)<br>**Q** (17/319)<br>**N** (16/319)<br>**G** (16/319) |
| **Mega Power** | **11** (37/319)<br>**26** (35/319)<br>**13** (35/319)<br>**3** (34/319)<br>**6** (32/319) | **T** (22/319)<br>**V** (20/319)<br>**U** (20/319)<br>**K** (18/319)<br>**J** (17/319) |
| **Nlb Jaya** | **5** (136/310)<br>**2** (120/310)<br>**0** (120/310)<br>**3** (118/310)<br>**7** (111/310) | **I** (18/310)<br>**T** (18/310)<br>**G** (17/310)<br>**H** (16/310)<br>**P** (15/310) |
| **Suba Dawasak** | **3** (130/319)<br>**4** (128/319)<br>**1** (123/319)<br>**8** (120/319)<br>**9** (118/319) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1838)<br>**20** (121/1838)<br>**57** (118/1838)<br>**38** (116/1838)<br>**75** (112/1838) | **B** (86/1838)<br>**R** (84/1838)<br>**M** (81/1838)<br>**P** (80/1838)<br>**N** (79/1838) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1726)<br>**10** (146/1726)<br>**6** (142/1726)<br>**29** (142/1726)<br>**15** (142/1726) | **H** (89/1726)<br>**U** (78/1726)<br>**M** (76/1726)<br>**D** (74/1726)<br>**G** (74/1726) |
| **Lagna Wasana** | **5** (140/1845)<br>**36** (137/1845)<br>**23** (137/1845)<br>**28** (137/1845)<br>**25** (136/1845) | N/A |
| **Sasiri** | **9** (79/1023)<br>**22** (76/1023)<br>**20** (75/1023)<br>**26** (75/1023)<br>**19** (74/1023) | N/A |
| **Super Ball** | **52** (111/1839)<br>**45** (111/1839)<br>**29** (111/1839)<br>**9** (110/1839)<br>**74** (109/1839) | **I** (92/1839)<br>**V** (82/1839)<br>**T** (82/1839)<br>**D** (82/1839)<br>**A** (81/1839) |
| **Supiri Dhana Sampatha** | **2** (500/997)<br>**0** (500/997)<br>**3** (494/997)<br>**7** (490/997)<br>**5** (475/997) | **V** (53/997)<br>**K** (47/997)<br>**G** (45/997)<br>**T** (45/997)<br>**S** (44/997) |

