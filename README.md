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

> **Last Updated (Sri Lanka Time):** `2026-07-31 12:25:05 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 287 Rows | 13.76 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 295 Rows | 12.56 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 294 Rows | 12.37 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 294 Rows | 12.06 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 294 Rows | 12.42 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 294 Rows | 13.22 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 285 Rows | 11.04 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 294 Rows | 13.48 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1813 Rows | 69.34 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1701 Rows | 69.50 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1820 Rows | 67.83 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 998 Rows | 33.03 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1814 Rows | 69.38 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 972 Rows | 36.13 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-31 12:25:05 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (107/287)<br>**2** (104/287)<br>**6** (101/287)<br>**3** (100/287)<br>**7** (99/287) | **D** (19/287)<br>**Q** (17/287)<br>**N** (16/287)<br>**J** (16/287)<br>**G** (16/287) |
| **Dhana Nidhanaya** | **9** (27/295)<br>**7** (26/295)<br>**28** (25/295)<br>**4** (24/295)<br>**6** (23/295) | **U** (20/295)<br>**F** (16/295)<br>**W** (16/295)<br>**Z** (15/295)<br>**T** (15/295) |
| **Govisetha** | **55** (25/294)<br>**10** (22/294)<br>**33** (22/294)<br>**23** (21/294)<br>**44** (21/294) | **P** (16/294)<br>**C** (16/294)<br>**O** (14/294)<br>**K** (14/294)<br>**D** (13/294) |
| **Handahana** | **58** (31/294)<br>**11** (28/294)<br>**21** (27/294)<br>**6** (27/294)<br>**55** (26/294) | N/A |
| **Mahajana Sampatha** | **2** (147/294)<br>**5** (144/294)<br>**1** (144/294)<br>**4** (143/294)<br>**7** (143/294) | **D** (19/294)<br>**Q** (17/294)<br>**J** (16/294)<br>**G** (16/294)<br>**N** (15/294) |
| **Mega Power** | **11** (36/294)<br>**6** (32/294)<br>**22** (32/294)<br>**3** (32/294)<br>**13** (32/294) | **T** (21/294)<br>**V** (20/294)<br>**U** (19/294)<br>**K** (17/294)<br>**J** (16/294) |
| **Nlb Jaya** | **5** (128/285)<br>**0** (109/285)<br>**2** (108/285)<br>**3** (107/285)<br>**7** (103/285) | **T** (18/285)<br>**I** (17/285)<br>**G** (16/285)<br>**Y** (15/285)<br>**M** (14/285) |
| **Suba Dawasak** | **3** (120/294)<br>**4** (120/294)<br>**1** (116/294)<br>**8** (109/294)<br>**9** (108/294) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1813)<br>**20** (119/1813)<br>**57** (117/1813)<br>**75** (112/1813)<br>**38** (112/1813) | **R** (83/1813)<br>**B** (82/1813)<br>**P** (80/1813)<br>**M** (80/1813)<br>**N** (78/1813) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1701)<br>**10** (145/1701)<br>**6** (141/1701)<br>**15** (140/1701)<br>**29** (139/1701) | **H** (88/1701)<br>**U** (78/1701)<br>**M** (73/1701)<br>**X** (73/1701)<br>**D** (72/1701) |
| **Lagna Wasana** | **5** (140/1820)<br>**25** (136/1820)<br>**28** (136/1820)<br>**36** (135/1820)<br>**23** (135/1820) | N/A |
| **Sasiri** | **9** (74/998)<br>**22** (73/998)<br>**20** (73/998)<br>**19** (71/998)<br>**26** (71/998) | N/A |
| **Super Ball** | **45** (111/1814)<br>**52** (110/1814)<br>**29** (110/1814)<br>**9** (109/1814)<br>**3** (107/1814) | **I** (92/1814)<br>**D** (82/1814)<br>**V** (81/1814)<br>**T** (81/1814)<br>**A** (79/1814) |
| **Supiri Dhana Sampatha** | **2** (489/972)<br>**0** (489/972)<br>**3** (484/972)<br>**7** (479/972)<br>**5** (463/972) | **V** (50/972)<br>**K** (46/972)<br>**S** (44/972)<br>**J** (44/972)<br>**T** (44/972) |

