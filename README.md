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

> **Last Updated (Sri Lanka Time):** `2026-07-16 12:07:43 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 272 Rows | 13.07 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 280 Rows | 11.95 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 279 Rows | 11.76 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 279 Rows | 11.47 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 279 Rows | 11.82 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 279 Rows | 12.58 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 270 Rows | 10.48 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 279 Rows | 12.82 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1798 Rows | 68.76 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1686 Rows | 68.88 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1805 Rows | 67.27 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 983 Rows | 32.52 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1799 Rows | 68.80 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 957 Rows | 35.58 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-16 12:07:43 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (100/272)<br>**6** (99/272)<br>**2** (96/272)<br>**7** (96/272)<br>**4** (94/272) | **Q** (17/272)<br>**N** (16/272)<br>**D** (16/272)<br>**J** (16/272)<br>**G** (15/272) |
| **Dhana Nidhanaya** | **9** (26/280)<br>**7** (25/280)<br>**28** (24/280)<br>**4** (23/280)<br>**6** (23/280) | **U** (17/280)<br>**F** (15/280)<br>**W** (15/280)<br>**Z** (14/280)<br>**T** (13/280) |
| **Govisetha** | **55** (23/279)<br>**10** (21/279)<br>**44** (21/279)<br>**23** (20/279)<br>**29** (20/279) | **P** (16/279)<br>**C** (15/279)<br>**K** (14/279)<br>**D** (13/279)<br>**A** (13/279) |
| **Handahana** | **58** (29/279)<br>**11** (27/279)<br>**21** (27/279)<br>**6** (26/279)<br>**55** (25/279) | N/A |
| **Mahajana Sampatha** | **4** (137/279)<br>**5** (137/279)<br>**2** (137/279)<br>**6** (137/279)<br>**7** (136/279) | **Q** (17/279)<br>**D** (16/279)<br>**J** (16/279)<br>**N** (15/279)<br>**G** (15/279) |
| **Mega Power** | **11** (36/279)<br>**6** (31/279)<br>**3** (31/279)<br>**22** (30/279)<br>**19** (30/279) | **T** (19/279)<br>**V** (19/279)<br>**U** (19/279)<br>**J** (16/279)<br>**K** (15/279) |
| **Nlb Jaya** | **5** (120/270)<br>**3** (103/270)<br>**2** (103/270)<br>**0** (103/270)<br>**7** (97/270) | **T** (17/270)<br>**I** (16/270)<br>**G** (16/270)<br>**M** (14/270)<br>**P** (14/270) |
| **Suba Dawasak** | **3** (114/279)<br>**4** (114/279)<br>**1** (108/279)<br>**8** (104/279)<br>**9** (101/279) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (121/1798)<br>**20** (119/1798)<br>**57** (116/1798)<br>**75** (111/1798)<br>**38** (111/1798) | **B** (82/1798)<br>**R** (81/1798)<br>**P** (80/1798)<br>**M** (80/1798)<br>**I** (77/1798) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1686)<br>**10** (145/1686)<br>**29** (138/1686)<br>**27** (138/1686)<br>**15** (138/1686) | **H** (88/1686)<br>**U** (77/1686)<br>**M** (73/1686)<br>**X** (72/1686)<br>**W** (72/1686) |
| **Lagna Wasana** | **5** (139/1805)<br>**28** (136/1805)<br>**36** (134/1805)<br>**25** (134/1805)<br>**39** (132/1805) | N/A |
| **Sasiri** | **9** (74/983)<br>**20** (73/983)<br>**22** (71/983)<br>**26** (71/983)<br>**5** (69/983) | N/A |
| **Super Ball** | **52** (110/1799)<br>**45** (110/1799)<br>**29** (110/1799)<br>**74** (107/1799)<br>**57** (107/1799) | **I** (90/1799)<br>**V** (81/1799)<br>**T** (81/1799)<br>**D** (81/1799)<br>**A** (79/1799) |
| **Supiri Dhana Sampatha** | **2** (484/957)<br>**0** (479/957)<br>**3** (478/957)<br>**7** (471/957)<br>**5** (456/957) | **V** (49/957)<br>**K** (46/957)<br>**S** (44/957)<br>**J** (44/957)<br>**T** (44/957) |

