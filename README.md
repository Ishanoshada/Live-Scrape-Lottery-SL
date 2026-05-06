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

> **Last Updated (Sri Lanka Time):** `2026-05-06 01:01:58 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 203 Rows | 9.92 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 211 Rows | 9.13 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 210 Rows | 9.02 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 210 Rows | 8.80 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 210 Rows | 9.07 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 210 Rows | 9.64 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 201 Rows | 7.93 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 210 Rows | 9.80 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1729 Rows | 66.12 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1617 Rows | 66.04 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1736 Rows | 64.70 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 914 Rows | 30.16 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1730 Rows | 66.16 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 888 Rows | 33.00 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-06 01:01:58 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (78/203)<br>**5** (75/203)<br>**7** (72/203)<br>**0** (71/203)<br>**3** (70/203) | **D** (14/203)<br>**N** (13/203)<br>**J** (13/203)<br>**Q** (12/203)<br>**Y** (12/203) |
| **Dhana Nidhanaya** | **28** (20/211)<br>**9** (20/211)<br>**6** (19/211)<br>**16** (18/211)<br>**4** (16/211) | **U** (13/211)<br>**W** (13/211)<br>**T** (12/211)<br>**M** (12/211)<br>**Q** (11/211) |
| **Govisetha** | **44** (18/210)<br>**19** (17/210)<br>**55** (17/210)<br>**23** (16/210)<br>**58** (16/210) | **D** (11/210)<br>**W** (11/210)<br>**P** (11/210)<br>**O** (11/210)<br>**X** (11/210) |
| **Handahana** | **58** (20/210)<br>**55** (20/210)<br>**6** (20/210)<br>**46** (20/210)<br>**60** (19/210) | N/A |
| **Mahajana Sampatha** | **6** (104/210)<br>**9** (103/210)<br>**5** (103/210)<br>**1** (103/210)<br>**3** (100/210) | **D** (14/210)<br>**J** (13/210)<br>**N** (12/210)<br>**Q** (12/210)<br>**Y** (12/210) |
| **Mega Power** | **6** (26/210)<br>**3** (26/210)<br>**22** (24/210)<br>**13** (24/210)<br>**19** (23/210) | **V** (17/210)<br>**T** (13/210)<br>**K** (12/210)<br>**U** (12/210)<br>**J** (10/210) |
| **Nlb Jaya** | **5** (87/201)<br>**3** (82/201)<br>**0** (77/201)<br>**2** (76/201)<br>**4** (71/201) | **M** (13/201)<br>**I** (13/201)<br>**T** (13/201)<br>**G** (13/201)<br>**P** (12/201) |
| **Suba Dawasak** | **1** (85/210)<br>**3** (84/210)<br>**4** (82/210)<br>**9** (81/210)<br>**2** (75/210) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1729)<br>**57** (113/1729)<br>**20** (111/1729)<br>**13** (109/1729)<br>**75** (105/1729) | **B** (81/1729)<br>**R** (77/1729)<br>**P** (77/1729)<br>**M** (77/1729)<br>**I** (73/1729) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1617)<br>**10** (141/1617)<br>**29** (133/1617)<br>**21** (132/1617)<br>**22** (131/1617) | **H** (86/1617)<br>**U** (74/1617)<br>**W** (71/1617)<br>**D** (69/1617)<br>**G** (69/1617) |
| **Lagna Wasana** | **5** (135/1736)<br>**28** (132/1736)<br>**36** (130/1736)<br>**25** (130/1736)<br>**23** (128/1736) | N/A |
| **Sasiri** | **20** (70/914)<br>**9** (69/914)<br>**22** (68/914)<br>**26** (68/914)<br>**19** (67/914) | N/A |
| **Super Ball** | **45** (108/1730)<br>**29** (105/1730)<br>**43** (105/1730)<br>**3** (104/1730)<br>**52** (102/1730) | **I** (86/1730)<br>**D** (80/1730)<br>**V** (77/1730)<br>**T** (77/1730)<br>**A** (76/1730) |
| **Supiri Dhana Sampatha** | **0** (450/888)<br>**2** (449/888)<br>**3** (446/888)<br>**7** (438/888)<br>**5** (422/888) | **K** (44/888)<br>**T** (43/888)<br>**V** (42/888)<br>**S** (41/888)<br>**G** (41/888) |

