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

> **Last Updated (Sri Lanka Time):** `2026-08-30 01:24:52 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 317 Rows | 15.20 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 325 Rows | 13.85 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 324 Rows | 13.63 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 324 Rows | 13.28 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 324 Rows | 13.69 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 324 Rows | 14.56 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 315 Rows | 12.22 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 324 Rows | 14.86 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1843 Rows | 70.49 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1731 Rows | 70.73 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1850 Rows | 68.95 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1028 Rows | 34.06 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1844 Rows | 70.52 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1002 Rows | 37.25 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-30 01:24:52 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (117/317)<br>**2** (115/317)<br>**3** (111/317)<br>**6** (111/317)<br>**4** (109/317) | **D** (19/317)<br>**J** (19/317)<br>**N** (17/317)<br>**Q** (17/317)<br>**G** (17/317) |
| **Dhana Nidhanaya** | **9** (32/325)<br>**4** (29/325)<br>**7** (28/325)<br>**28** (26/325)<br>**80** (24/325) | **U** (20/325)<br>**F** (18/325)<br>**W** (18/325)<br>**M** (17/325)<br>**Z** (16/325) |
| **Govisetha** | **55** (26/324)<br>**44** (24/324)<br>**29** (24/324)<br>**10** (23/324)<br>**33** (23/324) | **P** (18/324)<br>**C** (18/324)<br>**X** (17/324)<br>**K** (16/324)<br>**A** (14/324) |
| **Handahana** | **58** (32/324)<br>**11** (31/324)<br>**55** (29/324)<br>**6** (29/324)<br>**21** (28/324) | N/A |
| **Mahajana Sampatha** | **5** (162/324)<br>**2** (161/324)<br>**1** (160/324)<br>**7** (158/324)<br>**4** (157/324) | **D** (19/324)<br>**J** (19/324)<br>**Q** (17/324)<br>**G** (17/324)<br>**W** (17/324) |
| **Mega Power** | **11** (37/324)<br>**3** (36/324)<br>**26** (36/324)<br>**13** (35/324)<br>**6** (33/324) | **T** (22/324)<br>**V** (21/324)<br>**U** (20/324)<br>**K** (18/324)<br>**J** (17/324) |
| **Nlb Jaya** | **5** (137/315)<br>**3** (122/315)<br>**2** (121/315)<br>**0** (121/315)<br>**7** (113/315) | **I** (18/315)<br>**T** (18/315)<br>**G** (17/315)<br>**H** (16/315)<br>**O** (16/315) |
| **Suba Dawasak** | **3** (132/324)<br>**4** (131/324)<br>**1** (124/324)<br>**8** (122/324)<br>**9** (121/324) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1843)<br>**20** (121/1843)<br>**57** (118/1843)<br>**38** (116/1843)<br>**75** (113/1843) | **B** (86/1843)<br>**R** (84/1843)<br>**M** (81/1843)<br>**P** (80/1843)<br>**N** (79/1843) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1731)<br>**10** (146/1731)<br>**15** (143/1731)<br>**6** (142/1731)<br>**29** (142/1731) | **H** (89/1731)<br>**U** (78/1731)<br>**M** (76/1731)<br>**D** (74/1731)<br>**G** (74/1731) |
| **Lagna Wasana** | **5** (141/1850)<br>**23** (139/1850)<br>**36** (137/1850)<br>**28** (137/1850)<br>**39** (136/1850) | N/A |
| **Sasiri** | **9** (79/1028)<br>**22** (77/1028)<br>**20** (76/1028)<br>**26** (76/1028)<br>**19** (74/1028) | N/A |
| **Super Ball** | **52** (111/1844)<br>**9** (111/1844)<br>**45** (111/1844)<br>**29** (111/1844)<br>**74** (109/1844) | **I** (92/1844)<br>**V** (82/1844)<br>**T** (82/1844)<br>**D** (82/1844)<br>**A** (81/1844) |
| **Supiri Dhana Sampatha** | **2** (503/1002)<br>**0** (503/1002)<br>**3** (496/1002)<br>**7** (494/1002)<br>**5** (479/1002) | **V** (53/1002)<br>**K** (47/1002)<br>**G** (46/1002)<br>**T** (45/1002)<br>**S** (44/1002) |

