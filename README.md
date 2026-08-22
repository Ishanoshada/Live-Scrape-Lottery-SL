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

> **Last Updated (Sri Lanka Time):** `2026-08-22 11:15:18 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 310 Rows | 14.86 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 318 Rows | 13.55 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 317 Rows | 13.33 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 317 Rows | 12.99 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 317 Rows | 13.39 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 317 Rows | 14.25 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 308 Rows | 11.95 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 317 Rows | 14.53 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1836 Rows | 70.22 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1724 Rows | 70.45 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1843 Rows | 68.69 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1021 Rows | 33.82 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1837 Rows | 70.25 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 995 Rows | 36.99 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-22 11:15:18 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (114/310)<br>**2** (113/310)<br>**7** (108/310)<br>**3** (107/310)<br>**1** (107/310) | **D** (19/310)<br>**J** (19/310)<br>**N** (17/310)<br>**Q** (17/310)<br>**G** (16/310) |
| **Dhana Nidhanaya** | **9** (30/318)<br>**4** (28/318)<br>**7** (27/318)<br>**28** (25/318)<br>**80** (24/318) | **U** (20/318)<br>**W** (18/318)<br>**M** (17/318)<br>**Z** (16/318)<br>**F** (16/318) |
| **Govisetha** | **55** (25/317)<br>**44** (24/317)<br>**29** (24/317)<br>**10** (23/317)<br>**33** (23/317) | **P** (18/317)<br>**C** (17/317)<br>**X** (17/317)<br>**K** (16/317)<br>**A** (14/317) |
| **Handahana** | **58** (31/317)<br>**11** (30/317)<br>**55** (29/317)<br>**21** (28/317)<br>**6** (28/317) | N/A |
| **Mahajana Sampatha** | **1** (158/317)<br>**5** (157/317)<br>**2** (157/317)<br>**7** (155/317)<br>**4** (153/317) | **D** (19/317)<br>**J** (19/317)<br>**Q** (17/317)<br>**N** (16/317)<br>**G** (16/317) |
| **Mega Power** | **11** (37/317)<br>**26** (35/317)<br>**3** (34/317)<br>**13** (34/317)<br>**22** (32/317) | **T** (22/317)<br>**V** (20/317)<br>**U** (20/317)<br>**K** (17/317)<br>**J** (17/317) |
| **Nlb Jaya** | **5** (136/308)<br>**2** (119/308)<br>**0** (118/308)<br>**3** (117/308)<br>**7** (111/308) | **I** (18/308)<br>**T** (18/308)<br>**G** (17/308)<br>**H** (16/308)<br>**P** (15/308) |
| **Suba Dawasak** | **3** (130/317)<br>**4** (127/317)<br>**1** (122/317)<br>**8** (120/317)<br>**9** (116/317) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1836)<br>**20** (121/1836)<br>**57** (118/1836)<br>**38** (116/1836)<br>**75** (112/1836) | **B** (85/1836)<br>**R** (84/1836)<br>**M** (81/1836)<br>**P** (80/1836)<br>**N** (78/1836) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1724)<br>**10** (146/1724)<br>**6** (142/1724)<br>**29** (142/1724)<br>**15** (142/1724) | **H** (89/1724)<br>**U** (78/1724)<br>**M** (76/1724)<br>**D** (74/1724)<br>**G** (74/1724) |
| **Lagna Wasana** | **5** (140/1843)<br>**36** (137/1843)<br>**28** (137/1843)<br>**23** (136/1843)<br>**25** (136/1843) | N/A |
| **Sasiri** | **9** (79/1021)<br>**22** (76/1021)<br>**20** (75/1021)<br>**19** (74/1021)<br>**26** (74/1021) | N/A |
| **Super Ball** | **52** (111/1837)<br>**45** (111/1837)<br>**29** (111/1837)<br>**9** (110/1837)<br>**74** (109/1837) | **I** (92/1837)<br>**V** (82/1837)<br>**T** (82/1837)<br>**D** (82/1837)<br>**A** (81/1837) |
| **Supiri Dhana Sampatha** | **2** (500/995)<br>**0** (499/995)<br>**3** (492/995)<br>**7** (489/995)<br>**5** (475/995) | **V** (53/995)<br>**K** (46/995)<br>**T** (45/995)<br>**S** (44/995)<br>**G** (44/995) |

