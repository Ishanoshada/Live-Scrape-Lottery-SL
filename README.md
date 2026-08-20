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

> **Last Updated (Sri Lanka Time):** `2026-08-20 11:25:57 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 308 Rows | 14.77 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 316 Rows | 13.47 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 315 Rows | 13.25 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 315 Rows | 12.91 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 315 Rows | 13.31 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 315 Rows | 14.16 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 306 Rows | 11.87 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 315 Rows | 14.44 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1834 Rows | 70.14 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1722 Rows | 70.36 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1841 Rows | 68.61 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1019 Rows | 33.75 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1835 Rows | 70.18 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 993 Rows | 36.92 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-20 11:25:57 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (114/308)<br>**2** (112/308)<br>**7** (107/308)<br>**6** (106/308)<br>**3** (106/308) | **D** (19/308)<br>**J** (19/308)<br>**N** (17/308)<br>**Q** (17/308)<br>**G** (16/308) |
| **Dhana Nidhanaya** | **9** (29/316)<br>**4** (28/316)<br>**7** (27/316)<br>**28** (25/316)<br>**80** (24/316) | **U** (20/316)<br>**W** (17/316)<br>**M** (17/316)<br>**Z** (16/316)<br>**F** (16/316) |
| **Govisetha** | **55** (25/315)<br>**44** (24/315)<br>**29** (24/315)<br>**10** (23/315)<br>**33** (23/315) | **P** (18/315)<br>**C** (17/315)<br>**X** (17/315)<br>**K** (16/315)<br>**A** (14/315) |
| **Handahana** | **58** (31/315)<br>**11** (30/315)<br>**55** (29/315)<br>**21** (28/315)<br>**6** (28/315) | N/A |
| **Mahajana Sampatha** | **5** (156/315)<br>**2** (156/315)<br>**1** (156/315)<br>**7** (154/315)<br>**4** (152/315) | **D** (19/315)<br>**J** (19/315)<br>**Q** (17/315)<br>**N** (16/315)<br>**G** (16/315) |
| **Mega Power** | **11** (37/315)<br>**26** (35/315)<br>**3** (34/315)<br>**13** (34/315)<br>**6** (32/315) | **T** (22/315)<br>**V** (20/315)<br>**U** (20/315)<br>**K** (17/315)<br>**J** (17/315) |
| **Nlb Jaya** | **5** (135/306)<br>**0** (118/306)<br>**2** (117/306)<br>**3** (116/306)<br>**7** (110/306) | **I** (18/306)<br>**T** (18/306)<br>**G** (16/306)<br>**P** (15/306)<br>**H** (15/306) |
| **Suba Dawasak** | **3** (130/315)<br>**4** (127/315)<br>**1** (121/315)<br>**8** (119/315)<br>**9** (115/315) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1834)<br>**20** (121/1834)<br>**57** (117/1834)<br>**38** (116/1834)<br>**75** (112/1834) | **B** (85/1834)<br>**R** (84/1834)<br>**M** (81/1834)<br>**P** (80/1834)<br>**N** (78/1834) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1722)<br>**10** (146/1722)<br>**6** (142/1722)<br>**29** (142/1722)<br>**21** (141/1722) | **H** (89/1722)<br>**U** (78/1722)<br>**M** (76/1722)<br>**D** (74/1722)<br>**G** (73/1722) |
| **Lagna Wasana** | **5** (140/1841)<br>**36** (137/1841)<br>**28** (137/1841)<br>**23** (136/1841)<br>**25** (136/1841) | N/A |
| **Sasiri** | **9** (78/1019)<br>**22** (75/1019)<br>**20** (74/1019)<br>**19** (74/1019)<br>**26** (74/1019) | N/A |
| **Super Ball** | **52** (111/1835)<br>**45** (111/1835)<br>**29** (111/1835)<br>**9** (110/1835)<br>**3** (108/1835) | **I** (92/1835)<br>**V** (82/1835)<br>**T** (82/1835)<br>**D** (82/1835)<br>**A** (81/1835) |
| **Supiri Dhana Sampatha** | **2** (499/993)<br>**0** (498/993)<br>**3** (490/993)<br>**7** (488/993)<br>**5** (474/993) | **V** (53/993)<br>**K** (46/993)<br>**T** (45/993)<br>**S** (44/993)<br>**G** (44/993) |

