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

> **Last Updated (Sri Lanka Time):** `2026-07-23 12:10:53 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 279 Rows | 13.39 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 287 Rows | 12.23 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 286 Rows | 12.04 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 286 Rows | 11.75 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 286 Rows | 12.10 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 286 Rows | 12.88 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 277 Rows | 10.75 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 286 Rows | 13.13 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1805 Rows | 69.03 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1693 Rows | 69.17 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1812 Rows | 67.53 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 990 Rows | 32.76 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1806 Rows | 69.07 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 964 Rows | 35.84 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-23 12:10:53 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (103/279)<br>**6** (100/279)<br>**2** (100/279)<br>**3** (97/279)<br>**7** (97/279) | **Q** (17/279)<br>**D** (17/279)<br>**N** (16/279)<br>**J** (16/279)<br>**G** (16/279) |
| **Dhana Nidhanaya** | **7** (26/287)<br>**9** (26/287)<br>**28** (25/287)<br>**4** (23/287)<br>**6** (23/287) | **U** (17/287)<br>**F** (16/287)<br>**T** (15/287)<br>**W** (15/287)<br>**Z** (14/287) |
| **Govisetha** | **55** (23/286)<br>**10** (22/286)<br>**44** (21/286)<br>**33** (21/286)<br>**23** (20/286) | **P** (16/286)<br>**C** (15/286)<br>**K** (14/286)<br>**D** (13/286)<br>**A** (13/286) |
| **Handahana** | **58** (31/286)<br>**11** (27/286)<br>**21** (27/286)<br>**6** (27/286)<br>**55** (26/286) | N/A |
| **Mahajana Sampatha** | **2** (141/286)<br>**5** (140/286)<br>**4** (139/286)<br>**3** (139/286)<br>**7** (139/286) | **Q** (17/286)<br>**D** (17/286)<br>**J** (16/286)<br>**G** (16/286)<br>**N** (15/286) |
| **Mega Power** | **11** (36/286)<br>**3** (32/286)<br>**6** (31/286)<br>**22** (30/286)<br>**19** (30/286) | **T** (20/286)<br>**V** (19/286)<br>**U** (19/286)<br>**K** (17/286)<br>**J** (16/286) |
| **Nlb Jaya** | **5** (123/277)<br>**3** (106/277)<br>**0** (106/277)<br>**2** (105/277)<br>**7** (100/277) | **T** (18/277)<br>**I** (16/277)<br>**G** (16/277)<br>**M** (14/277)<br>**P** (14/277) |
| **Suba Dawasak** | **3** (118/286)<br>**4** (116/286)<br>**1** (110/286)<br>**8** (105/286)<br>**9** (105/286) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (122/1805)<br>**20** (119/1805)<br>**57** (116/1805)<br>**38** (112/1805)<br>**75** (111/1805) | **B** (82/1805)<br>**R** (81/1805)<br>**P** (80/1805)<br>**M** (80/1805)<br>**I** (77/1805) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1693)<br>**10** (145/1693)<br>**6** (139/1693)<br>**29** (139/1693)<br>**15** (139/1693) | **H** (88/1693)<br>**U** (78/1693)<br>**M** (73/1693)<br>**X** (73/1693)<br>**D** (72/1693) |
| **Lagna Wasana** | **5** (139/1812)<br>**28** (136/1812)<br>**36** (135/1812)<br>**25** (135/1812)<br>**23** (133/1812) | N/A |
| **Sasiri** | **9** (74/990)<br>**20** (73/990)<br>**22** (72/990)<br>**26** (71/990)<br>**19** (70/990) | N/A |
| **Super Ball** | **45** (111/1806)<br>**52** (110/1806)<br>**29** (110/1806)<br>**9** (108/1806)<br>**3** (107/1806) | **I** (92/1806)<br>**V** (81/1806)<br>**T** (81/1806)<br>**D** (81/1806)<br>**A** (79/1806) |
| **Supiri Dhana Sampatha** | **2** (485/964)<br>**0** (483/964)<br>**3** (482/964)<br>**7** (476/964)<br>**5** (460/964) | **V** (50/964)<br>**K** (46/964)<br>**S** (44/964)<br>**J** (44/964)<br>**T** (44/964) |

