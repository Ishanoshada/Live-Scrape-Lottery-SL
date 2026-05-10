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

> **Last Updated (Sri Lanka Time):** `2026-05-10 07:36:39 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 207 Rows | 10.10 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 215 Rows | 9.29 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 214 Rows | 9.18 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 214 Rows | 8.95 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 214 Rows | 9.23 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 214 Rows | 9.81 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 205 Rows | 8.08 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 214 Rows | 9.98 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1733 Rows | 66.28 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1621 Rows | 66.21 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1740 Rows | 64.85 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 918 Rows | 30.30 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1734 Rows | 66.32 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 892 Rows | 33.15 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-10 07:36:39 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (79/207)<br>**5** (76/207)<br>**7** (74/207)<br>**4** (72/207)<br>**2** (72/207) | **D** (14/207)<br>**J** (14/207)<br>**N** (13/207)<br>**Q** (12/207)<br>**Y** (12/207) |
| **Dhana Nidhanaya** | **28** (21/215)<br>**9** (20/215)<br>**6** (19/215)<br>**16** (18/215)<br>**7** (17/215) | **U** (13/215)<br>**W** (13/215)<br>**T** (12/215)<br>**M** (12/215)<br>**Q** (11/215) |
| **Govisetha** | **44** (18/214)<br>**19** (17/214)<br>**55** (17/214)<br>**23** (16/214)<br>**58** (16/214) | **P** (12/214)<br>**D** (11/214)<br>**W** (11/214)<br>**O** (11/214)<br>**X** (11/214) |
| **Handahana** | **58** (20/214)<br>**21** (20/214)<br>**55** (20/214)<br>**46** (20/214)<br>**6** (20/214) | N/A |
| **Mahajana Sampatha** | **6** (106/214)<br>**9** (105/214)<br>**1** (105/214)<br>**5** (104/214)<br>**2** (104/214) | **D** (14/214)<br>**J** (14/214)<br>**N** (12/214)<br>**Q** (12/214)<br>**Y** (12/214) |
| **Mega Power** | **6** (26/214)<br>**3** (26/214)<br>**13** (25/214)<br>**22** (24/214)<br>**19** (23/214) | **V** (17/214)<br>**T** (13/214)<br>**K** (13/214)<br>**U** (13/214)<br>**J** (10/214) |
| **Nlb Jaya** | **5** (89/205)<br>**3** (82/205)<br>**0** (79/205)<br>**2** (77/205)<br>**4** (72/205) | **M** (13/205)<br>**P** (13/205)<br>**I** (13/205)<br>**T** (13/205)<br>**G** (13/205) |
| **Suba Dawasak** | **3** (86/214)<br>**1** (85/214)<br>**4** (84/214)<br>**9** (81/214)<br>**8** (76/214) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1733)<br>**57** (113/1733)<br>**20** (111/1733)<br>**13** (109/1733)<br>**38** (106/1733) | **B** (81/1733)<br>**M** (78/1733)<br>**R** (77/1733)<br>**P** (77/1733)<br>**I** (73/1733) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1621)<br>**10** (142/1621)<br>**29** (133/1621)<br>**21** (132/1621)<br>**15** (132/1621) | **H** (87/1621)<br>**U** (74/1621)<br>**W** (71/1621)<br>**D** (69/1621)<br>**G** (69/1621) |
| **Lagna Wasana** | **5** (135/1740)<br>**28** (132/1740)<br>**36** (130/1740)<br>**25** (130/1740)<br>**23** (129/1740) | N/A |
| **Sasiri** | **20** (70/918)<br>**9** (69/918)<br>**22** (68/918)<br>**26** (68/918)<br>**19** (67/918) | N/A |
| **Super Ball** | **45** (109/1734)<br>**29** (105/1734)<br>**43** (105/1734)<br>**3** (104/1734)<br>**52** (103/1734) | **I** (86/1734)<br>**D** (80/1734)<br>**T** (78/1734)<br>**V** (77/1734)<br>**A** (77/1734) |
| **Supiri Dhana Sampatha** | **2** (450/892)<br>**0** (450/892)<br>**3** (448/892)<br>**7** (441/892)<br>**5** (425/892) | **K** (44/892)<br>**V** (43/892)<br>**T** (43/892)<br>**S** (41/892)<br>**G** (41/892) |

