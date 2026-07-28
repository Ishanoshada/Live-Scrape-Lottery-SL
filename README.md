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

> **Last Updated (Sri Lanka Time):** `2026-07-29 12:22:59 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 285 Rows | 13.67 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 293 Rows | 12.48 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 292 Rows | 12.28 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 292 Rows | 11.98 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 292 Rows | 12.34 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 292 Rows | 13.13 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 283 Rows | 10.97 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 292 Rows | 13.39 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1811 Rows | 69.26 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1699 Rows | 69.41 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1818 Rows | 67.75 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 996 Rows | 32.96 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1812 Rows | 69.30 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 970 Rows | 36.06 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-29 12:22:59 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (106/285)<br>**2** (103/285)<br>**6** (101/285)<br>**3** (99/285)<br>**7** (99/285) | **D** (19/285)<br>**Q** (17/285)<br>**N** (16/285)<br>**J** (16/285)<br>**G** (16/285) |
| **Dhana Nidhanaya** | **9** (27/293)<br>**7** (26/293)<br>**28** (25/293)<br>**4** (24/293)<br>**6** (23/293) | **U** (19/293)<br>**F** (16/293)<br>**W** (16/293)<br>**Z** (15/293)<br>**T** (15/293) |
| **Govisetha** | **55** (25/292)<br>**10** (22/292)<br>**33** (22/292)<br>**23** (21/292)<br>**44** (21/292) | **P** (16/292)<br>**C** (16/292)<br>**K** (14/292)<br>**D** (13/292)<br>**A** (13/292) |
| **Handahana** | **58** (31/292)<br>**11** (27/292)<br>**21** (27/292)<br>**6** (27/292)<br>**55** (26/292) | N/A |
| **Mahajana Sampatha** | **2** (146/292)<br>**5** (143/292)<br>**4** (142/292)<br>**7** (142/292)<br>**1** (142/292) | **D** (19/292)<br>**Q** (17/292)<br>**J** (16/292)<br>**G** (16/292)<br>**N** (15/292) |
| **Mega Power** | **11** (36/292)<br>**22** (32/292)<br>**6** (32/292)<br>**3** (32/292)<br>**19** (31/292) | **T** (21/292)<br>**V** (20/292)<br>**U** (19/292)<br>**K** (17/292)<br>**J** (16/292) |
| **Nlb Jaya** | **5** (128/283)<br>**0** (108/283)<br>**3** (107/283)<br>**2** (106/283)<br>**7** (102/283) | **T** (18/283)<br>**I** (17/283)<br>**G** (16/283)<br>**M** (14/283)<br>**P** (14/283) |
| **Suba Dawasak** | **3** (119/292)<br>**4** (119/292)<br>**1** (114/292)<br>**8** (108/292)<br>**9** (107/292) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1811)<br>**20** (119/1811)<br>**57** (117/1811)<br>**38** (112/1811)<br>**75** (111/1811) | **R** (83/1811)<br>**B** (82/1811)<br>**P** (80/1811)<br>**M** (80/1811)<br>**I** (77/1811) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1699)<br>**10** (145/1699)<br>**6** (141/1699)<br>**15** (140/1699)<br>**29** (139/1699) | **H** (88/1699)<br>**U** (78/1699)<br>**M** (73/1699)<br>**X** (73/1699)<br>**D** (72/1699) |
| **Lagna Wasana** | **5** (140/1818)<br>**25** (136/1818)<br>**28** (136/1818)<br>**36** (135/1818)<br>**23** (134/1818) | N/A |
| **Sasiri** | **9** (74/996)<br>**22** (73/996)<br>**20** (73/996)<br>**19** (71/996)<br>**26** (71/996) | N/A |
| **Super Ball** | **45** (111/1812)<br>**52** (110/1812)<br>**29** (110/1812)<br>**9** (109/1812)<br>**3** (107/1812) | **I** (92/1812)<br>**D** (82/1812)<br>**V** (81/1812)<br>**T** (81/1812)<br>**A** (79/1812) |
| **Supiri Dhana Sampatha** | **2** (489/970)<br>**0** (487/970)<br>**3** (483/970)<br>**7** (479/970)<br>**5** (463/970) | **V** (50/970)<br>**K** (46/970)<br>**S** (44/970)<br>**J** (44/970)<br>**T** (44/970) |

