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

> **Last Updated (Sri Lanka Time):** `2026-07-28 12:25:43 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 284 Rows | 13.62 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 292 Rows | 12.44 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 291 Rows | 12.24 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 291 Rows | 11.94 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 291 Rows | 12.30 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 291 Rows | 13.09 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 282 Rows | 10.93 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 291 Rows | 13.34 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1810 Rows | 69.22 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1698 Rows | 69.37 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1817 Rows | 67.72 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 995 Rows | 32.93 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1811 Rows | 69.26 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 969 Rows | 36.02 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-28 12:25:43 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (106/284)<br>**2** (102/284)<br>**6** (101/284)<br>**3** (99/284)<br>**7** (98/284) | **D** (19/284)<br>**Q** (17/284)<br>**N** (16/284)<br>**J** (16/284)<br>**G** (16/284) |
| **Dhana Nidhanaya** | **9** (27/292)<br>**7** (26/292)<br>**28** (25/292)<br>**4** (24/292)<br>**6** (23/292) | **U** (19/292)<br>**F** (16/292)<br>**Z** (15/292)<br>**T** (15/292)<br>**W** (15/292) |
| **Govisetha** | **55** (25/291)<br>**10** (22/291)<br>**33** (22/291)<br>**23** (21/291)<br>**44** (21/291) | **P** (16/291)<br>**C** (16/291)<br>**K** (14/291)<br>**D** (13/291)<br>**A** (13/291) |
| **Handahana** | **58** (31/291)<br>**11** (27/291)<br>**21** (27/291)<br>**6** (27/291)<br>**55** (26/291) | N/A |
| **Mahajana Sampatha** | **2** (145/291)<br>**5** (143/291)<br>**4** (142/291)<br>**1** (142/291)<br>**3** (141/291) | **D** (19/291)<br>**Q** (17/291)<br>**J** (16/291)<br>**G** (16/291)<br>**N** (15/291) |
| **Mega Power** | **11** (36/291)<br>**22** (32/291)<br>**6** (32/291)<br>**3** (32/291)<br>**19** (31/291) | **T** (21/291)<br>**V** (20/291)<br>**U** (19/291)<br>**K** (17/291)<br>**J** (16/291) |
| **Nlb Jaya** | **5** (127/282)<br>**0** (108/282)<br>**3** (107/282)<br>**2** (106/282)<br>**1** (102/282) | **T** (18/282)<br>**I** (17/282)<br>**G** (16/282)<br>**M** (14/282)<br>**P** (14/282) |
| **Suba Dawasak** | **3** (119/291)<br>**4** (119/291)<br>**1** (113/291)<br>**8** (107/291)<br>**9** (106/291) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (123/1810)<br>**20** (119/1810)<br>**57** (117/1810)<br>**38** (112/1810)<br>**75** (111/1810) | **R** (83/1810)<br>**B** (82/1810)<br>**P** (80/1810)<br>**M** (80/1810)<br>**I** (77/1810) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (157/1698)<br>**10** (145/1698)<br>**6** (140/1698)<br>**15** (140/1698)<br>**29** (139/1698) | **H** (88/1698)<br>**U** (78/1698)<br>**M** (73/1698)<br>**X** (73/1698)<br>**D** (72/1698) |
| **Lagna Wasana** | **5** (140/1817)<br>**28** (136/1817)<br>**36** (135/1817)<br>**25** (135/1817)<br>**23** (134/1817) | N/A |
| **Sasiri** | **9** (74/995)<br>**22** (73/995)<br>**20** (73/995)<br>**19** (71/995)<br>**26** (71/995) | N/A |
| **Super Ball** | **45** (111/1811)<br>**52** (110/1811)<br>**29** (110/1811)<br>**9** (109/1811)<br>**3** (107/1811) | **I** (92/1811)<br>**D** (82/1811)<br>**V** (81/1811)<br>**T** (81/1811)<br>**A** (79/1811) |
| **Supiri Dhana Sampatha** | **2** (488/969)<br>**0** (487/969)<br>**3** (483/969)<br>**7** (478/969)<br>**5** (463/969) | **V** (50/969)<br>**K** (46/969)<br>**S** (44/969)<br>**J** (44/969)<br>**T** (44/969) |

