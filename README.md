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

> **Last Updated (Sri Lanka Time):** `2026-07-27 12:01:23 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 283 Rows | 13.58 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 291 Rows | 12.40 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 290 Rows | 12.20 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 290 Rows | 11.90 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 290 Rows | 12.26 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 290 Rows | 13.05 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 281 Rows | 10.90 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 290 Rows | 13.30 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1809 Rows | 69.18 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1697 Rows | 69.33 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1816 Rows | 67.68 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 994 Rows | 32.89 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1810 Rows | 69.22 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 968 Rows | 35.98 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-27 12:01:23 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (105/283)<br>**2** (102/283)<br>**6** (101/283)<br>**3** (98/283)<br>**7** (98/283) | **D** (18/283)<br>**Q** (17/283)<br>**N** (16/283)<br>**J** (16/283)<br>**G** (16/283) |
| **Dhana Nidhanaya** | **9** (27/291)<br>**7** (26/291)<br>**28** (25/291)<br>**4** (24/291)<br>**6** (23/291) | **U** (19/291)<br>**F** (16/291)<br>**T** (15/291)<br>**W** (15/291)<br>**Z** (14/291) |
| **Govisetha** | **55** (24/290)<br>**10** (22/290)<br>**33** (22/290)<br>**23** (21/290)<br>**44** (21/290) | **P** (16/290)<br>**C** (15/290)<br>**K** (14/290)<br>**D** (13/290)<br>**A** (13/290) |
| **Handahana** | **58** (31/290)<br>**11** (27/290)<br>**21** (27/290)<br>**6** (27/290)<br>**55** (26/290) | N/A |
| **Mahajana Sampatha** | **2** (144/290)<br>**5** (142/290)<br>**1** (142/290)<br>**4** (141/290)<br>**7** (141/290) | **D** (18/290)<br>**Q** (17/290)<br>**J** (16/290)<br>**G** (16/290)<br>**N** (15/290) |
| **Mega Power** | **11** (36/290)<br>**6** (32/290)<br>**22** (32/290)<br>**3** (32/290)<br>**19** (31/290) | **T** (21/290)<br>**V** (20/290)<br>**U** (19/290)<br>**K** (17/290)<br>**J** (16/290) |
| **Nlb Jaya** | **5** (127/281)<br>**3** (107/281)<br>**0** (107/281)<br>**2** (106/281)<br>**1** (102/281) | **T** (18/281)<br>**I** (16/281)<br>**G** (16/281)<br>**M** (14/281)<br>**P** (14/281) |
| **Suba Dawasak** | **3** (119/290)<br>**4** (118/290)<br>**1** (112/290)<br>**9** (106/290)<br>**8** (106/290) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1809)<br>**20** (119/1809)<br>**57** (117/1809)<br>**38** (112/1809)<br>**75** (111/1809) | **R** (82/1809)<br>**B** (82/1809)<br>**P** (80/1809)<br>**M** (80/1809)<br>**I** (77/1809) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1697)<br>**10** (145/1697)<br>**15** (140/1697)<br>**6** (139/1697)<br>**29** (139/1697) | **H** (88/1697)<br>**U** (78/1697)<br>**M** (73/1697)<br>**X** (73/1697)<br>**D** (72/1697) |
| **Lagna Wasana** | **5** (139/1816)<br>**28** (136/1816)<br>**36** (135/1816)<br>**25** (135/1816)<br>**23** (134/1816) | N/A |
| **Sasiri** | **9** (74/994)<br>**22** (73/994)<br>**20** (73/994)<br>**19** (71/994)<br>**26** (71/994) | N/A |
| **Super Ball** | **45** (111/1810)<br>**52** (110/1810)<br>**29** (110/1810)<br>**9** (108/1810)<br>**3** (107/1810) | **I** (92/1810)<br>**D** (82/1810)<br>**V** (81/1810)<br>**T** (81/1810)<br>**A** (79/1810) |
| **Supiri Dhana Sampatha** | **2** (488/968)<br>**0** (486/968)<br>**3** (483/968)<br>**7** (478/968)<br>**5** (463/968) | **V** (50/968)<br>**K** (46/968)<br>**S** (44/968)<br>**J** (44/968)<br>**T** (44/968) |

