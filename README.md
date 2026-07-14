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

> **Last Updated (Sri Lanka Time):** `2026-07-15 12:08:39 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 271 Rows | 13.02 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 279 Rows | 11.90 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 278 Rows | 11.72 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 278 Rows | 11.43 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 278 Rows | 11.78 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 278 Rows | 12.54 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 269 Rows | 10.45 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 278 Rows | 12.77 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1797 Rows | 68.72 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1685 Rows | 68.84 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1804 Rows | 67.23 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 982 Rows | 32.48 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1798 Rows | 68.76 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 956 Rows | 35.54 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-15 12:08:40 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (100/271)<br>**6** (98/271)<br>**2** (96/271)<br>**7** (95/271)<br>**4** (94/271) | **Q** (17/271)<br>**N** (16/271)<br>**D** (16/271)<br>**J** (16/271)<br>**G** (15/271) |
| **Dhana Nidhanaya** | **9** (26/279)<br>**28** (24/279)<br>**7** (24/279)<br>**4** (23/279)<br>**6** (23/279) | **U** (17/279)<br>**F** (15/279)<br>**W** (15/279)<br>**Z** (14/279)<br>**T** (13/279) |
| **Govisetha** | **55** (23/278)<br>**10** (21/278)<br>**44** (21/278)<br>**23** (20/278)<br>**29** (20/278) | **P** (16/278)<br>**C** (15/278)<br>**K** (14/278)<br>**D** (13/278)<br>**A** (13/278) |
| **Handahana** | **58** (29/278)<br>**11** (27/278)<br>**21** (27/278)<br>**6** (26/278)<br>**55** (25/278) | N/A |
| **Mahajana Sampatha** | **2** (137/278)<br>**4** (136/278)<br>**5** (136/278)<br>**6** (136/278)<br>**7** (135/278) | **Q** (17/278)<br>**D** (16/278)<br>**J** (16/278)<br>**N** (15/278)<br>**G** (15/278) |
| **Mega Power** | **11** (36/278)<br>**6** (31/278)<br>**3** (31/278)<br>**22** (30/278)<br>**19** (30/278) | **T** (19/278)<br>**V** (19/278)<br>**U** (19/278)<br>**J** (16/278)<br>**K** (15/278) |
| **Nlb Jaya** | **5** (120/269)<br>**3** (103/269)<br>**2** (103/269)<br>**0** (103/269)<br>**7** (97/269) | **T** (17/269)<br>**I** (16/269)<br>**G** (16/269)<br>**M** (14/269)<br>**P** (14/269) |
| **Suba Dawasak** | **3** (114/278)<br>**4** (113/278)<br>**1** (108/278)<br>**8** (103/278)<br>**5** (100/278) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (121/1797)<br>**20** (119/1797)<br>**57** (116/1797)<br>**75** (111/1797)<br>**38** (111/1797) | **B** (82/1797)<br>**R** (81/1797)<br>**P** (80/1797)<br>**M** (80/1797)<br>**I** (77/1797) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1685)<br>**10** (145/1685)<br>**29** (138/1685)<br>**27** (138/1685)<br>**15** (138/1685) | **H** (88/1685)<br>**U** (77/1685)<br>**M** (73/1685)<br>**X** (72/1685)<br>**W** (72/1685) |
| **Lagna Wasana** | **5** (139/1804)<br>**28** (136/1804)<br>**36** (134/1804)<br>**25** (134/1804)<br>**39** (132/1804) | N/A |
| **Sasiri** | **9** (74/982)<br>**20** (73/982)<br>**22** (71/982)<br>**26** (71/982)<br>**5** (69/982) | N/A |
| **Super Ball** | **52** (110/1798)<br>**45** (110/1798)<br>**29** (110/1798)<br>**74** (107/1798)<br>**57** (107/1798) | **I** (90/1798)<br>**V** (81/1798)<br>**T** (81/1798)<br>**D** (81/1798)<br>**A** (79/1798) |
| **Supiri Dhana Sampatha** | **2** (484/956)<br>**0** (478/956)<br>**3** (478/956)<br>**7** (470/956)<br>**5** (455/956) | **V** (49/956)<br>**K** (46/956)<br>**S** (44/956)<br>**J** (44/956)<br>**T** (44/956) |

