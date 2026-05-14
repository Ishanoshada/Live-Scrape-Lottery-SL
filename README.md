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

> **Last Updated (Sri Lanka Time):** `2026-05-14 01:08:15 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 211 Rows | 10.28 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 219 Rows | 9.45 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 218 Rows | 9.33 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 218 Rows | 9.10 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 218 Rows | 9.38 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 218 Rows | 9.98 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 209 Rows | 8.22 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 218 Rows | 10.15 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1737 Rows | 66.43 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1625 Rows | 66.37 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1744 Rows | 65.00 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 922 Rows | 30.43 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1738 Rows | 66.47 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 896 Rows | 33.30 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-14 01:08:15 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (81/211)<br>**5** (78/211)<br>**7** (75/211)<br>**2** (75/211)<br>**0** (74/211) | **D** (14/211)<br>**J** (14/211)<br>**N** (13/211)<br>**Q** (12/211)<br>**Y** (12/211) |
| **Dhana Nidhanaya** | **28** (21/219)<br>**9** (20/219)<br>**6** (19/219)<br>**16** (18/219)<br>**7** (17/219) | **U** (14/219)<br>**W** (13/219)<br>**T** (12/219)<br>**M** (12/219)<br>**Q** (11/219) |
| **Govisetha** | **44** (18/218)<br>**19** (17/218)<br>**55** (17/218)<br>**23** (16/218)<br>**58** (16/218) | **P** (12/218)<br>**D** (11/218)<br>**W** (11/218)<br>**O** (11/218)<br>**X** (11/218) |
| **Handahana** | **58** (22/218)<br>**21** (21/218)<br>**60** (20/218)<br>**11** (20/218)<br>**61** (20/218) | N/A |
| **Mahajana Sampatha** | **6** (108/218)<br>**2** (107/218)<br>**1** (107/218)<br>**5** (106/218)<br>**3** (105/218) | **D** (14/218)<br>**J** (14/218)<br>**N** (12/218)<br>**Q** (12/218)<br>**Y** (12/218) |
| **Mega Power** | **6** (26/218)<br>**3** (26/218)<br>**13** (25/218)<br>**11** (25/218)<br>**22** (24/218) | **V** (17/218)<br>**T** (13/218)<br>**K** (13/218)<br>**U** (13/218)<br>**J** (11/218) |
| **Nlb Jaya** | **5** (90/209)<br>**3** (84/209)<br>**0** (80/209)<br>**2** (79/209)<br>**1** (74/209) | **T** (14/209)<br>**M** (13/209)<br>**P** (13/209)<br>**I** (13/209)<br>**G** (13/209) |
| **Suba Dawasak** | **3** (89/218)<br>**1** (89/218)<br>**4** (87/218)<br>**9** (81/218)<br>**5** (77/218) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (115/1737)<br>**57** (115/1737)<br>**20** (111/1737)<br>**13** (109/1737)<br>**38** (106/1737) | **B** (81/1737)<br>**M** (78/1737)<br>**R** (77/1737)<br>**P** (77/1737)<br>**I** (74/1737) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1625)<br>**10** (142/1625)<br>**29** (133/1625)<br>**21** (133/1625)<br>**22** (132/1625) | **H** (87/1625)<br>**U** (75/1625)<br>**W** (71/1625)<br>**G** (70/1625)<br>**D** (69/1625) |
| **Lagna Wasana** | **5** (135/1744)<br>**28** (133/1744)<br>**36** (130/1744)<br>**25** (130/1744)<br>**23** (129/1744) | N/A |
| **Sasiri** | **20** (70/922)<br>**9** (69/922)<br>**22** (68/922)<br>**26** (68/922)<br>**19** (67/922) | N/A |
| **Super Ball** | **45** (109/1738)<br>**3** (105/1738)<br>**29** (105/1738)<br>**43** (105/1738)<br>**52** (103/1738) | **I** (87/1738)<br>**D** (80/1738)<br>**T** (78/1738)<br>**V** (77/1738)<br>**A** (77/1738) |
| **Supiri Dhana Sampatha** | **2** (453/896)<br>**0** (452/896)<br>**3** (449/896)<br>**7** (444/896)<br>**5** (427/896) | **K** (44/896)<br>**V** (43/896)<br>**T** (43/896)<br>**J** (42/896)<br>**S** (41/896) |

