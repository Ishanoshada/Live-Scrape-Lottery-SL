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

> **Last Updated (Sri Lanka Time):** `2026-06-10 01:04:12 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 236 Rows | 11.41 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 244 Rows | 10.46 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 243 Rows | 10.32 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 243 Rows | 10.06 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 243 Rows | 10.37 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 243 Rows | 11.03 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 234 Rows | 9.14 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 243 Rows | 11.23 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1762 Rows | 67.39 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1650 Rows | 67.40 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1769 Rows | 65.93 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 947 Rows | 31.28 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1763 Rows | 67.42 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 921 Rows | 34.23 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-10 01:04:12 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (90/236)<br>**5** (87/236)<br>**0** (85/236)<br>**7** (84/236)<br>**2** (82/236) | **J** (15/236)<br>**N** (14/236)<br>**D** (14/236)<br>**Q** (13/236)<br>**Y** (12/236) |
| **Dhana Nidhanaya** | **28** (24/244)<br>**9** (23/244)<br>**6** (21/244)<br>**16** (20/244)<br>**7** (19/244) | **U** (15/244)<br>**W** (13/244)<br>**Z** (12/244)<br>**T** (12/244)<br>**M** (12/244) |
| **Govisetha** | **10** (20/243)<br>**44** (19/243)<br>**55** (19/243)<br>**33** (19/243)<br>**19** (17/243) | **P** (15/243)<br>**D** (12/243)<br>**O** (12/243)<br>**M** (12/243)<br>**Y** (12/243) |
| **Handahana** | **6** (25/243)<br>**21** (23/243)<br>**55** (23/243)<br>**58** (22/243)<br>**11** (22/243) | N/A |
| **Mahajana Sampatha** | **1** (122/243)<br>**6** (120/243)<br>**5** (118/243)<br>**4** (117/243)<br>**2** (117/243) | **J** (15/243)<br>**D** (14/243)<br>**N** (13/243)<br>**Q** (13/243)<br>**Y** (12/243) |
| **Mega Power** | **11** (31/243)<br>**3** (28/243)<br>**22** (27/243)<br>**13** (27/243)<br>**6** (26/243) | **V** (18/243)<br>**T** (14/243)<br>**K** (14/243)<br>**J** (14/243)<br>**U** (13/243) |
| **Nlb Jaya** | **5** (100/234)<br>**0** (92/234)<br>**3** (91/234)<br>**2** (87/234)<br>**1** (84/234) | **P** (14/234)<br>**I** (14/234)<br>**T** (14/234)<br>**M** (13/234)<br>**G** (13/234) |
| **Suba Dawasak** | **3** (102/243)<br>**4** (97/243)<br>**1** (96/243)<br>**9** (91/243)<br>**5** (90/243) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (119/1762)<br>**20** (116/1762)<br>**57** (115/1762)<br>**13** (109/1762)<br>**75** (108/1762) | **B** (82/1762)<br>**P** (79/1762)<br>**M** (79/1762)<br>**R** (78/1762)<br>**I** (76/1762) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1650)<br>**10** (142/1650)<br>**29** (134/1650)<br>**21** (134/1650)<br>**27** (134/1650) | **H** (88/1650)<br>**U** (76/1650)<br>**W** (72/1650)<br>**G** (71/1650)<br>**X** (71/1650) |
| **Lagna Wasana** | **28** (135/1769)<br>**5** (135/1769)<br>**36** (133/1769)<br>**23** (131/1769)<br>**39** (130/1769) | N/A |
| **Sasiri** | **9** (72/947)<br>**20** (70/947)<br>**22** (69/947)<br>**26** (69/947)<br>**19** (67/947) | N/A |
| **Super Ball** | **45** (109/1763)<br>**52** (107/1763)<br>**74** (107/1763)<br>**3** (106/1763)<br>**29** (106/1763) | **I** (87/1763)<br>**D** (81/1763)<br>**T** (79/1763)<br>**A** (79/1763)<br>**V** (78/1763) |
| **Supiri Dhana Sampatha** | **0** (467/921)<br>**2** (464/921)<br>**3** (462/921)<br>**7** (452/921)<br>**5** (439/921) | **K** (45/921)<br>**V** (44/921)<br>**S** (43/921)<br>**M** (43/921)<br>**T** (43/921) |

