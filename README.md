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

> **Last Updated (Sri Lanka Time):** `2026-10-17 01:31:12 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 365 Rows | 17.61 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 5 Rows | 263 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 373 Rows | 15.98 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 372 Rows | 15.75 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 372 Rows | 15.35 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 372 Rows | 15.81 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 372 Rows | 16.82 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 363 Rows | 14.17 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 372 Rows | 17.04 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1891 Rows | 72.32 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1779 Rows | 72.71 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1898 Rows | 70.73 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1076 Rows | 35.71 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1892 Rows | 72.36 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1050 Rows | 39.09 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-17 01:31:12 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (134/365)<br>**2** (133/365)<br>**3** (129/365)<br>**4** (127/365)<br>**6** (125/365) | **D** (23/365)<br>**Q** (22/365)<br>**G** (21/365)<br>**N** (20/365)<br>**J** (20/365) |
| **Ayubo** | **8** (3/5)<br>**5** (3/5)<br>**2** (3/5)<br>**9** (3/5)<br>**7** (2/5) | **K** (1/5)<br>**J** (1/5)<br>**V** (1/5)<br>**A** (1/5)<br>**W** (1/5) |
| **Dhana Nidhanaya** | **9** (33/373)<br>**4** (30/373)<br>**7** (30/373)<br>**3** (27/373)<br>**80** (26/373) | **U** (21/373)<br>**W** (21/373)<br>**M** (20/373)<br>**Z** (19/373)<br>**F** (18/373) |
| **Govisetha** | **55** (28/372)<br>**10** (27/372)<br>**32** (26/372)<br>**44** (26/372)<br>**29** (25/372) | **P** (20/372)<br>**I** (19/372)<br>**Y** (18/372)<br>**C** (18/372)<br>**X** (18/372) |
| **Handahana** | **58** (33/372)<br>**60** (31/372)<br>**11** (31/372)<br>**55** (31/372)<br>**6** (31/372) | N/A |
| **Mahajana Sampatha** | **5** (187/372)<br>**2** (186/372)<br>**1** (183/372)<br>**3** (182/372)<br>**4** (178/372) | **D** (23/372)<br>**Q** (22/372)<br>**G** (21/372)<br>**J** (20/372)<br>**W** (20/372) |
| **Mega Power** | **13** (42/372)<br>**11** (42/372)<br>**26** (40/372)<br>**3** (39/372)<br>**22** (38/372) | **V** (24/372)<br>**U** (24/372)<br>**T** (23/372)<br>**K** (19/372)<br>**J** (18/372) |
| **Nlb Jaya** | **5** (154/363)<br>**0** (139/363)<br>**3** (137/363)<br>**2** (137/363)<br>**6** (135/363) | **T** (22/363)<br>**I** (20/363)<br>**G** (19/363)<br>**P** (17/363)<br>**Y** (17/363) |
| **Suba Dawasak** | **4** (146/372)<br>**3** (142/372)<br>**9** (138/372)<br>**1** (136/372)<br>**2** (136/372) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1891)<br>**20** (124/1891)<br>**57** (124/1891)<br>**38** (118/1891)<br>**75** (116/1891) | **B** (88/1891)<br>**R** (85/1891)<br>**M** (84/1891)<br>**N** (82/1891)<br>**P** (81/1891) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (164/1779)<br>**21** (150/1779)<br>**10** (150/1779)<br>**15** (147/1779)<br>**16** (146/1779) | **H** (90/1779)<br>**U** (81/1779)<br>**M** (79/1779)<br>**G** (76/1779)<br>**D** (75/1779) |
| **Lagna Wasana** | **5** (144/1898)<br>**23** (143/1898)<br>**39** (141/1898)<br>**25** (141/1898)<br>**36** (140/1898) | N/A |
| **Sasiri** | **9** (84/1076)<br>**20** (81/1076)<br>**19** (79/1076)<br>**26** (79/1076)<br>**22** (78/1076) | N/A |
| **Super Ball** | **45** (115/1892)<br>**52** (113/1892)<br>**9** (113/1892)<br>**29** (113/1892)<br>**43** (112/1892) | **I** (93/1892)<br>**T** (86/1892)<br>**V** (84/1892)<br>**D** (82/1892)<br>**A** (82/1892) |
| **Supiri Dhana Sampatha** | **0** (531/1050)<br>**2** (523/1050)<br>**3** (521/1050)<br>**7** (519/1050)<br>**8** (500/1050) | **V** (56/1050)<br>**K** (51/1050)<br>**T** (50/1050)<br>**S** (48/1050)<br>**G** (47/1050) |

