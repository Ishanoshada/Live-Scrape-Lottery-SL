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

> **Last Updated (Sri Lanka Time):** `2026-09-02 01:32:08 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 320 Rows | 15.34 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 328 Rows | 13.99 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 326 Rows | 13.71 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 326 Rows | 13.36 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 326 Rows | 13.77 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 326 Rows | 14.65 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 317 Rows | 12.30 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 326 Rows | 14.95 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1846 Rows | 70.60 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1734 Rows | 70.85 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1853 Rows | 69.06 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1031 Rows | 34.16 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1847 Rows | 70.63 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1005 Rows | 37.37 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-02 01:32:08 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (119/320)<br>**2** (116/320)<br>**3** (112/320)<br>**6** (111/320)<br>**7** (110/320) | **D** (19/320)<br>**J** (19/320)<br>**G** (18/320)<br>**N** (17/320)<br>**Q** (17/320) |
| **Dhana Nidhanaya** | **9** (32/328)<br>**4** (30/328)<br>**7** (28/328)<br>**28** (26/328)<br>**6** (25/328) | **U** (20/328)<br>**F** (18/328)<br>**W** (18/328)<br>**M** (18/328)<br>**Z** (16/328) |
| **Govisetha** | **55** (27/326)<br>**10** (24/326)<br>**44** (24/326)<br>**29** (24/326)<br>**23** (23/326) | **P** (18/326)<br>**C** (18/326)<br>**X** (17/326)<br>**K** (16/326)<br>**A** (14/326) |
| **Handahana** | **58** (32/326)<br>**11** (31/326)<br>**55** (29/326)<br>**6** (29/326)<br>**21** (28/326) | N/A |
| **Mahajana Sampatha** | **5** (164/326)<br>**2** (161/326)<br>**1** (160/326)<br>**7** (159/326)<br>**4** (157/326) | **D** (19/326)<br>**J** (19/326)<br>**G** (18/326)<br>**Q** (17/326)<br>**W** (17/326) |
| **Mega Power** | **11** (37/326)<br>**3** (36/326)<br>**26** (36/326)<br>**13** (35/326)<br>**22** (33/326) | **T** (22/326)<br>**V** (21/326)<br>**U** (20/326)<br>**K** (18/326)<br>**J** (17/326) |
| **Nlb Jaya** | **5** (138/317)<br>**3** (123/317)<br>**0** (123/317)<br>**2** (122/317)<br>**7** (114/317) | **I** (18/317)<br>**T** (18/317)<br>**G** (17/317)<br>**H** (16/317)<br>**O** (16/317) |
| **Suba Dawasak** | **3** (133/326)<br>**4** (131/326)<br>**1** (124/326)<br>**9** (123/326)<br>**8** (123/326) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (125/1846)<br>**20** (121/1846)<br>**57** (119/1846)<br>**38** (116/1846)<br>**75** (114/1846) | **B** (87/1846)<br>**R** (84/1846)<br>**M** (81/1846)<br>**P** (80/1846)<br>**N** (79/1846) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1734)<br>**10** (146/1734)<br>**29** (143/1734)<br>**15** (143/1734)<br>**6** (142/1734) | **H** (89/1734)<br>**U** (78/1734)<br>**M** (77/1734)<br>**D** (75/1734)<br>**G** (75/1734) |
| **Lagna Wasana** | **5** (142/1853)<br>**23** (139/1853)<br>**39** (137/1853)<br>**36** (137/1853)<br>**28** (137/1853) | N/A |
| **Sasiri** | **9** (80/1031)<br>**22** (77/1031)<br>**20** (77/1031)<br>**26** (76/1031)<br>**19** (74/1031) | N/A |
| **Super Ball** | **9** (112/1847)<br>**52** (111/1847)<br>**45** (111/1847)<br>**29** (111/1847)<br>**74** (109/1847) | **I** (93/1847)<br>**V** (82/1847)<br>**T** (82/1847)<br>**D** (82/1847)<br>**A** (81/1847) |
| **Supiri Dhana Sampatha** | **2** (504/1005)<br>**0** (503/1005)<br>**3** (497/1005)<br>**7** (495/1005)<br>**5** (480/1005) | **V** (53/1005)<br>**K** (47/1005)<br>**G** (46/1005)<br>**S** (45/1005)<br>**T** (45/1005) |

