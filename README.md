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

> **Last Updated (Sri Lanka Time):** `2026-07-02 12:47:49 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 258 Rows | 12.43 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 266 Rows | 11.37 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 265 Rows | 11.20 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 265 Rows | 10.92 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 265 Rows | 11.26 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 265 Rows | 11.98 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 256 Rows | 9.96 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 265 Rows | 12.20 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1784 Rows | 68.23 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1672 Rows | 68.30 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1791 Rows | 66.75 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 969 Rows | 32.04 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1785 Rows | 68.27 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 943 Rows | 35.05 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-02 12:47:49 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (96/258)<br>**5** (96/258)<br>**7** (92/258)<br>**2** (92/258)<br>**0** (90/258) | **N** (16/258)<br>**Q** (15/258)<br>**J** (15/258)<br>**G** (15/258)<br>**D** (14/258) |
| **Dhana Nidhanaya** | **9** (25/266)<br>**28** (24/266)<br>**7** (23/266)<br>**4** (21/266)<br>**6** (21/266) | **U** (17/266)<br>**F** (15/266)<br>**W** (14/266)<br>**Z** (13/266)<br>**T** (12/266) |
| **Govisetha** | **10** (21/265)<br>**55** (21/265)<br>**23** (20/265)<br>**29** (20/265)<br>**44** (19/265) | **P** (15/265)<br>**C** (14/265)<br>**D** (13/265)<br>**A** (12/265)<br>**O** (12/265) |
| **Handahana** | **21** (27/265)<br>**58** (26/265)<br>**6** (26/265)<br>**11** (25/265)<br>**61** (23/265) | N/A |
| **Mahajana Sampatha** | **2** (131/265)<br>**5** (131/265)<br>**7** (130/265)<br>**6** (130/265)<br>**1** (129/265) | **N** (15/265)<br>**Q** (15/265)<br>**J** (15/265)<br>**G** (15/265)<br>**D** (14/265) |
| **Mega Power** | **11** (36/265)<br>**3** (31/265)<br>**13** (29/265)<br>**22** (28/265)<br>**6** (28/265) | **V** (19/265)<br>**T** (18/265)<br>**U** (18/265)<br>**K** (15/265)<br>**J** (15/265) |
| **Nlb Jaya** | **5** (115/256)<br>**3** (99/256)<br>**0** (98/256)<br>**2** (97/256)<br>**7** (91/256) | **T** (16/256)<br>**G** (16/256)<br>**I** (15/256)<br>**P** (14/256)<br>**Y** (14/256) |
| **Suba Dawasak** | **3** (110/265)<br>**4** (108/265)<br>**1** (106/265)<br>**2** (96/265)<br>**9** (95/265) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1784)<br>**20** (119/1784)<br>**57** (116/1784)<br>**75** (110/1784)<br>**38** (110/1784) | **B** (82/1784)<br>**R** (81/1784)<br>**P** (79/1784)<br>**M** (79/1784)<br>**I** (76/1784) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1672)<br>**10** (143/1672)<br>**27** (138/1672)<br>**15** (137/1672)<br>**29** (136/1672) | **H** (88/1672)<br>**U** (77/1672)<br>**M** (73/1672)<br>**X** (72/1672)<br>**W** (72/1672) |
| **Lagna Wasana** | **28** (136/1791)<br>**5** (135/1791)<br>**36** (134/1791)<br>**23** (132/1791)<br>**2** (131/1791) | N/A |
| **Sasiri** | **9** (73/969)<br>**22** (71/969)<br>**20** (71/969)<br>**26** (71/969)<br>**5** (69/969) | N/A |
| **Super Ball** | **45** (110/1785)<br>**52** (109/1785)<br>**29** (108/1785)<br>**74** (107/1785)<br>**3** (106/1785) | **I** (90/1785)<br>**D** (81/1785)<br>**V** (80/1785)<br>**T** (80/1785)<br>**A** (79/1785) |
| **Supiri Dhana Sampatha** | **2** (476/943)<br>**0** (473/943)<br>**3** (472/943)<br>**7** (463/943)<br>**5** (450/943) | **V** (47/943)<br>**K** (46/943)<br>**S** (43/943)<br>**J** (43/943)<br>**M** (43/943) |

