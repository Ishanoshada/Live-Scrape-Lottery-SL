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

> **Last Updated (Sri Lanka Time):** `2026-07-03 12:26:59 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 259 Rows | 12.47 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 267 Rows | 11.41 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 266 Rows | 11.24 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 266 Rows | 10.96 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 266 Rows | 11.30 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 266 Rows | 12.02 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 257 Rows | 10.00 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 266 Rows | 12.25 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1785 Rows | 68.27 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1673 Rows | 68.35 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1792 Rows | 66.79 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 970 Rows | 32.07 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1786 Rows | 68.31 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 944 Rows | 35.09 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-03 12:26:59 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (96/259)<br>**6** (96/259)<br>**2** (93/259)<br>**7** (92/259)<br>**0** (90/259) | **N** (16/259)<br>**Q** (15/259)<br>**J** (15/259)<br>**G** (15/259)<br>**D** (14/259) |
| **Dhana Nidhanaya** | **9** (25/267)<br>**28** (24/267)<br>**7** (24/267)<br>**4** (22/267)<br>**6** (21/267) | **U** (17/267)<br>**F** (15/267)<br>**W** (14/267)<br>**Z** (13/267)<br>**E** (13/267) |
| **Govisetha** | **55** (22/266)<br>**10** (21/266)<br>**23** (20/266)<br>**29** (20/266)<br>**44** (19/266) | **P** (15/266)<br>**C** (14/266)<br>**D** (13/266)<br>**A** (12/266)<br>**O** (12/266) |
| **Handahana** | **58** (27/266)<br>**21** (27/266)<br>**6** (26/266)<br>**11** (25/266)<br>**61** (23/266) | N/A |
| **Mahajana Sampatha** | **2** (132/266)<br>**5** (131/266)<br>**7** (130/266)<br>**1** (130/266)<br>**6** (130/266) | **N** (15/266)<br>**Q** (15/266)<br>**J** (15/266)<br>**G** (15/266)<br>**D** (14/266) |
| **Mega Power** | **11** (36/266)<br>**3** (31/266)<br>**6** (29/266)<br>**19** (29/266)<br>**13** (29/266) | **V** (19/266)<br>**T** (18/266)<br>**U** (18/266)<br>**K** (15/266)<br>**J** (15/266) |
| **Nlb Jaya** | **5** (116/257)<br>**3** (99/257)<br>**0** (99/257)<br>**2** (98/257)<br>**7** (92/257) | **T** (16/257)<br>**G** (16/257)<br>**I** (15/257)<br>**P** (14/257)<br>**Y** (14/257) |
| **Suba Dawasak** | **3** (110/266)<br>**4** (109/266)<br>**1** (106/266)<br>**9** (96/266)<br>**2** (96/266) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1785)<br>**20** (119/1785)<br>**57** (116/1785)<br>**75** (110/1785)<br>**38** (110/1785) | **B** (82/1785)<br>**R** (81/1785)<br>**P** (79/1785)<br>**M** (79/1785)<br>**I** (77/1785) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1673)<br>**10** (143/1673)<br>**27** (138/1673)<br>**29** (137/1673)<br>**15** (137/1673) | **H** (88/1673)<br>**U** (77/1673)<br>**M** (73/1673)<br>**X** (72/1673)<br>**W** (72/1673) |
| **Lagna Wasana** | **28** (136/1792)<br>**5** (136/1792)<br>**36** (134/1792)<br>**23** (132/1792)<br>**25** (132/1792) | N/A |
| **Sasiri** | **9** (73/970)<br>**22** (71/970)<br>**20** (71/970)<br>**26** (71/970)<br>**5** (69/970) | N/A |
| **Super Ball** | **45** (110/1786)<br>**52** (109/1786)<br>**29** (109/1786)<br>**74** (107/1786)<br>**3** (106/1786) | **I** (90/1786)<br>**D** (81/1786)<br>**V** (80/1786)<br>**T** (80/1786)<br>**A** (79/1786) |
| **Supiri Dhana Sampatha** | **2** (476/944)<br>**0** (473/944)<br>**3** (473/944)<br>**7** (463/944)<br>**5** (450/944) | **V** (47/944)<br>**K** (46/944)<br>**S** (43/944)<br>**J** (43/944)<br>**M** (43/944) |

