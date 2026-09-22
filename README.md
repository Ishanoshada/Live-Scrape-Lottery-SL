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

> **Last Updated (Sri Lanka Time):** `2026-09-23 01:51:18 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 341 Rows | 16.41 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 349 Rows | 14.93 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 348 Rows | 14.70 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 348 Rows | 14.33 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 348 Rows | 14.76 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 348 Rows | 15.70 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 339 Rows | 13.21 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 348 Rows | 16.02 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1867 Rows | 71.40 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1755 Rows | 71.72 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1874 Rows | 69.84 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1052 Rows | 34.88 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1868 Rows | 71.44 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1026 Rows | 38.17 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-23 01:51:18 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/341)<br>**2** (124/341)<br>**6** (118/341)<br>**4** (117/341)<br>**1** (117/341) | **D** (22/341)<br>**Q** (20/341)<br>**J** (20/341)<br>**N** (18/341)<br>**G** (18/341) |
| **Dhana Nidhanaya** | **9** (32/349)<br>**4** (30/349)<br>**7** (29/349)<br>**3** (27/349)<br>**28** (26/349) | **U** (20/349)<br>**W** (19/349)<br>**Z** (18/349)<br>**F** (18/349)<br>**M** (18/349) |
| **Govisetha** | **55** (28/348)<br>**10** (26/348)<br>**44** (26/348)<br>**33** (25/348)<br>**29** (24/348) | **P** (19/348)<br>**I** (18/348)<br>**C** (18/348)<br>**X** (17/348)<br>**W** (16/348) |
| **Handahana** | **58** (32/348)<br>**11** (31/348)<br>**55** (31/348)<br>**60** (30/348)<br>**21** (30/348) | N/A |
| **Mahajana Sampatha** | **1** (173/348)<br>**2** (172/348)<br>**5** (172/348)<br>**3** (167/348)<br>**9** (167/348) | **D** (22/348)<br>**Q** (20/348)<br>**J** (20/348)<br>**W** (19/348)<br>**G** (18/348) |
| **Mega Power** | **11** (40/348)<br>**26** (38/348)<br>**3** (37/348)<br>**13** (36/348)<br>**22** (34/348) | **T** (22/348)<br>**V** (22/348)<br>**U** (22/348)<br>**K** (19/348)<br>**J** (17/348) |
| **Nlb Jaya** | **5** (142/339)<br>**0** (131/339)<br>**3** (129/339)<br>**2** (128/339)<br>**7** (127/339) | **T** (20/339)<br>**I** (19/339)<br>**G** (18/339)<br>**P** (17/339)<br>**O** (17/339) |
| **Suba Dawasak** | **4** (141/348)<br>**3** (140/348)<br>**8** (132/348)<br>**9** (132/348)<br>**2** (132/348) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1867)<br>**20** (122/1867)<br>**57** (121/1867)<br>**38** (118/1867)<br>**29** (114/1867) | **B** (88/1867)<br>**R** (85/1867)<br>**M** (84/1867)<br>**P** (81/1867)<br>**N** (81/1867) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1755)<br>**10** (149/1755)<br>**21** (146/1755)<br>**6** (144/1755)<br>**29** (144/1755) | **H** (89/1755)<br>**U** (80/1755)<br>**M** (78/1755)<br>**G** (76/1755)<br>**D** (75/1755) |
| **Lagna Wasana** | **5** (143/1874)<br>**23** (142/1874)<br>**39** (139/1874)<br>**36** (139/1874)<br>**25** (139/1874) | N/A |
| **Sasiri** | **9** (82/1052)<br>**20** (79/1052)<br>**22** (78/1052)<br>**26** (77/1052)<br>**21** (77/1052) | N/A |
| **Super Ball** | **45** (113/1868)<br>**52** (112/1868)<br>**9** (112/1868)<br>**29** (112/1868)<br>**43** (111/1868) | **I** (93/1868)<br>**V** (84/1868)<br>**T** (84/1868)<br>**D** (82/1868)<br>**A** (82/1868) |
| **Supiri Dhana Sampatha** | **0** (516/1026)<br>**2** (514/1026)<br>**3** (507/1026)<br>**7** (505/1026)<br>**8** (490/1026) | **V** (55/1026)<br>**K** (48/1026)<br>**S** (48/1026)<br>**T** (47/1026)<br>**G** (46/1026) |

