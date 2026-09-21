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

> **Last Updated (Sri Lanka Time):** `2026-09-22 02:40:48 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 340 Rows | 16.36 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 348 Rows | 14.89 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 347 Rows | 14.65 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 347 Rows | 14.28 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 347 Rows | 14.72 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 347 Rows | 15.65 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 338 Rows | 13.17 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 347 Rows | 15.97 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1866 Rows | 71.36 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1754 Rows | 71.68 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1873 Rows | 69.80 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1051 Rows | 34.85 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1867 Rows | 71.40 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1025 Rows | 38.13 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-22 02:40:48 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/340)<br>**2** (124/340)<br>**6** (118/340)<br>**8** (116/340)<br>**3** (116/340) | **D** (22/340)<br>**Q** (20/340)<br>**J** (20/340)<br>**N** (18/340)<br>**G** (18/340) |
| **Dhana Nidhanaya** | **9** (32/348)<br>**4** (30/348)<br>**7** (28/348)<br>**3** (27/348)<br>**28** (26/348) | **U** (20/348)<br>**W** (19/348)<br>**Z** (18/348)<br>**F** (18/348)<br>**M** (18/348) |
| **Govisetha** | **55** (28/347)<br>**10** (26/347)<br>**44** (25/347)<br>**29** (24/347)<br>**33** (24/347) | **P** (19/347)<br>**C** (18/347)<br>**I** (17/347)<br>**X** (17/347)<br>**W** (16/347) |
| **Handahana** | **58** (32/347)<br>**11** (31/347)<br>**55** (31/347)<br>**60** (30/347)<br>**21** (30/347) | N/A |
| **Mahajana Sampatha** | **5** (172/347)<br>**2** (172/347)<br>**1** (172/347)<br>**3** (167/347)<br>**9** (167/347) | **D** (22/347)<br>**Q** (20/347)<br>**J** (20/347)<br>**W** (19/347)<br>**G** (18/347) |
| **Mega Power** | **11** (40/347)<br>**26** (38/347)<br>**3** (37/347)<br>**13** (35/347)<br>**22** (34/347) | **T** (22/347)<br>**V** (22/347)<br>**U** (22/347)<br>**K** (18/347)<br>**J** (17/347) |
| **Nlb Jaya** | **5** (142/338)<br>**0** (131/338)<br>**3** (128/338)<br>**2** (128/338)<br>**7** (126/338) | **T** (20/338)<br>**I** (19/338)<br>**G** (18/338)<br>**P** (17/338)<br>**O** (17/338) |
| **Suba Dawasak** | **3** (140/347)<br>**4** (140/347)<br>**8** (132/347)<br>**9** (132/347)<br>**2** (131/347) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1866)<br>**20** (122/1866)<br>**57** (121/1866)<br>**38** (118/1866)<br>**29** (114/1866) | **B** (88/1866)<br>**R** (85/1866)<br>**M** (83/1866)<br>**P** (81/1866)<br>**N** (81/1866) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1754)<br>**10** (149/1754)<br>**21** (146/1754)<br>**6** (144/1754)<br>**29** (144/1754) | **H** (89/1754)<br>**U** (80/1754)<br>**M** (78/1754)<br>**G** (76/1754)<br>**D** (75/1754) |
| **Lagna Wasana** | **5** (143/1873)<br>**23** (142/1873)<br>**39** (139/1873)<br>**36** (139/1873)<br>**25** (139/1873) | N/A |
| **Sasiri** | **9** (82/1051)<br>**20** (79/1051)<br>**22** (78/1051)<br>**26** (77/1051)<br>**21** (77/1051) | N/A |
| **Super Ball** | **52** (112/1867)<br>**9** (112/1867)<br>**45** (112/1867)<br>**29** (112/1867)<br>**43** (111/1867) | **I** (93/1867)<br>**T** (84/1867)<br>**V** (83/1867)<br>**D** (82/1867)<br>**A** (82/1867) |
| **Supiri Dhana Sampatha** | **0** (516/1025)<br>**2** (514/1025)<br>**3** (507/1025)<br>**7** (504/1025)<br>**8** (489/1025) | **V** (55/1025)<br>**K** (48/1025)<br>**S** (48/1025)<br>**T** (47/1025)<br>**G** (46/1025) |

