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

> **Last Updated (Sri Lanka Time):** `2026-06-25 12:40:03 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 251 Rows | 12.10 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 259 Rows | 11.08 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 258 Rows | 10.92 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 258 Rows | 10.65 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 258 Rows | 10.98 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 258 Rows | 11.68 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 249 Rows | 9.70 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 258 Rows | 11.90 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1777 Rows | 67.96 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1665 Rows | 68.02 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1784 Rows | 66.49 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 962 Rows | 31.79 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1778 Rows | 68.00 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 936 Rows | 34.79 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-25 12:40:03 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (95/251)<br>**6** (94/251)<br>**0** (90/251)<br>**2** (89/251)<br>**7** (88/251) | **N** (15/251)<br>**Q** (15/251)<br>**J** (15/251)<br>**D** (14/251)<br>**Y** (13/251) |
| **Dhana Nidhanaya** | **9** (25/259)<br>**28** (24/259)<br>**7** (22/259)<br>**4** (21/259)<br>**6** (21/259) | **U** (17/259)<br>**F** (14/259)<br>**W** (13/259)<br>**Z** (12/259)<br>**T** (12/259) |
| **Govisetha** | **55** (21/258)<br>**10** (20/258)<br>**23** (20/258)<br>**44** (19/258)<br>**29** (19/258) | **P** (15/258)<br>**C** (14/258)<br>**D** (12/258)<br>**A** (12/258)<br>**O** (12/258) |
| **Handahana** | **58** (26/258)<br>**21** (25/258)<br>**6** (25/258)<br>**11** (24/258)<br>**55** (23/258) | N/A |
| **Mahajana Sampatha** | **5** (127/258)<br>**2** (127/258)<br>**1** (127/258)<br>**6** (127/258)<br>**4** (124/258) | **Q** (15/258)<br>**J** (15/258)<br>**N** (14/258)<br>**D** (14/258)<br>**Y** (13/258) |
| **Mega Power** | **11** (35/258)<br>**3** (30/258)<br>**13** (29/258)<br>**22** (28/258)<br>**19** (28/258) | **V** (18/258)<br>**T** (16/258)<br>**U** (16/258)<br>**K** (15/258)<br>**J** (15/258) |
| **Nlb Jaya** | **5** (110/249)<br>**3** (96/249)<br>**0** (96/249)<br>**2** (94/249)<br>**1** (88/249) | **T** (15/249)<br>**G** (15/249)<br>**P** (14/249)<br>**I** (14/249)<br>**Y** (14/249) |
| **Suba Dawasak** | **3** (107/258)<br>**4** (105/258)<br>**1** (103/258)<br>**9** (95/258)<br>**5** (92/258) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1777)<br>**20** (118/1777)<br>**57** (116/1777)<br>**75** (110/1777)<br>**38** (109/1777) | **B** (82/1777)<br>**R** (80/1777)<br>**P** (79/1777)<br>**M** (79/1777)<br>**I** (76/1777) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1665)<br>**10** (142/1665)<br>**27** (137/1665)<br>**29** (136/1665)<br>**21** (136/1665) | **H** (88/1665)<br>**U** (77/1665)<br>**M** (72/1665)<br>**X** (72/1665)<br>**W** (72/1665) |
| **Lagna Wasana** | **28** (136/1784)<br>**5** (135/1784)<br>**36** (133/1784)<br>**23** (132/1784)<br>**2** (131/1784) | N/A |
| **Sasiri** | **9** (73/962)<br>**20** (71/962)<br>**26** (71/962)<br>**22** (70/962)<br>**5** (67/962) | N/A |
| **Super Ball** | **45** (110/1778)<br>**52** (108/1778)<br>**74** (107/1778)<br>**29** (107/1778)<br>**3** (106/1778) | **I** (90/1778)<br>**D** (81/1778)<br>**V** (80/1778)<br>**T** (79/1778)<br>**A** (79/1778) |
| **Supiri Dhana Sampatha** | **2** (473/936)<br>**0** (471/936)<br>**3** (469/936)<br>**7** (458/936)<br>**5** (448/936) | **K** (46/936)<br>**V** (46/936)<br>**S** (43/936)<br>**M** (43/936)<br>**T** (43/936) |

