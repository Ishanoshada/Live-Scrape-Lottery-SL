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

> **Last Updated (Sri Lanka Time):** `2026-10-08 03:40:44 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 356 Rows | 17.17 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 364 Rows | 15.60 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 363 Rows | 15.36 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 363 Rows | 14.97 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 363 Rows | 15.42 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 363 Rows | 16.41 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 354 Rows | 13.82 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 363 Rows | 16.69 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1882 Rows | 71.98 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1770 Rows | 72.34 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1889 Rows | 70.40 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1067 Rows | 35.40 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1883 Rows | 72.01 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1041 Rows | 38.75 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-08 03:40:44 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (129/356)<br>**2** (128/356)<br>**4** (125/356)<br>**3** (124/356)<br>**6** (123/356) | **D** (22/356)<br>**Q** (21/356)<br>**G** (21/356)<br>**N** (20/356)<br>**J** (20/356) |
| **Dhana Nidhanaya** | **9** (32/364)<br>**4** (30/364)<br>**7** (29/364)<br>**3** (27/364)<br>**80** (26/364) | **U** (20/364)<br>**W** (20/364)<br>**Z** (19/364)<br>**M** (19/364)<br>**F** (18/364) |
| **Govisetha** | **55** (28/363)<br>**10** (27/363)<br>**44** (26/363)<br>**32** (25/363)<br>**14** (25/363) | **P** (20/363)<br>**I** (18/363)<br>**C** (18/363)<br>**X** (18/363)<br>**W** (17/363) |
| **Handahana** | **58** (32/363)<br>**60** (31/363)<br>**11** (31/363)<br>**55** (31/363)<br>**21** (30/363) | N/A |
| **Mahajana Sampatha** | **5** (179/363)<br>**2** (178/363)<br>**1** (178/363)<br>**3** (176/363)<br>**4** (176/363) | **D** (22/363)<br>**Q** (21/363)<br>**G** (21/363)<br>**J** (20/363)<br>**W** (20/363) |
| **Mega Power** | **13** (42/363)<br>**26** (40/363)<br>**11** (40/363)<br>**22** (38/363)<br>**3** (38/363) | **V** (23/363)<br>**U** (23/363)<br>**T** (22/363)<br>**K** (19/363)<br>**S** (18/363) |
| **Nlb Jaya** | **5** (149/354)<br>**0** (135/354)<br>**3** (134/354)<br>**2** (134/354)<br>**6** (129/354) | **T** (21/354)<br>**I** (19/354)<br>**G** (19/354)<br>**P** (17/354)<br>**Y** (17/354) |
| **Suba Dawasak** | **4** (146/363)<br>**3** (142/363)<br>**9** (137/363)<br>**1** (136/363)<br>**2** (136/363) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1882)<br>**20** (124/1882)<br>**57** (123/1882)<br>**38** (118/1882)<br>**13** (116/1882) | **B** (88/1882)<br>**R** (85/1882)<br>**M** (84/1882)<br>**N** (82/1882)<br>**P** (81/1882) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1770)<br>**21** (149/1770)<br>**10** (149/1770)<br>**6** (145/1770)<br>**15** (145/1770) | **H** (89/1770)<br>**U** (81/1770)<br>**M** (79/1770)<br>**G** (76/1770)<br>**D** (75/1770) |
| **Lagna Wasana** | **5** (144/1889)<br>**23** (142/1889)<br>**39** (141/1889)<br>**36** (139/1889)<br>**25** (139/1889) | N/A |
| **Sasiri** | **9** (83/1067)<br>**20** (80/1067)<br>**26** (79/1067)<br>**22** (78/1067)<br>**21** (78/1067) | N/A |
| **Super Ball** | **45** (114/1883)<br>**9** (113/1883)<br>**52** (112/1883)<br>**29** (112/1883)<br>**74** (111/1883) | **I** (93/1883)<br>**T** (85/1883)<br>**V** (84/1883)<br>**D** (82/1883)<br>**A** (82/1883) |
| **Supiri Dhana Sampatha** | **0** (525/1041)<br>**2** (519/1041)<br>**7** (515/1041)<br>**3** (515/1041)<br>**8** (496/1041) | **V** (56/1041)<br>**K** (50/1041)<br>**T** (49/1041)<br>**S** (48/1041)<br>**G** (47/1041) |

