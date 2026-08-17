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

> **Last Updated (Sri Lanka Time):** `2026-08-17 11:25:24 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 305 Rows | 14.62 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 313 Rows | 13.34 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 312 Rows | 13.12 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 312 Rows | 12.79 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 312 Rows | 13.18 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 312 Rows | 14.02 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 303 Rows | 11.75 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 312 Rows | 14.30 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1831 Rows | 70.02 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1719 Rows | 70.24 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1838 Rows | 68.50 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1016 Rows | 33.65 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1832 Rows | 70.06 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 990 Rows | 36.80 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-17 11:25:24 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (114/305)<br>**2** (111/305)<br>**3** (106/305)<br>**7** (106/305)<br>**6** (105/305) | **D** (19/305)<br>**J** (19/305)<br>**N** (17/305)<br>**Q** (17/305)<br>**G** (16/305) |
| **Dhana Nidhanaya** | **9** (29/313)<br>**4** (28/313)<br>**7** (27/313)<br>**28** (25/313)<br>**80** (24/313) | **U** (20/313)<br>**W** (17/313)<br>**M** (17/313)<br>**Z** (16/313)<br>**F** (16/313) |
| **Govisetha** | **55** (25/312)<br>**44** (24/312)<br>**29** (24/312)<br>**10** (23/312)<br>**33** (23/312) | **C** (17/312)<br>**P** (16/312)<br>**K** (16/312)<br>**X** (16/312)<br>**A** (14/312) |
| **Handahana** | **58** (31/312)<br>**11** (30/312)<br>**55** (29/312)<br>**21** (28/312)<br>**6** (28/312) | N/A |
| **Mahajana Sampatha** | **5** (155/312)<br>**2** (155/312)<br>**1** (155/312)<br>**7** (153/312)<br>**4** (151/312) | **D** (19/312)<br>**J** (19/312)<br>**Q** (17/312)<br>**N** (16/312)<br>**G** (16/312) |
| **Mega Power** | **11** (37/312)<br>**26** (35/312)<br>**13** (34/312)<br>**3** (33/312)<br>**6** (32/312) | **T** (22/312)<br>**V** (20/312)<br>**U** (20/312)<br>**K** (17/312)<br>**J** (16/312) |
| **Nlb Jaya** | **5** (133/303)<br>**0** (117/303)<br>**3** (116/303)<br>**2** (116/303)<br>**7** (110/303) | **I** (18/303)<br>**T** (18/303)<br>**G** (16/303)<br>**P** (15/303)<br>**H** (15/303) |
| **Suba Dawasak** | **3** (128/312)<br>**4** (127/312)<br>**1** (120/312)<br>**8** (118/312)<br>**9** (114/312) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1831)<br>**20** (120/1831)<br>**57** (117/1831)<br>**38** (116/1831)<br>**75** (112/1831) | **B** (85/1831)<br>**R** (84/1831)<br>**M** (81/1831)<br>**P** (80/1831)<br>**N** (78/1831) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1719)<br>**10** (146/1719)<br>**6** (142/1719)<br>**21** (141/1719)<br>**15** (141/1719) | **H** (89/1719)<br>**U** (78/1719)<br>**M** (75/1719)<br>**D** (74/1719)<br>**G** (73/1719) |
| **Lagna Wasana** | **5** (140/1838)<br>**36** (137/1838)<br>**28** (137/1838)<br>**23** (136/1838)<br>**25** (136/1838) | N/A |
| **Sasiri** | **9** (77/1016)<br>**22** (74/1016)<br>**20** (74/1016)<br>**19** (74/1016)<br>**26** (74/1016) | N/A |
| **Super Ball** | **52** (111/1832)<br>**45** (111/1832)<br>**29** (111/1832)<br>**9** (109/1832)<br>**3** (108/1832) | **I** (92/1832)<br>**V** (82/1832)<br>**T** (82/1832)<br>**D** (82/1832)<br>**A** (81/1832) |
| **Supiri Dhana Sampatha** | **2** (499/990)<br>**0** (497/990)<br>**3** (490/990)<br>**7** (486/990)<br>**5** (473/990) | **V** (53/990)<br>**K** (46/990)<br>**T** (45/990)<br>**S** (44/990)<br>**J** (44/990) |

