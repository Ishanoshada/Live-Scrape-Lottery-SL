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

> **Last Updated (Sri Lanka Time):** `2026-06-09 01:09:42 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 235 Rows | 11.37 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 243 Rows | 10.42 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 242 Rows | 10.28 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 242 Rows | 10.02 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 242 Rows | 10.33 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 242 Rows | 10.99 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 233 Rows | 9.10 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 242 Rows | 11.19 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1761 Rows | 67.35 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1649 Rows | 67.36 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1768 Rows | 65.89 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 946 Rows | 31.24 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1762 Rows | 67.39 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 920 Rows | 34.20 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-09 01:09:42 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (90/235)<br>**5** (87/235)<br>**0** (84/235)<br>**7** (83/235)<br>**2** (82/235) | **J** (15/235)<br>**N** (14/235)<br>**D** (14/235)<br>**Q** (13/235)<br>**Y** (12/235) |
| **Dhana Nidhanaya** | **28** (24/243)<br>**9** (23/243)<br>**6** (21/243)<br>**16** (20/243)<br>**7** (19/243) | **U** (15/243)<br>**W** (13/243)<br>**Z** (12/243)<br>**T** (12/243)<br>**M** (12/243) |
| **Govisetha** | **10** (20/242)<br>**44** (19/242)<br>**55** (19/242)<br>**33** (19/242)<br>**19** (17/242) | **P** (15/242)<br>**D** (12/242)<br>**O** (12/242)<br>**M** (12/242)<br>**Y** (12/242) |
| **Handahana** | **6** (24/242)<br>**21** (23/242)<br>**55** (23/242)<br>**58** (22/242)<br>**11** (22/242) | N/A |
| **Mahajana Sampatha** | **1** (122/242)<br>**6** (119/242)<br>**5** (118/242)<br>**2** (117/242)<br>**4** (116/242) | **J** (15/242)<br>**D** (14/242)<br>**N** (13/242)<br>**Q** (13/242)<br>**Y** (12/242) |
| **Mega Power** | **11** (31/242)<br>**3** (28/242)<br>**22** (27/242)<br>**13** (27/242)<br>**6** (26/242) | **V** (18/242)<br>**T** (14/242)<br>**K** (14/242)<br>**J** (14/242)<br>**U** (13/242) |
| **Nlb Jaya** | **5** (100/233)<br>**3** (91/233)<br>**0** (91/233)<br>**2** (87/233)<br>**1** (84/233) | **P** (14/233)<br>**I** (14/233)<br>**T** (14/233)<br>**M** (13/233)<br>**G** (13/233) |
| **Suba Dawasak** | **3** (101/242)<br>**4** (97/242)<br>**1** (96/242)<br>**9** (91/242)<br>**5** (90/242) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (118/1761)<br>**20** (115/1761)<br>**57** (115/1761)<br>**13** (109/1761)<br>**75** (108/1761) | **B** (82/1761)<br>**P** (79/1761)<br>**M** (79/1761)<br>**R** (78/1761)<br>**I** (75/1761) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1649)<br>**10** (142/1649)<br>**29** (134/1649)<br>**21** (134/1649)<br>**27** (134/1649) | **H** (88/1649)<br>**U** (76/1649)<br>**W** (72/1649)<br>**G** (71/1649)<br>**X** (71/1649) |
| **Lagna Wasana** | **28** (135/1768)<br>**5** (135/1768)<br>**36** (132/1768)<br>**23** (130/1768)<br>**25** (130/1768) | N/A |
| **Sasiri** | **9** (72/946)<br>**20** (70/946)<br>**22** (69/946)<br>**26** (68/946)<br>**19** (67/946) | N/A |
| **Super Ball** | **45** (109/1762)<br>**52** (107/1762)<br>**74** (107/1762)<br>**3** (106/1762)<br>**29** (106/1762) | **I** (87/1762)<br>**D** (81/1762)<br>**T** (79/1762)<br>**A** (79/1762)<br>**V** (78/1762) |
| **Supiri Dhana Sampatha** | **0** (467/920)<br>**2** (464/920)<br>**3** (461/920)<br>**7** (452/920)<br>**5** (439/920) | **K** (44/920)<br>**V** (44/920)<br>**S** (43/920)<br>**M** (43/920)<br>**T** (43/920) |

