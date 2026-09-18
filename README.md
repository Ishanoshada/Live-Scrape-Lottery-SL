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

> **Last Updated (Sri Lanka Time):** `2026-09-19 01:21:35 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 337 Rows | 16.21 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 345 Rows | 14.75 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 344 Rows | 14.52 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 344 Rows | 14.15 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 344 Rows | 14.58 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 344 Rows | 15.51 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 335 Rows | 13.05 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 344 Rows | 15.83 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1863 Rows | 71.25 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1751 Rows | 71.56 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1870 Rows | 69.69 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1048 Rows | 34.75 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1864 Rows | 71.29 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1022 Rows | 38.02 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-19 01:21:36 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/337)<br>**2** (122/337)<br>**6** (117/337)<br>**4** (116/337)<br>**8** (115/337) | **D** (22/337)<br>**J** (20/337)<br>**N** (18/337)<br>**Q** (18/337)<br>**G** (18/337) |
| **Dhana Nidhanaya** | **9** (32/345)<br>**4** (30/345)<br>**7** (28/345)<br>**3** (27/345)<br>**28** (26/345) | **U** (20/345)<br>**W** (19/345)<br>**Z** (18/345)<br>**F** (18/345)<br>**M** (18/345) |
| **Govisetha** | **55** (28/344)<br>**10** (26/344)<br>**44** (25/344)<br>**29** (24/344)<br>**33** (24/344) | **P** (19/344)<br>**C** (18/344)<br>**I** (17/344)<br>**X** (17/344)<br>**K** (16/344) |
| **Handahana** | **58** (32/344)<br>**11** (31/344)<br>**55** (31/344)<br>**6** (30/344)<br>**60** (29/344) | N/A |
| **Mahajana Sampatha** | **5** (172/344)<br>**1** (171/344)<br>**2** (170/344)<br>**9** (166/344)<br>**3** (165/344) | **D** (22/344)<br>**J** (20/344)<br>**W** (19/344)<br>**Q** (18/344)<br>**G** (18/344) |
| **Mega Power** | **11** (40/344)<br>**3** (37/344)<br>**26** (37/344)<br>**13** (35/344)<br>**22** (34/344) | **T** (22/344)<br>**V** (22/344)<br>**U** (20/344)<br>**K** (18/344)<br>**J** (17/344) |
| **Nlb Jaya** | **5** (142/335)<br>**0** (130/335)<br>**3** (127/335)<br>**2** (127/335)<br>**7** (124/335) | **T** (20/335)<br>**I** (19/335)<br>**G** (18/335)<br>**P** (17/335)<br>**O** (17/335) |
| **Suba Dawasak** | **4** (140/344)<br>**3** (138/344)<br>**1** (130/344)<br>**8** (130/344)<br>**9** (130/344) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1863)<br>**20** (122/1863)<br>**57** (121/1863)<br>**38** (118/1863)<br>**75** (114/1863) | **B** (88/1863)<br>**R** (85/1863)<br>**M** (82/1863)<br>**N** (81/1863)<br>**P** (80/1863) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1751)<br>**10** (149/1751)<br>**21** (145/1751)<br>**6** (144/1751)<br>**29** (144/1751) | **H** (89/1751)<br>**U** (80/1751)<br>**M** (78/1751)<br>**G** (76/1751)<br>**D** (75/1751) |
| **Lagna Wasana** | **5** (143/1870)<br>**23** (142/1870)<br>**39** (138/1870)<br>**36** (138/1870)<br>**25** (138/1870) | N/A |
| **Sasiri** | **9** (81/1048)<br>**20** (79/1048)<br>**22** (78/1048)<br>**26** (77/1048)<br>**21** (75/1048) | N/A |
| **Super Ball** | **52** (112/1864)<br>**9** (112/1864)<br>**45** (112/1864)<br>**29** (112/1864)<br>**62** (110/1864) | **I** (93/1864)<br>**V** (83/1864)<br>**T** (83/1864)<br>**D** (82/1864)<br>**A** (82/1864) |
| **Supiri Dhana Sampatha** | **0** (515/1022)<br>**2** (511/1022)<br>**3** (506/1022)<br>**7** (502/1022)<br>**8** (487/1022) | **V** (55/1022)<br>**K** (48/1022)<br>**S** (47/1022)<br>**T** (47/1022)<br>**G** (46/1022) |

