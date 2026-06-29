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

> **Last Updated (Sri Lanka Time):** `2026-06-30 12:51:03 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 256 Rows | 12.33 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 264 Rows | 11.29 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 263 Rows | 11.12 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 263 Rows | 10.84 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 263 Rows | 11.18 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 263 Rows | 11.89 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 254 Rows | 9.89 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 263 Rows | 12.11 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1782 Rows | 68.15 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1670 Rows | 68.22 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1789 Rows | 66.67 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 967 Rows | 31.96 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1783 Rows | 68.19 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 941 Rows | 34.98 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-30 12:51:03 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (96/256)<br>**6** (96/256)<br>**0** (90/256)<br>**2** (90/256)<br>**7** (90/256) | **N** (16/256)<br>**Q** (15/256)<br>**J** (15/256)<br>**G** (15/256)<br>**D** (14/256) |
| **Dhana Nidhanaya** | **9** (25/264)<br>**28** (24/264)<br>**7** (23/264)<br>**4** (21/264)<br>**6** (21/264) | **U** (17/264)<br>**F** (15/264)<br>**W** (14/264)<br>**Z** (12/264)<br>**T** (12/264) |
| **Govisetha** | **10** (21/263)<br>**55** (21/263)<br>**23** (20/263)<br>**29** (20/263)<br>**44** (19/263) | **P** (15/263)<br>**C** (14/263)<br>**D** (13/263)<br>**A** (12/263)<br>**O** (12/263) |
| **Handahana** | **21** (27/263)<br>**58** (26/263)<br>**6** (26/263)<br>**11** (25/263)<br>**61** (23/263) | N/A |
| **Mahajana Sampatha** | **5** (130/263)<br>**6** (130/263)<br>**2** (129/263)<br>**1** (129/263)<br>**7** (128/263) | **N** (15/263)<br>**Q** (15/263)<br>**J** (15/263)<br>**G** (15/263)<br>**D** (14/263) |
| **Mega Power** | **11** (36/263)<br>**3** (31/263)<br>**13** (29/263)<br>**22** (28/263)<br>**6** (28/263) | **V** (19/263)<br>**U** (18/263)<br>**T** (17/263)<br>**K** (15/263)<br>**J** (15/263) |
| **Nlb Jaya** | **5** (114/254)<br>**3** (98/254)<br>**0** (98/254)<br>**2** (96/254)<br>**1** (90/254) | **G** (16/254)<br>**I** (15/254)<br>**T** (15/254)<br>**P** (14/254)<br>**Y** (14/254) |
| **Suba Dawasak** | **3** (110/263)<br>**4** (107/263)<br>**1** (104/263)<br>**9** (95/263)<br>**2** (95/263) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1782)<br>**20** (119/1782)<br>**57** (116/1782)<br>**75** (110/1782)<br>**38** (109/1782) | **B** (82/1782)<br>**R** (81/1782)<br>**P** (79/1782)<br>**M** (79/1782)<br>**I** (76/1782) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1670)<br>**10** (143/1670)<br>**27** (137/1670)<br>**15** (137/1670)<br>**29** (136/1670) | **H** (88/1670)<br>**U** (77/1670)<br>**M** (73/1670)<br>**X** (72/1670)<br>**W** (72/1670) |
| **Lagna Wasana** | **28** (136/1789)<br>**5** (135/1789)<br>**36** (133/1789)<br>**23** (132/1789)<br>**2** (131/1789) | N/A |
| **Sasiri** | **9** (73/967)<br>**20** (71/967)<br>**26** (71/967)<br>**22** (70/967)<br>**5** (69/967) | N/A |
| **Super Ball** | **45** (110/1783)<br>**52** (108/1783)<br>**74** (107/1783)<br>**29** (107/1783)<br>**3** (106/1783) | **I** (90/1783)<br>**D** (81/1783)<br>**V** (80/1783)<br>**T** (80/1783)<br>**A** (79/1783) |
| **Supiri Dhana Sampatha** | **2** (475/941)<br>**0** (472/941)<br>**3** (472/941)<br>**7** (461/941)<br>**5** (450/941) | **V** (47/941)<br>**K** (46/941)<br>**S** (43/941)<br>**M** (43/941)<br>**T** (43/941) |

