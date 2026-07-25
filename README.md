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

> **Last Updated (Sri Lanka Time):** `2026-07-25 11:56:29 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 282 Rows | 13.53 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 290 Rows | 12.35 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 289 Rows | 12.16 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 289 Rows | 11.86 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 289 Rows | 12.22 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 289 Rows | 13.00 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 280 Rows | 10.86 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 289 Rows | 13.26 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1808 Rows | 69.15 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1696 Rows | 69.29 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1815 Rows | 67.64 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 993 Rows | 32.86 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1809 Rows | 69.18 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 967 Rows | 35.95 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-25 11:56:29 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (105/282)<br>**2** (102/282)<br>**6** (100/282)<br>**7** (98/282)<br>**3** (97/282) | **D** (18/282)<br>**Q** (17/282)<br>**N** (16/282)<br>**J** (16/282)<br>**G** (16/282) |
| **Dhana Nidhanaya** | **7** (26/290)<br>**9** (26/290)<br>**28** (25/290)<br>**4** (24/290)<br>**6** (23/290) | **U** (18/290)<br>**F** (16/290)<br>**T** (15/290)<br>**W** (15/290)<br>**Z** (14/290) |
| **Govisetha** | **55** (24/289)<br>**10** (22/289)<br>**33** (22/289)<br>**23** (21/289)<br>**44** (21/289) | **P** (16/289)<br>**C** (15/289)<br>**K** (14/289)<br>**D** (13/289)<br>**A** (13/289) |
| **Handahana** | **58** (31/289)<br>**11** (27/289)<br>**21** (27/289)<br>**6** (27/289)<br>**55** (26/289) | N/A |
| **Mahajana Sampatha** | **2** (144/289)<br>**5** (142/289)<br>**1** (141/289)<br>**4** (140/289)<br>**7** (140/289) | **D** (18/289)<br>**Q** (17/289)<br>**J** (16/289)<br>**G** (16/289)<br>**N** (15/289) |
| **Mega Power** | **11** (36/289)<br>**6** (32/289)<br>**22** (32/289)<br>**3** (32/289)<br>**13** (31/289) | **T** (21/289)<br>**V** (20/289)<br>**U** (19/289)<br>**K** (17/289)<br>**J** (16/289) |
| **Nlb Jaya** | **5** (126/280)<br>**3** (107/280)<br>**2** (106/280)<br>**0** (106/280)<br>**1** (101/280) | **T** (18/280)<br>**I** (16/280)<br>**G** (16/280)<br>**M** (14/280)<br>**P** (14/280) |
| **Suba Dawasak** | **3** (119/289)<br>**4** (118/289)<br>**1** (111/289)<br>**8** (106/289)<br>**9** (106/289) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (122/1808)<br>**20** (119/1808)<br>**57** (117/1808)<br>**38** (112/1808)<br>**75** (111/1808) | **R** (82/1808)<br>**B** (82/1808)<br>**P** (80/1808)<br>**M** (80/1808)<br>**I** (77/1808) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1696)<br>**10** (145/1696)<br>**15** (140/1696)<br>**6** (139/1696)<br>**29** (139/1696) | **H** (88/1696)<br>**U** (78/1696)<br>**M** (73/1696)<br>**X** (73/1696)<br>**D** (72/1696) |
| **Lagna Wasana** | **5** (139/1815)<br>**28** (136/1815)<br>**36** (135/1815)<br>**25** (135/1815)<br>**23** (133/1815) | N/A |
| **Sasiri** | **9** (74/993)<br>**22** (73/993)<br>**20** (73/993)<br>**19** (71/993)<br>**26** (71/993) | N/A |
| **Super Ball** | **45** (111/1809)<br>**52** (110/1809)<br>**29** (110/1809)<br>**9** (108/1809)<br>**3** (107/1809) | **I** (92/1809)<br>**D** (82/1809)<br>**V** (81/1809)<br>**T** (81/1809)<br>**A** (79/1809) |
| **Supiri Dhana Sampatha** | **2** (487/967)<br>**0** (485/967)<br>**3** (483/967)<br>**7** (477/967)<br>**5** (462/967) | **V** (50/967)<br>**K** (46/967)<br>**S** (44/967)<br>**J** (44/967)<br>**T** (44/967) |

