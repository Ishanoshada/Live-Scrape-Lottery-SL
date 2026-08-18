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

> **Last Updated (Sri Lanka Time):** `2026-08-18 11:24:01 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 306 Rows | 14.67 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 314 Rows | 13.38 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 313 Rows | 13.16 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 313 Rows | 12.83 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 313 Rows | 13.22 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 313 Rows | 14.07 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 304 Rows | 11.79 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 313 Rows | 14.35 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1832 Rows | 70.06 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1720 Rows | 70.28 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1839 Rows | 68.54 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1017 Rows | 33.68 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1833 Rows | 70.10 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 991 Rows | 36.84 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-18 11:24:01 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (114/306)<br>**2** (111/306)<br>**7** (107/306)<br>**3** (106/306)<br>**6** (105/306) | **D** (19/306)<br>**J** (19/306)<br>**N** (17/306)<br>**Q** (17/306)<br>**G** (16/306) |
| **Dhana Nidhanaya** | **9** (29/314)<br>**4** (28/314)<br>**7** (27/314)<br>**28** (25/314)<br>**80** (24/314) | **U** (20/314)<br>**W** (17/314)<br>**M** (17/314)<br>**Z** (16/314)<br>**F** (16/314) |
| **Govisetha** | **55** (25/313)<br>**44** (24/313)<br>**29** (24/313)<br>**10** (23/313)<br>**33** (23/313) | **C** (17/313)<br>**X** (17/313)<br>**P** (16/313)<br>**K** (16/313)<br>**A** (14/313) |
| **Handahana** | **58** (31/313)<br>**11** (30/313)<br>**55** (29/313)<br>**21** (28/313)<br>**6** (28/313) | N/A |
| **Mahajana Sampatha** | **1** (156/313)<br>**2** (155/313)<br>**5** (155/313)<br>**7** (154/313)<br>**4** (151/313) | **D** (19/313)<br>**J** (19/313)<br>**Q** (17/313)<br>**N** (16/313)<br>**G** (16/313) |
| **Mega Power** | **11** (37/313)<br>**26** (35/313)<br>**13** (34/313)<br>**3** (33/313)<br>**6** (32/313) | **T** (22/313)<br>**V** (20/313)<br>**U** (20/313)<br>**K** (17/313)<br>**J** (17/313) |
| **Nlb Jaya** | **5** (133/304)<br>**2** (117/304)<br>**0** (117/304)<br>**3** (116/304)<br>**7** (110/304) | **I** (18/304)<br>**T** (18/304)<br>**G** (16/304)<br>**P** (15/304)<br>**H** (15/304) |
| **Suba Dawasak** | **3** (128/313)<br>**4** (127/313)<br>**1** (121/313)<br>**8** (118/313)<br>**9** (115/313) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1832)<br>**20** (121/1832)<br>**57** (117/1832)<br>**38** (116/1832)<br>**75** (112/1832) | **B** (85/1832)<br>**R** (84/1832)<br>**M** (81/1832)<br>**P** (80/1832)<br>**N** (78/1832) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1720)<br>**10** (146/1720)<br>**6** (142/1720)<br>**21** (141/1720)<br>**15** (141/1720) | **H** (89/1720)<br>**U** (78/1720)<br>**M** (75/1720)<br>**D** (74/1720)<br>**G** (73/1720) |
| **Lagna Wasana** | **5** (140/1839)<br>**36** (137/1839)<br>**28** (137/1839)<br>**23** (136/1839)<br>**25** (136/1839) | N/A |
| **Sasiri** | **9** (78/1017)<br>**22** (75/1017)<br>**20** (74/1017)<br>**19** (74/1017)<br>**26** (74/1017) | N/A |
| **Super Ball** | **52** (111/1833)<br>**45** (111/1833)<br>**29** (111/1833)<br>**9** (110/1833)<br>**3** (108/1833) | **I** (92/1833)<br>**V** (82/1833)<br>**T** (82/1833)<br>**D** (82/1833)<br>**A** (81/1833) |
| **Supiri Dhana Sampatha** | **2** (499/991)<br>**0** (497/991)<br>**3** (490/991)<br>**7** (487/991)<br>**5** (473/991) | **V** (53/991)<br>**K** (46/991)<br>**T** (45/991)<br>**S** (44/991)<br>**G** (44/991) |

