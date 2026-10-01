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

> **Last Updated (Sri Lanka Time):** `2026-10-02 03:25:06 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 350 Rows | 16.87 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 358 Rows | 15.34 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 357 Rows | 15.10 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 357 Rows | 14.72 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 357 Rows | 15.17 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 357 Rows | 16.13 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 348 Rows | 13.58 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 357 Rows | 16.46 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1876 Rows | 71.75 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1764 Rows | 72.09 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1883 Rows | 70.18 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1061 Rows | 35.19 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1877 Rows | 71.78 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1035 Rows | 38.52 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-02 03:25:06 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (128/350)<br>**2** (126/350)<br>**6** (122/350)<br>**3** (121/350)<br>**4** (120/350) | **D** (22/350)<br>**Q** (20/350)<br>**J** (20/350)<br>**G** (20/350)<br>**N** (18/350) |
| **Dhana Nidhanaya** | **9** (32/358)<br>**4** (30/358)<br>**7** (29/358)<br>**3** (27/358)<br>**80** (26/358) | **U** (20/358)<br>**W** (20/358)<br>**M** (19/358)<br>**Z** (18/358)<br>**F** (18/358) |
| **Govisetha** | **55** (28/357)<br>**10** (27/357)<br>**44** (26/357)<br>**33** (25/357)<br>**29** (24/357) | **P** (19/357)<br>**I** (18/357)<br>**C** (18/357)<br>**X** (17/357)<br>**D** (16/357) |
| **Handahana** | **58** (32/357)<br>**11** (31/357)<br>**55** (31/357)<br>**60** (30/357)<br>**21** (30/357) | N/A |
| **Mahajana Sampatha** | **1** (178/357)<br>**5** (177/357)<br>**2** (174/357)<br>**3** (173/357)<br>**9** (172/357) | **D** (22/357)<br>**Q** (20/357)<br>**J** (20/357)<br>**G** (20/357)<br>**W** (19/357) |
| **Mega Power** | **13** (41/357)<br>**26** (40/357)<br>**11** (40/357)<br>**3** (38/357)<br>**22** (37/357) | **V** (23/357)<br>**U** (23/357)<br>**T** (22/357)<br>**K** (19/357)<br>**J** (17/357) |
| **Nlb Jaya** | **5** (145/348)<br>**0** (133/348)<br>**3** (131/348)<br>**2** (130/348)<br>**7** (129/348) | **T** (21/348)<br>**I** (19/348)<br>**G** (19/348)<br>**P** (17/348)<br>**Y** (17/348) |
| **Suba Dawasak** | **4** (146/357)<br>**3** (142/357)<br>**9** (137/357)<br>**1** (136/357)<br>**2** (136/357) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1876)<br>**20** (122/1876)<br>**57** (122/1876)<br>**38** (118/1876)<br>**13** (115/1876) | **B** (88/1876)<br>**R** (85/1876)<br>**M** (84/1876)<br>**N** (82/1876)<br>**P** (81/1876) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1764)<br>**10** (149/1764)<br>**21** (148/1764)<br>**6** (145/1764)<br>**15** (145/1764) | **H** (89/1764)<br>**U** (81/1764)<br>**M** (79/1764)<br>**G** (76/1764)<br>**D** (75/1764) |
| **Lagna Wasana** | **5** (143/1883)<br>**23** (142/1883)<br>**39** (139/1883)<br>**36** (139/1883)<br>**25** (139/1883) | N/A |
| **Sasiri** | **9** (82/1061)<br>**20** (80/1061)<br>**22** (78/1061)<br>**26** (78/1061)<br>**21** (78/1061) | N/A |
| **Super Ball** | **45** (113/1877)<br>**52** (112/1877)<br>**9** (112/1877)<br>**29** (112/1877)<br>**74** (111/1877) | **I** (93/1877)<br>**T** (85/1877)<br>**V** (84/1877)<br>**D** (82/1877)<br>**A** (82/1877) |
| **Supiri Dhana Sampatha** | **0** (522/1035)<br>**2** (515/1035)<br>**7** (511/1035)<br>**3** (511/1035)<br>**8** (495/1035) | **V** (56/1035)<br>**K** (50/1035)<br>**T** (49/1035)<br>**S** (48/1035)<br>**G** (46/1035) |

