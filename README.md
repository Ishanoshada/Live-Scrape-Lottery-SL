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

> **Last Updated (Sri Lanka Time):** `2026-07-08 12:50:06 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 264 Rows | 12.70 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 272 Rows | 11.61 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 271 Rows | 11.44 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 271 Rows | 11.16 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 271 Rows | 11.50 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 271 Rows | 12.23 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 262 Rows | 10.18 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 271 Rows | 12.47 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1790 Rows | 68.46 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1678 Rows | 68.55 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1797 Rows | 66.97 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 975 Rows | 32.24 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1791 Rows | 68.49 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 949 Rows | 35.28 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-08 12:50:06 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (97/264)<br>**6** (96/264)<br>**2** (95/264)<br>**7** (93/264)<br>**0** (91/264) | **N** (16/264)<br>**D** (16/264)<br>**Q** (15/264)<br>**J** (15/264)<br>**G** (15/264) |
| **Dhana Nidhanaya** | **9** (26/272)<br>**28** (24/272)<br>**7** (24/272)<br>**4** (23/272)<br>**6** (21/272) | **U** (17/272)<br>**F** (15/272)<br>**Z** (14/272)<br>**W** (14/272)<br>**E** (13/272) |
| **Govisetha** | **55** (22/271)<br>**10** (21/271)<br>**23** (20/271)<br>**29** (20/271)<br>**19** (19/271) | **P** (15/271)<br>**C** (14/271)<br>**D** (13/271)<br>**A** (13/271)<br>**K** (13/271) |
| **Handahana** | **58** (27/271)<br>**21** (27/271)<br>**11** (26/271)<br>**6** (26/271)<br>**55** (25/271) | N/A |
| **Mahajana Sampatha** | **2** (134/271)<br>**5** (133/271)<br>**4** (132/271)<br>**1** (132/271)<br>**6** (132/271) | **D** (16/271)<br>**N** (15/271)<br>**Q** (15/271)<br>**J** (15/271)<br>**G** (15/271) |
| **Mega Power** | **11** (36/271)<br>**6** (31/271)<br>**3** (31/271)<br>**19** (30/271)<br>**13** (29/271) | **V** (19/271)<br>**U** (19/271)<br>**T** (18/271)<br>**J** (16/271)<br>**K** (15/271) |
| **Nlb Jaya** | **5** (118/262)<br>**0** (102/262)<br>**3** (100/262)<br>**2** (100/262)<br>**7** (94/262) | **T** (17/262)<br>**I** (16/262)<br>**G** (16/262)<br>**P** (14/262)<br>**Y** (14/262) |
| **Suba Dawasak** | **3** (111/271)<br>**4** (111/271)<br>**1** (107/271)<br>**9** (98/271)<br>**5** (97/271) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1790)<br>**20** (119/1790)<br>**57** (116/1790)<br>**75** (111/1790)<br>**38** (110/1790) | **B** (82/1790)<br>**R** (81/1790)<br>**P** (79/1790)<br>**M** (79/1790)<br>**I** (77/1790) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1678)<br>**10** (144/1678)<br>**27** (138/1678)<br>**29** (137/1678)<br>**15** (137/1678) | **H** (88/1678)<br>**U** (77/1678)<br>**M** (73/1678)<br>**X** (72/1678)<br>**W** (72/1678) |
| **Lagna Wasana** | **5** (137/1797)<br>**28** (136/1797)<br>**36** (134/1797)<br>**25** (133/1797)<br>**23** (132/1797) | N/A |
| **Sasiri** | **9** (73/975)<br>**22** (71/975)<br>**20** (71/975)<br>**26** (71/975)<br>**5** (69/975) | N/A |
| **Super Ball** | **52** (110/1791)<br>**45** (110/1791)<br>**29** (109/1791)<br>**74** (107/1791)<br>**43** (107/1791) | **I** (90/1791)<br>**D** (81/1791)<br>**V** (80/1791)<br>**T** (80/1791)<br>**A** (79/1791) |
| **Supiri Dhana Sampatha** | **2** (480/949)<br>**0** (475/949)<br>**3** (475/949)<br>**7** (467/949)<br>**5** (451/949) | **V** (48/949)<br>**K** (46/949)<br>**T** (44/949)<br>**S** (43/949)<br>**J** (43/949) |

