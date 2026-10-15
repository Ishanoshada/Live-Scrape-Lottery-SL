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

> **Last Updated (Sri Lanka Time):** `2026-10-16 01:57:47 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 364 Rows | 17.56 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 4 Rows | 224 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 372 Rows | 15.94 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 371 Rows | 15.71 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 371 Rows | 15.31 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 371 Rows | 15.77 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 371 Rows | 16.78 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 362 Rows | 14.13 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 371 Rows | 17.00 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1890 Rows | 72.28 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1778 Rows | 72.67 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1897 Rows | 70.70 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1075 Rows | 35.67 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1891 Rows | 72.32 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1049 Rows | 39.05 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-16 01:57:47 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (133/364)<br>**2** (132/364)<br>**3** (129/364)<br>**4** (127/364)<br>**6** (125/364) | **D** (23/364)<br>**Q** (21/364)<br>**G** (21/364)<br>**N** (20/364)<br>**J** (20/364) |
| **Ayubo** | **2** (3/4)<br>**9** (3/4)<br>**1** (2/4)<br>**5** (2/4)<br>**7** (2/4) | **K** (1/4)<br>**J** (1/4)<br>**V** (1/4)<br>**A** (1/4) |
| **Dhana Nidhanaya** | **9** (33/372)<br>**4** (30/372)<br>**7** (30/372)<br>**3** (27/372)<br>**80** (26/372) | **U** (21/372)<br>**W** (21/372)<br>**M** (20/372)<br>**Z** (19/372)<br>**F** (18/372) |
| **Govisetha** | **55** (28/371)<br>**10** (27/371)<br>**32** (26/371)<br>**44** (26/371)<br>**29** (25/371) | **P** (20/371)<br>**I** (19/371)<br>**Y** (18/371)<br>**C** (18/371)<br>**X** (18/371) |
| **Handahana** | **58** (33/371)<br>**60** (31/371)<br>**11** (31/371)<br>**55** (31/371)<br>**6** (31/371) | N/A |
| **Mahajana Sampatha** | **5** (186/371)<br>**2** (185/371)<br>**1** (183/371)<br>**3** (182/371)<br>**4** (178/371) | **D** (23/371)<br>**Q** (21/371)<br>**G** (21/371)<br>**J** (20/371)<br>**W** (20/371) |
| **Mega Power** | **13** (42/371)<br>**11** (42/371)<br>**26** (40/371)<br>**3** (39/371)<br>**22** (38/371) | **V** (24/371)<br>**U** (24/371)<br>**T** (23/371)<br>**K** (19/371)<br>**J** (18/371) |
| **Nlb Jaya** | **5** (154/362)<br>**0** (139/362)<br>**3** (137/362)<br>**2** (136/362)<br>**6** (135/362) | **T** (21/362)<br>**I** (20/362)<br>**G** (19/362)<br>**P** (17/362)<br>**Y** (17/362) |
| **Suba Dawasak** | **4** (146/371)<br>**3** (142/371)<br>**9** (138/371)<br>**1** (136/371)<br>**2** (136/371) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1890)<br>**20** (124/1890)<br>**57** (124/1890)<br>**38** (118/1890)<br>**75** (116/1890) | **B** (88/1890)<br>**R** (85/1890)<br>**M** (84/1890)<br>**N** (82/1890)<br>**P** (81/1890) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (164/1778)<br>**10** (150/1778)<br>**21** (149/1778)<br>**15** (147/1778)<br>**16** (146/1778) | **H** (90/1778)<br>**U** (81/1778)<br>**M** (79/1778)<br>**G** (76/1778)<br>**D** (75/1778) |
| **Lagna Wasana** | **5** (144/1897)<br>**23** (143/1897)<br>**39** (141/1897)<br>**25** (141/1897)<br>**36** (140/1897) | N/A |
| **Sasiri** | **9** (84/1075)<br>**20** (81/1075)<br>**19** (79/1075)<br>**26** (79/1075)<br>**22** (78/1075) | N/A |
| **Super Ball** | **45** (115/1891)<br>**52** (113/1891)<br>**9** (113/1891)<br>**29** (113/1891)<br>**43** (112/1891) | **I** (93/1891)<br>**T** (86/1891)<br>**V** (84/1891)<br>**D** (82/1891)<br>**A** (82/1891) |
| **Supiri Dhana Sampatha** | **0** (531/1049)<br>**2** (523/1049)<br>**3** (520/1049)<br>**7** (519/1049)<br>**8** (500/1049) | **V** (56/1049)<br>**K** (51/1049)<br>**T** (50/1049)<br>**S** (48/1049)<br>**G** (47/1049) |

