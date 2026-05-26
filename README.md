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

> **Last Updated (Sri Lanka Time):** `2026-05-27 12:54:23 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 224 Rows | 10.86 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 232 Rows | 9.97 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 231 Rows | 9.84 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 231 Rows | 9.60 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 231 Rows | 9.89 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 231 Rows | 10.52 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 222 Rows | 8.70 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 231 Rows | 10.71 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1750 Rows | 66.93 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1638 Rows | 66.90 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1757 Rows | 65.48 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 935 Rows | 30.87 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1751 Rows | 66.96 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 909 Rows | 33.79 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-27 12:54:23 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (86/224)<br>**5** (82/224)<br>**2** (81/224)<br>**0** (78/224)<br>**4** (77/224) | **N** (14/224)<br>**D** (14/224)<br>**J** (14/224)<br>**Q** (13/224)<br>**Y** (12/224) |
| **Dhana Nidhanaya** | **28** (22/232)<br>**9** (22/232)<br>**6** (20/232)<br>**7** (18/232)<br>**16** (18/232) | **U** (14/232)<br>**W** (13/232)<br>**Z** (12/232)<br>**T** (12/232)<br>**M** (12/232) |
| **Govisetha** | **44** (19/231)<br>**10** (18/231)<br>**19** (17/231)<br>**58** (17/231)<br>**29** (17/231) | **P** (14/231)<br>**O** (12/231)<br>**D** (11/231)<br>**W** (11/231)<br>**K** (11/231) |
| **Handahana** | **58** (22/231)<br>**61** (22/231)<br>**55** (22/231)<br>**6** (22/231)<br>**21** (21/231) | N/A |
| **Mahajana Sampatha** | **2** (115/231)<br>**1** (115/231)<br>**6** (115/231)<br>**3** (112/231)<br>**5** (112/231) | **D** (14/231)<br>**J** (14/231)<br>**N** (13/231)<br>**Q** (13/231)<br>**Y** (12/231) |
| **Mega Power** | **3** (28/231)<br>**11** (28/231)<br>**6** (26/231)<br>**22** (26/231)<br>**13** (26/231) | **V** (17/231)<br>**T** (14/231)<br>**K** (13/231)<br>**U** (13/231)<br>**J** (12/231) |
| **Nlb Jaya** | **5** (96/222)<br>**0** (89/222)<br>**3** (87/222)<br>**2** (82/222)<br>**4** (79/222) | **P** (14/222)<br>**T** (14/222)<br>**M** (13/222)<br>**I** (13/222)<br>**G** (13/222) |
| **Suba Dawasak** | **3** (97/231)<br>**1** (92/231)<br>**4** (91/231)<br>**9** (86/231)<br>**5** (85/231) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1750)<br>**57** (115/1750)<br>**20** (114/1750)<br>**13** (109/1750)<br>**38** (107/1750) | **B** (82/1750)<br>**R** (78/1750)<br>**P** (78/1750)<br>**M** (78/1750)<br>**I** (75/1750) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1638)<br>**10** (142/1638)<br>**29** (134/1638)<br>**21** (133/1638)<br>**38** (133/1638) | **H** (88/1638)<br>**U** (75/1638)<br>**W** (72/1638)<br>**G** (70/1638)<br>**X** (70/1638) |
| **Lagna Wasana** | **5** (135/1757)<br>**28** (133/1757)<br>**36** (130/1757)<br>**23** (130/1757)<br>**25** (130/1757) | N/A |
| **Sasiri** | **9** (70/935)<br>**20** (70/935)<br>**22** (68/935)<br>**26** (68/935)<br>**19** (67/935) | N/A |
| **Super Ball** | **45** (109/1751)<br>**74** (106/1751)<br>**29** (106/1751)<br>**52** (105/1751)<br>**3** (105/1751) | **I** (87/1751)<br>**D** (80/1751)<br>**T** (79/1751)<br>**V** (77/1751)<br>**A** (77/1751) |
| **Supiri Dhana Sampatha** | **0** (460/909)<br>**2** (458/909)<br>**3** (454/909)<br>**7** (449/909)<br>**5** (436/909) | **K** (44/909)<br>**V** (44/909)<br>**T** (43/909)<br>**S** (42/909)<br>**J** (42/909) |

