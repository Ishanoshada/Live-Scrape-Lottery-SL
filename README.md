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

> **Last Updated (Sri Lanka Time):** `2026-07-05 12:01:17 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 261 Rows | 12.57 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 269 Rows | 11.49 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 268 Rows | 11.32 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 268 Rows | 11.04 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 268 Rows | 11.38 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 268 Rows | 12.11 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 259 Rows | 10.07 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 268 Rows | 12.34 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1787 Rows | 68.34 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1675 Rows | 68.43 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1794 Rows | 66.86 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 972 Rows | 32.14 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1788 Rows | 68.38 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 946 Rows | 35.17 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-05 12:01:17 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (96/261)<br>**6** (96/261)<br>**2** (94/261)<br>**7** (93/261)<br>**0** (90/261) | **N** (16/261)<br>**Q** (15/261)<br>**D** (15/261)<br>**J** (15/261)<br>**G** (15/261) |
| **Dhana Nidhanaya** | **9** (25/269)<br>**28** (24/269)<br>**7** (24/269)<br>**4** (22/269)<br>**6** (21/269) | **U** (17/269)<br>**F** (15/269)<br>**W** (14/269)<br>**Z** (13/269)<br>**E** (13/269) |
| **Govisetha** | **55** (22/268)<br>**10** (21/268)<br>**23** (20/268)<br>**29** (20/268)<br>**19** (19/268) | **P** (15/268)<br>**C** (14/268)<br>**D** (13/268)<br>**A** (13/268)<br>**O** (12/268) |
| **Handahana** | **58** (27/268)<br>**21** (27/268)<br>**11** (26/268)<br>**6** (26/268)<br>**55** (24/268) | N/A |
| **Mahajana Sampatha** | **2** (133/268)<br>**5** (131/268)<br>**7** (131/268)<br>**1** (131/268)<br>**6** (131/268) | **N** (15/268)<br>**Q** (15/268)<br>**D** (15/268)<br>**J** (15/268)<br>**G** (15/268) |
| **Mega Power** | **11** (36/268)<br>**3** (31/268)<br>**6** (30/268)<br>**19** (30/268)<br>**13** (29/268) | **V** (19/268)<br>**T** (18/268)<br>**U** (18/268)<br>**K** (15/268)<br>**J** (15/268) |
| **Nlb Jaya** | **5** (117/259)<br>**0** (100/259)<br>**3** (99/259)<br>**2** (99/259)<br>**7** (92/259) | **I** (16/259)<br>**T** (16/259)<br>**G** (16/259)<br>**P** (14/259)<br>**Y** (14/259) |
| **Suba Dawasak** | **3** (111/268)<br>**4** (109/268)<br>**1** (106/268)<br>**9** (97/268)<br>**5** (96/268) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1787)<br>**20** (119/1787)<br>**57** (116/1787)<br>**75** (110/1787)<br>**38** (110/1787) | **B** (82/1787)<br>**R** (81/1787)<br>**P** (79/1787)<br>**M** (79/1787)<br>**I** (77/1787) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1675)<br>**10** (143/1675)<br>**27** (138/1675)<br>**29** (137/1675)<br>**15** (137/1675) | **H** (88/1675)<br>**U** (77/1675)<br>**M** (73/1675)<br>**X** (72/1675)<br>**W** (72/1675) |
| **Lagna Wasana** | **5** (137/1794)<br>**28** (136/1794)<br>**36** (134/1794)<br>**23** (132/1794)<br>**25** (132/1794) | N/A |
| **Sasiri** | **9** (73/972)<br>**22** (71/972)<br>**20** (71/972)<br>**26** (71/972)<br>**5** (69/972) | N/A |
| **Super Ball** | **52** (110/1788)<br>**45** (110/1788)<br>**29** (109/1788)<br>**74** (107/1788)<br>**3** (106/1788) | **I** (90/1788)<br>**D** (81/1788)<br>**V** (80/1788)<br>**T** (80/1788)<br>**A** (79/1788) |
| **Supiri Dhana Sampatha** | **2** (477/946)<br>**3** (474/946)<br>**0** (474/946)<br>**7** (465/946)<br>**5** (451/946) | **V** (47/946)<br>**K** (46/946)<br>**S** (43/946)<br>**J** (43/946)<br>**M** (43/946) |

