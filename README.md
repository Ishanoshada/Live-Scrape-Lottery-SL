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

> **Last Updated (Sri Lanka Time):** `2026-05-07 05:13:09 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 204 Rows | 9.96 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 212 Rows | 9.17 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 211 Rows | 9.06 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 211 Rows | 8.84 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 211 Rows | 9.11 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 211 Rows | 9.68 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 202 Rows | 7.97 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 211 Rows | 9.85 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1730 Rows | 66.17 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1618 Rows | 66.08 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1737 Rows | 64.74 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 915 Rows | 30.20 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1731 Rows | 66.20 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 889 Rows | 33.04 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-07 05:13:09 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (79/204)<br>**5** (75/204)<br>**7** (72/204)<br>**0** (71/204)<br>**3** (70/204) | **D** (14/204)<br>**N** (13/204)<br>**J** (13/204)<br>**Q** (12/204)<br>**Y** (12/204) |
| **Dhana Nidhanaya** | **28** (20/212)<br>**9** (20/212)<br>**6** (19/212)<br>**16** (18/212)<br>**4** (16/212) | **U** (13/212)<br>**W** (13/212)<br>**T** (12/212)<br>**M** (12/212)<br>**Q** (11/212) |
| **Govisetha** | **44** (18/211)<br>**19** (17/211)<br>**55** (17/211)<br>**23** (16/211)<br>**58** (16/211) | **D** (11/211)<br>**W** (11/211)<br>**P** (11/211)<br>**O** (11/211)<br>**X** (11/211) |
| **Handahana** | **58** (20/211)<br>**55** (20/211)<br>**6** (20/211)<br>**46** (20/211)<br>**60** (19/211) | N/A |
| **Mahajana Sampatha** | **6** (105/211)<br>**1** (104/211)<br>**5** (103/211)<br>**9** (103/211)<br>**3** (101/211) | **D** (14/211)<br>**J** (13/211)<br>**N** (12/211)<br>**Q** (12/211)<br>**Y** (12/211) |
| **Mega Power** | **6** (26/211)<br>**3** (26/211)<br>**22** (24/211)<br>**13** (24/211)<br>**19** (23/211) | **V** (17/211)<br>**T** (13/211)<br>**U** (13/211)<br>**K** (12/211)<br>**J** (10/211) |
| **Nlb Jaya** | **5** (88/202)<br>**3** (82/202)<br>**2** (77/202)<br>**0** (77/202)<br>**4** (72/202) | **M** (13/202)<br>**I** (13/202)<br>**T** (13/202)<br>**G** (13/202)<br>**P** (12/202) |
| **Suba Dawasak** | **1** (85/211)<br>**3** (84/211)<br>**4** (83/211)<br>**9** (81/211)<br>**2** (75/211) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1730)<br>**57** (113/1730)<br>**20** (111/1730)<br>**13** (109/1730)<br>**75** (105/1730) | **B** (81/1730)<br>**R** (77/1730)<br>**P** (77/1730)<br>**M** (77/1730)<br>**I** (73/1730) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1618)<br>**10** (141/1618)<br>**29** (133/1618)<br>**21** (132/1618)<br>**22** (131/1618) | **H** (86/1618)<br>**U** (74/1618)<br>**W** (71/1618)<br>**D** (69/1618)<br>**G** (69/1618) |
| **Lagna Wasana** | **5** (135/1737)<br>**28** (132/1737)<br>**36** (130/1737)<br>**25** (130/1737)<br>**23** (128/1737) | N/A |
| **Sasiri** | **20** (70/915)<br>**9** (69/915)<br>**22** (68/915)<br>**26** (68/915)<br>**19** (67/915) | N/A |
| **Super Ball** | **45** (108/1731)<br>**29** (105/1731)<br>**43** (105/1731)<br>**3** (104/1731)<br>**52** (102/1731) | **I** (86/1731)<br>**D** (80/1731)<br>**V** (77/1731)<br>**T** (77/1731)<br>**A** (76/1731) |
| **Supiri Dhana Sampatha** | **0** (450/889)<br>**2** (449/889)<br>**3** (446/889)<br>**7** (439/889)<br>**5** (423/889) | **K** (44/889)<br>**T** (43/889)<br>**V** (42/889)<br>**S** (41/889)<br>**G** (41/889) |

