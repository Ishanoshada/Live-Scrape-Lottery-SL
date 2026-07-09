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

> **Last Updated (Sri Lanka Time):** `2026-07-10 12:37:35 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 266 Rows | 12.80 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 274 Rows | 11.70 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 273 Rows | 11.52 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 273 Rows | 11.24 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 273 Rows | 11.58 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 273 Rows | 12.32 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 264 Rows | 10.26 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 273 Rows | 12.56 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1792 Rows | 68.54 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1680 Rows | 68.63 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1799 Rows | 67.05 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 977 Rows | 32.31 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1793 Rows | 68.57 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 951 Rows | 35.35 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-10 12:37:35 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (98/266)<br>**6** (97/266)<br>**2** (95/266)<br>**7** (94/266)<br>**3** (91/266) | **N** (16/266)<br>**Q** (16/266)<br>**D** (16/266)<br>**J** (15/266)<br>**G** (15/266) |
| **Dhana Nidhanaya** | **9** (26/274)<br>**28** (24/274)<br>**7** (24/274)<br>**4** (23/274)<br>**6** (21/274) | **U** (17/274)<br>**F** (15/274)<br>**W** (15/274)<br>**Z** (14/274)<br>**E** (13/274) |
| **Govisetha** | **55** (23/273)<br>**10** (21/273)<br>**23** (20/273)<br>**29** (20/273)<br>**33** (20/273) | **P** (15/273)<br>**C** (15/273)<br>**D** (13/273)<br>**A** (13/273)<br>**K** (13/273) |
| **Handahana** | **58** (28/273)<br>**11** (27/273)<br>**21** (27/273)<br>**6** (26/273)<br>**55** (25/273) | N/A |
| **Mahajana Sampatha** | **5** (134/273)<br>**2** (134/273)<br>**6** (134/273)<br>**4** (133/273)<br>**1** (133/273) | **Q** (16/273)<br>**D** (16/273)<br>**N** (15/273)<br>**J** (15/273)<br>**G** (15/273) |
| **Mega Power** | **11** (36/273)<br>**6** (31/273)<br>**3** (31/273)<br>**19** (30/273)<br>**22** (29/273) | **V** (19/273)<br>**U** (19/273)<br>**T** (18/273)<br>**J** (16/273)<br>**K** (15/273) |
| **Nlb Jaya** | **5** (118/264)<br>**0** (102/264)<br>**3** (101/264)<br>**2** (101/264)<br>**7** (94/264) | **T** (17/264)<br>**I** (16/264)<br>**G** (16/264)<br>**P** (14/264)<br>**Y** (14/264) |
| **Suba Dawasak** | **4** (113/273)<br>**3** (112/273)<br>**1** (107/273)<br>**5** (98/273)<br>**8** (98/273) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1792)<br>**20** (119/1792)<br>**57** (116/1792)<br>**75** (111/1792)<br>**38** (110/1792) | **B** (82/1792)<br>**R** (81/1792)<br>**P** (79/1792)<br>**M** (79/1792)<br>**I** (77/1792) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1680)<br>**10** (144/1680)<br>**27** (138/1680)<br>**29** (137/1680)<br>**15** (137/1680) | **H** (88/1680)<br>**U** (77/1680)<br>**M** (73/1680)<br>**X** (72/1680)<br>**W** (72/1680) |
| **Lagna Wasana** | **5** (137/1799)<br>**28** (136/1799)<br>**36** (134/1799)<br>**25** (134/1799)<br>**23** (132/1799) | N/A |
| **Sasiri** | **9** (73/977)<br>**20** (72/977)<br>**22** (71/977)<br>**26** (71/977)<br>**5** (69/977) | N/A |
| **Super Ball** | **52** (110/1793)<br>**45** (110/1793)<br>**29** (109/1793)<br>**74** (107/1793)<br>**43** (107/1793) | **I** (90/1793)<br>**T** (81/1793)<br>**D** (81/1793)<br>**V** (80/1793)<br>**A** (79/1793) |
| **Supiri Dhana Sampatha** | **2** (481/951)<br>**0** (476/951)<br>**3** (476/951)<br>**7** (468/951)<br>**5** (452/951) | **V** (49/951)<br>**K** (46/951)<br>**T** (44/951)<br>**S** (43/951)<br>**J** (43/951) |

