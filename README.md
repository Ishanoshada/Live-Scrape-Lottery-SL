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

> **Last Updated (Sri Lanka Time):** `2026-09-27 01:33:13 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 345 Rows | 16.62 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 353 Rows | 15.12 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 351 Rows | 14.83 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 351 Rows | 14.46 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 351 Rows | 14.90 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 351 Rows | 15.85 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 342 Rows | 13.33 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 351 Rows | 16.17 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1871 Rows | 71.56 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1759 Rows | 71.89 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1878 Rows | 69.99 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1056 Rows | 35.02 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1872 Rows | 71.59 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1030 Rows | 38.33 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-27 01:33:13 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (125/345)<br>**2** (125/345)<br>**6** (121/345)<br>**1** (119/345)<br>**4** (118/345) | **D** (22/345)<br>**Q** (20/345)<br>**J** (20/345)<br>**G** (19/345)<br>**N** (18/345) |
| **Dhana Nidhanaya** | **9** (32/353)<br>**4** (30/353)<br>**7** (29/353)<br>**3** (27/353)<br>**28** (26/353) | **U** (20/353)<br>**W** (20/353)<br>**Z** (18/353)<br>**F** (18/353)<br>**M** (18/353) |
| **Govisetha** | **55** (28/351)<br>**10** (26/351)<br>**44** (26/351)<br>**33** (25/351)<br>**29** (24/351) | **P** (19/351)<br>**I** (18/351)<br>**C** (18/351)<br>**X** (17/351)<br>**W** (16/351) |
| **Handahana** | **58** (32/351)<br>**11** (31/351)<br>**55** (31/351)<br>**60** (30/351)<br>**21** (30/351) | N/A |
| **Mahajana Sampatha** | **1** (176/351)<br>**5** (173/351)<br>**2** (173/351)<br>**3** (168/351)<br>**9** (168/351) | **D** (22/351)<br>**Q** (20/351)<br>**J** (20/351)<br>**G** (19/351)<br>**W** (19/351) |
| **Mega Power** | **11** (40/351)<br>**3** (38/351)<br>**26** (38/351)<br>**13** (37/351)<br>**22** (36/351) | **T** (22/351)<br>**V** (22/351)<br>**U** (22/351)<br>**K** (19/351)<br>**J** (17/351) |
| **Nlb Jaya** | **5** (143/342)<br>**0** (133/342)<br>**3** (130/342)<br>**2** (129/342)<br>**7** (128/342) | **T** (21/342)<br>**I** (19/342)<br>**G** (18/342)<br>**P** (17/342)<br>**O** (17/342) |
| **Suba Dawasak** | **4** (144/351)<br>**3** (140/351)<br>**2** (134/351)<br>**1** (133/351)<br>**9** (133/351) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1871)<br>**20** (122/1871)<br>**57** (122/1871)<br>**38** (118/1871)<br>**29** (114/1871) | **B** (88/1871)<br>**R** (85/1871)<br>**M** (84/1871)<br>**P** (81/1871)<br>**N** (81/1871) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1759)<br>**10** (149/1759)<br>**21** (148/1759)<br>**6** (145/1759)<br>**15** (145/1759) | **H** (89/1759)<br>**U** (81/1759)<br>**M** (78/1759)<br>**G** (76/1759)<br>**D** (75/1759) |
| **Lagna Wasana** | **5** (143/1878)<br>**23** (142/1878)<br>**39** (139/1878)<br>**36** (139/1878)<br>**25** (139/1878) | N/A |
| **Sasiri** | **9** (82/1056)<br>**20** (79/1056)<br>**22** (78/1056)<br>**26** (78/1056)<br>**21** (77/1056) | N/A |
| **Super Ball** | **45** (113/1872)<br>**52** (112/1872)<br>**9** (112/1872)<br>**29** (112/1872)<br>**43** (111/1872) | **I** (93/1872)<br>**T** (85/1872)<br>**V** (84/1872)<br>**D** (82/1872)<br>**A** (82/1872) |
| **Supiri Dhana Sampatha** | **0** (518/1030)<br>**2** (514/1030)<br>**3** (510/1030)<br>**7** (509/1030)<br>**8** (493/1030) | **V** (55/1030)<br>**K** (49/1030)<br>**S** (48/1030)<br>**T** (48/1030)<br>**G** (46/1030) |

