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

> **Last Updated (Sri Lanka Time):** `2026-06-01 12:13:35 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 227 Rows | 11.00 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 235 Rows | 10.09 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 234 Rows | 9.96 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 234 Rows | 9.71 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 234 Rows | 10.01 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 234 Rows | 10.65 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 225 Rows | 8.80 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 234 Rows | 10.84 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1753 Rows | 67.04 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1641 Rows | 67.03 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1760 Rows | 65.59 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 938 Rows | 30.97 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1754 Rows | 67.08 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 912 Rows | 33.90 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-01 12:13:35 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (86/227)<br>**5** (83/227)<br>**2** (81/227)<br>**4** (79/227)<br>**0** (78/227) | **N** (14/227)<br>**D** (14/227)<br>**J** (14/227)<br>**Q** (13/227)<br>**Y** (12/227) |
| **Dhana Nidhanaya** | **28** (23/235)<br>**9** (23/235)<br>**6** (20/235)<br>**7** (19/235)<br>**16** (18/235) | **U** (15/235)<br>**W** (13/235)<br>**Z** (12/235)<br>**T** (12/235)<br>**M** (12/235) |
| **Govisetha** | **10** (19/234)<br>**44** (19/234)<br>**33** (18/234)<br>**19** (17/234)<br>**58** (17/234) | **P** (14/234)<br>**O** (12/234)<br>**D** (11/234)<br>**W** (11/234)<br>**K** (11/234) |
| **Handahana** | **58** (22/234)<br>**61** (22/234)<br>**21** (22/234)<br>**55** (22/234)<br>**6** (22/234) | N/A |
| **Mahajana Sampatha** | **1** (117/234)<br>**2** (115/234)<br>**6** (115/234)<br>**5** (114/234)<br>**4** (113/234) | **D** (14/234)<br>**J** (14/234)<br>**N** (13/234)<br>**Q** (13/234)<br>**Y** (12/234) |
| **Mega Power** | **11** (29/234)<br>**3** (28/234)<br>**13** (27/234)<br>**6** (26/234)<br>**22** (26/234) | **V** (17/234)<br>**T** (14/234)<br>**K** (14/234)<br>**U** (13/234)<br>**J** (12/234) |
| **Nlb Jaya** | **5** (97/225)<br>**0** (89/225)<br>**3** (87/225)<br>**2** (83/225)<br>**4** (80/225) | **P** (14/225)<br>**I** (14/225)<br>**T** (14/225)<br>**M** (13/225)<br>**G** (13/225) |
| **Suba Dawasak** | **3** (97/234)<br>**1** (93/234)<br>**4** (91/234)<br>**5** (87/234)<br>**9** (87/234) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (117/1753)<br>**57** (115/1753)<br>**20** (114/1753)<br>**13** (109/1753)<br>**38** (107/1753) | **B** (82/1753)<br>**M** (79/1753)<br>**R** (78/1753)<br>**P** (78/1753)<br>**I** (75/1753) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1641)<br>**10** (142/1641)<br>**29** (134/1641)<br>**21** (134/1641)<br>**27** (133/1641) | **H** (88/1641)<br>**U** (76/1641)<br>**W** (72/1641)<br>**G** (70/1641)<br>**X** (70/1641) |
| **Lagna Wasana** | **5** (135/1760)<br>**28** (134/1760)<br>**36** (131/1760)<br>**23** (130/1760)<br>**25** (130/1760) | N/A |
| **Sasiri** | **9** (71/938)<br>**20** (70/938)<br>**22** (68/938)<br>**26** (68/938)<br>**19** (67/938) | N/A |
| **Super Ball** | **45** (109/1754)<br>**52** (106/1754)<br>**74** (106/1754)<br>**29** (106/1754)<br>**3** (105/1754) | **I** (87/1754)<br>**D** (80/1754)<br>**T** (79/1754)<br>**V** (77/1754)<br>**A** (77/1754) |
| **Supiri Dhana Sampatha** | **0** (463/912)<br>**2** (459/912)<br>**3** (456/912)<br>**7** (449/912)<br>**5** (437/912) | **K** (44/912)<br>**V** (44/912)<br>**T** (43/912)<br>**S** (42/912)<br>**J** (42/912) |

