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

> **Last Updated (Sri Lanka Time):** `2026-06-23 01:50:08 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 249 Rows | 12.01 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 257 Rows | 11.00 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 256 Rows | 10.84 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 256 Rows | 10.57 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 256 Rows | 10.89 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 255 Rows | 11.55 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 246 Rows | 9.59 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 255 Rows | 11.76 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1775 Rows | 67.88 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1663 Rows | 67.93 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1782 Rows | 66.41 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 960 Rows | 31.72 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1776 Rows | 67.92 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 934 Rows | 34.72 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-23 01:50:08 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (94/249)<br>**6** (92/249)<br>**0** (90/249)<br>**2** (88/249)<br>**7** (87/249) | **N** (15/249)<br>**J** (15/249)<br>**Q** (14/249)<br>**D** (14/249)<br>**Y** (13/249) |
| **Dhana Nidhanaya** | **9** (25/257)<br>**28** (24/257)<br>**6** (21/257)<br>**7** (21/257)<br>**4** (20/257) | **U** (17/257)<br>**F** (14/257)<br>**W** (13/257)<br>**Z** (12/257)<br>**T** (12/257) |
| **Govisetha** | **55** (21/256)<br>**10** (20/256)<br>**23** (20/256)<br>**44** (19/256)<br>**29** (19/256) | **P** (15/256)<br>**C** (14/256)<br>**D** (12/256)<br>**O** (12/256)<br>**M** (12/256) |
| **Handahana** | **58** (26/256)<br>**21** (25/256)<br>**6** (25/256)<br>**11** (23/256)<br>**55** (23/256) | N/A |
| **Mahajana Sampatha** | **1** (127/256)<br>**2** (126/256)<br>**5** (125/256)<br>**6** (125/256)<br>**4** (123/256) | **J** (15/256)<br>**N** (14/256)<br>**Q** (14/256)<br>**D** (14/256)<br>**Y** (13/256) |
| **Mega Power** | **11** (33/255)<br>**3** (29/255)<br>**22** (28/255)<br>**19** (28/255)<br>**13** (28/255) | **V** (18/255)<br>**U** (16/255)<br>**T** (15/255)<br>**K** (15/255)<br>**J** (14/255) |
| **Nlb Jaya** | **5** (109/246)<br>**3** (96/246)<br>**0** (95/246)<br>**2** (91/246)<br>**7** (87/246) | **T** (15/246)<br>**G** (15/246)<br>**P** (14/246)<br>**I** (14/246)<br>**Y** (14/246) |
| **Suba Dawasak** | **3** (107/255)<br>**1** (102/255)<br>**4** (102/255)<br>**9** (95/255)<br>**5** (92/255) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1775)<br>**20** (117/1775)<br>**57** (116/1775)<br>**75** (110/1775)<br>**38** (109/1775) | **B** (82/1775)<br>**R** (79/1775)<br>**P** (79/1775)<br>**M** (79/1775)<br>**I** (76/1775) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1663)<br>**10** (142/1663)<br>**27** (137/1663)<br>**29** (136/1663)<br>**21** (136/1663) | **H** (88/1663)<br>**U** (77/1663)<br>**X** (72/1663)<br>**W** (72/1663)<br>**G** (71/1663) |
| **Lagna Wasana** | **28** (136/1782)<br>**5** (135/1782)<br>**36** (133/1782)<br>**23** (132/1782)<br>**2** (131/1782) | N/A |
| **Sasiri** | **9** (73/960)<br>**20** (71/960)<br>**26** (71/960)<br>**22** (70/960)<br>**19** (67/960) | N/A |
| **Super Ball** | **45** (110/1776)<br>**52** (107/1776)<br>**74** (107/1776)<br>**3** (106/1776)<br>**57** (106/1776) | **I** (90/1776)<br>**D** (81/1776)<br>**V** (80/1776)<br>**T** (79/1776)<br>**A** (79/1776) |
| **Supiri Dhana Sampatha** | **2** (471/934)<br>**0** (471/934)<br>**3** (468/934)<br>**7** (458/934)<br>**5** (447/934) | **K** (46/934)<br>**V** (46/934)<br>**S** (43/934)<br>**M** (43/934)<br>**T** (43/934) |

