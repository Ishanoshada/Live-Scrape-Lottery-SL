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

> **Last Updated (Sri Lanka Time):** `2026-08-02 11:59:06 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 290 Rows | 13.90 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 298 Rows | 12.69 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 297 Rows | 12.49 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 297 Rows | 12.18 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 297 Rows | 12.55 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 297 Rows | 13.35 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 287 Rows | 11.12 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 296 Rows | 13.57 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1816 Rows | 69.45 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1704 Rows | 69.62 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1823 Rows | 67.94 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1001 Rows | 33.13 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1817 Rows | 69.49 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 975 Rows | 36.25 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-02 11:59:06 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (108/290)<br>**2** (104/290)<br>**6** (103/290)<br>**3** (101/290)<br>**4** (100/290) | **D** (19/290)<br>**Q** (17/290)<br>**J** (17/290)<br>**N** (16/290)<br>**G** (16/290) |
| **Dhana Nidhanaya** | **9** (27/298)<br>**7** (26/298)<br>**4** (25/298)<br>**28** (25/298)<br>**6** (23/298) | **U** (20/298)<br>**F** (16/298)<br>**W** (16/298)<br>**Z** (15/298)<br>**T** (15/298) |
| **Govisetha** | **55** (25/297)<br>**10** (23/297)<br>**44** (22/297)<br>**33** (22/297)<br>**23** (21/297) | **P** (16/297)<br>**C** (16/297)<br>**K** (15/297)<br>**O** (14/297)<br>**Y** (14/297) |
| **Handahana** | **58** (31/297)<br>**11** (29/297)<br>**6** (28/297)<br>**21** (27/297)<br>**55** (27/297) | N/A |
| **Mahajana Sampatha** | **2** (147/297)<br>**5** (146/297)<br>**4** (145/297)<br>**7** (145/297)<br>**1** (144/297) | **D** (19/297)<br>**Q** (17/297)<br>**J** (17/297)<br>**G** (16/297)<br>**N** (15/297) |
| **Mega Power** | **11** (36/297)<br>**22** (32/297)<br>**6** (32/297)<br>**3** (32/297)<br>**13** (32/297) | **T** (21/297)<br>**V** (20/297)<br>**U** (19/297)<br>**K** (17/297)<br>**J** (16/297) |
| **Nlb Jaya** | **5** (128/287)<br>**0** (110/287)<br>**2** (109/287)<br>**3** (108/287)<br>**7** (103/287) | **T** (18/287)<br>**I** (17/287)<br>**G** (16/287)<br>**Y** (15/287)<br>**M** (14/287) |
| **Suba Dawasak** | **3** (120/296)<br>**4** (120/296)<br>**1** (116/296)<br>**9** (110/296)<br>**8** (110/296) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1816)<br>**20** (119/1816)<br>**57** (117/1816)<br>**38** (113/1816)<br>**75** (112/1816) | **R** (83/1816)<br>**B** (82/1816)<br>**P** (80/1816)<br>**M** (80/1816)<br>**N** (78/1816) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (158/1704)<br>**10** (145/1704)<br>**6** (141/1704)<br>**29** (140/1704)<br>**15** (140/1704) | **H** (88/1704)<br>**U** (78/1704)<br>**G** (73/1704)<br>**M** (73/1704)<br>**X** (73/1704) |
| **Lagna Wasana** | **5** (140/1823)<br>**25** (136/1823)<br>**28** (136/1823)<br>**36** (135/1823)<br>**23** (135/1823) | N/A |
| **Sasiri** | **9** (75/1001)<br>**22** (74/1001)<br>**20** (74/1001)<br>**19** (71/1001)<br>**26** (71/1001) | N/A |
| **Super Ball** | **45** (111/1817)<br>**29** (111/1817)<br>**52** (110/1817)<br>**9** (109/1817)<br>**3** (107/1817) | **I** (92/1817)<br>**D** (82/1817)<br>**V** (81/1817)<br>**T** (81/1817)<br>**A** (79/1817) |
| **Supiri Dhana Sampatha** | **2** (492/975)<br>**0** (490/975)<br>**3** (484/975)<br>**7** (480/975)<br>**5** (464/975) | **V** (51/975)<br>**K** (46/975)<br>**S** (44/975)<br>**J** (44/975)<br>**T** (44/975) |

