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

> **Last Updated (Sri Lanka Time):** `2026-05-22 10:33:16 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 220 Rows | 10.68 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 228 Rows | 9.81 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 227 Rows | 9.68 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 227 Rows | 9.45 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 227 Rows | 9.74 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 227 Rows | 10.35 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 218 Rows | 8.55 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 227 Rows | 10.54 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1746 Rows | 66.78 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1634 Rows | 66.74 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1753 Rows | 65.33 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 931 Rows | 30.73 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1747 Rows | 66.81 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 905 Rows | 33.64 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-22 10:33:16 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (86/220)<br>**5** (82/220)<br>**2** (80/220)<br>**0** (77/220)<br>**4** (76/220) | **N** (14/220)<br>**D** (14/220)<br>**J** (14/220)<br>**Q** (13/220)<br>**Y** (12/220) |
| **Dhana Nidhanaya** | **28** (22/228)<br>**9** (21/228)<br>**6** (19/228)<br>**7** (18/228)<br>**16** (18/228) | **U** (14/228)<br>**W** (13/228)<br>**Z** (12/228)<br>**T** (12/228)<br>**M** (12/228) |
| **Govisetha** | **44** (19/227)<br>**19** (17/227)<br>**55** (17/227)<br>**10** (16/227)<br>**23** (16/227) | **P** (13/227)<br>**D** (11/227)<br>**W** (11/227)<br>**O** (11/227)<br>**K** (11/227) |
| **Handahana** | **58** (22/227)<br>**61** (22/227)<br>**6** (22/227)<br>**21** (21/227)<br>**46** (21/227) | N/A |
| **Mahajana Sampatha** | **6** (114/227)<br>**2** (113/227)<br>**5** (111/227)<br>**1** (111/227)<br>**3** (110/227) | **D** (14/227)<br>**J** (14/227)<br>**N** (13/227)<br>**Q** (13/227)<br>**Y** (12/227) |
| **Mega Power** | **3** (27/227)<br>**11** (27/227)<br>**6** (26/227)<br>**13** (26/227)<br>**22** (25/227) | **V** (17/227)<br>**T** (13/227)<br>**K** (13/227)<br>**U** (13/227)<br>**J** (12/227) |
| **Nlb Jaya** | **5** (94/218)<br>**3** (87/218)<br>**0** (85/218)<br>**2** (81/218)<br>**1** (78/218) | **P** (14/218)<br>**T** (14/218)<br>**M** (13/218)<br>**I** (13/218)<br>**G** (13/218) |
| **Suba Dawasak** | **3** (95/227)<br>**1** (91/227)<br>**4** (90/227)<br>**9** (85/227)<br>**5** (83/227) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1746)<br>**57** (115/1746)<br>**20** (113/1746)<br>**13** (109/1746)<br>**38** (107/1746) | **B** (82/1746)<br>**R** (78/1746)<br>**P** (78/1746)<br>**M** (78/1746)<br>**I** (75/1746) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1634)<br>**10** (142/1634)<br>**29** (134/1634)<br>**21** (133/1634)<br>**22** (132/1634) | **H** (88/1634)<br>**U** (75/1634)<br>**W** (72/1634)<br>**G** (70/1634)<br>**X** (70/1634) |
| **Lagna Wasana** | **5** (135/1753)<br>**28** (133/1753)<br>**36** (130/1753)<br>**25** (130/1753)<br>**23** (129/1753) | N/A |
| **Sasiri** | **9** (70/931)<br>**20** (70/931)<br>**22** (68/931)<br>**26** (68/931)<br>**19** (67/931) | N/A |
| **Super Ball** | **45** (109/1747)<br>**52** (105/1747)<br>**3** (105/1747)<br>**74** (105/1747)<br>**29** (105/1747) | **I** (87/1747)<br>**D** (80/1747)<br>**T** (78/1747)<br>**V** (77/1747)<br>**A** (77/1747) |
| **Supiri Dhana Sampatha** | **2** (458/905)<br>**0** (458/905)<br>**3** (452/905)<br>**7** (447/905)<br>**5** (433/905) | **K** (44/905)<br>**V** (44/905)<br>**T** (43/905)<br>**J** (42/905)<br>**C** (42/905) |

