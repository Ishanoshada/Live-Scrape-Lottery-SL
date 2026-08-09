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

> **Last Updated (Sri Lanka Time):** `2026-08-09 11:28:19 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 297 Rows | 14.24 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 305 Rows | 13.00 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 304 Rows | 12.78 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 304 Rows | 12.46 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 304 Rows | 12.84 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 304 Rows | 13.67 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 295 Rows | 11.44 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 304 Rows | 13.93 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1823 Rows | 69.72 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1711 Rows | 69.91 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1830 Rows | 68.20 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1008 Rows | 33.37 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1824 Rows | 69.76 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 982 Rows | 36.51 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-09 11:28:19 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (111/297)<br>**2** (107/297)<br>**3** (104/297)<br>**6** (104/297)<br>**4** (102/297) | **D** (19/297)<br>**J** (18/297)<br>**Q** (17/297)<br>**N** (16/297)<br>**G** (16/297) |
| **Dhana Nidhanaya** | **9** (28/305)<br>**4** (27/305)<br>**7** (26/305)<br>**28** (25/305)<br>**80** (23/305) | **U** (20/305)<br>**Z** (16/305)<br>**F** (16/305)<br>**W** (16/305)<br>**T** (15/305) |
| **Govisetha** | **55** (25/304)<br>**10** (23/304)<br>**44** (23/304)<br>**33** (23/304)<br>**23** (22/304) | **C** (17/304)<br>**P** (16/304)<br>**K** (16/304)<br>**X** (15/304)<br>**O** (14/304) |
| **Handahana** | **58** (31/304)<br>**11** (29/304)<br>**55** (28/304)<br>**6** (28/304)<br>**21** (27/304) | N/A |
| **Mahajana Sampatha** | **5** (151/304)<br>**2** (150/304)<br>**1** (149/304)<br>**4** (148/304)<br>**7** (148/304) | **D** (19/304)<br>**J** (18/304)<br>**Q** (17/304)<br>**G** (16/304)<br>**N** (15/304) |
| **Mega Power** | **11** (36/304)<br>**13** (34/304)<br>**26** (33/304)<br>**6** (32/304)<br>**22** (32/304) | **T** (21/304)<br>**V** (20/304)<br>**U** (19/304)<br>**K** (17/304)<br>**J** (16/304) |
| **Nlb Jaya** | **5** (132/295)<br>**0** (116/295)<br>**2** (113/295)<br>**3** (112/295)<br>**7** (106/295) | **I** (18/295)<br>**T** (18/295)<br>**G** (16/295)<br>**Y** (15/295)<br>**M** (14/295) |
| **Suba Dawasak** | **3** (125/304)<br>**4** (123/304)<br>**1** (117/304)<br>**8** (113/304)<br>**9** (111/304) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1823)<br>**20** (120/1823)<br>**57** (117/1823)<br>**38** (114/1823)<br>**75** (112/1823) | **B** (84/1823)<br>**R** (83/1823)<br>**P** (80/1823)<br>**M** (80/1823)<br>**N** (78/1823) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (159/1711)<br>**10** (146/1711)<br>**6** (141/1711)<br>**21** (141/1711)<br>**15** (141/1711) | **H** (89/1711)<br>**U** (78/1711)<br>**M** (74/1711)<br>**D** (73/1711)<br>**G** (73/1711) |
| **Lagna Wasana** | **5** (140/1830)<br>**25** (136/1830)<br>**28** (136/1830)<br>**36** (135/1830)<br>**23** (135/1830) | N/A |
| **Sasiri** | **9** (75/1008)<br>**22** (74/1008)<br>**20** (74/1008)<br>**19** (73/1008)<br>**26** (72/1008) | N/A |
| **Super Ball** | **52** (111/1824)<br>**45** (111/1824)<br>**29** (111/1824)<br>**9** (109/1824)<br>**3** (108/1824) | **I** (92/1824)<br>**V** (82/1824)<br>**T** (82/1824)<br>**D** (82/1824)<br>**A** (79/1824) |
| **Supiri Dhana Sampatha** | **2** (496/982)<br>**0** (492/982)<br>**3** (486/982)<br>**7** (481/982)<br>**5** (469/982) | **V** (52/982)<br>**K** (46/982)<br>**T** (45/982)<br>**S** (44/982)<br>**J** (44/982) |

