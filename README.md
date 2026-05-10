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

> **Last Updated (Sri Lanka Time):** `2026-05-11 02:09:23 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 208 Rows | 10.14 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 216 Rows | 9.33 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 215 Rows | 9.21 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 215 Rows | 8.99 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 215 Rows | 9.27 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 215 Rows | 9.85 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 206 Rows | 8.12 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 215 Rows | 10.02 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1734 Rows | 66.32 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1622 Rows | 66.25 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1741 Rows | 64.89 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 919 Rows | 30.33 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1735 Rows | 66.35 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 893 Rows | 33.19 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-11 02:09:23 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (79/208)<br>**5** (77/208)<br>**7** (74/208)<br>**2** (73/208)<br>**4** (72/208) | **D** (14/208)<br>**J** (14/208)<br>**N** (13/208)<br>**Q** (12/208)<br>**Y** (12/208) |
| **Dhana Nidhanaya** | **28** (21/216)<br>**9** (20/216)<br>**6** (19/216)<br>**16** (18/216)<br>**7** (17/216) | **U** (13/216)<br>**W** (13/216)<br>**T** (12/216)<br>**M** (12/216)<br>**Q** (11/216) |
| **Govisetha** | **44** (18/215)<br>**19** (17/215)<br>**55** (17/215)<br>**23** (16/215)<br>**58** (16/215) | **P** (12/215)<br>**D** (11/215)<br>**W** (11/215)<br>**O** (11/215)<br>**X** (11/215) |
| **Handahana** | **58** (21/215)<br>**60** (20/215)<br>**21** (20/215)<br>**55** (20/215)<br>**6** (20/215) | N/A |
| **Mahajana Sampatha** | **6** (106/215)<br>**2** (105/215)<br>**9** (105/215)<br>**5** (105/215)<br>**1** (105/215) | **D** (14/215)<br>**J** (14/215)<br>**N** (12/215)<br>**Q** (12/215)<br>**Y** (12/215) |
| **Mega Power** | **6** (26/215)<br>**3** (26/215)<br>**13** (25/215)<br>**22** (24/215)<br>**11** (24/215) | **V** (17/215)<br>**T** (13/215)<br>**K** (13/215)<br>**U** (13/215)<br>**J** (11/215) |
| **Nlb Jaya** | **5** (90/206)<br>**3** (82/206)<br>**0** (79/206)<br>**2** (78/206)<br>**4** (73/206) | **M** (13/206)<br>**P** (13/206)<br>**I** (13/206)<br>**T** (13/206)<br>**G** (13/206) |
| **Suba Dawasak** | **3** (87/215)<br>**1** (86/215)<br>**4** (85/215)<br>**9** (81/215)<br>**5** (76/215) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1734)<br>**57** (114/1734)<br>**20** (111/1734)<br>**13** (109/1734)<br>**38** (106/1734) | **B** (81/1734)<br>**M** (78/1734)<br>**R** (77/1734)<br>**P** (77/1734)<br>**I** (74/1734) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1622)<br>**10** (142/1622)<br>**29** (133/1622)<br>**21** (132/1622)<br>**15** (132/1622) | **H** (87/1622)<br>**U** (75/1622)<br>**W** (71/1622)<br>**D** (69/1622)<br>**G** (69/1622) |
| **Lagna Wasana** | **5** (135/1741)<br>**28** (132/1741)<br>**36** (130/1741)<br>**25** (130/1741)<br>**23** (129/1741) | N/A |
| **Sasiri** | **20** (70/919)<br>**9** (69/919)<br>**22** (68/919)<br>**26** (68/919)<br>**19** (67/919) | N/A |
| **Super Ball** | **45** (109/1735)<br>**29** (105/1735)<br>**43** (105/1735)<br>**3** (104/1735)<br>**52** (103/1735) | **I** (86/1735)<br>**D** (80/1735)<br>**T** (78/1735)<br>**V** (77/1735)<br>**A** (77/1735) |
| **Supiri Dhana Sampatha** | **2** (450/893)<br>**0** (450/893)<br>**3** (449/893)<br>**7** (442/893)<br>**5** (425/893) | **K** (44/893)<br>**V** (43/893)<br>**T** (43/893)<br>**J** (42/893)<br>**S** (41/893) |

