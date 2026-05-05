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

> **Last Updated (Sri Lanka Time):** `2026-05-05 04:42:53 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 202 Rows | 9.87 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 210 Rows | 9.09 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 209 Rows | 8.98 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 209 Rows | 8.76 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 209 Rows | 9.03 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 209 Rows | 9.60 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 200 Rows | 7.90 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 209 Rows | 9.76 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1728 Rows | 66.09 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1616 Rows | 66.00 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1735 Rows | 64.66 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 913 Rows | 30.13 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1729 Rows | 66.12 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 887 Rows | 32.97 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-05 04:42:53 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (78/202)<br>**5** (74/202)<br>**7** (72/202)<br>**0** (71/202)<br>**8** (70/202) | **D** (14/202)<br>**N** (13/202)<br>**J** (13/202)<br>**Q** (12/202)<br>**Y** (12/202) |
| **Dhana Nidhanaya** | **28** (20/210)<br>**6** (19/210)<br>**9** (19/210)<br>**16** (18/210)<br>**4** (16/210) | **U** (13/210)<br>**W** (13/210)<br>**T** (12/210)<br>**M** (12/210)<br>**Q** (11/210) |
| **Govisetha** | **44** (18/209)<br>**55** (17/209)<br>**19** (16/209)<br>**23** (16/209)<br>**58** (16/209) | **D** (11/209)<br>**W** (11/209)<br>**P** (11/209)<br>**O** (11/209)<br>**X** (11/209) |
| **Handahana** | **55** (20/209)<br>**6** (20/209)<br>**46** (20/209)<br>**60** (19/209)<br>**58** (19/209) | N/A |
| **Mahajana Sampatha** | **6** (104/209)<br>**9** (103/209)<br>**1** (103/209)<br>**5** (102/209)<br>**4** (99/209) | **D** (14/209)<br>**J** (13/209)<br>**N** (12/209)<br>**Q** (12/209)<br>**Y** (12/209) |
| **Mega Power** | **6** (26/209)<br>**3** (26/209)<br>**13** (24/209)<br>**22** (23/209)<br>**23** (23/209) | **V** (17/209)<br>**T** (13/209)<br>**K** (12/209)<br>**U** (12/209)<br>**J** (10/209) |
| **Nlb Jaya** | **5** (87/200)<br>**3** (82/200)<br>**0** (76/200)<br>**2** (75/200)<br>**4** (71/200) | **M** (13/200)<br>**I** (13/200)<br>**T** (13/200)<br>**G** (13/200)<br>**P** (12/200) |
| **Suba Dawasak** | **1** (85/209)<br>**3** (84/209)<br>**4** (81/209)<br>**9** (80/209)<br>**2** (75/209) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1728)<br>**57** (113/1728)<br>**20** (111/1728)<br>**13** (109/1728)<br>**75** (105/1728) | **B** (80/1728)<br>**R** (77/1728)<br>**P** (77/1728)<br>**M** (77/1728)<br>**I** (73/1728) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1616)<br>**10** (141/1616)<br>**29** (133/1616)<br>**22** (131/1616)<br>**21** (131/1616) | **H** (86/1616)<br>**U** (74/1616)<br>**W** (71/1616)<br>**D** (69/1616)<br>**G** (69/1616) |
| **Lagna Wasana** | **5** (135/1735)<br>**28** (132/1735)<br>**36** (130/1735)<br>**25** (130/1735)<br>**23** (128/1735) | N/A |
| **Sasiri** | **20** (70/913)<br>**9** (69/913)<br>**22** (68/913)<br>**26** (68/913)<br>**19** (67/913) | N/A |
| **Super Ball** | **45** (108/1729)<br>**29** (105/1729)<br>**43** (105/1729)<br>**3** (104/1729)<br>**52** (102/1729) | **I** (86/1729)<br>**D** (80/1729)<br>**V** (77/1729)<br>**T** (77/1729)<br>**A** (76/1729) |
| **Supiri Dhana Sampatha** | **0** (449/887)<br>**2** (448/887)<br>**3** (446/887)<br>**7** (438/887)<br>**5** (422/887) | **K** (44/887)<br>**T** (43/887)<br>**V** (42/887)<br>**S** (41/887)<br>**G** (41/887) |

