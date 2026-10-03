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

> **Last Updated (Sri Lanka Time):** `2026-10-04 01:33:58 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 352 Rows | 16.97 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 360 Rows | 15.42 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 359 Rows | 15.19 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 359 Rows | 14.81 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 359 Rows | 15.25 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 359 Rows | 16.22 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 350 Rows | 13.66 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 359 Rows | 16.53 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1878 Rows | 71.82 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1766 Rows | 72.17 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1885 Rows | 70.25 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1063 Rows | 35.26 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1879 Rows | 71.86 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1037 Rows | 38.59 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-04 01:33:58 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (128/352)<br>**2** (126/352)<br>**6** (123/352)<br>**3** (122/352)<br>**4** (122/352) | **D** (22/352)<br>**Q** (21/352)<br>**J** (20/352)<br>**G** (20/352)<br>**N** (19/352) |
| **Dhana Nidhanaya** | **9** (32/360)<br>**4** (30/360)<br>**7** (29/360)<br>**3** (27/360)<br>**80** (26/360) | **U** (20/360)<br>**W** (20/360)<br>**M** (19/360)<br>**Z** (18/360)<br>**F** (18/360) |
| **Govisetha** | **55** (28/359)<br>**10** (27/359)<br>**44** (26/359)<br>**33** (25/359)<br>**23** (24/359) | **P** (20/359)<br>**I** (18/359)<br>**C** (18/359)<br>**X** (17/359)<br>**D** (16/359) |
| **Handahana** | **58** (32/359)<br>**60** (31/359)<br>**11** (31/359)<br>**55** (31/359)<br>**21** (30/359) | N/A |
| **Mahajana Sampatha** | **5** (178/359)<br>**1** (178/359)<br>**2** (175/359)<br>**3** (174/359)<br>**4** (173/359) | **D** (22/359)<br>**Q** (21/359)<br>**J** (20/359)<br>**G** (20/359)<br>**W** (19/359) |
| **Mega Power** | **13** (41/359)<br>**26** (40/359)<br>**11** (40/359)<br>**3** (38/359)<br>**22** (37/359) | **V** (23/359)<br>**U** (23/359)<br>**T** (22/359)<br>**K** (19/359)<br>**S** (18/359) |
| **Nlb Jaya** | **5** (146/350)<br>**3** (133/350)<br>**0** (133/350)<br>**2** (131/350)<br>**7** (129/350) | **T** (21/350)<br>**I** (19/350)<br>**G** (19/350)<br>**P** (17/350)<br>**Y** (17/350) |
| **Suba Dawasak** | **4** (146/359)<br>**3** (142/359)<br>**9** (137/359)<br>**1** (136/359)<br>**2** (136/359) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1878)<br>**20** (122/1878)<br>**57** (122/1878)<br>**38** (118/1878)<br>**13** (115/1878) | **B** (88/1878)<br>**R** (85/1878)<br>**M** (84/1878)<br>**N** (82/1878)<br>**P** (81/1878) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1766)<br>**10** (149/1766)<br>**21** (148/1766)<br>**6** (145/1766)<br>**15** (145/1766) | **H** (89/1766)<br>**U** (81/1766)<br>**M** (79/1766)<br>**G** (76/1766)<br>**D** (75/1766) |
| **Lagna Wasana** | **5** (144/1885)<br>**23** (142/1885)<br>**39** (140/1885)<br>**36** (139/1885)<br>**25** (139/1885) | N/A |
| **Sasiri** | **9** (83/1063)<br>**20** (80/1063)<br>**22** (78/1063)<br>**26** (78/1063)<br>**21** (78/1063) | N/A |
| **Super Ball** | **9** (113/1879)<br>**45** (113/1879)<br>**52** (112/1879)<br>**29** (112/1879)<br>**74** (111/1879) | **I** (93/1879)<br>**T** (85/1879)<br>**V** (84/1879)<br>**D** (82/1879)<br>**A** (82/1879) |
| **Supiri Dhana Sampatha** | **0** (522/1037)<br>**2** (517/1037)<br>**3** (513/1037)<br>**7** (512/1037)<br>**8** (495/1037) | **V** (56/1037)<br>**K** (50/1037)<br>**T** (49/1037)<br>**S** (48/1037)<br>**G** (46/1037) |

