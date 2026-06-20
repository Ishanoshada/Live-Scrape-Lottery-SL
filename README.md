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

> **Last Updated (Sri Lanka Time):** `2026-06-21 12:24:19 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 247 Rows | 11.92 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 255 Rows | 10.91 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 254 Rows | 10.76 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 254 Rows | 10.50 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 254 Rows | 10.82 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 254 Rows | 11.51 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 245 Rows | 9.55 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 254 Rows | 11.72 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1773 Rows | 67.81 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1661 Rows | 67.85 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1780 Rows | 66.34 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 958 Rows | 31.66 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1774 Rows | 67.85 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 932 Rows | 34.64 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-21 12:24:19 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (92/247)<br>**6** (91/247)<br>**0** (90/247)<br>**2** (87/247)<br>**7** (86/247) | **N** (15/247)<br>**J** (15/247)<br>**Q** (14/247)<br>**D** (14/247)<br>**Y** (13/247) |
| **Dhana Nidhanaya** | **28** (24/255)<br>**9** (24/255)<br>**6** (21/255)<br>**16** (20/255)<br>**4** (19/255) | **U** (17/255)<br>**F** (13/255)<br>**W** (13/255)<br>**Z** (12/255)<br>**T** (12/255) |
| **Govisetha** | **55** (21/254)<br>**10** (20/254)<br>**23** (19/254)<br>**44** (19/254)<br>**33** (19/254) | **P** (15/254)<br>**C** (14/254)<br>**D** (12/254)<br>**O** (12/254)<br>**M** (12/254) |
| **Handahana** | **21** (25/254)<br>**6** (25/254)<br>**58** (24/254)<br>**11** (23/254)<br>**55** (23/254) | N/A |
| **Mahajana Sampatha** | **1** (127/254)<br>**2** (124/254)<br>**6** (124/254)<br>**5** (123/254)<br>**4** (121/254) | **J** (15/254)<br>**N** (14/254)<br>**Q** (14/254)<br>**D** (14/254)<br>**Y** (13/254) |
| **Mega Power** | **11** (32/254)<br>**3** (29/254)<br>**22** (28/254)<br>**13** (28/254)<br>**6** (27/254) | **V** (18/254)<br>**U** (16/254)<br>**K** (15/254)<br>**T** (14/254)<br>**J** (14/254) |
| **Nlb Jaya** | **5** (108/245)<br>**3** (95/245)<br>**0** (95/245)<br>**2** (90/245)<br>**7** (87/245) | **T** (15/245)<br>**G** (15/245)<br>**P** (14/245)<br>**I** (14/245)<br>**Y** (14/245) |
| **Suba Dawasak** | **3** (106/254)<br>**1** (102/254)<br>**4** (102/254)<br>**9** (95/254)<br>**5** (92/254) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1773)<br>**20** (117/1773)<br>**57** (115/1773)<br>**75** (110/1773)<br>**38** (109/1773) | **B** (82/1773)<br>**R** (79/1773)<br>**P** (79/1773)<br>**M** (79/1773)<br>**I** (76/1773) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1661)<br>**10** (142/1661)<br>**29** (136/1661)<br>**21** (136/1661)<br>**27** (136/1661) | **H** (88/1661)<br>**U** (77/1661)<br>**X** (72/1661)<br>**W** (72/1661)<br>**G** (71/1661) |
| **Lagna Wasana** | **28** (136/1780)<br>**5** (135/1780)<br>**36** (133/1780)<br>**23** (132/1780)<br>**2** (131/1780) | N/A |
| **Sasiri** | **9** (73/958)<br>**20** (71/958)<br>**26** (71/958)<br>**22** (70/958)<br>**19** (67/958) | N/A |
| **Super Ball** | **45** (110/1774)<br>**52** (107/1774)<br>**74** (107/1774)<br>**3** (106/1774)<br>**57** (106/1774) | **I** (89/1774)<br>**D** (81/1774)<br>**V** (80/1774)<br>**T** (79/1774)<br>**A** (79/1774) |
| **Supiri Dhana Sampatha** | **0** (471/932)<br>**2** (469/932)<br>**3** (467/932)<br>**7** (457/932)<br>**5** (445/932) | **K** (46/932)<br>**V** (46/932)<br>**S** (43/932)<br>**M** (43/932)<br>**T** (43/932) |

