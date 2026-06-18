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

> **Last Updated (Sri Lanka Time):** `2026-06-19 01:09:08 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 245 Rows | 11.83 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 253 Rows | 10.83 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 252 Rows | 10.68 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 252 Rows | 10.42 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 252 Rows | 10.74 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 252 Rows | 11.42 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 243 Rows | 9.47 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 252 Rows | 11.63 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1771 Rows | 67.73 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1659 Rows | 67.77 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1778 Rows | 66.27 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 956 Rows | 31.59 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1772 Rows | 67.77 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 930 Rows | 34.57 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-19 01:09:08 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (91/245)<br>**5** (91/245)<br>**0** (89/245)<br>**2** (86/245)<br>**7** (85/245) | **J** (15/245)<br>**N** (14/245)<br>**Q** (14/245)<br>**D** (14/245)<br>**Y** (13/245) |
| **Dhana Nidhanaya** | **28** (24/253)<br>**9** (24/253)<br>**6** (21/253)<br>**16** (20/253)<br>**4** (19/253) | **U** (16/253)<br>**W** (13/253)<br>**Z** (12/253)<br>**T** (12/253)<br>**S** (12/253) |
| **Govisetha** | **55** (21/252)<br>**10** (20/252)<br>**23** (19/252)<br>**44** (19/252)<br>**33** (19/252) | **P** (15/252)<br>**C** (14/252)<br>**D** (12/252)<br>**O** (12/252)<br>**M** (12/252) |
| **Handahana** | **21** (25/252)<br>**6** (25/252)<br>**58** (24/252)<br>**11** (23/252)<br>**55** (23/252) | N/A |
| **Mahajana Sampatha** | **1** (126/252)<br>**6** (124/252)<br>**2** (123/252)<br>**5** (122/252)<br>**4** (120/252) | **J** (15/252)<br>**Q** (14/252)<br>**D** (14/252)<br>**N** (13/252)<br>**Y** (13/252) |
| **Mega Power** | **11** (32/252)<br>**3** (29/252)<br>**22** (28/252)<br>**13** (28/252)<br>**6** (27/252) | **V** (18/252)<br>**U** (16/252)<br>**K** (15/252)<br>**T** (14/252)<br>**J** (14/252) |
| **Nlb Jaya** | **5** (107/243)<br>**0** (95/243)<br>**3** (94/243)<br>**2** (90/243)<br>**7** (86/243) | **T** (15/243)<br>**G** (15/243)<br>**P** (14/243)<br>**I** (14/243)<br>**Y** (14/243) |
| **Suba Dawasak** | **3** (105/252)<br>**4** (101/252)<br>**1** (100/252)<br>**9** (95/252)<br>**5** (90/252) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1771)<br>**20** (117/1771)<br>**57** (115/1771)<br>**75** (110/1771)<br>**38** (109/1771) | **B** (82/1771)<br>**P** (79/1771)<br>**M** (79/1771)<br>**R** (78/1771)<br>**I** (76/1771) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1659)<br>**10** (142/1659)<br>**21** (136/1659)<br>**27** (136/1659)<br>**29** (135/1659) | **H** (88/1659)<br>**U** (77/1659)<br>**X** (72/1659)<br>**W** (72/1659)<br>**G** (71/1659) |
| **Lagna Wasana** | **28** (136/1778)<br>**5** (135/1778)<br>**36** (133/1778)<br>**23** (132/1778)<br>**2** (131/1778) | N/A |
| **Sasiri** | **9** (73/956)<br>**20** (71/956)<br>**26** (71/956)<br>**22** (69/956)<br>**19** (67/956) | N/A |
| **Super Ball** | **45** (110/1772)<br>**52** (107/1772)<br>**74** (107/1772)<br>**3** (106/1772)<br>**57** (106/1772) | **I** (89/1772)<br>**D** (81/1772)<br>**V** (80/1772)<br>**T** (79/1772)<br>**A** (79/1772) |
| **Supiri Dhana Sampatha** | **0** (470/930)<br>**2** (469/930)<br>**3** (466/930)<br>**7** (455/930)<br>**5** (445/930) | **K** (46/930)<br>**V** (45/930)<br>**S** (43/930)<br>**M** (43/930)<br>**T** (43/930) |

