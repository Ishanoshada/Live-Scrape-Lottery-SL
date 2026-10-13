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

> **Last Updated (Sri Lanka Time):** `2026-10-14 03:25:26 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 362 Rows | 17.46 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 2 Rows | 141 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 370 Rows | 15.85 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 369 Rows | 15.62 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 369 Rows | 15.22 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 369 Rows | 15.68 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 369 Rows | 16.68 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 360 Rows | 14.05 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 369 Rows | 16.92 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1888 Rows | 72.20 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1776 Rows | 72.58 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1895 Rows | 70.62 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1073 Rows | 35.60 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1889 Rows | 72.24 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1047 Rows | 38.97 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-14 03:25:26 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (132/362)<br>**2** (131/362)<br>**3** (128/362)<br>**4** (126/362)<br>**6** (125/362) | **D** (23/362)<br>**Q** (21/362)<br>**G** (21/362)<br>**N** (20/362)<br>**J** (20/362) |
| **Ayubo** | **2** (2/2)<br>**5** (2/2)<br>**7** (2/2)<br>**0** (1/2)<br>**1** (1/2) | **K** (1/2)<br>**J** (1/2) |
| **Dhana Nidhanaya** | **9** (33/370)<br>**4** (30/370)<br>**7** (29/370)<br>**3** (27/370)<br>**80** (26/370) | **U** (21/370)<br>**W** (20/370)<br>**M** (20/370)<br>**Z** (19/370)<br>**F** (18/370) |
| **Govisetha** | **55** (28/369)<br>**10** (27/369)<br>**44** (26/369)<br>**32** (25/369)<br>**29** (25/369) | **P** (20/369)<br>**I** (19/369)<br>**Y** (18/369)<br>**C** (18/369)<br>**X** (18/369) |
| **Handahana** | **58** (33/369)<br>**60** (31/369)<br>**11** (31/369)<br>**55** (31/369)<br>**6** (31/369) | N/A |
| **Mahajana Sampatha** | **5** (185/369)<br>**2** (183/369)<br>**1** (182/369)<br>**3** (180/369)<br>**4** (177/369) | **D** (23/369)<br>**Q** (21/369)<br>**G** (21/369)<br>**J** (20/369)<br>**W** (20/369) |
| **Mega Power** | **13** (42/369)<br>**11** (42/369)<br>**26** (40/369)<br>**3** (39/369)<br>**22** (38/369) | **V** (24/369)<br>**U** (24/369)<br>**T** (23/369)<br>**K** (19/369)<br>**S** (18/369) |
| **Nlb Jaya** | **5** (153/360)<br>**0** (138/360)<br>**3** (136/360)<br>**6** (134/360)<br>**2** (134/360) | **T** (21/360)<br>**I** (20/360)<br>**G** (19/360)<br>**P** (17/360)<br>**Y** (17/360) |
| **Suba Dawasak** | **4** (146/369)<br>**3** (142/369)<br>**9** (138/369)<br>**1** (136/369)<br>**2** (136/369) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1888)<br>**20** (124/1888)<br>**57** (124/1888)<br>**38** (118/1888)<br>**75** (116/1888) | **B** (88/1888)<br>**R** (85/1888)<br>**M** (84/1888)<br>**N** (82/1888)<br>**P** (81/1888) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1776)<br>**10** (150/1776)<br>**21** (149/1776)<br>**15** (146/1776)<br>**6** (145/1776) | **H** (89/1776)<br>**U** (81/1776)<br>**M** (79/1776)<br>**G** (76/1776)<br>**D** (75/1776) |
| **Lagna Wasana** | **5** (144/1895)<br>**23** (142/1895)<br>**39** (141/1895)<br>**36** (140/1895)<br>**25** (140/1895) | N/A |
| **Sasiri** | **9** (83/1073)<br>**20** (81/1073)<br>**19** (79/1073)<br>**26** (79/1073)<br>**22** (78/1073) | N/A |
| **Super Ball** | **45** (115/1889)<br>**52** (113/1889)<br>**9** (113/1889)<br>**29** (113/1889)<br>**43** (112/1889) | **I** (93/1889)<br>**T** (86/1889)<br>**V** (84/1889)<br>**D** (82/1889)<br>**A** (82/1889) |
| **Supiri Dhana Sampatha** | **0** (530/1047)<br>**2** (522/1047)<br>**7** (519/1047)<br>**3** (519/1047)<br>**8** (499/1047) | **V** (56/1047)<br>**K** (51/1047)<br>**T** (50/1047)<br>**S** (48/1047)<br>**G** (47/1047) |

