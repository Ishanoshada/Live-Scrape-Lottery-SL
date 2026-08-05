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

> **Last Updated (Sri Lanka Time):** `2026-08-06 12:30:53 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 293 Rows | 14.05 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 301 Rows | 12.82 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 300 Rows | 12.62 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 300 Rows | 12.30 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 300 Rows | 12.67 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 300 Rows | 13.49 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 291 Rows | 11.28 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 300 Rows | 13.75 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1819 Rows | 69.57 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1707 Rows | 69.75 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1826 Rows | 68.05 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1004 Rows | 33.24 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1820 Rows | 69.60 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 978 Rows | 36.36 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-06 12:30:53 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (109/293)<br>**2** (105/293)<br>**6** (103/293)<br>**3** (103/293)<br>**4** (101/293) | **D** (19/293)<br>**Q** (17/293)<br>**J** (17/293)<br>**N** (16/293)<br>**G** (16/293) |
| **Dhana Nidhanaya** | **9** (27/301)<br>**7** (26/301)<br>**4** (25/301)<br>**28** (25/301)<br>**80** (23/301) | **U** (20/301)<br>**F** (16/301)<br>**W** (16/301)<br>**Z** (15/301)<br>**T** (15/301) |
| **Govisetha** | **55** (25/300)<br>**10** (23/300)<br>**44** (23/300)<br>**33** (23/300)<br>**23** (22/300) | **P** (16/300)<br>**K** (16/300)<br>**C** (16/300)<br>**O** (14/300)<br>**Y** (14/300) |
| **Handahana** | **58** (31/300)<br>**11** (29/300)<br>**55** (28/300)<br>**6** (28/300)<br>**21** (27/300) | N/A |
| **Mahajana Sampatha** | **5** (148/300)<br>**2** (148/300)<br>**4** (146/300)<br>**7** (146/300)<br>**1** (146/300) | **D** (19/300)<br>**Q** (17/300)<br>**J** (17/300)<br>**G** (16/300)<br>**N** (15/300) |
| **Mega Power** | **11** (36/300)<br>**13** (33/300)<br>**22** (32/300)<br>**6** (32/300)<br>**3** (32/300) | **T** (21/300)<br>**V** (20/300)<br>**U** (19/300)<br>**K** (17/300)<br>**J** (16/300) |
| **Nlb Jaya** | **5** (131/291)<br>**0** (112/291)<br>**2** (111/291)<br>**3** (110/291)<br>**7** (105/291) | **I** (18/291)<br>**T** (18/291)<br>**G** (16/291)<br>**Y** (15/291)<br>**M** (14/291) |
| **Suba Dawasak** | **3** (123/300)<br>**4** (121/300)<br>**1** (117/300)<br>**9** (111/300)<br>**8** (110/300) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1819)<br>**20** (120/1819)<br>**57** (117/1819)<br>**38** (114/1819)<br>**75** (112/1819) | **R** (83/1819)<br>**B** (82/1819)<br>**P** (80/1819)<br>**M** (80/1819)<br>**N** (78/1819) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (159/1707)<br>**10** (145/1707)<br>**6** (141/1707)<br>**15** (141/1707)<br>**29** (140/1707) | **H** (88/1707)<br>**U** (78/1707)<br>**G** (73/1707)<br>**M** (73/1707)<br>**X** (73/1707) |
| **Lagna Wasana** | **5** (140/1826)<br>**25** (136/1826)<br>**28** (136/1826)<br>**36** (135/1826)<br>**23** (135/1826) | N/A |
| **Sasiri** | **9** (75/1004)<br>**22** (74/1004)<br>**20** (74/1004)<br>**19** (72/1004)<br>**26** (71/1004) | N/A |
| **Super Ball** | **45** (111/1820)<br>**29** (111/1820)<br>**52** (110/1820)<br>**9** (109/1820)<br>**3** (107/1820) | **I** (92/1820)<br>**T** (82/1820)<br>**D** (82/1820)<br>**V** (81/1820)<br>**A** (79/1820) |
| **Supiri Dhana Sampatha** | **2** (494/978)<br>**0** (491/978)<br>**3** (485/978)<br>**7** (480/978)<br>**5** (466/978) | **V** (51/978)<br>**K** (46/978)<br>**T** (45/978)<br>**S** (44/978)<br>**J** (44/978) |

