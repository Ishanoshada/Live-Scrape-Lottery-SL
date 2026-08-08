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

> **Last Updated (Sri Lanka Time):** `2026-08-08 11:27:25 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 296 Rows | 14.19 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 304 Rows | 12.95 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 303 Rows | 12.74 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 303 Rows | 12.42 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 303 Rows | 12.80 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 303 Rows | 13.62 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 294 Rows | 11.39 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 303 Rows | 13.89 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1822 Rows | 69.68 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1710 Rows | 69.87 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1829 Rows | 68.17 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1007 Rows | 33.34 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1823 Rows | 69.72 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 981 Rows | 36.47 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-08 11:27:25 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (111/296)<br>**2** (107/296)<br>**6** (104/296)<br>**3** (103/296)<br>**7** (102/296) | **D** (19/296)<br>**J** (18/296)<br>**Q** (17/296)<br>**N** (16/296)<br>**G** (16/296) |
| **Dhana Nidhanaya** | **9** (27/304)<br>**4** (26/304)<br>**7** (26/304)<br>**28** (25/304)<br>**80** (23/304) | **U** (20/304)<br>**Z** (16/304)<br>**F** (16/304)<br>**W** (16/304)<br>**T** (15/304) |
| **Govisetha** | **55** (25/303)<br>**10** (23/303)<br>**44** (23/303)<br>**33** (23/303)<br>**23** (22/303) | **C** (17/303)<br>**P** (16/303)<br>**K** (16/303)<br>**X** (15/303)<br>**O** (14/303) |
| **Handahana** | **58** (31/303)<br>**11** (29/303)<br>**55** (28/303)<br>**6** (28/303)<br>**21** (27/303) | N/A |
| **Mahajana Sampatha** | **5** (150/303)<br>**2** (150/303)<br>**7** (148/303)<br>**1** (148/303)<br>**4** (147/303) | **D** (19/303)<br>**J** (18/303)<br>**Q** (17/303)<br>**G** (16/303)<br>**N** (15/303) |
| **Mega Power** | **11** (36/303)<br>**13** (34/303)<br>**26** (33/303)<br>**6** (32/303)<br>**22** (32/303) | **T** (21/303)<br>**V** (20/303)<br>**U** (19/303)<br>**K** (17/303)<br>**J** (16/303) |
| **Nlb Jaya** | **5** (131/294)<br>**0** (115/294)<br>**2** (113/294)<br>**3** (112/294)<br>**7** (105/294) | **I** (18/294)<br>**T** (18/294)<br>**G** (16/294)<br>**Y** (15/294)<br>**M** (14/294) |
| **Suba Dawasak** | **3** (125/303)<br>**4** (122/303)<br>**1** (117/303)<br>**8** (112/303)<br>**9** (111/303) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1822)<br>**20** (120/1822)<br>**57** (117/1822)<br>**38** (114/1822)<br>**75** (112/1822) | **B** (84/1822)<br>**R** (83/1822)<br>**P** (80/1822)<br>**M** (80/1822)<br>**N** (78/1822) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (159/1710)<br>**10** (145/1710)<br>**6** (141/1710)<br>**15** (141/1710)<br>**29** (140/1710) | **H** (89/1710)<br>**U** (78/1710)<br>**M** (74/1710)<br>**G** (73/1710)<br>**X** (73/1710) |
| **Lagna Wasana** | **5** (140/1829)<br>**25** (136/1829)<br>**28** (136/1829)<br>**36** (135/1829)<br>**23** (135/1829) | N/A |
| **Sasiri** | **9** (75/1007)<br>**22** (74/1007)<br>**20** (74/1007)<br>**19** (73/1007)<br>**26** (72/1007) | N/A |
| **Super Ball** | **52** (111/1823)<br>**45** (111/1823)<br>**29** (111/1823)<br>**9** (109/1823)<br>**3** (107/1823) | **I** (92/1823)<br>**V** (82/1823)<br>**T** (82/1823)<br>**D** (82/1823)<br>**A** (79/1823) |
| **Supiri Dhana Sampatha** | **2** (495/981)<br>**0** (492/981)<br>**3** (486/981)<br>**7** (481/981)<br>**5** (469/981) | **V** (52/981)<br>**K** (46/981)<br>**T** (45/981)<br>**S** (44/981)<br>**J** (44/981) |

