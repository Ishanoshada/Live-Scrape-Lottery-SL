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

> **Last Updated (Sri Lanka Time):** `2026-07-30 12:01:58 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 286 Rows | 13.72 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 294 Rows | 12.52 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 293 Rows | 12.32 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 293 Rows | 12.02 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 293 Rows | 12.38 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 293 Rows | 13.18 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 284 Rows | 11.01 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 293 Rows | 13.43 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1812 Rows | 69.30 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1700 Rows | 69.46 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1819 Rows | 67.79 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 997 Rows | 33.00 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1813 Rows | 69.34 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 971 Rows | 36.10 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-30 12:01:58 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (107/286)<br>**2** (104/286)<br>**6** (101/286)<br>**3** (99/286)<br>**7** (99/286) | **D** (19/286)<br>**Q** (17/286)<br>**N** (16/286)<br>**J** (16/286)<br>**G** (16/286) |
| **Dhana Nidhanaya** | **9** (27/294)<br>**7** (26/294)<br>**28** (25/294)<br>**4** (24/294)<br>**6** (23/294) | **U** (19/294)<br>**F** (16/294)<br>**W** (16/294)<br>**Z** (15/294)<br>**T** (15/294) |
| **Govisetha** | **55** (25/293)<br>**10** (22/293)<br>**33** (22/293)<br>**23** (21/293)<br>**44** (21/293) | **P** (16/293)<br>**C** (16/293)<br>**K** (14/293)<br>**D** (13/293)<br>**A** (13/293) |
| **Handahana** | **58** (31/293)<br>**11** (28/293)<br>**21** (27/293)<br>**6** (27/293)<br>**55** (26/293) | N/A |
| **Mahajana Sampatha** | **2** (147/293)<br>**5** (144/293)<br>**1** (143/293)<br>**4** (142/293)<br>**7** (142/293) | **D** (19/293)<br>**Q** (17/293)<br>**J** (16/293)<br>**G** (16/293)<br>**N** (15/293) |
| **Mega Power** | **11** (36/293)<br>**6** (32/293)<br>**22** (32/293)<br>**3** (32/293)<br>**13** (32/293) | **T** (21/293)<br>**V** (20/293)<br>**U** (19/293)<br>**K** (17/293)<br>**J** (16/293) |
| **Nlb Jaya** | **5** (128/284)<br>**0** (109/284)<br>**3** (107/284)<br>**2** (107/284)<br>**7** (102/284) | **T** (18/284)<br>**I** (17/284)<br>**G** (16/284)<br>**M** (14/284)<br>**P** (14/284) |
| **Suba Dawasak** | **4** (120/293)<br>**3** (119/293)<br>**1** (115/293)<br>**8** (109/293)<br>**9** (107/293) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1812)<br>**20** (119/1812)<br>**57** (117/1812)<br>**75** (112/1812)<br>**38** (112/1812) | **R** (83/1812)<br>**B** (82/1812)<br>**P** (80/1812)<br>**M** (80/1812)<br>**I** (77/1812) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1700)<br>**10** (145/1700)<br>**6** (141/1700)<br>**15** (140/1700)<br>**29** (139/1700) | **H** (88/1700)<br>**U** (78/1700)<br>**M** (73/1700)<br>**X** (73/1700)<br>**D** (72/1700) |
| **Lagna Wasana** | **5** (140/1819)<br>**25** (136/1819)<br>**28** (136/1819)<br>**36** (135/1819)<br>**23** (135/1819) | N/A |
| **Sasiri** | **9** (74/997)<br>**22** (73/997)<br>**20** (73/997)<br>**19** (71/997)<br>**26** (71/997) | N/A |
| **Super Ball** | **45** (111/1813)<br>**52** (110/1813)<br>**29** (110/1813)<br>**9** (109/1813)<br>**3** (107/1813) | **I** (92/1813)<br>**D** (82/1813)<br>**V** (81/1813)<br>**T** (81/1813)<br>**A** (79/1813) |
| **Supiri Dhana Sampatha** | **2** (489/971)<br>**0** (488/971)<br>**3** (483/971)<br>**7** (479/971)<br>**5** (463/971) | **V** (50/971)<br>**K** (46/971)<br>**S** (44/971)<br>**J** (44/971)<br>**T** (44/971) |

