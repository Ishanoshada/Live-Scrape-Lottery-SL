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

> **Last Updated (Sri Lanka Time):** `2026-09-05 01:17:06 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 323 Rows | 15.50 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 331 Rows | 14.12 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 330 Rows | 13.89 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 330 Rows | 13.54 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 330 Rows | 13.95 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 330 Rows | 14.84 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 321 Rows | 12.47 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 330 Rows | 15.14 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1849 Rows | 70.71 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1737 Rows | 70.98 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1856 Rows | 69.17 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1034 Rows | 34.27 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1850 Rows | 70.75 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1008 Rows | 37.48 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-05 01:17:06 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (120/323)<br>**2** (117/323)<br>**3** (112/323)<br>**6** (111/323)<br>**8** (111/323) | **D** (19/323)<br>**J** (19/323)<br>**G** (18/323)<br>**W** (18/323)<br>**N** (17/323) |
| **Dhana Nidhanaya** | **9** (32/331)<br>**4** (30/331)<br>**7** (28/331)<br>**28** (26/331)<br>**3** (26/331) | **U** (20/331)<br>**F** (18/331)<br>**W** (18/331)<br>**M** (18/331)<br>**Z** (17/331) |
| **Govisetha** | **55** (27/330)<br>**10** (25/330)<br>**44** (24/330)<br>**29** (24/330)<br>**23** (23/330) | **P** (18/330)<br>**C** (18/330)<br>**X** (17/330)<br>**K** (16/330)<br>**W** (15/330) |
| **Handahana** | **58** (32/330)<br>**11** (31/330)<br>**55** (30/330)<br>**6** (29/330)<br>**16** (28/330) | N/A |
| **Mahajana Sampatha** | **5** (165/330)<br>**2** (163/330)<br>**1** (162/330)<br>**7** (161/330)<br>**9** (160/330) | **D** (19/330)<br>**J** (19/330)<br>**W** (19/330)<br>**G** (18/330)<br>**Q** (17/330) |
| **Mega Power** | **11** (39/330)<br>**26** (37/330)<br>**3** (36/330)<br>**13** (35/330)<br>**6** (34/330) | **T** (22/330)<br>**V** (21/330)<br>**U** (20/330)<br>**K** (18/330)<br>**J** (17/330) |
| **Nlb Jaya** | **5** (139/321)<br>**0** (126/321)<br>**3** (125/321)<br>**2** (123/321)<br>**7** (116/321) | **I** (18/321)<br>**T** (18/321)<br>**G** (17/321)<br>**O** (17/321)<br>**H** (16/321) |
| **Suba Dawasak** | **3** (134/330)<br>**4** (133/330)<br>**1** (125/330)<br>**9** (125/330)<br>**8** (123/330) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1849)<br>**20** (121/1849)<br>**57** (120/1849)<br>**38** (116/1849)<br>**75** (114/1849) | **B** (88/1849)<br>**R** (84/1849)<br>**M** (81/1849)<br>**P** (80/1849)<br>**N** (79/1849) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1737)<br>**10** (146/1737)<br>**6** (143/1737)<br>**29** (143/1737)<br>**15** (143/1737) | **H** (89/1737)<br>**U** (79/1737)<br>**M** (77/1737)<br>**D** (75/1737)<br>**G** (75/1737) |
| **Lagna Wasana** | **5** (142/1856)<br>**23** (140/1856)<br>**39** (138/1856)<br>**36** (138/1856)<br>**28** (138/1856) | N/A |
| **Sasiri** | **9** (80/1034)<br>**22** (77/1034)<br>**20** (77/1034)<br>**26** (76/1034)<br>**19** (74/1034) | N/A |
| **Super Ball** | **9** (112/1850)<br>**45** (112/1850)<br>**29** (112/1850)<br>**52** (111/1850)<br>**74** (109/1850) | **I** (93/1850)<br>**V** (83/1850)<br>**T** (82/1850)<br>**D** (82/1850)<br>**A** (81/1850) |
| **Supiri Dhana Sampatha** | **2** (506/1008)<br>**0** (506/1008)<br>**3** (499/1008)<br>**7** (496/1008)<br>**5** (482/1008) | **V** (53/1008)<br>**K** (47/1008)<br>**S** (46/1008)<br>**G** (46/1008)<br>**T** (46/1008) |

