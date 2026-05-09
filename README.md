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

> **Last Updated (Sri Lanka Time):** `2026-05-09 04:20:08 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 206 Rows | 10.05 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 214 Rows | 9.25 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 213 Rows | 9.14 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 213 Rows | 8.91 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 213 Rows | 9.19 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 213 Rows | 9.77 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 204 Rows | 8.04 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 213 Rows | 9.94 KB |

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

> **Analytic Report Last Updated:** `2026-05-09 04:20:09 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (79/206)<br>**5** (75/206)<br>**7** (74/206)<br>**4** (72/206)<br>**0** (71/206) | **D** (14/206)<br>**N** (13/206)<br>**J** (13/206)<br>**Q** (12/206)<br>**Y** (12/206) |
| **Dhana Nidhanaya** | **28** (21/214)<br>**9** (20/214)<br>**6** (19/214)<br>**16** (18/214)<br>**7** (17/214) | **U** (13/214)<br>**W** (13/214)<br>**T** (12/214)<br>**M** (12/214)<br>**Q** (11/214) |
| **Govisetha** | **44** (18/213)<br>**19** (17/213)<br>**55** (17/213)<br>**23** (16/213)<br>**58** (16/213) | **D** (11/213)<br>**W** (11/213)<br>**P** (11/213)<br>**O** (11/213)<br>**X** (11/213) |
| **Handahana** | **58** (20/213)<br>**55** (20/213)<br>**46** (20/213)<br>**6** (20/213)<br>**60** (19/213) | N/A |
| **Mahajana Sampatha** | **6** (106/213)<br>**1** (105/213)<br>**9** (104/213)<br>**2** (103/213)<br>**5** (103/213) | **D** (14/213)<br>**J** (13/213)<br>**N** (12/213)<br>**Q** (12/213)<br>**Y** (12/213) |
| **Mega Power** | **6** (26/213)<br>**3** (26/213)<br>**13** (25/213)<br>**22** (24/213)<br>**19** (23/213) | **V** (17/213)<br>**T** (13/213)<br>**U** (13/213)<br>**K** (12/213)<br>**J** (10/213) |
| **Nlb Jaya** | **5** (89/204)<br>**3** (82/204)<br>**0** (79/204)<br>**2** (77/204)<br>**4** (72/204) | **M** (13/204)<br>**P** (13/204)<br>**I** (13/204)<br>**T** (13/204)<br>**G** (13/204) |
| **Suba Dawasak** | **3** (85/213)<br>**1** (85/213)<br>**4** (84/213)<br>**9** (81/213)<br>**8** (76/213) | N/A |

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

