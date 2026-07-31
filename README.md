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

> **Last Updated (Sri Lanka Time):** `2026-08-01 12:23:00 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 288 Rows | 13.81 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 296 Rows | 12.60 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 295 Rows | 12.40 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 295 Rows | 12.09 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 295 Rows | 12.46 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 295 Rows | 13.26 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 286 Rows | 11.08 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 295 Rows | 13.52 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1814 Rows | 69.38 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1702 Rows | 69.54 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1821 Rows | 67.87 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 999 Rows | 33.06 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1815 Rows | 69.41 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 973 Rows | 36.17 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-01 12:23:01 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (107/288)<br>**2** (104/288)<br>**6** (102/288)<br>**3** (100/288)<br>**4** (99/288) | **D** (19/288)<br>**Q** (17/288)<br>**N** (16/288)<br>**J** (16/288)<br>**G** (16/288) |
| **Dhana Nidhanaya** | **9** (27/296)<br>**7** (26/296)<br>**28** (25/296)<br>**4** (24/296)<br>**6** (23/296) | **U** (20/296)<br>**F** (16/296)<br>**W** (16/296)<br>**Z** (15/296)<br>**T** (15/296) |
| **Govisetha** | **55** (25/295)<br>**10** (23/295)<br>**44** (22/295)<br>**33** (22/295)<br>**23** (21/295) | **P** (16/295)<br>**C** (16/295)<br>**O** (14/295)<br>**K** (14/295)<br>**Y** (14/295) |
| **Handahana** | **58** (31/295)<br>**11** (29/295)<br>**21** (27/295)<br>**6** (27/295)<br>**55** (26/295) | N/A |
| **Mahajana Sampatha** | **2** (147/295)<br>**4** (144/295)<br>**5** (144/295)<br>**7** (144/295)<br>**1** (144/295) | **D** (19/295)<br>**Q** (17/295)<br>**J** (16/295)<br>**G** (16/295)<br>**N** (15/295) |
| **Mega Power** | **11** (36/295)<br>**22** (32/295)<br>**6** (32/295)<br>**3** (32/295)<br>**13** (32/295) | **T** (21/295)<br>**V** (20/295)<br>**U** (19/295)<br>**K** (17/295)<br>**J** (16/295) |
| **Nlb Jaya** | **5** (128/286)<br>**2** (109/286)<br>**0** (109/286)<br>**3** (107/286)<br>**7** (103/286) | **T** (18/286)<br>**I** (17/286)<br>**G** (16/286)<br>**Y** (15/286)<br>**M** (14/286) |
| **Suba Dawasak** | **3** (120/295)<br>**4** (120/295)<br>**1** (116/295)<br>**9** (109/295)<br>**8** (109/295) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1814)<br>**20** (119/1814)<br>**57** (117/1814)<br>**75** (112/1814)<br>**38** (112/1814) | **R** (83/1814)<br>**B** (82/1814)<br>**P** (80/1814)<br>**M** (80/1814)<br>**N** (78/1814) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1702)<br>**10** (145/1702)<br>**6** (141/1702)<br>**15** (140/1702)<br>**29** (139/1702) | **H** (88/1702)<br>**U** (78/1702)<br>**G** (73/1702)<br>**M** (73/1702)<br>**X** (73/1702) |
| **Lagna Wasana** | **5** (140/1821)<br>**25** (136/1821)<br>**28** (136/1821)<br>**36** (135/1821)<br>**23** (135/1821) | N/A |
| **Sasiri** | **22** (74/999)<br>**9** (74/999)<br>**20** (74/999)<br>**19** (71/999)<br>**26** (71/999) | N/A |
| **Super Ball** | **45** (111/1815)<br>**29** (111/1815)<br>**52** (110/1815)<br>**9** (109/1815)<br>**3** (107/1815) | **I** (92/1815)<br>**D** (82/1815)<br>**V** (81/1815)<br>**T** (81/1815)<br>**A** (79/1815) |
| **Supiri Dhana Sampatha** | **2** (490/973)<br>**0** (489/973)<br>**3** (484/973)<br>**7** (479/973)<br>**5** (463/973) | **V** (50/973)<br>**K** (46/973)<br>**S** (44/973)<br>**J** (44/973)<br>**T** (44/973) |

