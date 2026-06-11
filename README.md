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

> **Last Updated (Sri Lanka Time):** `2026-06-12 01:28:19 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 238 Rows | 11.51 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 246 Rows | 10.54 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 245 Rows | 10.40 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 245 Rows | 10.14 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 245 Rows | 10.46 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 245 Rows | 11.12 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 236 Rows | 9.21 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 245 Rows | 11.32 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1764 Rows | 67.47 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1652 Rows | 67.48 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1771 Rows | 66.00 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 949 Rows | 31.35 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1765 Rows | 67.50 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 923 Rows | 34.31 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-12 01:28:19 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (90/238)<br>**5** (89/238)<br>**0** (85/238)<br>**7** (84/238)<br>**2** (82/238) | **J** (15/238)<br>**N** (14/238)<br>**D** (14/238)<br>**Q** (13/238)<br>**Y** (12/238) |
| **Dhana Nidhanaya** | **28** (24/246)<br>**9** (23/246)<br>**6** (21/246)<br>**16** (20/246)<br>**7** (19/246) | **U** (15/246)<br>**W** (13/246)<br>**Z** (12/246)<br>**T** (12/246)<br>**M** (12/246) |
| **Govisetha** | **10** (20/245)<br>**55** (20/245)<br>**44** (19/245)<br>**33** (19/245)<br>**19** (17/245) | **P** (15/245)<br>**C** (13/245)<br>**D** (12/245)<br>**O** (12/245)<br>**M** (12/245) |
| **Handahana** | **6** (25/245)<br>**21** (24/245)<br>**55** (23/245)<br>**58** (22/245)<br>**11** (22/245) | N/A |
| **Mahajana Sampatha** | **1** (122/245)<br>**5** (120/245)<br>**6** (120/245)<br>**2** (119/245)<br>**3** (118/245) | **J** (15/245)<br>**D** (14/245)<br>**N** (13/245)<br>**Q** (13/245)<br>**Y** (12/245) |
| **Mega Power** | **11** (31/245)<br>**3** (29/245)<br>**22** (27/245)<br>**6** (27/245)<br>**13** (27/245) | **V** (18/245)<br>**T** (14/245)<br>**K** (14/245)<br>**J** (14/245)<br>**U** (13/245) |
| **Nlb Jaya** | **5** (101/236)<br>**0** (92/236)<br>**3** (91/236)<br>**2** (88/236)<br>**1** (85/236) | **P** (14/236)<br>**I** (14/236)<br>**T** (14/236)<br>**Y** (14/236)<br>**M** (13/236) |
| **Suba Dawasak** | **3** (102/245)<br>**4** (98/245)<br>**1** (96/245)<br>**9** (92/245)<br>**5** (90/245) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1764)<br>**20** (116/1764)<br>**57** (115/1764)<br>**38** (109/1764)<br>**13** (109/1764) | **B** (82/1764)<br>**P** (79/1764)<br>**M** (79/1764)<br>**R** (78/1764)<br>**I** (76/1764) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1652)<br>**10** (142/1652)<br>**29** (134/1652)<br>**21** (134/1652)<br>**27** (134/1652) | **H** (88/1652)<br>**U** (76/1652)<br>**W** (72/1652)<br>**G** (71/1652)<br>**X** (71/1652) |
| **Lagna Wasana** | **28** (135/1771)<br>**5** (135/1771)<br>**36** (133/1771)<br>**23** (131/1771)<br>**39** (130/1771) | N/A |
| **Sasiri** | **9** (72/949)<br>**20** (70/949)<br>**26** (70/949)<br>**22** (69/949)<br>**19** (67/949) | N/A |
| **Super Ball** | **45** (110/1765)<br>**52** (107/1765)<br>**74** (107/1765)<br>**3** (106/1765)<br>**29** (106/1765) | **I** (87/1765)<br>**D** (81/1765)<br>**V** (79/1765)<br>**T** (79/1765)<br>**A** (79/1765) |
| **Supiri Dhana Sampatha** | **0** (467/923)<br>**2** (466/923)<br>**3** (462/923)<br>**7** (452/923)<br>**5** (441/923) | **K** (46/923)<br>**V** (44/923)<br>**S** (43/923)<br>**M** (43/923)<br>**T** (43/923) |

