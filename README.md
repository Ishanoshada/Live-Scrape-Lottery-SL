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

> **Last Updated (Sri Lanka Time):** `2026-07-09 12:24:13 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 265 Rows | 12.75 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 273 Rows | 11.66 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 272 Rows | 11.48 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 272 Rows | 11.20 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 272 Rows | 11.54 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 272 Rows | 12.28 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 263 Rows | 10.22 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 272 Rows | 12.51 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1791 Rows | 68.50 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1679 Rows | 68.59 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1798 Rows | 67.01 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 976 Rows | 32.28 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1792 Rows | 68.53 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 950 Rows | 35.31 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-09 12:24:13 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (97/265)<br>**6** (96/265)<br>**2** (95/265)<br>**7** (94/265)<br>**0** (91/265) | **N** (16/265)<br>**Q** (16/265)<br>**D** (16/265)<br>**J** (15/265)<br>**G** (15/265) |
| **Dhana Nidhanaya** | **9** (26/273)<br>**28** (24/273)<br>**7** (24/273)<br>**4** (23/273)<br>**6** (21/273) | **U** (17/273)<br>**F** (15/273)<br>**W** (15/273)<br>**Z** (14/273)<br>**E** (13/273) |
| **Govisetha** | **55** (22/272)<br>**10** (21/272)<br>**23** (20/272)<br>**29** (20/272)<br>**33** (20/272) | **P** (15/272)<br>**C** (15/272)<br>**D** (13/272)<br>**A** (13/272)<br>**K** (13/272) |
| **Handahana** | **58** (27/272)<br>**11** (27/272)<br>**21** (27/272)<br>**6** (26/272)<br>**55** (25/272) | N/A |
| **Mahajana Sampatha** | **2** (134/272)<br>**4** (133/272)<br>**5** (133/272)<br>**1** (133/272)<br>**6** (133/272) | **Q** (16/272)<br>**D** (16/272)<br>**N** (15/272)<br>**J** (15/272)<br>**G** (15/272) |
| **Mega Power** | **11** (36/272)<br>**6** (31/272)<br>**3** (31/272)<br>**19** (30/272)<br>**22** (29/272) | **V** (19/272)<br>**U** (19/272)<br>**T** (18/272)<br>**J** (16/272)<br>**K** (15/272) |
| **Nlb Jaya** | **5** (118/263)<br>**0** (102/263)<br>**3** (101/263)<br>**2** (100/263)<br>**7** (94/263) | **T** (17/263)<br>**I** (16/263)<br>**G** (16/263)<br>**P** (14/263)<br>**Y** (14/263) |
| **Suba Dawasak** | **4** (112/272)<br>**3** (111/272)<br>**1** (107/272)<br>**5** (98/272)<br>**8** (98/272) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1791)<br>**20** (119/1791)<br>**57** (116/1791)<br>**75** (111/1791)<br>**38** (110/1791) | **B** (82/1791)<br>**R** (81/1791)<br>**P** (79/1791)<br>**M** (79/1791)<br>**I** (77/1791) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1679)<br>**10** (144/1679)<br>**27** (138/1679)<br>**29** (137/1679)<br>**15** (137/1679) | **H** (88/1679)<br>**U** (77/1679)<br>**M** (73/1679)<br>**X** (72/1679)<br>**W** (72/1679) |
| **Lagna Wasana** | **5** (137/1798)<br>**28** (136/1798)<br>**36** (134/1798)<br>**25** (133/1798)<br>**23** (132/1798) | N/A |
| **Sasiri** | **9** (73/976)<br>**20** (72/976)<br>**22** (71/976)<br>**26** (71/976)<br>**5** (69/976) | N/A |
| **Super Ball** | **52** (110/1792)<br>**45** (110/1792)<br>**29** (109/1792)<br>**74** (107/1792)<br>**43** (107/1792) | **I** (90/1792)<br>**T** (81/1792)<br>**D** (81/1792)<br>**V** (80/1792)<br>**A** (79/1792) |
| **Supiri Dhana Sampatha** | **2** (481/950)<br>**3** (476/950)<br>**0** (475/950)<br>**7** (467/950)<br>**5** (452/950) | **V** (49/950)<br>**K** (46/950)<br>**T** (44/950)<br>**S** (43/950)<br>**J** (43/950) |

