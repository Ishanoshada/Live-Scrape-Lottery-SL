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

> **Last Updated (Sri Lanka Time):** `2026-08-29 06:35:08 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 316 Rows | 15.15 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 324 Rows | 13.81 KB |
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
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1842 Rows | 70.45 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1730 Rows | 70.69 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1849 Rows | 68.91 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1027 Rows | 34.03 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1843 Rows | 70.48 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1001 Rows | 37.22 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-29 06:35:08 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (117/316)<br>**2** (114/316)<br>**3** (110/316)<br>**6** (110/316)<br>**4** (109/316) | **D** (19/316)<br>**J** (19/316)<br>**N** (17/316)<br>**Q** (17/316)<br>**G** (16/316) |
| **Dhana Nidhanaya** | **9** (31/324)<br>**4** (28/324)<br>**7** (28/324)<br>**28** (26/324)<br>**80** (24/324) | **U** (20/324)<br>**F** (18/324)<br>**W** (18/324)<br>**M** (17/324)<br>**Z** (16/324) |
| **Govisetha** | **55** (25/322)<br>**44** (24/322)<br>**29** (24/322)<br>**10** (23/322)<br>**33** (23/322) | **P** (18/322)<br>**C** (18/322)<br>**X** (17/322)<br>**K** (16/322)<br>**A** (14/322) |
| **Handahana** | **58** (32/322)<br>**11** (30/322)<br>**55** (29/322)<br>**21** (28/322)<br>**6** (28/322) | N/A |
| **Mahajana Sampatha** | **5** (160/322)<br>**2** (160/322)<br>**7** (158/322)<br>**1** (158/322)<br>**4** (156/322) | **D** (19/322)<br>**J** (19/322)<br>**Q** (17/322)<br>**W** (17/322)<br>**N** (16/322) |
| **Mega Power** | **11** (37/321)<br>**26** (36/321)<br>**13** (35/321)<br>**3** (34/321)<br>**22** (32/321) | **T** (22/321)<br>**V** (20/321)<br>**U** (20/321)<br>**K** (18/321)<br>**J** (17/321) |
| **Nlb Jaya** | **5** (136/312)<br>**2** (121/312)<br>**3** (120/312)<br>**0** (120/312)<br>**7** (112/312) | **I** (18/312)<br>**T** (18/312)<br>**G** (17/312)<br>**H** (16/312)<br>**O** (16/312) |
| **Suba Dawasak** | **3** (131/321)<br>**4** (130/321)<br>**1** (123/321)<br>**8** (120/321)<br>**9** (119/321) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1842)<br>**20** (121/1842)<br>**57** (118/1842)<br>**38** (116/1842)<br>**75** (112/1842) | **B** (86/1842)<br>**R** (84/1842)<br>**M** (81/1842)<br>**P** (80/1842)<br>**N** (79/1842) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1730)<br>**10** (146/1730)<br>**6** (142/1730)<br>**29** (142/1730)<br>**15** (142/1730) | **H** (89/1730)<br>**U** (78/1730)<br>**M** (76/1730)<br>**D** (74/1730)<br>**G** (74/1730) |
| **Lagna Wasana** | **5** (141/1849)<br>**23** (139/1849)<br>**36** (137/1849)<br>**28** (137/1849)<br>**39** (136/1849) | N/A |
| **Sasiri** | **9** (79/1027)<br>**22** (77/1027)<br>**20** (76/1027)<br>**26** (76/1027)<br>**19** (74/1027) | N/A |
| **Super Ball** | **52** (111/1843)<br>**9** (111/1843)<br>**45** (111/1843)<br>**29** (111/1843)<br>**74** (109/1843) | **I** (92/1843)<br>**V** (82/1843)<br>**T** (82/1843)<br>**D** (82/1843)<br>**A** (81/1843) |
| **Supiri Dhana Sampatha** | **2** (503/1001)<br>**0** (502/1001)<br>**3** (495/1001)<br>**7** (493/1001)<br>**5** (478/1001) | **V** (53/1001)<br>**K** (47/1001)<br>**G** (46/1001)<br>**T** (45/1001)<br>**S** (44/1001) |

