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

> **Last Updated (Sri Lanka Time):** `2026-06-11 01:27:02 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 237 Rows | 11.46 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 245 Rows | 10.50 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 244 Rows | 10.36 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 244 Rows | 10.10 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 244 Rows | 10.41 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 244 Rows | 11.08 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 235 Rows | 9.18 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 244 Rows | 11.28 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1763 Rows | 67.43 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1651 Rows | 67.44 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1770 Rows | 65.97 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 948 Rows | 31.31 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1764 Rows | 67.46 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 922 Rows | 34.27 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-11 01:27:02 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (90/237)<br>**5** (88/237)<br>**0** (85/237)<br>**7** (84/237)<br>**2** (82/237) | **J** (15/237)<br>**N** (14/237)<br>**D** (14/237)<br>**Q** (13/237)<br>**Y** (12/237) |
| **Dhana Nidhanaya** | **28** (24/245)<br>**9** (23/245)<br>**6** (21/245)<br>**16** (20/245)<br>**7** (19/245) | **U** (15/245)<br>**W** (13/245)<br>**Z** (12/245)<br>**T** (12/245)<br>**M** (12/245) |
| **Govisetha** | **10** (20/244)<br>**44** (19/244)<br>**55** (19/244)<br>**33** (19/244)<br>**19** (17/244) | **P** (15/244)<br>**D** (12/244)<br>**O** (12/244)<br>**M** (12/244)<br>**Y** (12/244) |
| **Handahana** | **6** (25/244)<br>**21** (23/244)<br>**55** (23/244)<br>**58** (22/244)<br>**11** (22/244) | N/A |
| **Mahajana Sampatha** | **1** (122/244)<br>**6** (120/244)<br>**5** (119/244)<br>**2** (118/244)<br>**3** (117/244) | **J** (15/244)<br>**D** (14/244)<br>**N** (13/244)<br>**Q** (13/244)<br>**Y** (12/244) |
| **Mega Power** | **11** (31/244)<br>**3** (28/244)<br>**22** (27/244)<br>**13** (27/244)<br>**6** (26/244) | **V** (18/244)<br>**T** (14/244)<br>**K** (14/244)<br>**J** (14/244)<br>**U** (13/244) |
| **Nlb Jaya** | **5** (100/235)<br>**0** (92/235)<br>**3** (91/235)<br>**2** (87/235)<br>**1** (85/235) | **P** (14/235)<br>**I** (14/235)<br>**T** (14/235)<br>**M** (13/235)<br>**G** (13/235) |
| **Suba Dawasak** | **3** (102/244)<br>**4** (98/244)<br>**1** (96/244)<br>**9** (91/244)<br>**5** (90/244) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (119/1763)<br>**20** (116/1763)<br>**57** (115/1763)<br>**13** (109/1763)<br>**75** (108/1763) | **B** (82/1763)<br>**P** (79/1763)<br>**M** (79/1763)<br>**R** (78/1763)<br>**I** (76/1763) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1651)<br>**10** (142/1651)<br>**29** (134/1651)<br>**21** (134/1651)<br>**27** (134/1651) | **H** (88/1651)<br>**U** (76/1651)<br>**W** (72/1651)<br>**G** (71/1651)<br>**X** (71/1651) |
| **Lagna Wasana** | **28** (135/1770)<br>**5** (135/1770)<br>**36** (133/1770)<br>**23** (131/1770)<br>**39** (130/1770) | N/A |
| **Sasiri** | **9** (72/948)<br>**20** (70/948)<br>**26** (70/948)<br>**22** (69/948)<br>**19** (67/948) | N/A |
| **Super Ball** | **45** (110/1764)<br>**52** (107/1764)<br>**74** (107/1764)<br>**3** (106/1764)<br>**29** (106/1764) | **I** (87/1764)<br>**D** (81/1764)<br>**V** (79/1764)<br>**T** (79/1764)<br>**A** (79/1764) |
| **Supiri Dhana Sampatha** | **0** (467/922)<br>**2** (465/922)<br>**3** (462/922)<br>**7** (452/922)<br>**5** (440/922) | **K** (46/922)<br>**V** (44/922)<br>**S** (43/922)<br>**M** (43/922)<br>**T** (43/922) |

