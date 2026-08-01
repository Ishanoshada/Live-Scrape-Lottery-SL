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

> **Last Updated (Sri Lanka Time):** `2026-08-01 11:58:33 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 289 Rows | 13.86 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 297 Rows | 12.65 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 296 Rows | 12.45 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 296 Rows | 12.14 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 296 Rows | 12.51 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 296 Rows | 13.31 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 287 Rows | 11.12 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 296 Rows | 13.57 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1815 Rows | 69.42 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1703 Rows | 69.58 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1822 Rows | 67.90 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1000 Rows | 33.10 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1816 Rows | 69.45 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 974 Rows | 36.21 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-01 11:58:33 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (107/289)<br>**2** (104/289)<br>**6** (103/289)<br>**3** (101/289)<br>**4** (100/289) | **D** (19/289)<br>**Q** (17/289)<br>**N** (16/289)<br>**J** (16/289)<br>**G** (16/289) |
| **Dhana Nidhanaya** | **9** (27/297)<br>**7** (26/297)<br>**28** (25/297)<br>**4** (24/297)<br>**6** (23/297) | **U** (20/297)<br>**F** (16/297)<br>**W** (16/297)<br>**Z** (15/297)<br>**T** (15/297) |
| **Govisetha** | **55** (25/296)<br>**10** (23/296)<br>**44** (22/296)<br>**33** (22/296)<br>**23** (21/296) | **P** (16/296)<br>**C** (16/296)<br>**K** (15/296)<br>**O** (14/296)<br>**Y** (14/296) |
| **Handahana** | **58** (31/296)<br>**11** (29/296)<br>**21** (27/296)<br>**55** (27/296)<br>**6** (27/296) | N/A |
| **Mahajana Sampatha** | **2** (147/296)<br>**4** (145/296)<br>**5** (145/296)<br>**7** (144/296)<br>**1** (144/296) | **D** (19/296)<br>**Q** (17/296)<br>**J** (16/296)<br>**G** (16/296)<br>**N** (15/296) |
| **Mega Power** | **11** (36/296)<br>**22** (32/296)<br>**6** (32/296)<br>**3** (32/296)<br>**13** (32/296) | **T** (21/296)<br>**V** (20/296)<br>**U** (19/296)<br>**K** (17/296)<br>**J** (16/296) |
| **Nlb Jaya** | **5** (128/287)<br>**0** (110/287)<br>**2** (109/287)<br>**3** (108/287)<br>**7** (103/287) | **T** (18/287)<br>**I** (17/287)<br>**G** (16/287)<br>**Y** (15/287)<br>**M** (14/287) |
| **Suba Dawasak** | **3** (120/296)<br>**4** (120/296)<br>**1** (116/296)<br>**8** (110/296)<br>**9** (110/296) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1815)<br>**20** (119/1815)<br>**57** (117/1815)<br>**38** (113/1815)<br>**75** (112/1815) | **R** (83/1815)<br>**B** (82/1815)<br>**P** (80/1815)<br>**M** (80/1815)<br>**N** (78/1815) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (158/1703)<br>**10** (145/1703)<br>**6** (141/1703)<br>**15** (140/1703)<br>**29** (139/1703) | **H** (88/1703)<br>**U** (78/1703)<br>**G** (73/1703)<br>**M** (73/1703)<br>**X** (73/1703) |
| **Lagna Wasana** | **5** (140/1822)<br>**25** (136/1822)<br>**28** (136/1822)<br>**36** (135/1822)<br>**23** (135/1822) | N/A |
| **Sasiri** | **22** (74/1000)<br>**9** (74/1000)<br>**20** (74/1000)<br>**19** (71/1000)<br>**26** (71/1000) | N/A |
| **Super Ball** | **45** (111/1816)<br>**29** (111/1816)<br>**52** (110/1816)<br>**9** (109/1816)<br>**3** (107/1816) | **I** (92/1816)<br>**D** (82/1816)<br>**V** (81/1816)<br>**T** (81/1816)<br>**A** (79/1816) |
| **Supiri Dhana Sampatha** | **2** (491/974)<br>**0** (489/974)<br>**3** (484/974)<br>**7** (480/974)<br>**5** (463/974) | **V** (51/974)<br>**K** (46/974)<br>**S** (44/974)<br>**J** (44/974)<br>**T** (44/974) |

