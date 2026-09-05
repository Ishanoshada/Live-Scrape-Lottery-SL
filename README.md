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

> **Last Updated (Sri Lanka Time):** `2026-09-06 12:44:35 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 324 Rows | 15.55 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 332 Rows | 14.17 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 331 Rows | 13.94 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 331 Rows | 13.58 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 331 Rows | 14.00 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 331 Rows | 14.89 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 322 Rows | 12.51 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 331 Rows | 15.19 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1850 Rows | 70.75 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1738 Rows | 71.02 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1857 Rows | 69.21 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1035 Rows | 34.30 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1851 Rows | 70.79 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1009 Rows | 37.52 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-06 12:44:35 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (120/324)<br>**2** (118/324)<br>**3** (112/324)<br>**6** (112/324)<br>**8** (111/324) | **D** (19/324)<br>**J** (19/324)<br>**G** (18/324)<br>**W** (18/324)<br>**N** (17/324) |
| **Dhana Nidhanaya** | **9** (32/332)<br>**4** (30/332)<br>**7** (28/332)<br>**28** (26/332)<br>**3** (26/332) | **U** (20/332)<br>**F** (18/332)<br>**W** (18/332)<br>**M** (18/332)<br>**Z** (17/332) |
| **Govisetha** | **55** (27/331)<br>**10** (26/331)<br>**44** (24/331)<br>**29** (24/331)<br>**23** (23/331) | **P** (18/331)<br>**C** (18/331)<br>**X** (17/331)<br>**K** (16/331)<br>**W** (15/331) |
| **Handahana** | **58** (32/331)<br>**11** (31/331)<br>**55** (30/331)<br>**6** (29/331)<br>**60** (28/331) | N/A |
| **Mahajana Sampatha** | **5** (166/331)<br>**2** (164/331)<br>**1** (163/331)<br>**7** (161/331)<br>**9** (160/331) | **D** (19/331)<br>**J** (19/331)<br>**W** (19/331)<br>**G** (18/331)<br>**Q** (17/331) |
| **Mega Power** | **11** (39/331)<br>**26** (37/331)<br>**3** (36/331)<br>**13** (35/331)<br>**6** (34/331) | **T** (22/331)<br>**V** (21/331)<br>**U** (20/331)<br>**K** (18/331)<br>**J** (17/331) |
| **Nlb Jaya** | **5** (139/322)<br>**0** (126/322)<br>**3** (125/322)<br>**2** (123/322)<br>**7** (117/322) | **I** (18/322)<br>**T** (18/322)<br>**G** (17/322)<br>**O** (17/322)<br>**H** (16/322) |
| **Suba Dawasak** | **3** (134/331)<br>**4** (133/331)<br>**1** (126/331)<br>**9** (125/331)<br>**2** (124/331) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1850)<br>**20** (121/1850)<br>**57** (120/1850)<br>**38** (117/1850)<br>**75** (114/1850) | **B** (88/1850)<br>**R** (84/1850)<br>**M** (82/1850)<br>**P** (80/1850)<br>**N** (79/1850) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1738)<br>**10** (146/1738)<br>**6** (143/1738)<br>**29** (143/1738)<br>**15** (143/1738) | **H** (89/1738)<br>**U** (79/1738)<br>**M** (77/1738)<br>**D** (75/1738)<br>**G** (75/1738) |
| **Lagna Wasana** | **5** (142/1857)<br>**23** (140/1857)<br>**39** (138/1857)<br>**36** (138/1857)<br>**28** (138/1857) | N/A |
| **Sasiri** | **9** (80/1035)<br>**22** (77/1035)<br>**20** (77/1035)<br>**26** (76/1035)<br>**19** (74/1035) | N/A |
| **Super Ball** | **9** (112/1851)<br>**45** (112/1851)<br>**29** (112/1851)<br>**52** (111/1851)<br>**62** (109/1851) | **I** (93/1851)<br>**V** (83/1851)<br>**T** (82/1851)<br>**D** (82/1851)<br>**A** (81/1851) |
| **Supiri Dhana Sampatha** | **0** (507/1009)<br>**2** (506/1009)<br>**3** (500/1009)<br>**7** (497/1009)<br>**5** (482/1009) | **V** (53/1009)<br>**K** (47/1009)<br>**S** (46/1009)<br>**G** (46/1009)<br>**T** (46/1009) |

