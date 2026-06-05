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

> **Last Updated (Sri Lanka Time):** `2026-06-06 12:47:26 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 232 Rows | 11.23 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 240 Rows | 10.29 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 239 Rows | 10.16 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 239 Rows | 9.91 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 239 Rows | 10.21 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 239 Rows | 10.86 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 230 Rows | 8.99 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 239 Rows | 11.06 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1758 Rows | 67.24 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1646 Rows | 67.23 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1765 Rows | 65.78 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 943 Rows | 31.14 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1759 Rows | 67.27 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 917 Rows | 34.08 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-06 12:47:26 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (89/232)<br>**5** (86/232)<br>**7** (82/232)<br>**0** (81/232)<br>**2** (81/232) | **J** (15/232)<br>**N** (14/232)<br>**D** (14/232)<br>**Q** (13/232)<br>**Y** (12/232) |
| **Dhana Nidhanaya** | **28** (23/240)<br>**9** (23/240)<br>**6** (20/240)<br>**7** (19/240)<br>**16** (19/240) | **U** (15/240)<br>**W** (13/240)<br>**Z** (12/240)<br>**T** (12/240)<br>**M** (12/240) |
| **Govisetha** | **10** (20/239)<br>**44** (19/239)<br>**55** (19/239)<br>**33** (18/239)<br>**19** (17/239) | **P** (15/239)<br>**D** (12/239)<br>**O** (12/239)<br>**W** (11/239)<br>**K** (11/239) |
| **Handahana** | **6** (24/239)<br>**55** (23/239)<br>**58** (22/239)<br>**11** (22/239)<br>**61** (22/239) | N/A |
| **Mahajana Sampatha** | **1** (119/239)<br>**6** (118/239)<br>**5** (117/239)<br>**2** (116/239)<br>**4** (115/239) | **J** (15/239)<br>**D** (14/239)<br>**N** (13/239)<br>**Q** (13/239)<br>**Y** (12/239) |
| **Mega Power** | **11** (30/239)<br>**3** (28/239)<br>**22** (27/239)<br>**13** (27/239)<br>**6** (26/239) | **V** (17/239)<br>**T** (14/239)<br>**K** (14/239)<br>**J** (13/239)<br>**U** (13/239) |
| **Nlb Jaya** | **5** (99/230)<br>**3** (90/230)<br>**0** (90/230)<br>**2** (86/230)<br>**1** (82/230) | **P** (14/230)<br>**I** (14/230)<br>**T** (14/230)<br>**M** (13/230)<br>**G** (13/230) |
| **Suba Dawasak** | **3** (99/239)<br>**1** (95/239)<br>**4** (95/239)<br>**5** (90/239)<br>**9** (90/239) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (118/1758)<br>**57** (115/1758)<br>**20** (114/1758)<br>**13** (109/1758)<br>**75** (108/1758) | **B** (82/1758)<br>**M** (79/1758)<br>**R** (78/1758)<br>**P** (78/1758)<br>**I** (75/1758) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1646)<br>**10** (142/1646)<br>**29** (134/1646)<br>**21** (134/1646)<br>**22** (133/1646) | **H** (88/1646)<br>**U** (76/1646)<br>**W** (72/1646)<br>**G** (71/1646)<br>**X** (71/1646) |
| **Lagna Wasana** | **28** (135/1765)<br>**5** (135/1765)<br>**36** (132/1765)<br>**23** (130/1765)<br>**25** (130/1765) | N/A |
| **Sasiri** | **9** (72/943)<br>**20** (70/943)<br>**22** (68/943)<br>**26** (68/943)<br>**19** (67/943) | N/A |
| **Super Ball** | **45** (109/1759)<br>**52** (107/1759)<br>**74** (107/1759)<br>**29** (106/1759)<br>**43** (106/1759) | **I** (87/1759)<br>**D** (81/1759)<br>**T** (79/1759)<br>**V** (77/1759)<br>**A** (77/1759) |
| **Supiri Dhana Sampatha** | **0** (466/917)<br>**2** (461/917)<br>**3** (459/917)<br>**7** (451/917)<br>**5** (437/917) | **K** (44/917)<br>**V** (44/917)<br>**S** (43/917)<br>**M** (43/917)<br>**T** (43/917) |

