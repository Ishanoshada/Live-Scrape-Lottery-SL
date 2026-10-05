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

> **Last Updated (Sri Lanka Time):** `2026-10-06 04:46:23 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 354 Rows | 17.07 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 362 Rows | 15.51 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 361 Rows | 15.27 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 361 Rows | 14.89 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 361 Rows | 15.34 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 361 Rows | 16.31 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 352 Rows | 13.74 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 361 Rows | 16.61 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1880 Rows | 71.90 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1768 Rows | 72.25 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1887 Rows | 70.32 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1065 Rows | 35.33 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1881 Rows | 71.93 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1039 Rows | 38.67 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-06 04:46:23 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (128/354)<br>**2** (128/354)<br>**3** (124/354)<br>**4** (124/354)<br>**6** (123/354) | **D** (22/354)<br>**Q** (21/354)<br>**N** (20/354)<br>**J** (20/354)<br>**G** (20/354) |
| **Dhana Nidhanaya** | **9** (32/362)<br>**4** (30/362)<br>**7** (29/362)<br>**3** (27/362)<br>**80** (26/362) | **U** (20/362)<br>**W** (20/362)<br>**Z** (19/362)<br>**M** (19/362)<br>**F** (18/362) |
| **Govisetha** | **55** (28/361)<br>**10** (27/361)<br>**44** (26/361)<br>**14** (25/361)<br>**33** (25/361) | **P** (20/361)<br>**I** (18/361)<br>**C** (18/361)<br>**W** (17/361)<br>**Y** (17/361) |
| **Handahana** | **58** (32/361)<br>**60** (31/361)<br>**11** (31/361)<br>**55** (31/361)<br>**21** (30/361) | N/A |
| **Mahajana Sampatha** | **5** (178/361)<br>**1** (178/361)<br>**2** (177/361)<br>**3** (176/361)<br>**4** (175/361) | **D** (22/361)<br>**Q** (21/361)<br>**J** (20/361)<br>**G** (20/361)<br>**N** (19/361) |
| **Mega Power** | **13** (42/361)<br>**26** (40/361)<br>**11** (40/361)<br>**3** (38/361)<br>**22** (37/361) | **V** (23/361)<br>**U** (23/361)<br>**T** (22/361)<br>**K** (19/361)<br>**S** (18/361) |
| **Nlb Jaya** | **5** (147/352)<br>**0** (135/352)<br>**3** (133/352)<br>**2** (132/352)<br>**7** (129/352) | **T** (21/352)<br>**I** (19/352)<br>**G** (19/352)<br>**P** (17/352)<br>**Y** (17/352) |
| **Suba Dawasak** | **4** (146/361)<br>**3** (142/361)<br>**9** (137/361)<br>**1** (136/361)<br>**2** (136/361) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1880)<br>**20** (123/1880)<br>**57** (122/1880)<br>**38** (118/1880)<br>**13** (116/1880) | **B** (88/1880)<br>**R** (85/1880)<br>**M** (84/1880)<br>**N** (82/1880)<br>**P** (81/1880) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1768)<br>**21** (149/1768)<br>**10** (149/1768)<br>**6** (145/1768)<br>**15** (145/1768) | **H** (89/1768)<br>**U** (81/1768)<br>**M** (79/1768)<br>**G** (76/1768)<br>**D** (75/1768) |
| **Lagna Wasana** | **5** (144/1887)<br>**23** (142/1887)<br>**39** (140/1887)<br>**36** (139/1887)<br>**25** (139/1887) | N/A |
| **Sasiri** | **9** (83/1065)<br>**20** (80/1065)<br>**22** (78/1065)<br>**26** (78/1065)<br>**21** (78/1065) | N/A |
| **Super Ball** | **45** (114/1881)<br>**9** (113/1881)<br>**52** (112/1881)<br>**29** (112/1881)<br>**74** (111/1881) | **I** (93/1881)<br>**T** (85/1881)<br>**V** (84/1881)<br>**D** (82/1881)<br>**A** (82/1881) |
| **Supiri Dhana Sampatha** | **0** (523/1039)<br>**2** (519/1039)<br>**3** (514/1039)<br>**7** (513/1039)<br>**8** (495/1039) | **V** (56/1039)<br>**K** (50/1039)<br>**T** (49/1039)<br>**S** (48/1039)<br>**G** (47/1039) |

