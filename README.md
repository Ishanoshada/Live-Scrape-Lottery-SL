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

> **Last Updated (Sri Lanka Time):** `2026-09-20 12:57:56 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 338 Rows | 16.26 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 346 Rows | 14.80 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 345 Rows | 14.56 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 345 Rows | 14.20 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 345 Rows | 14.63 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 345 Rows | 15.56 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 336 Rows | 13.09 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 345 Rows | 15.88 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1864 Rows | 71.29 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1752 Rows | 71.60 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1871 Rows | 69.73 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1049 Rows | 34.78 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1865 Rows | 71.33 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1023 Rows | 38.06 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-20 12:57:56 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (124/338)<br>**2** (123/338)<br>**6** (118/338)<br>**4** (116/338)<br>**1** (116/338) | **D** (22/338)<br>**J** (20/338)<br>**Q** (19/338)<br>**N** (18/338)<br>**G** (18/338) |
| **Dhana Nidhanaya** | **9** (32/346)<br>**4** (30/346)<br>**7** (28/346)<br>**3** (27/346)<br>**28** (26/346) | **U** (20/346)<br>**W** (19/346)<br>**Z** (18/346)<br>**F** (18/346)<br>**M** (18/346) |
| **Govisetha** | **55** (28/345)<br>**10** (26/345)<br>**44** (25/345)<br>**29** (24/345)<br>**33** (24/345) | **P** (19/345)<br>**C** (18/345)<br>**I** (17/345)<br>**X** (17/345)<br>**W** (16/345) |
| **Handahana** | **58** (32/345)<br>**11** (31/345)<br>**55** (31/345)<br>**60** (30/345)<br>**6** (30/345) | N/A |
| **Mahajana Sampatha** | **5** (172/345)<br>**1** (172/345)<br>**2** (171/345)<br>**9** (166/345)<br>**3** (165/345) | **D** (22/345)<br>**J** (20/345)<br>**Q** (19/345)<br>**W** (19/345)<br>**G** (18/345) |
| **Mega Power** | **11** (40/345)<br>**3** (37/345)<br>**26** (37/345)<br>**13** (35/345)<br>**6** (34/345) | **T** (22/345)<br>**V** (22/345)<br>**U** (21/345)<br>**K** (18/345)<br>**J** (17/345) |
| **Nlb Jaya** | **5** (142/336)<br>**0** (130/336)<br>**3** (127/336)<br>**2** (127/336)<br>**7** (125/336) | **T** (20/336)<br>**I** (19/336)<br>**G** (18/336)<br>**P** (17/336)<br>**O** (17/336) |
| **Suba Dawasak** | **4** (140/345)<br>**3** (139/345)<br>**9** (131/345)<br>**8** (131/345)<br>**1** (130/345) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (127/1864)<br>**20** (122/1864)<br>**57** (121/1864)<br>**38** (118/1864)<br>**75** (114/1864) | **B** (88/1864)<br>**R** (85/1864)<br>**M** (83/1864)<br>**N** (81/1864)<br>**P** (80/1864) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1752)<br>**10** (149/1752)<br>**21** (145/1752)<br>**6** (144/1752)<br>**29** (144/1752) | **H** (89/1752)<br>**U** (80/1752)<br>**M** (78/1752)<br>**G** (76/1752)<br>**D** (75/1752) |
| **Lagna Wasana** | **5** (143/1871)<br>**23** (142/1871)<br>**36** (139/1871)<br>**25** (139/1871)<br>**39** (138/1871) | N/A |
| **Sasiri** | **9** (81/1049)<br>**20** (79/1049)<br>**22** (78/1049)<br>**26** (77/1049)<br>**21** (76/1049) | N/A |
| **Super Ball** | **52** (112/1865)<br>**9** (112/1865)<br>**45** (112/1865)<br>**29** (112/1865)<br>**62** (110/1865) | **I** (93/1865)<br>**V** (83/1865)<br>**T** (83/1865)<br>**D** (82/1865)<br>**A** (82/1865) |
| **Supiri Dhana Sampatha** | **0** (516/1023)<br>**2** (512/1023)<br>**3** (506/1023)<br>**7** (503/1023)<br>**8** (487/1023) | **V** (55/1023)<br>**K** (48/1023)<br>**S** (48/1023)<br>**T** (47/1023)<br>**G** (46/1023) |

