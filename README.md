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

> **Last Updated (Sri Lanka Time):** `2026-07-25 12:27:20 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 281 Rows | 13.49 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 289 Rows | 12.31 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 288 Rows | 12.12 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 288 Rows | 11.82 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 288 Rows | 12.18 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 288 Rows | 12.96 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 279 Rows | 10.82 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 288 Rows | 13.21 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1807 Rows | 69.11 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1695 Rows | 69.25 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1814 Rows | 67.61 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 992 Rows | 32.82 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1808 Rows | 69.15 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 966 Rows | 35.91 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-25 12:27:20 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (104/281)<br>**2** (102/281)<br>**6** (100/281)<br>**3** (97/281)<br>**7** (97/281) | **Q** (17/281)<br>**D** (17/281)<br>**N** (16/281)<br>**J** (16/281)<br>**G** (16/281) |
| **Dhana Nidhanaya** | **7** (26/289)<br>**9** (26/289)<br>**28** (25/289)<br>**4** (24/289)<br>**6** (23/289) | **U** (18/289)<br>**F** (16/289)<br>**T** (15/289)<br>**W** (15/289)<br>**Z** (14/289) |
| **Govisetha** | **55** (24/288)<br>**10** (22/288)<br>**33** (22/288)<br>**23** (21/288)<br>**44** (21/288) | **P** (16/288)<br>**C** (15/288)<br>**K** (14/288)<br>**D** (13/288)<br>**A** (13/288) |
| **Handahana** | **58** (31/288)<br>**11** (27/288)<br>**21** (27/288)<br>**6** (27/288)<br>**55** (26/288) | N/A |
| **Mahajana Sampatha** | **2** (143/288)<br>**5** (141/288)<br>**4** (140/288)<br>**1** (140/288)<br>**6** (140/288) | **Q** (17/288)<br>**D** (17/288)<br>**J** (16/288)<br>**G** (16/288)<br>**N** (15/288) |
| **Mega Power** | **11** (36/288)<br>**6** (32/288)<br>**3** (32/288)<br>**22** (31/288)<br>**19** (30/288) | **T** (21/288)<br>**V** (20/288)<br>**U** (19/288)<br>**K** (17/288)<br>**J** (16/288) |
| **Nlb Jaya** | **5** (125/279)<br>**3** (107/279)<br>**0** (106/279)<br>**2** (105/279)<br>**1** (101/279) | **T** (18/279)<br>**I** (16/279)<br>**G** (16/279)<br>**M** (14/279)<br>**P** (14/279) |
| **Suba Dawasak** | **3** (118/288)<br>**4** (117/288)<br>**1** (111/288)<br>**9** (106/288)<br>**8** (105/288) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (122/1807)<br>**20** (119/1807)<br>**57** (117/1807)<br>**38** (112/1807)<br>**75** (111/1807) | **B** (82/1807)<br>**R** (81/1807)<br>**P** (80/1807)<br>**M** (80/1807)<br>**I** (77/1807) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1695)<br>**10** (145/1695)<br>**15** (140/1695)<br>**6** (139/1695)<br>**29** (139/1695) | **H** (88/1695)<br>**U** (78/1695)<br>**M** (73/1695)<br>**X** (73/1695)<br>**D** (72/1695) |
| **Lagna Wasana** | **5** (139/1814)<br>**28** (136/1814)<br>**36** (135/1814)<br>**25** (135/1814)<br>**23** (133/1814) | N/A |
| **Sasiri** | **9** (74/992)<br>**20** (73/992)<br>**22** (72/992)<br>**19** (71/992)<br>**26** (71/992) | N/A |
| **Super Ball** | **45** (111/1808)<br>**52** (110/1808)<br>**29** (110/1808)<br>**9** (108/1808)<br>**3** (107/1808) | **I** (92/1808)<br>**V** (81/1808)<br>**T** (81/1808)<br>**D** (81/1808)<br>**A** (79/1808) |
| **Supiri Dhana Sampatha** | **2** (486/966)<br>**0** (485/966)<br>**3** (483/966)<br>**7** (476/966)<br>**5** (461/966) | **V** (50/966)<br>**K** (46/966)<br>**S** (44/966)<br>**J** (44/966)<br>**T** (44/966) |

