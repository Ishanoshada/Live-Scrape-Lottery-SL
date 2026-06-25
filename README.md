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

> **Last Updated (Sri Lanka Time):** `2026-06-26 12:53:29 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 252 Rows | 12.15 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 260 Rows | 11.12 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 259 Rows | 10.96 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 259 Rows | 10.69 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 259 Rows | 11.02 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 259 Rows | 11.72 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 250 Rows | 9.74 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 259 Rows | 11.94 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1778 Rows | 68.00 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1666 Rows | 68.06 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1785 Rows | 66.53 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 963 Rows | 31.83 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1779 Rows | 68.04 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 937 Rows | 34.83 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-26 12:53:29 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (95/252)<br>**5** (95/252)<br>**0** (90/252)<br>**2** (90/252)<br>**7** (89/252) | **N** (15/252)<br>**Q** (15/252)<br>**J** (15/252)<br>**D** (14/252)<br>**Y** (13/252) |
| **Dhana Nidhanaya** | **9** (25/260)<br>**28** (24/260)<br>**7** (22/260)<br>**4** (21/260)<br>**6** (21/260) | **U** (17/260)<br>**F** (14/260)<br>**W** (13/260)<br>**Z** (12/260)<br>**T** (12/260) |
| **Govisetha** | **55** (21/259)<br>**10** (20/259)<br>**23** (20/259)<br>**44** (19/259)<br>**29** (19/259) | **P** (15/259)<br>**C** (14/259)<br>**D** (12/259)<br>**A** (12/259)<br>**O** (12/259) |
| **Handahana** | **58** (26/259)<br>**21** (25/259)<br>**6** (25/259)<br>**11** (24/259)<br>**55** (23/259) | N/A |
| **Mahajana Sampatha** | **5** (128/259)<br>**2** (128/259)<br>**6** (128/259)<br>**1** (127/259)<br>**4** (125/259) | **Q** (15/259)<br>**J** (15/259)<br>**N** (14/259)<br>**D** (14/259)<br>**Y** (13/259) |
| **Mega Power** | **11** (35/259)<br>**3** (31/259)<br>**13** (29/259)<br>**22** (28/259)<br>**19** (28/259) | **V** (18/259)<br>**U** (17/259)<br>**T** (16/259)<br>**K** (15/259)<br>**J** (15/259) |
| **Nlb Jaya** | **5** (111/250)<br>**3** (96/250)<br>**0** (96/250)<br>**2** (95/250)<br>**7** (88/250) | **T** (15/250)<br>**G** (15/250)<br>**P** (14/250)<br>**I** (14/250)<br>**Y** (14/250) |
| **Suba Dawasak** | **3** (108/259)<br>**4** (105/259)<br>**1** (103/259)<br>**9** (95/259)<br>**5** (93/259) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1778)<br>**20** (118/1778)<br>**57** (116/1778)<br>**75** (110/1778)<br>**38** (109/1778) | **B** (82/1778)<br>**R** (80/1778)<br>**P** (79/1778)<br>**M** (79/1778)<br>**I** (76/1778) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1666)<br>**10** (142/1666)<br>**27** (137/1666)<br>**29** (136/1666)<br>**21** (136/1666) | **H** (88/1666)<br>**U** (77/1666)<br>**M** (72/1666)<br>**X** (72/1666)<br>**W** (72/1666) |
| **Lagna Wasana** | **28** (136/1785)<br>**5** (135/1785)<br>**36** (133/1785)<br>**23** (132/1785)<br>**2** (131/1785) | N/A |
| **Sasiri** | **9** (73/963)<br>**20** (71/963)<br>**26** (71/963)<br>**22** (70/963)<br>**5** (67/963) | N/A |
| **Super Ball** | **45** (110/1779)<br>**52** (108/1779)<br>**74** (107/1779)<br>**29** (107/1779)<br>**3** (106/1779) | **I** (90/1779)<br>**D** (81/1779)<br>**V** (80/1779)<br>**T** (79/1779)<br>**A** (79/1779) |
| **Supiri Dhana Sampatha** | **2** (473/937)<br>**0** (471/937)<br>**3** (470/937)<br>**7** (458/937)<br>**5** (448/937) | **K** (46/937)<br>**V** (46/937)<br>**S** (43/937)<br>**M** (43/937)<br>**T** (43/937) |

