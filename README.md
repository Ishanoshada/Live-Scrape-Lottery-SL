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

> **Last Updated (Sri Lanka Time):** `2026-05-13 02:40:51 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 210 Rows | 10.23 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 218 Rows | 9.41 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 217 Rows | 9.29 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 217 Rows | 9.06 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 217 Rows | 9.34 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 217 Rows | 9.93 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 208 Rows | 8.19 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 217 Rows | 10.11 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1736 Rows | 66.39 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1624 Rows | 66.33 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1743 Rows | 64.96 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 921 Rows | 30.39 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1737 Rows | 66.43 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 895 Rows | 33.26 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-13 02:40:51 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (81/210)<br>**5** (78/210)<br>**2** (75/210)<br>**7** (74/210)<br>**0** (73/210) | **D** (14/210)<br>**J** (14/210)<br>**N** (13/210)<br>**Q** (12/210)<br>**Y** (12/210) |
| **Dhana Nidhanaya** | **28** (21/218)<br>**9** (20/218)<br>**6** (19/218)<br>**16** (18/218)<br>**7** (17/218) | **U** (13/218)<br>**W** (13/218)<br>**T** (12/218)<br>**M** (12/218)<br>**Q** (11/218) |
| **Govisetha** | **44** (18/217)<br>**19** (17/217)<br>**55** (17/217)<br>**23** (16/217)<br>**58** (16/217) | **P** (12/217)<br>**D** (11/217)<br>**W** (11/217)<br>**O** (11/217)<br>**X** (11/217) |
| **Handahana** | **58** (21/217)<br>**21** (21/217)<br>**60** (20/217)<br>**61** (20/217)<br>**55** (20/217) | N/A |
| **Mahajana Sampatha** | **6** (108/217)<br>**2** (107/217)<br>**5** (106/217)<br>**1** (106/217)<br>**9** (105/217) | **D** (14/217)<br>**J** (14/217)<br>**N** (12/217)<br>**Q** (12/217)<br>**Y** (12/217) |
| **Mega Power** | **6** (26/217)<br>**3** (26/217)<br>**13** (25/217)<br>**11** (25/217)<br>**22** (24/217) | **V** (17/217)<br>**T** (13/217)<br>**K** (13/217)<br>**U** (13/217)<br>**J** (11/217) |
| **Nlb Jaya** | **5** (90/208)<br>**3** (83/208)<br>**0** (80/208)<br>**2** (78/208)<br>**4** (73/208) | **T** (14/208)<br>**M** (13/208)<br>**P** (13/208)<br>**I** (13/208)<br>**G** (13/208) |
| **Suba Dawasak** | **3** (88/217)<br>**1** (88/217)<br>**4** (87/217)<br>**9** (81/217)<br>**5** (77/217) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1736)<br>**57** (114/1736)<br>**20** (111/1736)<br>**13** (109/1736)<br>**38** (106/1736) | **B** (81/1736)<br>**M** (78/1736)<br>**R** (77/1736)<br>**P** (77/1736)<br>**I** (74/1736) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1624)<br>**10** (142/1624)<br>**29** (133/1624)<br>**21** (133/1624)<br>**22** (132/1624) | **H** (87/1624)<br>**U** (75/1624)<br>**W** (71/1624)<br>**G** (70/1624)<br>**D** (69/1624) |
| **Lagna Wasana** | **5** (135/1743)<br>**28** (133/1743)<br>**36** (130/1743)<br>**25** (130/1743)<br>**23** (129/1743) | N/A |
| **Sasiri** | **20** (70/921)<br>**9** (69/921)<br>**22** (68/921)<br>**26** (68/921)<br>**19** (67/921) | N/A |
| **Super Ball** | **45** (109/1737)<br>**3** (105/1737)<br>**29** (105/1737)<br>**43** (105/1737)<br>**52** (103/1737) | **I** (87/1737)<br>**D** (80/1737)<br>**T** (78/1737)<br>**V** (77/1737)<br>**A** (77/1737) |
| **Supiri Dhana Sampatha** | **2** (452/895)<br>**0** (451/895)<br>**3** (449/895)<br>**7** (443/895)<br>**5** (427/895) | **K** (44/895)<br>**V** (43/895)<br>**T** (43/895)<br>**J** (42/895)<br>**S** (41/895) |

