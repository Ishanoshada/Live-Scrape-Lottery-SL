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

> **Last Updated (Sri Lanka Time):** `2026-05-11 10:50:31 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 209 Rows | 10.19 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 217 Rows | 9.37 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 216 Rows | 9.25 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 216 Rows | 9.03 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 216 Rows | 9.30 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 216 Rows | 9.89 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 207 Rows | 8.15 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 216 Rows | 10.06 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1735 Rows | 66.35 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1623 Rows | 66.29 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1742 Rows | 64.92 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 920 Rows | 30.36 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1736 Rows | 66.39 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 894 Rows | 33.23 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-11 10:50:31 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (80/209)<br>**5** (78/209)<br>**7** (74/209)<br>**2** (74/209)<br>**4** (72/209) | **D** (14/209)<br>**J** (14/209)<br>**N** (13/209)<br>**Q** (12/209)<br>**Y** (12/209) |
| **Dhana Nidhanaya** | **28** (21/217)<br>**9** (20/217)<br>**6** (19/217)<br>**16** (18/217)<br>**7** (17/217) | **U** (13/217)<br>**W** (13/217)<br>**T** (12/217)<br>**M** (12/217)<br>**Q** (11/217) |
| **Govisetha** | **44** (18/216)<br>**19** (17/216)<br>**55** (17/216)<br>**23** (16/216)<br>**58** (16/216) | **P** (12/216)<br>**D** (11/216)<br>**W** (11/216)<br>**O** (11/216)<br>**X** (11/216) |
| **Handahana** | **58** (21/216)<br>**21** (21/216)<br>**60** (20/216)<br>**61** (20/216)<br>**55** (20/216) | N/A |
| **Mahajana Sampatha** | **6** (107/216)<br>**5** (106/216)<br>**2** (106/216)<br>**1** (106/216)<br>**9** (105/216) | **D** (14/216)<br>**J** (14/216)<br>**N** (12/216)<br>**Q** (12/216)<br>**Y** (12/216) |
| **Mega Power** | **6** (26/216)<br>**3** (26/216)<br>**13** (25/216)<br>**22** (24/216)<br>**11** (24/216) | **V** (17/216)<br>**T** (13/216)<br>**K** (13/216)<br>**U** (13/216)<br>**J** (11/216) |
| **Nlb Jaya** | **5** (90/207)<br>**3** (83/207)<br>**0** (80/207)<br>**2** (78/207)<br>**4** (73/207) | **T** (14/207)<br>**M** (13/207)<br>**P** (13/207)<br>**I** (13/207)<br>**G** (13/207) |
| **Suba Dawasak** | **3** (87/216)<br>**1** (87/216)<br>**4** (86/216)<br>**9** (81/216)<br>**5** (76/216) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1735)<br>**57** (114/1735)<br>**20** (111/1735)<br>**13** (109/1735)<br>**38** (106/1735) | **B** (81/1735)<br>**M** (78/1735)<br>**R** (77/1735)<br>**P** (77/1735)<br>**I** (74/1735) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1623)<br>**10** (142/1623)<br>**29** (133/1623)<br>**21** (133/1623)<br>**15** (132/1623) | **H** (87/1623)<br>**U** (75/1623)<br>**W** (71/1623)<br>**D** (69/1623)<br>**G** (69/1623) |
| **Lagna Wasana** | **5** (135/1742)<br>**28** (132/1742)<br>**36** (130/1742)<br>**25** (130/1742)<br>**23** (129/1742) | N/A |
| **Sasiri** | **20** (70/920)<br>**9** (69/920)<br>**22** (68/920)<br>**26** (68/920)<br>**19** (67/920) | N/A |
| **Super Ball** | **45** (109/1736)<br>**29** (105/1736)<br>**43** (105/1736)<br>**3** (104/1736)<br>**52** (103/1736) | **I** (87/1736)<br>**D** (80/1736)<br>**T** (78/1736)<br>**V** (77/1736)<br>**A** (77/1736) |
| **Supiri Dhana Sampatha** | **2** (451/894)<br>**0** (450/894)<br>**3** (449/894)<br>**7** (443/894)<br>**5** (426/894) | **K** (44/894)<br>**V** (43/894)<br>**T** (43/894)<br>**J** (42/894)<br>**S** (41/894) |

