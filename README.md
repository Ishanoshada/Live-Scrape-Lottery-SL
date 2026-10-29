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

<p align="center">
  <a href="https://www.paypal.com/donate/?business=ic31908%40gmail.com&currency_code=USD">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donate with PayPal" height="80">
  </a>
</p>

<p align="center">
  <a href="https://www.paypal.com/donate/?business=ic31908%40gmail.com&currency_code=USD">
    <img src="https://raw.githubusercontent.com/elestyle/elepay-payment-logos/master/payment_logos/svg/paypal.svg" alt="Donate with PayPal" height="100">
  </a>
</p>
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

> **Last Updated (Sri Lanka Time):** `2026-10-30 03:26:03 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 378 Rows | 18.24 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 18 Rows | 786 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 386 Rows | 16.54 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 385 Rows | 16.31 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 385 Rows | 15.90 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 385 Rows | 16.37 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 385 Rows | 17.42 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 376 Rows | 14.68 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 385 Rows | 17.55 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1904 Rows | 72.82 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1792 Rows | 73.24 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1911 Rows | 71.22 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1089 Rows | 36.15 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1905 Rows | 72.85 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1063 Rows | 39.59 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-30 03:26:03 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (138/378)<br>**5** (135/378)<br>**3** (132/378)<br>**4** (132/378)<br>**6** (131/378) | **D** (24/378)<br>**Q** (22/378)<br>**J** (22/378)<br>**N** (21/378)<br>**G** (21/378) |
| **Ayubo** | **5** (8/18)<br>**2** (8/18)<br>**9** (8/18)<br>**7** (7/18)<br>**0** (7/18) | **K** (2/18)<br>**V** (2/18)<br>**W** (2/18)<br>**J** (1/18)<br>**A** (1/18) |
| **Dhana Nidhanaya** | **9** (33/386)<br>**4** (30/386)<br>**7** (30/386)<br>**80** (28/386)<br>**19** (28/386) | **U** (21/386)<br>**W** (21/386)<br>**M** (21/386)<br>**Z** (19/386)<br>**F** (19/386) |
| **Govisetha** | **55** (29/385)<br>**10** (28/385)<br>**32** (27/385)<br>**44** (26/385)<br>**14** (26/385) | **P** (20/385)<br>**I** (20/385)<br>**W** (18/385)<br>**Y** (18/385)<br>**C** (18/385) |
| **Handahana** | **58** (34/385)<br>**11** (34/385)<br>**55** (34/385)<br>**6** (34/385)<br>**60** (32/385) | N/A |
| **Mahajana Sampatha** | **2** (194/385)<br>**5** (189/385)<br>**1** (189/385)<br>**3** (186/385)<br>**8** (184/385) | **D** (24/385)<br>**Q** (22/385)<br>**J** (22/385)<br>**G** (21/385)<br>**W** (21/385) |
| **Mega Power** | **13** (43/385)<br>**11** (42/385)<br>**3** (41/385)<br>**26** (41/385)<br>**22** (40/385) | **U** (26/385)<br>**V** (24/385)<br>**T** (23/385)<br>**K** (20/385)<br>**J** (19/385) |
| **Nlb Jaya** | **5** (161/376)<br>**2** (143/376)<br>**0** (141/376)<br>**3** (140/376)<br>**6** (140/376) | **T** (22/376)<br>**I** (21/376)<br>**G** (20/376)<br>**P** (18/376)<br>**O** (18/376) |
| **Suba Dawasak** | **4** (147/385)<br>**3** (142/385)<br>**9** (138/385)<br>**1** (136/385)<br>**2** (136/385) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1904)<br>**20** (125/1904)<br>**57** (125/1904)<br>**38** (118/1904)<br>**29** (117/1904) | **B** (89/1904)<br>**R** (85/1904)<br>**M** (84/1904)<br>**N** (83/1904)<br>**P** (81/1904) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (166/1792)<br>**21** (151/1792)<br>**10** (150/1792)<br>**15** (148/1792)<br>**16** (147/1792) | **H** (90/1792)<br>**U** (81/1792)<br>**M** (79/1792)<br>**S** (76/1792)<br>**G** (76/1792) |
| **Lagna Wasana** | **23** (144/1911)<br>**5** (144/1911)<br>**25** (143/1911)<br>**39** (142/1911)<br>**36** (141/1911) | N/A |
| **Sasiri** | **9** (86/1089)<br>**20** (81/1089)<br>**19** (81/1089)<br>**22** (79/1089)<br>**26** (79/1089) | N/A |
| **Super Ball** | **45** (116/1905)<br>**9** (114/1905)<br>**29** (114/1905)<br>**52** (113/1905)<br>**3** (113/1905) | **I** (95/1905)<br>**T** (86/1905)<br>**V** (84/1905)<br>**D** (84/1905)<br>**A** (83/1905) |
| **Supiri Dhana Sampatha** | **0** (536/1063)<br>**2** (528/1063)<br>**3** (528/1063)<br>**7** (523/1063)<br>**5** (503/1063) | **V** (56/1063)<br>**K** (51/1063)<br>**T** (50/1063)<br>**S** (48/1063)<br>**G** (47/1063) |

