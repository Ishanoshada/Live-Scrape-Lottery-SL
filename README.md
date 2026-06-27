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

> **Last Updated (Sri Lanka Time):** `2026-06-28 12:14:26 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 254 Rows | 12.24 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 262 Rows | 11.20 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 261 Rows | 11.04 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 261 Rows | 10.77 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 261 Rows | 11.10 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 261 Rows | 11.81 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 252 Rows | 9.81 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 261 Rows | 12.03 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1780 Rows | 68.08 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1668 Rows | 68.14 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1787 Rows | 66.60 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 965 Rows | 31.90 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1781 Rows | 68.11 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 939 Rows | 34.91 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-28 12:14:26 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (96/254)<br>**5** (95/254)<br>**0** (90/254)<br>**2** (90/254)<br>**7** (89/254) | **N** (15/254)<br>**Q** (15/254)<br>**J** (15/254)<br>**D** (14/254)<br>**G** (14/254) |
| **Dhana Nidhanaya** | **9** (25/262)<br>**28** (24/262)<br>**7** (22/262)<br>**4** (21/262)<br>**6** (21/262) | **U** (17/262)<br>**F** (14/262)<br>**W** (14/262)<br>**Z** (12/262)<br>**T** (12/262) |
| **Govisetha** | **10** (21/261)<br>**55** (21/261)<br>**23** (20/261)<br>**29** (20/261)<br>**44** (19/261) | **P** (15/261)<br>**C** (14/261)<br>**D** (13/261)<br>**A** (12/261)<br>**O** (12/261) |
| **Handahana** | **58** (26/261)<br>**21** (26/261)<br>**11** (25/261)<br>**6** (25/261)<br>**55** (23/261) | N/A |
| **Mahajana Sampatha** | **2** (129/261)<br>**6** (129/261)<br>**5** (128/261)<br>**1** (128/261)<br>**4** (126/261) | **Q** (15/261)<br>**J** (15/261)<br>**N** (14/261)<br>**D** (14/261)<br>**G** (14/261) |
| **Mega Power** | **11** (35/261)<br>**3** (31/261)<br>**13** (29/261)<br>**22** (28/261)<br>**6** (28/261) | **V** (18/261)<br>**U** (18/261)<br>**T** (17/261)<br>**K** (15/261)<br>**J** (15/261) |
| **Nlb Jaya** | **5** (113/252)<br>**3** (97/252)<br>**2** (96/252)<br>**0** (96/252)<br>**1** (89/252) | **G** (16/252)<br>**I** (15/252)<br>**T** (15/252)<br>**P** (14/252)<br>**Y** (14/252) |
| **Suba Dawasak** | **3** (109/261)<br>**4** (105/261)<br>**1** (103/261)<br>**9** (95/261)<br>**2** (94/261) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1780)<br>**20** (118/1780)<br>**57** (116/1780)<br>**75** (110/1780)<br>**38** (109/1780) | **B** (82/1780)<br>**R** (81/1780)<br>**P** (79/1780)<br>**M** (79/1780)<br>**I** (76/1780) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1668)<br>**10** (143/1668)<br>**27** (137/1668)<br>**29** (136/1668)<br>**21** (136/1668) | **H** (88/1668)<br>**U** (77/1668)<br>**M** (73/1668)<br>**X** (72/1668)<br>**W** (72/1668) |
| **Lagna Wasana** | **28** (136/1787)<br>**5** (135/1787)<br>**36** (133/1787)<br>**23** (132/1787)<br>**2** (131/1787) | N/A |
| **Sasiri** | **9** (73/965)<br>**20** (71/965)<br>**26** (71/965)<br>**22** (70/965)<br>**5** (68/965) | N/A |
| **Super Ball** | **45** (110/1781)<br>**52** (108/1781)<br>**74** (107/1781)<br>**29** (107/1781)<br>**3** (106/1781) | **I** (90/1781)<br>**D** (81/1781)<br>**V** (80/1781)<br>**T** (80/1781)<br>**A** (79/1781) |
| **Supiri Dhana Sampatha** | **2** (474/939)<br>**0** (472/939)<br>**3** (471/939)<br>**7** (459/939)<br>**5** (449/939) | **K** (46/939)<br>**V** (46/939)<br>**S** (43/939)<br>**M** (43/939)<br>**T** (43/939) |

