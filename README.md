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

> **Last Updated (Sri Lanka Time):** `2026-06-22 12:29:34 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 248 Rows | 11.97 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 256 Rows | 10.96 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 255 Rows | 10.80 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 255 Rows | 10.53 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 255 Rows | 10.86 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 255 Rows | 11.55 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 246 Rows | 9.59 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 255 Rows | 11.76 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1774 Rows | 67.85 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1662 Rows | 67.89 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1781 Rows | 66.38 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 959 Rows | 31.69 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1775 Rows | 67.88 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 933 Rows | 34.68 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-22 12:29:34 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (93/248)<br>**6** (92/248)<br>**0** (90/248)<br>**2** (87/248)<br>**7** (86/248) | **N** (15/248)<br>**J** (15/248)<br>**Q** (14/248)<br>**D** (14/248)<br>**Y** (13/248) |
| **Dhana Nidhanaya** | **9** (25/256)<br>**28** (24/256)<br>**6** (21/256)<br>**4** (20/256)<br>**7** (20/256) | **U** (17/256)<br>**F** (14/256)<br>**W** (13/256)<br>**Z** (12/256)<br>**T** (12/256) |
| **Govisetha** | **55** (21/255)<br>**10** (20/255)<br>**23** (20/255)<br>**44** (19/255)<br>**29** (19/255) | **P** (15/255)<br>**C** (14/255)<br>**D** (12/255)<br>**O** (12/255)<br>**M** (12/255) |
| **Handahana** | **58** (25/255)<br>**21** (25/255)<br>**6** (25/255)<br>**11** (23/255)<br>**55** (23/255) | N/A |
| **Mahajana Sampatha** | **1** (127/255)<br>**2** (125/255)<br>**6** (125/255)<br>**5** (124/255)<br>**3** (122/255) | **J** (15/255)<br>**N** (14/255)<br>**Q** (14/255)<br>**D** (14/255)<br>**Y** (13/255) |
| **Mega Power** | **11** (33/255)<br>**3** (29/255)<br>**22** (28/255)<br>**19** (28/255)<br>**13** (28/255) | **V** (18/255)<br>**U** (16/255)<br>**T** (15/255)<br>**K** (15/255)<br>**J** (14/255) |
| **Nlb Jaya** | **5** (109/246)<br>**3** (96/246)<br>**0** (95/246)<br>**2** (91/246)<br>**7** (87/246) | **T** (15/246)<br>**G** (15/246)<br>**P** (14/246)<br>**I** (14/246)<br>**Y** (14/246) |
| **Suba Dawasak** | **3** (107/255)<br>**1** (102/255)<br>**4** (102/255)<br>**9** (95/255)<br>**5** (92/255) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1774)<br>**20** (117/1774)<br>**57** (116/1774)<br>**75** (110/1774)<br>**38** (109/1774) | **B** (82/1774)<br>**R** (79/1774)<br>**P** (79/1774)<br>**M** (79/1774)<br>**I** (76/1774) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1662)<br>**10** (142/1662)<br>**29** (136/1662)<br>**21** (136/1662)<br>**27** (136/1662) | **H** (88/1662)<br>**U** (77/1662)<br>**X** (72/1662)<br>**W** (72/1662)<br>**G** (71/1662) |
| **Lagna Wasana** | **28** (136/1781)<br>**5** (135/1781)<br>**36** (133/1781)<br>**23** (132/1781)<br>**2** (131/1781) | N/A |
| **Sasiri** | **9** (73/959)<br>**20** (71/959)<br>**26** (71/959)<br>**22** (70/959)<br>**19** (67/959) | N/A |
| **Super Ball** | **45** (110/1775)<br>**52** (107/1775)<br>**74** (107/1775)<br>**3** (106/1775)<br>**57** (106/1775) | **I** (90/1775)<br>**D** (81/1775)<br>**V** (80/1775)<br>**T** (79/1775)<br>**A** (79/1775) |
| **Supiri Dhana Sampatha** | **0** (471/933)<br>**2** (470/933)<br>**3** (467/933)<br>**7** (458/933)<br>**5** (446/933) | **K** (46/933)<br>**V** (46/933)<br>**S** (43/933)<br>**M** (43/933)<br>**T** (43/933) |

