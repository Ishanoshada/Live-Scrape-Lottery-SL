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

> **Last Updated (Sri Lanka Time):** `2026-06-15 12:21:04 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 241 Rows | 11.64 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 249 Rows | 10.67 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 248 Rows | 10.52 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 248 Rows | 10.26 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 248 Rows | 10.57 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 248 Rows | 11.25 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 239 Rows | 9.33 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 248 Rows | 11.46 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1767 Rows | 67.58 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1655 Rows | 67.60 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1774 Rows | 66.12 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 952 Rows | 31.45 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1768 Rows | 67.62 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 926 Rows | 34.42 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-15 12:21:04 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (91/241)<br>**5** (90/241)<br>**0** (87/241)<br>**7** (85/241)<br>**3** (82/241) | **J** (15/241)<br>**N** (14/241)<br>**Q** (14/241)<br>**D** (14/241)<br>**Y** (12/241) |
| **Dhana Nidhanaya** | **28** (24/249)<br>**9** (23/249)<br>**6** (21/249)<br>**16** (20/249)<br>**4** (19/249) | **U** (16/249)<br>**W** (13/249)<br>**Z** (12/249)<br>**T** (12/249)<br>**S** (12/249) |
| **Govisetha** | **55** (21/248)<br>**10** (20/248)<br>**44** (19/248)<br>**33** (19/248)<br>**23** (18/248) | **P** (15/248)<br>**C** (14/248)<br>**D** (12/248)<br>**O** (12/248)<br>**M** (12/248) |
| **Handahana** | **21** (25/248)<br>**6** (25/248)<br>**55** (23/248)<br>**58** (22/248)<br>**11** (22/248) | N/A |
| **Mahajana Sampatha** | **1** (124/248)<br>**5** (121/248)<br>**6** (121/248)<br>**3** (119/248)<br>**4** (119/248) | **J** (15/248)<br>**Q** (14/248)<br>**D** (14/248)<br>**N** (13/248)<br>**Y** (12/248) |
| **Mega Power** | **11** (32/248)<br>**3** (29/248)<br>**6** (27/248)<br>**22** (27/248)<br>**19** (27/248) | **V** (18/248)<br>**U** (15/248)<br>**T** (14/248)<br>**K** (14/248)<br>**J** (14/248) |
| **Nlb Jaya** | **5** (104/239)<br>**0** (94/239)<br>**3** (93/239)<br>**2** (90/239)<br>**1** (85/239) | **T** (15/239)<br>**P** (14/239)<br>**I** (14/239)<br>**Y** (14/239)<br>**M** (13/239) |
| **Suba Dawasak** | **3** (104/248)<br>**4** (100/248)<br>**1** (98/248)<br>**9** (93/248)<br>**5** (90/248) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1767)<br>**20** (117/1767)<br>**57** (115/1767)<br>**38** (109/1767)<br>**13** (109/1767) | **B** (82/1767)<br>**P** (79/1767)<br>**M** (79/1767)<br>**R** (78/1767)<br>**I** (76/1767) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1655)<br>**10** (142/1655)<br>**27** (135/1655)<br>**29** (134/1655)<br>**21** (134/1655) | **H** (88/1655)<br>**U** (76/1655)<br>**W** (72/1655)<br>**G** (71/1655)<br>**X** (71/1655) |
| **Lagna Wasana** | **28** (135/1774)<br>**5** (135/1774)<br>**36** (133/1774)<br>**2** (131/1774)<br>**23** (131/1774) | N/A |
| **Sasiri** | **9** (72/952)<br>**20** (71/952)<br>**26** (70/952)<br>**22** (69/952)<br>**19** (67/952) | N/A |
| **Super Ball** | **45** (110/1768)<br>**52** (107/1768)<br>**74** (107/1768)<br>**3** (106/1768)<br>**29** (106/1768) | **I** (89/1768)<br>**D** (81/1768)<br>**V** (79/1768)<br>**T** (79/1768)<br>**A** (79/1768) |
| **Supiri Dhana Sampatha** | **2** (468/926)<br>**0** (467/926)<br>**3** (463/926)<br>**7** (453/926)<br>**5** (444/926) | **K** (46/926)<br>**V** (44/926)<br>**S** (43/926)<br>**M** (43/926)<br>**T** (43/926) |

