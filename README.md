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

> **Last Updated (Sri Lanka Time):** `2026-07-21 12:42:51 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 277 Rows | 13.30 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 285 Rows | 12.15 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 284 Rows | 11.96 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 284 Rows | 11.67 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 284 Rows | 12.02 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 284 Rows | 12.79 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 275 Rows | 10.67 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 284 Rows | 13.04 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1803 Rows | 68.95 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1691 Rows | 69.08 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1810 Rows | 67.46 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 988 Rows | 32.69 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1804 Rows | 68.99 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 962 Rows | 35.76 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-21 12:42:51 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (103/277)<br>**6** (100/277)<br>**2** (98/277)<br>**7** (97/277)<br>**3** (95/277) | **Q** (17/277)<br>**D** (17/277)<br>**N** (16/277)<br>**J** (16/277)<br>**G** (16/277) |
| **Dhana Nidhanaya** | **7** (26/285)<br>**9** (26/285)<br>**28** (25/285)<br>**4** (23/285)<br>**6** (23/285) | **U** (17/285)<br>**F** (16/285)<br>**W** (15/285)<br>**Z** (14/285)<br>**T** (14/285) |
| **Govisetha** | **55** (23/284)<br>**10** (21/284)<br>**44** (21/284)<br>**33** (21/284)<br>**23** (20/284) | **P** (16/284)<br>**C** (15/284)<br>**K** (14/284)<br>**D** (13/284)<br>**A** (13/284) |
| **Handahana** | **58** (31/284)<br>**11** (27/284)<br>**21** (27/284)<br>**6** (27/284)<br>**55** (25/284) | N/A |
| **Mahajana Sampatha** | **5** (140/284)<br>**2** (139/284)<br>**7** (139/284)<br>**6** (139/284)<br>**4** (138/284) | **Q** (17/284)<br>**D** (17/284)<br>**J** (16/284)<br>**G** (16/284)<br>**N** (15/284) |
| **Mega Power** | **11** (36/284)<br>**3** (32/284)<br>**6** (31/284)<br>**22** (30/284)<br>**19** (30/284) | **T** (19/284)<br>**V** (19/284)<br>**U** (19/284)<br>**K** (17/284)<br>**J** (16/284) |
| **Nlb Jaya** | **5** (122/275)<br>**3** (106/275)<br>**0** (105/275)<br>**2** (104/275)<br>**1** (99/275) | **T** (18/275)<br>**I** (16/275)<br>**G** (16/275)<br>**M** (14/275)<br>**P** (14/275) |
| **Suba Dawasak** | **3** (118/284)<br>**4** (115/284)<br>**1** (110/284)<br>**8** (105/284)<br>**9** (104/284) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (122/1803)<br>**20** (119/1803)<br>**57** (116/1803)<br>**38** (112/1803)<br>**75** (111/1803) | **B** (82/1803)<br>**R** (81/1803)<br>**P** (80/1803)<br>**M** (80/1803)<br>**I** (77/1803) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1691)<br>**10** (145/1691)<br>**6** (139/1691)<br>**29** (138/1691)<br>**27** (138/1691) | **H** (88/1691)<br>**U** (78/1691)<br>**M** (73/1691)<br>**X** (73/1691)<br>**W** (72/1691) |
| **Lagna Wasana** | **5** (139/1810)<br>**28** (136/1810)<br>**36** (135/1810)<br>**25** (135/1810)<br>**39** (132/1810) | N/A |
| **Sasiri** | **9** (74/988)<br>**20** (73/988)<br>**22** (72/988)<br>**26** (71/988)<br>**19** (70/988) | N/A |
| **Super Ball** | **52** (110/1804)<br>**45** (110/1804)<br>**29** (110/1804)<br>**3** (107/1804)<br>**74** (107/1804) | **I** (92/1804)<br>**V** (81/1804)<br>**T** (81/1804)<br>**D** (81/1804)<br>**A** (79/1804) |
| **Supiri Dhana Sampatha** | **2** (485/962)<br>**0** (482/962)<br>**3** (480/962)<br>**7** (474/962)<br>**5** (458/962) | **V** (50/962)<br>**K** (46/962)<br>**S** (44/962)<br>**J** (44/962)<br>**T** (44/962) |

