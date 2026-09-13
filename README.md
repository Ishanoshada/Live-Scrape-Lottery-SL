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

> **Last Updated (Sri Lanka Time):** `2026-09-14 01:08:41 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 332 Rows | 15.96 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 340 Rows | 14.53 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 339 Rows | 14.29 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 339 Rows | 13.93 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 339 Rows | 14.36 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 339 Rows | 15.27 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 330 Rows | 12.84 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 339 Rows | 15.58 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1858 Rows | 71.06 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1746 Rows | 71.35 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1865 Rows | 69.50 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1043 Rows | 34.57 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1859 Rows | 71.09 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1017 Rows | 37.83 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-09-14 01:08:41 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (123/332)<br>**2** (121/332)<br>**6** (116/332)<br>**1** (114/332)<br>**8** (113/332) | **D** (20/332)<br>**J** (19/332)<br>**Q** (18/332)<br>**G** (18/332)<br>**W** (18/332) |
| **Dhana Nidhanaya** | **9** (32/340)<br>**4** (30/340)<br>**7** (28/340)<br>**28** (26/340)<br>**3** (26/340) | **U** (20/340)<br>**W** (19/340)<br>**Z** (18/340)<br>**F** (18/340)<br>**M** (18/340) |
| **Govisetha** | **55** (27/339)<br>**10** (26/339)<br>**44** (25/339)<br>**29** (24/339)<br>**33** (24/339) | **P** (19/339)<br>**C** (18/339)<br>**X** (17/339)<br>**K** (16/339)<br>**W** (15/339) |
| **Handahana** | **58** (32/339)<br>**11** (31/339)<br>**55** (31/339)<br>**6** (30/339)<br>**21** (29/339) | N/A |
| **Mahajana Sampatha** | **5** (170/339)<br>**1** (169/339)<br>**2** (167/339)<br>**9** (164/339)<br>**7** (163/339) | **D** (20/339)<br>**J** (19/339)<br>**W** (19/339)<br>**Q** (18/339)<br>**G** (18/339) |
| **Mega Power** | **11** (40/339)<br>**3** (37/339)<br>**26** (37/339)<br>**13** (35/339)<br>**22** (34/339) | **T** (22/339)<br>**V** (22/339)<br>**U** (20/339)<br>**K** (18/339)<br>**J** (17/339) |
| **Nlb Jaya** | **5** (142/330)<br>**0** (129/330)<br>**3** (127/330)<br>**2** (127/330)<br>**7** (120/330) | **I** (18/330)<br>**T** (18/330)<br>**G** (18/330)<br>**O** (17/330)<br>**P** (16/330) |
| **Suba Dawasak** | **4** (138/339)<br>**3** (137/339)<br>**1** (129/339)<br>**9** (128/339)<br>**8** (128/339) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (126/1858)<br>**20** (122/1858)<br>**57** (121/1858)<br>**38** (118/1858)<br>**75** (114/1858) | **B** (88/1858)<br>**R** (85/1858)<br>**M** (82/1858)<br>**P** (80/1858)<br>**N** (80/1858) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1746)<br>**10** (147/1746)<br>**6** (144/1746)<br>**29** (144/1746)<br>**21** (143/1746) | **H** (89/1746)<br>**U** (80/1746)<br>**M** (78/1746)<br>**G** (76/1746)<br>**D** (75/1746) |
| **Lagna Wasana** | **5** (142/1865)<br>**23** (141/1865)<br>**39** (138/1865)<br>**36** (138/1865)<br>**28** (138/1865) | N/A |
| **Sasiri** | **9** (80/1043)<br>**22** (78/1043)<br>**20** (77/1043)<br>**26** (77/1043)<br>**19** (74/1043) | N/A |
| **Super Ball** | **52** (112/1859)<br>**9** (112/1859)<br>**45** (112/1859)<br>**29** (112/1859)<br>**62** (110/1859) | **I** (93/1859)<br>**V** (83/1859)<br>**T** (83/1859)<br>**D** (82/1859)<br>**A** (81/1859) |
| **Supiri Dhana Sampatha** | **0** (512/1017)<br>**2** (509/1017)<br>**3** (503/1017)<br>**7** (501/1017)<br>**5** (485/1017) | **V** (54/1017)<br>**K** (47/1017)<br>**S** (47/1017)<br>**T** (47/1017)<br>**G** (46/1017) |

