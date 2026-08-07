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

> **Last Updated (Sri Lanka Time):** `2026-08-07 11:40:46 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 295 Rows | 14.14 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 303 Rows | 12.91 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 302 Rows | 12.70 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 302 Rows | 12.38 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 302 Rows | 12.76 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 302 Rows | 13.58 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 293 Rows | 11.36 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 302 Rows | 13.84 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1821 Rows | 69.64 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1709 Rows | 69.83 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1828 Rows | 68.13 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1006 Rows | 33.30 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1822 Rows | 69.68 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 980 Rows | 36.43 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-07 11:40:46 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (110/295)<br>**2** (107/295)<br>**3** (103/295)<br>**6** (103/295)<br>**7** (102/295) | **D** (19/295)<br>**J** (18/295)<br>**Q** (17/295)<br>**N** (16/295)<br>**G** (16/295) |
| **Dhana Nidhanaya** | **9** (27/303)<br>**4** (26/303)<br>**7** (26/303)<br>**28** (25/303)<br>**80** (23/303) | **U** (20/303)<br>**Z** (16/303)<br>**F** (16/303)<br>**W** (16/303)<br>**T** (15/303) |
| **Govisetha** | **55** (25/302)<br>**10** (23/302)<br>**44** (23/302)<br>**33** (23/302)<br>**23** (22/302) | **C** (17/302)<br>**P** (16/302)<br>**K** (16/302)<br>**X** (15/302)<br>**O** (14/302) |
| **Handahana** | **58** (31/302)<br>**11** (29/302)<br>**55** (28/302)<br>**6** (28/302)<br>**21** (27/302) | N/A |
| **Mahajana Sampatha** | **2** (150/302)<br>**5** (149/302)<br>**4** (147/302)<br>**7** (147/302)<br>**1** (147/302) | **D** (19/302)<br>**J** (18/302)<br>**Q** (17/302)<br>**G** (16/302)<br>**N** (15/302) |
| **Mega Power** | **11** (36/302)<br>**26** (33/302)<br>**13** (33/302)<br>**6** (32/302)<br>**22** (32/302) | **T** (21/302)<br>**V** (20/302)<br>**U** (19/302)<br>**K** (17/302)<br>**J** (16/302) |
| **Nlb Jaya** | **5** (131/293)<br>**0** (114/293)<br>**3** (112/293)<br>**2** (112/293)<br>**7** (105/293) | **I** (18/293)<br>**T** (18/293)<br>**G** (16/293)<br>**Y** (15/293)<br>**M** (14/293) |
| **Suba Dawasak** | **3** (124/302)<br>**4** (122/302)<br>**1** (117/302)<br>**9** (111/302)<br>**8** (111/302) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1821)<br>**20** (120/1821)<br>**57** (117/1821)<br>**38** (114/1821)<br>**75** (112/1821) | **B** (84/1821)<br>**R** (83/1821)<br>**P** (80/1821)<br>**M** (80/1821)<br>**N** (78/1821) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (159/1709)<br>**10** (145/1709)<br>**6** (141/1709)<br>**15** (141/1709)<br>**29** (140/1709) | **H** (89/1709)<br>**U** (78/1709)<br>**G** (73/1709)<br>**M** (73/1709)<br>**X** (73/1709) |
| **Lagna Wasana** | **5** (140/1828)<br>**25** (136/1828)<br>**28** (136/1828)<br>**36** (135/1828)<br>**23** (135/1828) | N/A |
| **Sasiri** | **9** (75/1006)<br>**22** (74/1006)<br>**20** (74/1006)<br>**19** (73/1006)<br>**26** (71/1006) | N/A |
| **Super Ball** | **52** (111/1822)<br>**45** (111/1822)<br>**29** (111/1822)<br>**9** (109/1822)<br>**3** (107/1822) | **I** (92/1822)<br>**V** (82/1822)<br>**T** (82/1822)<br>**D** (82/1822)<br>**A** (79/1822) |
| **Supiri Dhana Sampatha** | **2** (494/980)<br>**0** (492/980)<br>**3** (486/980)<br>**7** (480/980)<br>**5** (468/980) | **V** (52/980)<br>**K** (46/980)<br>**T** (45/980)<br>**S** (44/980)<br>**J** (44/980) |

