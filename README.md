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

> **Last Updated (Sri Lanka Time):** `2026-08-12 11:55:34 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 300 Rows | 14.38 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 308 Rows | 13.12 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 307 Rows | 12.91 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 307 Rows | 12.58 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 307 Rows | 12.97 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 307 Rows | 13.80 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 298 Rows | 11.55 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 307 Rows | 14.07 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1826 Rows | 69.83 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1714 Rows | 70.03 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1833 Rows | 68.31 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1011 Rows | 33.48 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1827 Rows | 69.87 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 985 Rows | 36.62 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-08-12 11:55:34 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (112/300)<br>**2** (108/300)<br>**3** (105/300)<br>**6** (104/300)<br>**7** (104/300) | **D** (19/300)<br>**J** (18/300)<br>**Q** (17/300)<br>**N** (16/300)<br>**G** (16/300) |
| **Dhana Nidhanaya** | **9** (29/308)<br>**4** (27/308)<br>**7** (27/308)<br>**28** (25/308)<br>**80** (24/308) | **U** (20/308)<br>**W** (17/308)<br>**Z** (16/308)<br>**F** (16/308)<br>**M** (16/308) |
| **Govisetha** | **55** (25/307)<br>**44** (24/307)<br>**10** (23/307)<br>**33** (23/307)<br>**23** (22/307) | **C** (17/307)<br>**P** (16/307)<br>**K** (16/307)<br>**X** (16/307)<br>**O** (14/307) |
| **Handahana** | **58** (31/307)<br>**11** (29/307)<br>**21** (28/307)<br>**55** (28/307)<br>**6** (28/307) | N/A |
| **Mahajana Sampatha** | **5** (152/307)<br>**1** (152/307)<br>**7** (151/307)<br>**2** (151/307)<br>**4** (148/307) | **D** (19/307)<br>**J** (18/307)<br>**Q** (17/307)<br>**G** (16/307)<br>**N** (15/307) |
| **Mega Power** | **11** (37/307)<br>**26** (34/307)<br>**13** (34/307)<br>**22** (32/307)<br>**6** (32/307) | **T** (21/307)<br>**V** (20/307)<br>**U** (20/307)<br>**K** (17/307)<br>**J** (16/307) |
| **Nlb Jaya** | **5** (133/298)<br>**0** (116/298)<br>**3** (114/298)<br>**2** (113/298)<br>**7** (108/298) | **I** (18/298)<br>**T** (18/298)<br>**G** (16/298)<br>**P** (15/298)<br>**H** (15/298) |
| **Suba Dawasak** | **3** (127/307)<br>**4** (125/307)<br>**1** (118/307)<br>**8** (114/307)<br>**9** (112/307) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (124/1826)<br>**20** (120/1826)<br>**57** (117/1826)<br>**38** (115/1826)<br>**75** (112/1826) | **B** (85/1826)<br>**R** (83/1826)<br>**P** (80/1826)<br>**M** (80/1826)<br>**N** (78/1826) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (160/1714)<br>**10** (146/1714)<br>**6** (141/1714)<br>**21** (141/1714)<br>**15** (141/1714) | **H** (89/1714)<br>**U** (78/1714)<br>**M** (75/1714)<br>**D** (73/1714)<br>**G** (73/1714) |
| **Lagna Wasana** | **5** (140/1833)<br>**36** (136/1833)<br>**25** (136/1833)<br>**28** (136/1833)<br>**23** (135/1833) | N/A |
| **Sasiri** | **9** (76/1011)<br>**22** (74/1011)<br>**20** (74/1011)<br>**19** (73/1011)<br>**26** (73/1011) | N/A |
| **Super Ball** | **52** (111/1827)<br>**45** (111/1827)<br>**29** (111/1827)<br>**9** (109/1827)<br>**3** (108/1827) | **I** (92/1827)<br>**V** (82/1827)<br>**T** (82/1827)<br>**D** (82/1827)<br>**Y** (79/1827) |
| **Supiri Dhana Sampatha** | **2** (498/985)<br>**0** (493/985)<br>**3** (487/985)<br>**7** (483/985)<br>**5** (472/985) | **V** (53/985)<br>**K** (46/985)<br>**T** (45/985)<br>**S** (44/985)<br>**J** (44/985) |

