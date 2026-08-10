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

> **Last Updated (Sri Lanka Time):** `2026-08-10 11:42:38 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 298 Rows | 14.29 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 306 Rows | 13.04 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 305 Rows | 12.82 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 305 Rows | 12.50 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 305 Rows | 12.88 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 305 Rows | 13.71 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 296 Rows | 11.48 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 305 Rows | 13.98 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1824 Rows | 69.76 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1712 Rows | 69.95 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1831 Rows | 68.24 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1009 Rows | 33.41 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1825 Rows | 69.79 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 983 Rows | 36.54 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-10 11:42:38 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (112/298)<br>**2** (107/298)<br>**3** (104/298)<br>**6** (104/298)<br>**7** (103/298) | **D** (19/298)<br>**J** (18/298)<br>**Q** (17/298)<br>**N** (16/298)<br>**G** (16/298) |
| **Dhana Nidhanaya** | **9** (28/306)<br>**4** (27/306)<br>**7** (26/306)<br>**28** (25/306)<br>**80** (24/306) | **U** (20/306)<br>**Z** (16/306)<br>**F** (16/306)<br>**W** (16/306)<br>**T** (15/306) |
| **Govisetha** | **55** (25/305)<br>**10** (23/305)<br>**44** (23/305)<br>**33** (23/305)<br>**23** (22/305) | **C** (17/305)<br>**P** (16/305)<br>**K** (16/305)<br>**X** (16/305)<br>**O** (14/305) |
| **Handahana** | **58** (31/305)<br>**11** (29/305)<br>**55** (28/305)<br>**6** (28/305)<br>**21** (27/305) | N/A |
| **Mahajana Sampatha** | **5** (152/305)<br>**2** (150/305)<br>**1** (150/305)<br>**7** (149/305)<br>**4** (148/305) | **D** (19/305)<br>**J** (18/305)<br>**Q** (17/305)<br>**G** (16/305)<br>**N** (15/305) |
| **Mega Power** | **11** (36/305)<br>**26** (34/305)<br>**13** (34/305)<br>**22** (32/305)<br>**6** (32/305) | **T** (21/305)<br>**V** (20/305)<br>**U** (20/305)<br>**K** (17/305)<br>**J** (16/305) |
| **Nlb Jaya** | **5** (132/296)<br>**0** (116/296)<br>**3** (113/296)<br>**2** (113/296)<br>**7** (107/296) | **I** (18/296)<br>**T** (18/296)<br>**G** (16/296)<br>**P** (15/296)<br>**Y** (15/296) |
| **Suba Dawasak** | **3** (126/305)<br>**4** (124/305)<br>**1** (118/305)<br>**8** (113/305)<br>**9** (112/305) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1824)<br>**20** (120/1824)<br>**57** (117/1824)<br>**38** (114/1824)<br>**75** (112/1824) | **B** (84/1824)<br>**R** (83/1824)<br>**P** (80/1824)<br>**M** (80/1824)<br>**N** (78/1824) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (159/1712)<br>**10** (146/1712)<br>**6** (141/1712)<br>**21** (141/1712)<br>**15** (141/1712) | **H** (89/1712)<br>**U** (78/1712)<br>**M** (75/1712)<br>**D** (73/1712)<br>**G** (73/1712) |
| **Lagna Wasana** | **5** (140/1831)<br>**25** (136/1831)<br>**28** (136/1831)<br>**36** (135/1831)<br>**23** (135/1831) | N/A |
| **Sasiri** | **9** (76/1009)<br>**22** (74/1009)<br>**20** (74/1009)<br>**19** (73/1009)<br>**26** (72/1009) | N/A |
| **Super Ball** | **52** (111/1825)<br>**45** (111/1825)<br>**29** (111/1825)<br>**9** (109/1825)<br>**3** (108/1825) | **I** (92/1825)<br>**V** (82/1825)<br>**T** (82/1825)<br>**D** (82/1825)<br>**A** (79/1825) |
| **Supiri Dhana Sampatha** | **2** (496/983)<br>**0** (492/983)<br>**3** (486/983)<br>**7** (481/983)<br>**5** (470/983) | **V** (52/983)<br>**K** (46/983)<br>**T** (45/983)<br>**S** (44/983)<br>**J** (44/983) |

