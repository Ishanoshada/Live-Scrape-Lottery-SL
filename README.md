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

> **Last Updated (Sri Lanka Time):** `2026-06-29 12:14:30 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 255 Rows | 12.29 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 263 Rows | 11.25 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 262 Rows | 11.08 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 262 Rows | 10.81 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 262 Rows | 11.14 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 262 Rows | 11.85 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 253 Rows | 9.85 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 262 Rows | 12.07 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1781 Rows | 68.11 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1669 Rows | 68.18 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1788 Rows | 66.64 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 966 Rows | 31.93 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1782 Rows | 68.15 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 940 Rows | 34.94 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-29 12:14:30 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (96/255)<br>**5** (95/255)<br>**0** (90/255)<br>**7** (90/255)<br>**2** (90/255) | **N** (15/255)<br>**Q** (15/255)<br>**J** (15/255)<br>**G** (15/255)<br>**D** (14/255) |
| **Dhana Nidhanaya** | **9** (25/263)<br>**28** (24/263)<br>**7** (23/263)<br>**4** (21/263)<br>**6** (21/263) | **U** (17/263)<br>**F** (14/263)<br>**W** (14/263)<br>**Z** (12/263)<br>**T** (12/263) |
| **Govisetha** | **10** (21/262)<br>**55** (21/262)<br>**23** (20/262)<br>**29** (20/262)<br>**44** (19/262) | **P** (15/262)<br>**C** (14/262)<br>**D** (13/262)<br>**A** (12/262)<br>**O** (12/262) |
| **Handahana** | **58** (26/262)<br>**21** (26/262)<br>**11** (25/262)<br>**6** (25/262)<br>**61** (23/262) | N/A |
| **Mahajana Sampatha** | **6** (130/262)<br>**2** (129/262)<br>**5** (129/262)<br>**1** (129/262)<br>**7** (127/262) | **Q** (15/262)<br>**J** (15/262)<br>**G** (15/262)<br>**N** (14/262)<br>**D** (14/262) |
| **Mega Power** | **11** (36/262)<br>**3** (31/262)<br>**13** (29/262)<br>**6** (28/262)<br>**22** (28/262) | **V** (19/262)<br>**U** (18/262)<br>**T** (17/262)<br>**K** (15/262)<br>**J** (15/262) |
| **Nlb Jaya** | **5** (114/253)<br>**3** (98/253)<br>**0** (97/253)<br>**2** (96/253)<br>**1** (90/253) | **G** (16/253)<br>**I** (15/253)<br>**T** (15/253)<br>**P** (14/253)<br>**Y** (14/253) |
| **Suba Dawasak** | **3** (110/262)<br>**4** (106/262)<br>**1** (103/262)<br>**9** (95/262)<br>**2** (95/262) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1781)<br>**20** (119/1781)<br>**57** (116/1781)<br>**75** (110/1781)<br>**38** (109/1781) | **B** (82/1781)<br>**R** (81/1781)<br>**P** (79/1781)<br>**M** (79/1781)<br>**I** (76/1781) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1669)<br>**10** (143/1669)<br>**27** (137/1669)<br>**29** (136/1669)<br>**21** (136/1669) | **H** (88/1669)<br>**U** (77/1669)<br>**M** (73/1669)<br>**X** (72/1669)<br>**W** (72/1669) |
| **Lagna Wasana** | **28** (136/1788)<br>**5** (135/1788)<br>**36** (133/1788)<br>**23** (132/1788)<br>**2** (131/1788) | N/A |
| **Sasiri** | **9** (73/966)<br>**20** (71/966)<br>**26** (71/966)<br>**22** (70/966)<br>**5** (68/966) | N/A |
| **Super Ball** | **45** (110/1782)<br>**52** (108/1782)<br>**74** (107/1782)<br>**29** (107/1782)<br>**3** (106/1782) | **I** (90/1782)<br>**D** (81/1782)<br>**V** (80/1782)<br>**T** (80/1782)<br>**A** (79/1782) |
| **Supiri Dhana Sampatha** | **2** (475/940)<br>**0** (472/940)<br>**3** (472/940)<br>**7** (460/940)<br>**5** (450/940) | **K** (46/940)<br>**V** (46/940)<br>**S** (43/940)<br>**M** (43/940)<br>**T** (43/940) |

