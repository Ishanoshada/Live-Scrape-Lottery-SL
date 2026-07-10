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

> **Last Updated (Sri Lanka Time):** `2026-07-11 12:28:41 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 267 Rows | 12.84 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 275 Rows | 11.74 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 274 Rows | 11.56 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 274 Rows | 11.28 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 274 Rows | 11.62 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 274 Rows | 12.37 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 265 Rows | 10.29 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 274 Rows | 12.60 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1793 Rows | 68.57 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1681 Rows | 68.67 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1800 Rows | 67.08 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 978 Rows | 32.34 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1794 Rows | 68.61 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 952 Rows | 35.39 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-11 12:28:41 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (98/267)<br>**6** (97/267)<br>**7** (95/267)<br>**2** (95/267)<br>**4** (92/267) | **N** (16/267)<br>**Q** (16/267)<br>**D** (16/267)<br>**J** (15/267)<br>**G** (15/267) |
| **Dhana Nidhanaya** | **9** (26/275)<br>**28** (24/275)<br>**7** (24/275)<br>**4** (23/275)<br>**6** (21/275) | **U** (17/275)<br>**F** (15/275)<br>**W** (15/275)<br>**Z** (14/275)<br>**E** (13/275) |
| **Govisetha** | **55** (23/274)<br>**10** (21/274)<br>**23** (20/274)<br>**29** (20/274)<br>**33** (20/274) | **P** (15/274)<br>**C** (15/274)<br>**D** (13/274)<br>**A** (13/274)<br>**K** (13/274) |
| **Handahana** | **58** (28/274)<br>**11** (27/274)<br>**21** (27/274)<br>**6** (26/274)<br>**55** (25/274) | N/A |
| **Mahajana Sampatha** | **2** (135/274)<br>**4** (134/274)<br>**5** (134/274)<br>**6** (134/274)<br>**7** (133/274) | **Q** (16/274)<br>**D** (16/274)<br>**N** (15/274)<br>**J** (15/274)<br>**G** (15/274) |
| **Mega Power** | **11** (36/274)<br>**6** (31/274)<br>**3** (31/274)<br>**19** (30/274)<br>**22** (29/274) | **V** (19/274)<br>**U** (19/274)<br>**T** (18/274)<br>**J** (16/274)<br>**K** (15/274) |
| **Nlb Jaya** | **5** (118/265)<br>**3** (102/265)<br>**2** (102/265)<br>**0** (102/265)<br>**4** (94/265) | **T** (17/265)<br>**I** (16/265)<br>**G** (16/265)<br>**P** (14/265)<br>**Y** (14/265) |
| **Suba Dawasak** | **4** (113/274)<br>**3** (112/274)<br>**1** (107/274)<br>**5** (99/274)<br>**8** (99/274) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1793)<br>**20** (119/1793)<br>**57** (116/1793)<br>**75** (111/1793)<br>**38** (110/1793) | **B** (82/1793)<br>**R** (81/1793)<br>**P** (79/1793)<br>**M** (79/1793)<br>**I** (77/1793) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1681)<br>**10** (144/1681)<br>**27** (138/1681)<br>**15** (138/1681)<br>**29** (137/1681) | **H** (88/1681)<br>**U** (77/1681)<br>**M** (73/1681)<br>**X** (72/1681)<br>**W** (72/1681) |
| **Lagna Wasana** | **5** (138/1800)<br>**28** (136/1800)<br>**36** (134/1800)<br>**25** (134/1800)<br>**23** (132/1800) | N/A |
| **Sasiri** | **9** (74/978)<br>**20** (72/978)<br>**22** (71/978)<br>**26** (71/978)<br>**5** (69/978) | N/A |
| **Super Ball** | **52** (110/1794)<br>**45** (110/1794)<br>**29** (109/1794)<br>**74** (107/1794)<br>**57** (107/1794) | **I** (90/1794)<br>**T** (81/1794)<br>**D** (81/1794)<br>**V** (80/1794)<br>**A** (79/1794) |
| **Supiri Dhana Sampatha** | **2** (481/952)<br>**0** (477/952)<br>**3** (476/952)<br>**7** (468/952)<br>**5** (453/952) | **V** (49/952)<br>**K** (46/952)<br>**T** (44/952)<br>**S** (43/952)<br>**J** (43/952) |

