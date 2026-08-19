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

> **Last Updated (Sri Lanka Time):** `2026-08-19 11:20:19 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 307 Rows | 14.72 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 315 Rows | 13.42 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 314 Rows | 13.20 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 314 Rows | 12.87 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 314 Rows | 13.26 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 314 Rows | 14.11 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 305 Rows | 11.83 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 314 Rows | 14.39 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1833 Rows | 70.10 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1721 Rows | 70.32 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1840 Rows | 68.57 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1018 Rows | 33.72 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1834 Rows | 70.14 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 992 Rows | 36.88 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-19 11:20:19 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (114/307)<br>**2** (112/307)<br>**7** (107/307)<br>**3** (106/307)<br>**6** (105/307) | **D** (19/307)<br>**J** (19/307)<br>**N** (17/307)<br>**Q** (17/307)<br>**G** (16/307) |
| **Dhana Nidhanaya** | **9** (29/315)<br>**4** (28/315)<br>**7** (27/315)<br>**28** (25/315)<br>**80** (24/315) | **U** (20/315)<br>**W** (17/315)<br>**M** (17/315)<br>**Z** (16/315)<br>**F** (16/315) |
| **Govisetha** | **55** (25/314)<br>**44** (24/314)<br>**29** (24/314)<br>**10** (23/314)<br>**33** (23/314) | **P** (17/314)<br>**C** (17/314)<br>**X** (17/314)<br>**K** (16/314)<br>**A** (14/314) |
| **Handahana** | **58** (31/314)<br>**11** (30/314)<br>**55** (29/314)<br>**21** (28/314)<br>**6** (28/314) | N/A |
| **Mahajana Sampatha** | **2** (156/314)<br>**1** (156/314)<br>**5** (155/314)<br>**7** (154/314)<br>**4** (151/314) | **D** (19/314)<br>**J** (19/314)<br>**Q** (17/314)<br>**N** (16/314)<br>**G** (16/314) |
| **Mega Power** | **11** (37/314)<br>**26** (35/314)<br>**3** (34/314)<br>**13** (34/314)<br>**6** (32/314) | **T** (22/314)<br>**V** (20/314)<br>**U** (20/314)<br>**K** (17/314)<br>**J** (17/314) |
| **Nlb Jaya** | **5** (134/305)<br>**2** (117/305)<br>**0** (117/305)<br>**3** (116/305)<br>**7** (110/305) | **I** (18/305)<br>**T** (18/305)<br>**G** (16/305)<br>**P** (15/305)<br>**H** (15/305) |
| **Suba Dawasak** | **3** (129/314)<br>**4** (127/314)<br>**1** (121/314)<br>**8** (118/314)<br>**9** (115/314) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1833)<br>**20** (121/1833)<br>**57** (117/1833)<br>**38** (116/1833)<br>**75** (112/1833) | **B** (85/1833)<br>**R** (84/1833)<br>**M** (81/1833)<br>**P** (80/1833)<br>**N** (78/1833) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1721)<br>**10** (146/1721)<br>**6** (142/1721)<br>**29** (141/1721)<br>**21** (141/1721) | **H** (89/1721)<br>**U** (78/1721)<br>**M** (76/1721)<br>**D** (74/1721)<br>**G** (73/1721) |
| **Lagna Wasana** | **5** (140/1840)<br>**36** (137/1840)<br>**28** (137/1840)<br>**23** (136/1840)<br>**25** (136/1840) | N/A |
| **Sasiri** | **9** (78/1018)<br>**22** (75/1018)<br>**20** (74/1018)<br>**19** (74/1018)<br>**26** (74/1018) | N/A |
| **Super Ball** | **52** (111/1834)<br>**45** (111/1834)<br>**29** (111/1834)<br>**9** (110/1834)<br>**3** (108/1834) | **I** (92/1834)<br>**V** (82/1834)<br>**T** (82/1834)<br>**D** (82/1834)<br>**A** (81/1834) |
| **Supiri Dhana Sampatha** | **2** (499/992)<br>**0** (498/992)<br>**3** (490/992)<br>**7** (487/992)<br>**5** (473/992) | **V** (53/992)<br>**K** (46/992)<br>**T** (45/992)<br>**S** (44/992)<br>**G** (44/992) |

