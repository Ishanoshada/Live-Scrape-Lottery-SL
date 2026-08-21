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

> **Last Updated (Sri Lanka Time):** `2026-08-21 11:26:22 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 309 Rows | 14.82 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 317 Rows | 13.51 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 316 Rows | 13.29 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 316 Rows | 12.95 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 316 Rows | 13.35 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 316 Rows | 14.20 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 307 Rows | 11.91 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 316 Rows | 14.48 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1835 Rows | 70.18 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1723 Rows | 70.40 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1842 Rows | 68.65 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1020 Rows | 33.79 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1836 Rows | 70.22 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 994 Rows | 36.95 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-21 11:26:23 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (114/309)<br>**2** (112/309)<br>**7** (108/309)<br>**3** (106/309)<br>**6** (106/309) | **D** (19/309)<br>**J** (19/309)<br>**N** (17/309)<br>**Q** (17/309)<br>**G** (16/309) |
| **Dhana Nidhanaya** | **9** (30/317)<br>**4** (28/317)<br>**7** (27/317)<br>**28** (25/317)<br>**80** (24/317) | **U** (20/317)<br>**W** (17/317)<br>**M** (17/317)<br>**Z** (16/317)<br>**F** (16/317) |
| **Govisetha** | **55** (25/316)<br>**44** (24/316)<br>**29** (24/316)<br>**10** (23/316)<br>**33** (23/316) | **P** (18/316)<br>**C** (17/316)<br>**X** (17/316)<br>**K** (16/316)<br>**A** (14/316) |
| **Handahana** | **58** (31/316)<br>**11** (30/316)<br>**55** (29/316)<br>**21** (28/316)<br>**6** (28/316) | N/A |
| **Mahajana Sampatha** | **1** (157/316)<br>**5** (156/316)<br>**2** (156/316)<br>**7** (155/316)<br>**4** (153/316) | **D** (19/316)<br>**J** (19/316)<br>**Q** (17/316)<br>**N** (16/316)<br>**G** (16/316) |
| **Mega Power** | **11** (37/316)<br>**26** (35/316)<br>**3** (34/316)<br>**13** (34/316)<br>**22** (32/316) | **T** (22/316)<br>**V** (20/316)<br>**U** (20/316)<br>**K** (17/316)<br>**J** (17/316) |
| **Nlb Jaya** | **5** (136/307)<br>**2** (118/307)<br>**0** (118/307)<br>**3** (116/307)<br>**7** (111/307) | **I** (18/307)<br>**T** (18/307)<br>**H** (16/307)<br>**G** (16/307)<br>**P** (15/307) |
| **Suba Dawasak** | **3** (130/316)<br>**4** (127/316)<br>**1** (121/316)<br>**8** (119/316)<br>**2** (116/316) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1835)<br>**20** (121/1835)<br>**57** (118/1835)<br>**38** (116/1835)<br>**75** (112/1835) | **B** (85/1835)<br>**R** (84/1835)<br>**M** (81/1835)<br>**P** (80/1835)<br>**N** (78/1835) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (162/1723)<br>**10** (146/1723)<br>**6** (142/1723)<br>**29** (142/1723)<br>**15** (142/1723) | **H** (89/1723)<br>**U** (78/1723)<br>**M** (76/1723)<br>**D** (74/1723)<br>**G** (74/1723) |
| **Lagna Wasana** | **5** (140/1842)<br>**36** (137/1842)<br>**28** (137/1842)<br>**23** (136/1842)<br>**25** (136/1842) | N/A |
| **Sasiri** | **9** (79/1020)<br>**22** (75/1020)<br>**20** (75/1020)<br>**19** (74/1020)<br>**26** (74/1020) | N/A |
| **Super Ball** | **52** (111/1836)<br>**45** (111/1836)<br>**29** (111/1836)<br>**9** (110/1836)<br>**74** (109/1836) | **I** (92/1836)<br>**V** (82/1836)<br>**T** (82/1836)<br>**D** (82/1836)<br>**A** (81/1836) |
| **Supiri Dhana Sampatha** | **2** (499/994)<br>**0** (499/994)<br>**3** (491/994)<br>**7** (488/994)<br>**5** (474/994) | **V** (53/994)<br>**K** (46/994)<br>**T** (45/994)<br>**S** (44/994)<br>**G** (44/994) |

