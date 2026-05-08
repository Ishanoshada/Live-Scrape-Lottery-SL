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

> **Last Updated (Sri Lanka Time):** `2026-05-08 09:39:58 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 205 Rows | 10.01 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 213 Rows | 9.21 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 212 Rows | 9.10 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 212 Rows | 8.88 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 212 Rows | 9.15 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 212 Rows | 9.73 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 203 Rows | 8.01 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 212 Rows | 9.89 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1732 Rows | 66.24 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1620 Rows | 66.16 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1739 Rows | 64.81 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 917 Rows | 30.26 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1733 Rows | 66.28 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 891 Rows | 33.12 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-08 09:39:58 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (79/205)<br>**5** (75/205)<br>**7** (73/205)<br>**4** (71/205)<br>**0** (71/205) | **D** (14/205)<br>**N** (13/205)<br>**J** (13/205)<br>**Q** (12/205)<br>**Y** (12/205) |
| **Dhana Nidhanaya** | **28** (21/213)<br>**9** (20/213)<br>**6** (19/213)<br>**16** (18/213)<br>**4** (16/213) | **U** (13/213)<br>**W** (13/213)<br>**T** (12/213)<br>**M** (12/213)<br>**Q** (11/213) |
| **Govisetha** | **44** (18/212)<br>**19** (17/212)<br>**55** (17/212)<br>**23** (16/212)<br>**58** (16/212) | **D** (11/212)<br>**W** (11/212)<br>**P** (11/212)<br>**O** (11/212)<br>**X** (11/212) |
| **Handahana** | **58** (20/212)<br>**55** (20/212)<br>**46** (20/212)<br>**6** (20/212)<br>**60** (19/212) | N/A |
| **Mahajana Sampatha** | **1** (105/212)<br>**6** (105/212)<br>**9** (103/212)<br>**5** (103/212)<br>**3** (102/212) | **D** (14/212)<br>**J** (13/212)<br>**N** (12/212)<br>**Q** (12/212)<br>**Y** (12/212) |
| **Mega Power** | **6** (26/212)<br>**3** (26/212)<br>**22** (24/212)<br>**13** (24/212)<br>**19** (23/212) | **V** (17/212)<br>**T** (13/212)<br>**U** (13/212)<br>**K** (12/212)<br>**J** (10/212) |
| **Nlb Jaya** | **5** (89/203)<br>**3** (82/203)<br>**0** (78/203)<br>**2** (77/203)<br>**4** (72/203) | **M** (13/203)<br>**I** (13/203)<br>**T** (13/203)<br>**G** (13/203)<br>**P** (12/203) |
| **Suba Dawasak** | **3** (85/212)<br>**1** (85/212)<br>**4** (83/212)<br>**9** (81/212)<br>**8** (75/212) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1732)<br>**57** (113/1732)<br>**20** (111/1732)<br>**13** (109/1732)<br>**75** (105/1732) | **B** (81/1732)<br>**R** (77/1732)<br>**P** (77/1732)<br>**M** (77/1732)<br>**I** (73/1732) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1620)<br>**10** (142/1620)<br>**29** (133/1620)<br>**21** (132/1620)<br>**15** (132/1620) | **H** (87/1620)<br>**U** (74/1620)<br>**W** (71/1620)<br>**D** (69/1620)<br>**G** (69/1620) |
| **Lagna Wasana** | **5** (135/1739)<br>**28** (132/1739)<br>**36** (130/1739)<br>**25** (130/1739)<br>**23** (128/1739) | N/A |
| **Sasiri** | **20** (70/917)<br>**9** (69/917)<br>**22** (68/917)<br>**26** (68/917)<br>**19** (67/917) | N/A |
| **Super Ball** | **45** (109/1733)<br>**29** (105/1733)<br>**43** (105/1733)<br>**3** (104/1733)<br>**59** (103/1733) | **I** (86/1733)<br>**D** (80/1733)<br>**V** (77/1733)<br>**T** (77/1733)<br>**A** (77/1733) |
| **Supiri Dhana Sampatha** | **2** (450/891)<br>**0** (450/891)<br>**3** (447/891)<br>**7** (440/891)<br>**5** (424/891) | **K** (44/891)<br>**V** (43/891)<br>**T** (43/891)<br>**S** (41/891)<br>**G** (41/891) |

