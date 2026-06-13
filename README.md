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

> **Last Updated (Sri Lanka Time):** `2026-06-14 12:22:27 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 240 Rows | 11.60 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 248 Rows | 10.62 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 247 Rows | 10.48 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 247 Rows | 10.22 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 247 Rows | 10.54 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 247 Rows | 11.21 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 238 Rows | 9.29 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 247 Rows | 11.41 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1766 Rows | 67.54 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1654 Rows | 67.56 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1773 Rows | 66.08 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 951 Rows | 31.42 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1767 Rows | 67.58 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 925 Rows | 34.38 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-14 12:22:27 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (90/240)<br>**5** (90/240)<br>**0** (86/240)<br>**7** (85/240)<br>**3** (82/240) | **J** (15/240)<br>**N** (14/240)<br>**Q** (14/240)<br>**D** (14/240)<br>**Y** (12/240) |
| **Dhana Nidhanaya** | **28** (24/248)<br>**9** (23/248)<br>**6** (21/248)<br>**16** (20/248)<br>**4** (19/248) | **U** (16/248)<br>**W** (13/248)<br>**Z** (12/248)<br>**T** (12/248)<br>**S** (12/248) |
| **Govisetha** | **55** (21/247)<br>**10** (20/247)<br>**44** (19/247)<br>**33** (19/247)<br>**19** (17/247) | **P** (15/247)<br>**C** (13/247)<br>**D** (12/247)<br>**O** (12/247)<br>**M** (12/247) |
| **Handahana** | **21** (25/247)<br>**6** (25/247)<br>**55** (23/247)<br>**58** (22/247)<br>**11** (22/247) | N/A |
| **Mahajana Sampatha** | **1** (124/247)<br>**5** (121/247)<br>**6** (120/247)<br>**4** (119/247)<br>**3** (119/247) | **J** (15/247)<br>**Q** (14/247)<br>**D** (14/247)<br>**N** (13/247)<br>**Y** (12/247) |
| **Mega Power** | **11** (32/247)<br>**3** (29/247)<br>**6** (27/247)<br>**22** (27/247)<br>**19** (27/247) | **V** (18/247)<br>**T** (14/247)<br>**K** (14/247)<br>**J** (14/247)<br>**U** (14/247) |
| **Nlb Jaya** | **5** (103/238)<br>**0** (93/238)<br>**3** (92/238)<br>**2** (90/238)<br>**1** (85/238) | **T** (15/238)<br>**P** (14/238)<br>**I** (14/238)<br>**Y** (14/238)<br>**M** (13/238) |
| **Suba Dawasak** | **3** (103/247)<br>**4** (100/247)<br>**1** (98/247)<br>**9** (92/247)<br>**5** (90/247) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1766)<br>**20** (117/1766)<br>**57** (115/1766)<br>**38** (109/1766)<br>**13** (109/1766) | **B** (82/1766)<br>**P** (79/1766)<br>**M** (79/1766)<br>**R** (78/1766)<br>**I** (76/1766) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1654)<br>**10** (142/1654)<br>**29** (134/1654)<br>**21** (134/1654)<br>**27** (134/1654) | **H** (88/1654)<br>**U** (76/1654)<br>**W** (72/1654)<br>**G** (71/1654)<br>**X** (71/1654) |
| **Lagna Wasana** | **28** (135/1773)<br>**5** (135/1773)<br>**36** (133/1773)<br>**2** (131/1773)<br>**23** (131/1773) | N/A |
| **Sasiri** | **9** (72/951)<br>**20** (71/951)<br>**26** (70/951)<br>**22** (69/951)<br>**19** (67/951) | N/A |
| **Super Ball** | **45** (110/1767)<br>**52** (107/1767)<br>**74** (107/1767)<br>**3** (106/1767)<br>**29** (106/1767) | **I** (88/1767)<br>**D** (81/1767)<br>**V** (79/1767)<br>**T** (79/1767)<br>**A** (79/1767) |
| **Supiri Dhana Sampatha** | **2** (468/925)<br>**0** (467/925)<br>**3** (462/925)<br>**7** (453/925)<br>**5** (443/925) | **K** (46/925)<br>**V** (44/925)<br>**S** (43/925)<br>**M** (43/925)<br>**T** (43/925) |

