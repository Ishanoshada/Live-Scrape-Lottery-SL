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

> **Last Updated (Sri Lanka Time):** `2026-07-12 11:56:55 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 269 Rows | 12.93 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 277 Rows | 11.82 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 276 Rows | 11.64 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 276 Rows | 11.35 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 276 Rows | 11.70 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 276 Rows | 12.45 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 267 Rows | 10.38 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 276 Rows | 12.69 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1795 Rows | 68.65 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1683 Rows | 68.76 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1802 Rows | 67.16 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 980 Rows | 32.41 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1796 Rows | 68.69 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 954 Rows | 35.46 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-12 11:56:55 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (98/269)<br>**6** (97/269)<br>**2** (96/269)<br>**7** (95/269)<br>**4** (94/269) | **Q** (17/269)<br>**N** (16/269)<br>**D** (16/269)<br>**J** (16/269)<br>**G** (15/269) |
| **Dhana Nidhanaya** | **9** (26/277)<br>**28** (24/277)<br>**7** (24/277)<br>**4** (23/277)<br>**6** (23/277) | **U** (17/277)<br>**F** (15/277)<br>**W** (15/277)<br>**Z** (14/277)<br>**E** (13/277) |
| **Govisetha** | **55** (23/276)<br>**10** (21/276)<br>**23** (20/276)<br>**29** (20/276)<br>**33** (20/276) | **P** (16/276)<br>**C** (15/276)<br>**D** (13/276)<br>**A** (13/276)<br>**K** (13/276) |
| **Handahana** | **58** (28/276)<br>**11** (27/276)<br>**21** (27/276)<br>**6** (26/276)<br>**55** (25/276) | N/A |
| **Mahajana Sampatha** | **2** (137/276)<br>**4** (136/276)<br>**6** (135/276)<br>**7** (134/276)<br>**5** (134/276) | **Q** (17/276)<br>**D** (16/276)<br>**J** (16/276)<br>**N** (15/276)<br>**G** (15/276) |
| **Mega Power** | **11** (36/276)<br>**6** (31/276)<br>**3** (31/276)<br>**22** (30/276)<br>**19** (30/276) | **V** (19/276)<br>**U** (19/276)<br>**T** (18/276)<br>**J** (16/276)<br>**K** (15/276) |
| **Nlb Jaya** | **5** (119/267)<br>**2** (103/267)<br>**3** (102/267)<br>**0** (102/267)<br>**4** (96/267) | **T** (17/267)<br>**I** (16/267)<br>**G** (16/267)<br>**M** (14/267)<br>**P** (14/267) |
| **Suba Dawasak** | **3** (113/276)<br>**4** (113/276)<br>**1** (108/276)<br>**8** (101/276)<br>**5** (100/276) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (121/1795)<br>**20** (119/1795)<br>**57** (116/1795)<br>**75** (111/1795)<br>**38** (111/1795) | **B** (82/1795)<br>**R** (81/1795)<br>**P** (80/1795)<br>**M** (79/1795)<br>**I** (77/1795) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1683)<br>**10** (144/1683)<br>**27** (138/1683)<br>**15** (138/1683)<br>**29** (137/1683) | **H** (88/1683)<br>**U** (77/1683)<br>**M** (73/1683)<br>**X** (72/1683)<br>**W** (72/1683) |
| **Lagna Wasana** | **5** (138/1802)<br>**28** (136/1802)<br>**36** (134/1802)<br>**25** (134/1802)<br>**23** (132/1802) | N/A |
| **Sasiri** | **9** (74/980)<br>**20** (72/980)<br>**22** (71/980)<br>**26** (71/980)<br>**5** (69/980) | N/A |
| **Super Ball** | **52** (110/1796)<br>**45** (110/1796)<br>**29** (110/1796)<br>**74** (107/1796)<br>**57** (107/1796) | **I** (90/1796)<br>**V** (81/1796)<br>**T** (81/1796)<br>**D** (81/1796)<br>**A** (79/1796) |
| **Supiri Dhana Sampatha** | **2** (483/954)<br>**3** (478/954)<br>**0** (477/954)<br>**7** (469/954)<br>**5** (454/954) | **V** (49/954)<br>**K** (46/954)<br>**T** (44/954)<br>**S** (43/954)<br>**J** (43/954) |

