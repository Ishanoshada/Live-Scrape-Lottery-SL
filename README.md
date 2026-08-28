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

> **Last Updated (Sri Lanka Time):** `2026-08-28 07:06:14 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 315 Rows | 15.10 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 323 Rows | 13.77 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 322 Rows | 13.54 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 322 Rows | 13.20 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 322 Rows | 13.60 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 321 Rows | 14.43 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 312 Rows | 12.11 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 321 Rows | 14.71 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1841 Rows | 70.41 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1729 Rows | 70.65 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1848 Rows | 68.87 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1026 Rows | 33.99 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1842 Rows | 70.45 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1000 Rows | 37.18 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-28 07:06:14 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (116/315)<br>**2** (114/315)<br>**6** (110/315)<br>**3** (109/315)<br>**4** (109/315) | **D** (19/315)<br>**J** (19/315)<br>**N** (17/315)<br>**Q** (17/315)<br>**G** (16/315) |
| **Dhana Nidhanaya** | **9** (31/323)<br>**4** (28/323)<br>**7** (28/323)<br>**28** (25/323)<br>**80** (24/323) | **U** (20/323)<br>**W** (18/323)<br>**F** (17/323)<br>**M** (17/323)<br>**Z** (16/323) |
| **Govisetha** | **55** (25/322)<br>**44** (24/322)<br>**29** (24/322)<br>**10** (23/322)<br>**33** (23/322) | **P** (18/322)<br>**C** (18/322)<br>**X** (17/322)<br>**K** (16/322)<br>**A** (14/322) |
| **Handahana** | **58** (32/322)<br>**11** (30/322)<br>**55** (29/322)<br>**21** (28/322)<br>**6** (28/322) | N/A |
| **Mahajana Sampatha** | **5** (160/322)<br>**2** (160/322)<br>**7** (158/322)<br>**1** (158/322)<br>**4** (156/322) | **D** (19/322)<br>**J** (19/322)<br>**Q** (17/322)<br>**W** (17/322)<br>**N** (16/322) |
| **Mega Power** | **11** (37/321)<br>**26** (36/321)<br>**13** (35/321)<br>**3** (34/321)<br>**22** (32/321) | **T** (22/321)<br>**V** (20/321)<br>**U** (20/321)<br>**K** (18/321)<br>**J** (17/321) |
| **Nlb Jaya** | **5** (136/312)<br>**2** (121/312)<br>**3** (120/312)<br>**0** (120/312)<br>**7** (112/312) | **I** (18/312)<br>**T** (18/312)<br>**G** (17/312)<br>**H** (16/312)<br>**O** (16/312) |
| **Suba Dawasak** | **3** (131/321)<br>**4** (130/321)<br>**1** (123/321)<br>**8** (120/321)<br>**9** (119/321) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1841)<br>**20** (121/1841)<br>**57** (118/1841)<br>**38** (116/1841)<br>**75** (112/1841) | **B** (86/1841)<br>**R** (84/1841)<br>**M** (81/1841)<br>**P** (80/1841)<br>**N** (79/1841) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1729)<br>**10** (146/1729)<br>**6** (142/1729)<br>**29** (142/1729)<br>**15** (142/1729) | **H** (89/1729)<br>**U** (78/1729)<br>**M** (76/1729)<br>**D** (74/1729)<br>**G** (74/1729) |
| **Lagna Wasana** | **5** (140/1848)<br>**23** (139/1848)<br>**36** (137/1848)<br>**28** (137/1848)<br>**39** (136/1848) | N/A |
| **Sasiri** | **9** (79/1026)<br>**22** (77/1026)<br>**26** (76/1026)<br>**20** (75/1026)<br>**19** (74/1026) | N/A |
| **Super Ball** | **52** (111/1842)<br>**45** (111/1842)<br>**29** (111/1842)<br>**9** (110/1842)<br>**74** (109/1842) | **I** (92/1842)<br>**V** (82/1842)<br>**T** (82/1842)<br>**D** (82/1842)<br>**A** (81/1842) |
| **Supiri Dhana Sampatha** | **2** (502/1000)<br>**0** (502/1000)<br>**3** (495/1000)<br>**7** (492/1000)<br>**5** (477/1000) | **V** (53/1000)<br>**K** (47/1000)<br>**G** (45/1000)<br>**T** (45/1000)<br>**S** (44/1000) |

