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

> **Last Updated (Sri Lanka Time):** `2026-06-20 12:44:42 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 246 Rows | 11.87 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 254 Rows | 10.87 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 253 Rows | 10.72 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 253 Rows | 10.46 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 253 Rows | 10.78 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 253 Rows | 11.46 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 244 Rows | 9.51 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 253 Rows | 11.68 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1772 Rows | 67.77 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1660 Rows | 67.81 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1779 Rows | 66.30 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 957 Rows | 31.62 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1773 Rows | 67.81 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 931 Rows | 34.61 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-20 12:44:42 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (92/246)<br>**6** (91/246)<br>**0** (90/246)<br>**2** (86/246)<br>**7** (86/246) | **N** (15/246)<br>**J** (15/246)<br>**Q** (14/246)<br>**D** (14/246)<br>**Y** (13/246) |
| **Dhana Nidhanaya** | **28** (24/254)<br>**9** (24/254)<br>**6** (21/254)<br>**16** (20/254)<br>**4** (19/254) | **U** (17/254)<br>**W** (13/254)<br>**Z** (12/254)<br>**T** (12/254)<br>**S** (12/254) |
| **Govisetha** | **55** (21/253)<br>**10** (20/253)<br>**23** (19/253)<br>**44** (19/253)<br>**33** (19/253) | **P** (15/253)<br>**C** (14/253)<br>**D** (12/253)<br>**O** (12/253)<br>**M** (12/253) |
| **Handahana** | **21** (25/253)<br>**6** (25/253)<br>**58** (24/253)<br>**11** (23/253)<br>**55** (23/253) | N/A |
| **Mahajana Sampatha** | **1** (126/253)<br>**6** (124/253)<br>**2** (123/253)<br>**5** (123/253)<br>**0** (121/253) | **J** (15/253)<br>**N** (14/253)<br>**Q** (14/253)<br>**D** (14/253)<br>**Y** (13/253) |
| **Mega Power** | **11** (32/253)<br>**3** (29/253)<br>**22** (28/253)<br>**13** (28/253)<br>**6** (27/253) | **V** (18/253)<br>**U** (16/253)<br>**K** (15/253)<br>**T** (14/253)<br>**J** (14/253) |
| **Nlb Jaya** | **5** (108/244)<br>**3** (95/244)<br>**0** (95/244)<br>**2** (90/244)<br>**7** (86/244) | **T** (15/244)<br>**G** (15/244)<br>**P** (14/244)<br>**I** (14/244)<br>**Y** (14/244) |
| **Suba Dawasak** | **3** (105/253)<br>**1** (101/253)<br>**4** (101/253)<br>**9** (95/253)<br>**5** (91/253) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1772)<br>**20** (117/1772)<br>**57** (115/1772)<br>**75** (110/1772)<br>**38** (109/1772) | **B** (82/1772)<br>**R** (79/1772)<br>**P** (79/1772)<br>**M** (79/1772)<br>**I** (76/1772) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1660)<br>**10** (142/1660)<br>**29** (136/1660)<br>**21** (136/1660)<br>**27** (136/1660) | **H** (88/1660)<br>**U** (77/1660)<br>**X** (72/1660)<br>**W** (72/1660)<br>**G** (71/1660) |
| **Lagna Wasana** | **28** (136/1779)<br>**5** (135/1779)<br>**36** (133/1779)<br>**23** (132/1779)<br>**2** (131/1779) | N/A |
| **Sasiri** | **9** (73/957)<br>**20** (71/957)<br>**26** (71/957)<br>**22** (70/957)<br>**19** (67/957) | N/A |
| **Super Ball** | **45** (110/1773)<br>**52** (107/1773)<br>**74** (107/1773)<br>**3** (106/1773)<br>**57** (106/1773) | **I** (89/1773)<br>**D** (81/1773)<br>**V** (80/1773)<br>**T** (79/1773)<br>**A** (79/1773) |
| **Supiri Dhana Sampatha** | **0** (471/931)<br>**2** (469/931)<br>**3** (467/931)<br>**7** (456/931)<br>**5** (445/931) | **K** (46/931)<br>**V** (45/931)<br>**S** (43/931)<br>**M** (43/931)<br>**T** (43/931) |

