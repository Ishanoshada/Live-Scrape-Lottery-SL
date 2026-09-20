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

> **Last Updated (Sri Lanka Time):** `2026-09-21 01:08:32 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 339 Rows | 16.31 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 347 Rows | 14.84 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 346 Rows | 14.61 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 346 Rows | 14.24 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 346 Rows | 14.67 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 346 Rows | 15.61 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 337 Rows | 13.13 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 346 Rows | 15.93 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1865 Rows | 71.33 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1753 Rows | 71.64 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1872 Rows | 69.77 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1050 Rows | 34.81 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1866 Rows | 71.36 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1024 Rows | 38.09 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-21 01:08:32 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/339)<br>**2** (124/339)<br>**6** (118/339)<br>**8** (116/339)<br>**4** (116/339) | **D** (22/339)<br>**Q** (20/339)<br>**J** (20/339)<br>**N** (18/339)<br>**G** (18/339) |
| **Dhana Nidhanaya** | **9** (32/347)<br>**4** (30/347)<br>**7** (28/347)<br>**3** (27/347)<br>**28** (26/347) | **U** (20/347)<br>**W** (19/347)<br>**Z** (18/347)<br>**F** (18/347)<br>**M** (18/347) |
| **Govisetha** | **55** (28/346)<br>**10** (26/346)<br>**44** (25/346)<br>**29** (24/346)<br>**33** (24/346) | **P** (19/346)<br>**C** (18/346)<br>**I** (17/346)<br>**X** (17/346)<br>**W** (16/346) |
| **Handahana** | **58** (32/346)<br>**11** (31/346)<br>**55** (31/346)<br>**60** (30/346)<br>**21** (30/346) | N/A |
| **Mahajana Sampatha** | **5** (172/346)<br>**2** (172/346)<br>**1** (172/346)<br>**9** (167/346)<br>**3** (166/346) | **D** (22/346)<br>**Q** (20/346)<br>**J** (20/346)<br>**W** (19/346)<br>**G** (18/346) |
| **Mega Power** | **11** (40/346)<br>**3** (37/346)<br>**26** (37/346)<br>**13** (35/346)<br>**22** (34/346) | **T** (22/346)<br>**V** (22/346)<br>**U** (22/346)<br>**K** (18/346)<br>**J** (17/346) |
| **Nlb Jaya** | **5** (142/337)<br>**0** (130/337)<br>**3** (127/337)<br>**2** (127/337)<br>**7** (126/337) | **T** (20/337)<br>**I** (19/337)<br>**G** (18/337)<br>**P** (17/337)<br>**O** (17/337) |
| **Suba Dawasak** | **3** (140/346)<br>**4** (140/346)<br>**9** (132/346)<br>**8** (131/346)<br>**1** (130/346) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1865)<br>**20** (122/1865)<br>**57** (121/1865)<br>**38** (118/1865)<br>**75** (114/1865) | **B** (88/1865)<br>**R** (85/1865)<br>**M** (83/1865)<br>**N** (81/1865)<br>**P** (80/1865) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1753)<br>**10** (149/1753)<br>**21** (146/1753)<br>**6** (144/1753)<br>**29** (144/1753) | **H** (89/1753)<br>**U** (80/1753)<br>**M** (78/1753)<br>**G** (76/1753)<br>**D** (75/1753) |
| **Lagna Wasana** | **5** (143/1872)<br>**23** (142/1872)<br>**39** (139/1872)<br>**36** (139/1872)<br>**25** (139/1872) | N/A |
| **Sasiri** | **9** (82/1050)<br>**20** (79/1050)<br>**22** (78/1050)<br>**26** (77/1050)<br>**21** (77/1050) | N/A |
| **Super Ball** | **52** (112/1866)<br>**9** (112/1866)<br>**45** (112/1866)<br>**29** (112/1866)<br>**62** (110/1866) | **I** (93/1866)<br>**V** (83/1866)<br>**T** (83/1866)<br>**D** (82/1866)<br>**A** (82/1866) |
| **Supiri Dhana Sampatha** | **0** (516/1024)<br>**2** (513/1024)<br>**3** (507/1024)<br>**7** (504/1024)<br>**8** (488/1024) | **V** (55/1024)<br>**K** (48/1024)<br>**S** (48/1024)<br>**T** (47/1024)<br>**G** (46/1024) |

