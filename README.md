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

> **Last Updated (Sri Lanka Time):** `2026-07-11 11:55:28 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 268 Rows | 12.89 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 276 Rows | 11.78 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 275 Rows | 11.60 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 275 Rows | 11.32 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 275 Rows | 11.66 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 275 Rows | 12.41 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 266 Rows | 10.33 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 275 Rows | 12.64 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1794 Rows | 68.61 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1682 Rows | 68.72 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1801 Rows | 67.12 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 979 Rows | 32.38 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1795 Rows | 68.65 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 953 Rows | 35.43 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-11 11:55:28 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (98/268)<br>**6** (97/268)<br>**7** (95/268)<br>**2** (95/268)<br>**4** (93/268) | **Q** (17/268)<br>**N** (16/268)<br>**D** (16/268)<br>**J** (15/268)<br>**G** (15/268) |
| **Dhana Nidhanaya** | **9** (26/276)<br>**28** (24/276)<br>**7** (24/276)<br>**4** (23/276)<br>**6** (22/276) | **U** (17/276)<br>**F** (15/276)<br>**W** (15/276)<br>**Z** (14/276)<br>**E** (13/276) |
| **Govisetha** | **55** (23/275)<br>**10** (21/275)<br>**23** (20/275)<br>**29** (20/275)<br>**33** (20/275) | **P** (15/275)<br>**C** (15/275)<br>**D** (13/275)<br>**A** (13/275)<br>**K** (13/275) |
| **Handahana** | **58** (28/275)<br>**11** (27/275)<br>**21** (27/275)<br>**6** (26/275)<br>**55** (25/275) | N/A |
| **Mahajana Sampatha** | **2** (136/275)<br>**4** (135/275)<br>**5** (134/275)<br>**6** (134/275)<br>**7** (133/275) | **Q** (17/275)<br>**D** (16/275)<br>**N** (15/275)<br>**J** (15/275)<br>**G** (15/275) |
| **Mega Power** | **11** (36/275)<br>**6** (31/275)<br>**3** (31/275)<br>**19** (30/275)<br>**22** (29/275) | **V** (19/275)<br>**U** (19/275)<br>**T** (18/275)<br>**J** (16/275)<br>**K** (15/275) |
| **Nlb Jaya** | **5** (118/266)<br>**3** (102/266)<br>**2** (102/266)<br>**0** (102/266)<br>**4** (95/266) | **T** (17/266)<br>**I** (16/266)<br>**G** (16/266)<br>**M** (14/266)<br>**P** (14/266) |
| **Suba Dawasak** | **3** (113/275)<br>**4** (113/275)<br>**1** (107/275)<br>**5** (100/275)<br>**8** (100/275) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (121/1794)<br>**20** (119/1794)<br>**57** (116/1794)<br>**75** (111/1794)<br>**38** (110/1794) | **B** (82/1794)<br>**R** (81/1794)<br>**P** (80/1794)<br>**M** (79/1794)<br>**I** (77/1794) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1682)<br>**10** (144/1682)<br>**27** (138/1682)<br>**15** (138/1682)<br>**29** (137/1682) | **H** (88/1682)<br>**U** (77/1682)<br>**M** (73/1682)<br>**X** (72/1682)<br>**W** (72/1682) |
| **Lagna Wasana** | **5** (138/1801)<br>**28** (136/1801)<br>**36** (134/1801)<br>**25** (134/1801)<br>**23** (132/1801) | N/A |
| **Sasiri** | **9** (74/979)<br>**20** (72/979)<br>**22** (71/979)<br>**26** (71/979)<br>**5** (69/979) | N/A |
| **Super Ball** | **52** (110/1795)<br>**45** (110/1795)<br>**29** (110/1795)<br>**74** (107/1795)<br>**57** (107/1795) | **I** (90/1795)<br>**T** (81/1795)<br>**D** (81/1795)<br>**V** (80/1795)<br>**A** (79/1795) |
| **Supiri Dhana Sampatha** | **2** (482/953)<br>**0** (477/953)<br>**3** (477/953)<br>**7** (469/953)<br>**5** (453/953) | **V** (49/953)<br>**K** (46/953)<br>**T** (44/953)<br>**S** (43/953)<br>**J** (43/953) |

