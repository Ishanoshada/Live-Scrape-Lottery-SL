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

> **Last Updated (Sri Lanka Time):** `2026-09-28 01:47:04 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 346 Rows | 16.67 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 354 Rows | 15.16 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 353 Rows | 14.92 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 353 Rows | 14.55 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 353 Rows | 14.99 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 353 Rows | 15.94 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 344 Rows | 13.42 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 353 Rows | 16.27 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1872 Rows | 71.59 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1760 Rows | 71.93 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1879 Rows | 70.03 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1057 Rows | 35.05 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1873 Rows | 71.63 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1031 Rows | 38.36 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-28 01:47:04 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (126/346)<br>**2** (125/346)<br>**6** (121/346)<br>**4** (119/346)<br>**1** (119/346) | **D** (22/346)<br>**Q** (20/346)<br>**J** (20/346)<br>**G** (19/346)<br>**N** (18/346) |
| **Dhana Nidhanaya** | **9** (32/354)<br>**4** (30/354)<br>**7** (29/354)<br>**3** (27/354)<br>**28** (26/354) | **U** (20/354)<br>**W** (20/354)<br>**Z** (18/354)<br>**F** (18/354)<br>**M** (18/354) |
| **Govisetha** | **55** (28/353)<br>**10** (27/353)<br>**44** (26/353)<br>**33** (25/353)<br>**29** (24/353) | **P** (19/353)<br>**I** (18/353)<br>**C** (18/353)<br>**X** (17/353)<br>**D** (16/353) |
| **Handahana** | **58** (32/353)<br>**11** (31/353)<br>**55** (31/353)<br>**60** (30/353)<br>**21** (30/353) | N/A |
| **Mahajana Sampatha** | **1** (178/353)<br>**5** (174/353)<br>**2** (173/353)<br>**9** (170/353)<br>**3** (169/353) | **D** (22/353)<br>**Q** (20/353)<br>**J** (20/353)<br>**G** (19/353)<br>**W** (19/353) |
| **Mega Power** | **11** (40/353)<br>**3** (38/353)<br>**26** (38/353)<br>**13** (37/353)<br>**22** (36/353) | **U** (23/353)<br>**T** (22/353)<br>**V** (22/353)<br>**K** (19/353)<br>**J** (17/353) |
| **Nlb Jaya** | **5** (144/344)<br>**0** (133/344)<br>**3** (130/344)<br>**2** (130/344)<br>**7** (128/344) | **T** (21/344)<br>**I** (19/344)<br>**G** (19/344)<br>**P** (17/344)<br>**O** (17/344) |
| **Suba Dawasak** | **4** (145/353)<br>**3** (141/353)<br>**1** (134/353)<br>**9** (134/353)<br>**2** (134/353) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1872)<br>**20** (122/1872)<br>**57** (122/1872)<br>**38** (118/1872)<br>**29** (114/1872) | **B** (88/1872)<br>**R** (85/1872)<br>**M** (84/1872)<br>**P** (81/1872)<br>**N** (81/1872) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1760)<br>**10** (149/1760)<br>**21** (148/1760)<br>**6** (145/1760)<br>**15** (145/1760) | **H** (89/1760)<br>**U** (81/1760)<br>**M** (78/1760)<br>**G** (76/1760)<br>**D** (75/1760) |
| **Lagna Wasana** | **5** (143/1879)<br>**23** (142/1879)<br>**39** (139/1879)<br>**36** (139/1879)<br>**25** (139/1879) | N/A |
| **Sasiri** | **9** (82/1057)<br>**20** (79/1057)<br>**22** (78/1057)<br>**26** (78/1057)<br>**21** (77/1057) | N/A |
| **Super Ball** | **45** (113/1873)<br>**52** (112/1873)<br>**9** (112/1873)<br>**29** (112/1873)<br>**43** (111/1873) | **I** (93/1873)<br>**T** (85/1873)<br>**V** (84/1873)<br>**D** (82/1873)<br>**A** (82/1873) |
| **Supiri Dhana Sampatha** | **0** (519/1031)<br>**2** (514/1031)<br>**7** (510/1031)<br>**3** (510/1031)<br>**8** (493/1031) | **V** (56/1031)<br>**K** (49/1031)<br>**S** (48/1031)<br>**T** (48/1031)<br>**G** (46/1031) |

