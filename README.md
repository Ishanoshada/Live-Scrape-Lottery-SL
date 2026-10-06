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

> **Last Updated (Sri Lanka Time):** `2026-10-07 03:17:48 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 355 Rows | 17.12 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 363 Rows | 15.55 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 362 Rows | 15.32 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 362 Rows | 14.93 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 362 Rows | 15.38 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 362 Rows | 16.36 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 353 Rows | 13.77 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 362 Rows | 16.65 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1881 Rows | 71.94 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1769 Rows | 72.29 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1888 Rows | 70.36 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1066 Rows | 35.36 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1882 Rows | 71.97 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1040 Rows | 38.71 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-07 03:17:48 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (129/355)<br>**2** (128/355)<br>**4** (125/355)<br>**3** (124/355)<br>**6** (123/355) | **D** (22/355)<br>**Q** (21/355)<br>**G** (21/355)<br>**N** (20/355)<br>**J** (20/355) |
| **Dhana Nidhanaya** | **9** (32/363)<br>**4** (30/363)<br>**7** (29/363)<br>**3** (27/363)<br>**80** (26/363) | **U** (20/363)<br>**W** (20/363)<br>**Z** (19/363)<br>**M** (19/363)<br>**F** (18/363) |
| **Govisetha** | **55** (28/362)<br>**10** (27/362)<br>**44** (26/362)<br>**14** (25/362)<br>**33** (25/362) | **P** (20/362)<br>**I** (18/362)<br>**C** (18/362)<br>**X** (18/362)<br>**W** (17/362) |
| **Handahana** | **58** (32/362)<br>**60** (31/362)<br>**11** (31/362)<br>**55** (31/362)<br>**21** (30/362) | N/A |
| **Mahajana Sampatha** | **5** (179/362)<br>**2** (178/362)<br>**1** (178/362)<br>**4** (176/362)<br>**3** (176/362) | **D** (22/362)<br>**Q** (21/362)<br>**G** (21/362)<br>**J** (20/362)<br>**N** (19/362) |
| **Mega Power** | **13** (42/362)<br>**26** (40/362)<br>**11** (40/362)<br>**22** (38/362)<br>**3** (38/362) | **V** (23/362)<br>**U** (23/362)<br>**T** (22/362)<br>**K** (19/362)<br>**S** (18/362) |
| **Nlb Jaya** | **5** (148/353)<br>**0** (135/353)<br>**3** (134/353)<br>**2** (133/353)<br>**7** (129/353) | **T** (21/353)<br>**I** (19/353)<br>**G** (19/353)<br>**P** (17/353)<br>**Y** (17/353) |
| **Suba Dawasak** | **4** (146/362)<br>**3** (142/362)<br>**9** (137/362)<br>**1** (136/362)<br>**2** (136/362) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1881)<br>**20** (124/1881)<br>**57** (122/1881)<br>**38** (118/1881)<br>**13** (116/1881) | **B** (88/1881)<br>**R** (85/1881)<br>**M** (84/1881)<br>**N** (82/1881)<br>**P** (81/1881) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1769)<br>**21** (149/1769)<br>**10** (149/1769)<br>**6** (145/1769)<br>**15** (145/1769) | **H** (89/1769)<br>**U** (81/1769)<br>**M** (79/1769)<br>**G** (76/1769)<br>**D** (75/1769) |
| **Lagna Wasana** | **5** (144/1888)<br>**23** (142/1888)<br>**39** (141/1888)<br>**36** (139/1888)<br>**25** (139/1888) | N/A |
| **Sasiri** | **9** (83/1066)<br>**20** (80/1066)<br>**26** (79/1066)<br>**22** (78/1066)<br>**21** (78/1066) | N/A |
| **Super Ball** | **45** (114/1882)<br>**9** (113/1882)<br>**52** (112/1882)<br>**29** (112/1882)<br>**74** (111/1882) | **I** (93/1882)<br>**T** (85/1882)<br>**V** (84/1882)<br>**D** (82/1882)<br>**A** (82/1882) |
| **Supiri Dhana Sampatha** | **0** (524/1040)<br>**2** (519/1040)<br>**7** (514/1040)<br>**3** (514/1040)<br>**8** (495/1040) | **V** (56/1040)<br>**K** (50/1040)<br>**T** (49/1040)<br>**S** (48/1040)<br>**G** (47/1040) |

