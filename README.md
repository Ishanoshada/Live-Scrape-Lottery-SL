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

> **Last Updated (Sri Lanka Time):** `2026-07-14 12:25:34 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 270 Rows | 12.98 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 278 Rows | 11.86 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 277 Rows | 11.68 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 277 Rows | 11.39 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 277 Rows | 11.74 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 277 Rows | 12.49 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 268 Rows | 10.41 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 277 Rows | 12.73 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1796 Rows | 68.69 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1684 Rows | 68.80 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1803 Rows | 67.19 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 981 Rows | 32.45 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1797 Rows | 68.72 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 955 Rows | 35.50 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-14 12:25:34 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (99/270)<br>**6** (98/270)<br>**2** (96/270)<br>**7** (95/270)<br>**4** (94/270) | **Q** (17/270)<br>**N** (16/270)<br>**D** (16/270)<br>**J** (16/270)<br>**G** (15/270) |
| **Dhana Nidhanaya** | **9** (26/278)<br>**28** (24/278)<br>**7** (24/278)<br>**4** (23/278)<br>**6** (23/278) | **U** (17/278)<br>**F** (15/278)<br>**W** (15/278)<br>**Z** (14/278)<br>**E** (13/278) |
| **Govisetha** | **55** (23/277)<br>**10** (21/277)<br>**23** (20/277)<br>**44** (20/277)<br>**29** (20/277) | **P** (16/277)<br>**C** (15/277)<br>**K** (14/277)<br>**D** (13/277)<br>**A** (13/277) |
| **Handahana** | **58** (29/277)<br>**11** (27/277)<br>**21** (27/277)<br>**6** (26/277)<br>**55** (25/277) | N/A |
| **Mahajana Sampatha** | **2** (137/277)<br>**4** (136/277)<br>**6** (136/277)<br>**5** (135/277)<br>**7** (134/277) | **Q** (17/277)<br>**D** (16/277)<br>**J** (16/277)<br>**N** (15/277)<br>**G** (15/277) |
| **Mega Power** | **11** (36/277)<br>**6** (31/277)<br>**3** (31/277)<br>**22** (30/277)<br>**19** (30/277) | **V** (19/277)<br>**U** (19/277)<br>**T** (18/277)<br>**J** (16/277)<br>**K** (15/277) |
| **Nlb Jaya** | **5** (120/268)<br>**2** (103/268)<br>**3** (102/268)<br>**0** (102/268)<br>**7** (97/268) | **T** (17/268)<br>**I** (16/268)<br>**G** (16/268)<br>**M** (14/268)<br>**P** (14/268) |
| **Suba Dawasak** | **3** (113/277)<br>**4** (113/277)<br>**1** (108/277)<br>**8** (102/277)<br>**5** (100/277) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (121/1796)<br>**20** (119/1796)<br>**57** (116/1796)<br>**75** (111/1796)<br>**38** (111/1796) | **B** (82/1796)<br>**R** (81/1796)<br>**P** (80/1796)<br>**M** (79/1796)<br>**I** (77/1796) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1684)<br>**10** (144/1684)<br>**29** (138/1684)<br>**27** (138/1684)<br>**15** (138/1684) | **H** (88/1684)<br>**U** (77/1684)<br>**M** (73/1684)<br>**X** (72/1684)<br>**W** (72/1684) |
| **Lagna Wasana** | **5** (139/1803)<br>**28** (136/1803)<br>**36** (134/1803)<br>**25** (134/1803)<br>**39** (132/1803) | N/A |
| **Sasiri** | **9** (74/981)<br>**20** (73/981)<br>**22** (71/981)<br>**26** (71/981)<br>**5** (69/981) | N/A |
| **Super Ball** | **52** (110/1797)<br>**45** (110/1797)<br>**29** (110/1797)<br>**74** (107/1797)<br>**57** (107/1797) | **I** (90/1797)<br>**V** (81/1797)<br>**T** (81/1797)<br>**D** (81/1797)<br>**A** (79/1797) |
| **Supiri Dhana Sampatha** | **2** (483/955)<br>**0** (478/955)<br>**3** (478/955)<br>**7** (470/955)<br>**5** (454/955) | **V** (49/955)<br>**K** (46/955)<br>**S** (44/955)<br>**T** (44/955)<br>**J** (43/955) |

