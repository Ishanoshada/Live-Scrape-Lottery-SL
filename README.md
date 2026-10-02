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

> **Last Updated (Sri Lanka Time):** `2026-10-03 02:54:34 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 351 Rows | 16.92 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 359 Rows | 15.38 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 358 Rows | 15.15 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 358 Rows | 14.76 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 358 Rows | 15.21 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 358 Rows | 16.18 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 349 Rows | 13.62 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 358 Rows | 16.49 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1877 Rows | 71.78 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1765 Rows | 72.13 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1884 Rows | 70.21 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1062 Rows | 35.23 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1878 Rows | 71.82 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1036 Rows | 38.55 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-03 02:54:34 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (128/351)<br>**2** (126/351)<br>**6** (123/351)<br>**3** (122/351)<br>**4** (121/351) | **D** (22/351)<br>**Q** (20/351)<br>**J** (20/351)<br>**G** (20/351)<br>**N** (19/351) |
| **Dhana Nidhanaya** | **9** (32/359)<br>**4** (30/359)<br>**7** (29/359)<br>**3** (27/359)<br>**80** (26/359) | **U** (20/359)<br>**W** (20/359)<br>**M** (19/359)<br>**Z** (18/359)<br>**F** (18/359) |
| **Govisetha** | **55** (28/358)<br>**10** (27/358)<br>**44** (26/358)<br>**33** (25/358)<br>**29** (24/358) | **P** (20/358)<br>**I** (18/358)<br>**C** (18/358)<br>**X** (17/358)<br>**D** (16/358) |
| **Handahana** | **58** (32/358)<br>**60** (31/358)<br>**11** (31/358)<br>**55** (31/358)<br>**21** (30/358) | N/A |
| **Mahajana Sampatha** | **1** (178/358)<br>**5** (177/358)<br>**2** (175/358)<br>**3** (174/358)<br>**4** (172/358) | **D** (22/358)<br>**Q** (20/358)<br>**J** (20/358)<br>**G** (20/358)<br>**W** (19/358) |
| **Mega Power** | **13** (41/358)<br>**26** (40/358)<br>**11** (40/358)<br>**3** (38/358)<br>**22** (37/358) | **V** (23/358)<br>**U** (23/358)<br>**T** (22/358)<br>**K** (19/358)<br>**J** (17/358) |
| **Nlb Jaya** | **5** (145/349)<br>**0** (133/349)<br>**3** (132/349)<br>**2** (131/349)<br>**7** (129/349) | **T** (21/349)<br>**I** (19/349)<br>**G** (19/349)<br>**P** (17/349)<br>**Y** (17/349) |
| **Suba Dawasak** | **4** (146/358)<br>**3** (142/358)<br>**9** (137/358)<br>**1** (136/358)<br>**2** (136/358) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1877)<br>**20** (122/1877)<br>**57** (122/1877)<br>**38** (118/1877)<br>**13** (115/1877) | **B** (88/1877)<br>**R** (85/1877)<br>**M** (84/1877)<br>**N** (82/1877)<br>**P** (81/1877) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1765)<br>**10** (149/1765)<br>**21** (148/1765)<br>**6** (145/1765)<br>**15** (145/1765) | **H** (89/1765)<br>**U** (81/1765)<br>**M** (79/1765)<br>**G** (76/1765)<br>**D** (75/1765) |
| **Lagna Wasana** | **5** (144/1884)<br>**23** (142/1884)<br>**39** (139/1884)<br>**36** (139/1884)<br>**25** (139/1884) | N/A |
| **Sasiri** | **9** (82/1062)<br>**20** (80/1062)<br>**22** (78/1062)<br>**26** (78/1062)<br>**21** (78/1062) | N/A |
| **Super Ball** | **45** (113/1878)<br>**52** (112/1878)<br>**9** (112/1878)<br>**29** (112/1878)<br>**74** (111/1878) | **I** (93/1878)<br>**T** (85/1878)<br>**V** (84/1878)<br>**D** (82/1878)<br>**A** (82/1878) |
| **Supiri Dhana Sampatha** | **0** (522/1036)<br>**2** (516/1036)<br>**7** (512/1036)<br>**3** (512/1036)<br>**8** (495/1036) | **V** (56/1036)<br>**K** (50/1036)<br>**T** (49/1036)<br>**S** (48/1036)<br>**G** (46/1036) |

