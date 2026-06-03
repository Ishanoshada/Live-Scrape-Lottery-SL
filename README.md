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

> **Last Updated (Sri Lanka Time):** `2026-06-04 02:07:02 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 230 Rows | 11.14 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 238 Rows | 10.21 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 237 Rows | 10.08 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 237 Rows | 9.83 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 237 Rows | 10.13 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 237 Rows | 10.78 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 228 Rows | 8.91 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 237 Rows | 10.97 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1756 Rows | 67.16 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1644 Rows | 67.15 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1763 Rows | 65.71 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 941 Rows | 31.07 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1757 Rows | 67.20 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 915 Rows | 34.01 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-04 02:07:02 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (88/230)<br>**5** (85/230)<br>**7** (81/230)<br>**2** (81/230)<br>**0** (79/230) | **N** (14/230)<br>**D** (14/230)<br>**J** (14/230)<br>**Q** (13/230)<br>**Y** (12/230) |
| **Dhana Nidhanaya** | **28** (23/238)<br>**9** (23/238)<br>**6** (20/238)<br>**7** (19/238)<br>**16** (18/238) | **U** (15/238)<br>**W** (13/238)<br>**Z** (12/238)<br>**T** (12/238)<br>**M** (12/238) |
| **Govisetha** | **10** (20/237)<br>**44** (19/237)<br>**55** (18/237)<br>**33** (18/237)<br>**19** (17/237) | **P** (14/237)<br>**D** (12/237)<br>**O** (12/237)<br>**W** (11/237)<br>**K** (11/237) |
| **Handahana** | **58** (22/237)<br>**61** (22/237)<br>**21** (22/237)<br>**55** (22/237)<br>**6** (22/237) | N/A |
| **Mahajana Sampatha** | **1** (118/237)<br>**6** (117/237)<br>**2** (116/237)<br>**5** (116/237)<br>**4** (114/237) | **D** (14/237)<br>**J** (14/237)<br>**N** (13/237)<br>**Q** (13/237)<br>**Y** (12/237) |
| **Mega Power** | **11** (30/237)<br>**3** (28/237)<br>**22** (27/237)<br>**13** (27/237)<br>**6** (26/237) | **V** (17/237)<br>**T** (14/237)<br>**K** (14/237)<br>**J** (13/237)<br>**U** (13/237) |
| **Nlb Jaya** | **5** (99/228)<br>**0** (90/228)<br>**3** (88/228)<br>**2** (86/228)<br>**1** (81/228) | **P** (14/228)<br>**I** (14/228)<br>**T** (14/228)<br>**M** (13/228)<br>**G** (13/228) |
| **Suba Dawasak** | **3** (99/237)<br>**1** (94/237)<br>**4** (93/237)<br>**9** (89/237)<br>**5** (88/237) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (117/1756)<br>**57** (115/1756)<br>**20** (114/1756)<br>**13** (109/1756)<br>**75** (108/1756) | **B** (82/1756)<br>**M** (79/1756)<br>**R** (78/1756)<br>**P** (78/1756)<br>**I** (75/1756) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1644)<br>**10** (142/1644)<br>**29** (134/1644)<br>**21** (134/1644)<br>**22** (133/1644) | **H** (88/1644)<br>**U** (76/1644)<br>**W** (72/1644)<br>**G** (70/1644)<br>**X** (70/1644) |
| **Lagna Wasana** | **5** (135/1763)<br>**28** (134/1763)<br>**36** (132/1763)<br>**23** (130/1763)<br>**25** (130/1763) | N/A |
| **Sasiri** | **9** (72/941)<br>**20** (70/941)<br>**22** (68/941)<br>**26** (68/941)<br>**19** (67/941) | N/A |
| **Super Ball** | **45** (109/1757)<br>**74** (107/1757)<br>**52** (106/1757)<br>**29** (106/1757)<br>**43** (106/1757) | **I** (87/1757)<br>**D** (81/1757)<br>**T** (79/1757)<br>**V** (77/1757)<br>**A** (77/1757) |
| **Supiri Dhana Sampatha** | **0** (464/915)<br>**2** (461/915)<br>**3** (459/915)<br>**7** (450/915)<br>**5** (437/915) | **K** (44/915)<br>**V** (44/915)<br>**S** (43/915)<br>**M** (43/915)<br>**T** (43/915) |

