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

> **Last Updated (Sri Lanka Time):** `2026-10-10 03:19:08 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 358 Rows | 17.26 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 0 Rows | 28 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 366 Rows | 15.68 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 365 Rows | 15.45 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 365 Rows | 15.06 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 365 Rows | 15.51 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 365 Rows | 16.50 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 356 Rows | 13.89 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 364 Rows | 16.73 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1884 Rows | 72.05 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1772 Rows | 72.42 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1891 Rows | 70.47 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1069 Rows | 35.47 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1885 Rows | 72.09 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1043 Rows | 38.82 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-10 03:19:08 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (130/358)<br>**2** (128/358)<br>**3** (126/358)<br>**4** (125/358)<br>**6** (123/358) | **D** (22/358)<br>**Q** (21/358)<br>**G** (21/358)<br>**N** (20/358)<br>**J** (20/358) |
| **Dhana Nidhanaya** | **9** (33/366)<br>**4** (30/366)<br>**7** (29/366)<br>**3** (27/366)<br>**80** (26/366) | **U** (20/366)<br>**W** (20/366)<br>**Z** (19/366)<br>**M** (19/366)<br>**F** (18/366) |
| **Govisetha** | **55** (28/365)<br>**10** (27/365)<br>**44** (26/365)<br>**32** (25/365)<br>**29** (25/365) | **P** (20/365)<br>**I** (18/365)<br>**C** (18/365)<br>**X** (18/365)<br>**W** (17/365) |
| **Handahana** | **58** (32/365)<br>**60** (31/365)<br>**11** (31/365)<br>**55** (31/365)<br>**21** (30/365) | N/A |
| **Mahajana Sampatha** | **5** (181/365)<br>**2** (179/365)<br>**1** (179/365)<br>**3** (178/365)<br>**4** (176/365) | **D** (22/365)<br>**Q** (21/365)<br>**G** (21/365)<br>**J** (20/365)<br>**W** (20/365) |
| **Mega Power** | **13** (42/365)<br>**26** (40/365)<br>**11** (40/365)<br>**22** (38/365)<br>**3** (38/365) | **T** (23/365)<br>**V** (23/365)<br>**U** (23/365)<br>**K** (19/365)<br>**S** (18/365) |
| **Nlb Jaya** | **5** (150/356)<br>**0** (137/356)<br>**3** (135/356)<br>**2** (134/356)<br>**6** (130/356) | **T** (21/356)<br>**I** (19/356)<br>**G** (19/356)<br>**P** (17/356)<br>**Y** (17/356) |
| **Suba Dawasak** | **4** (146/364)<br>**3** (142/364)<br>**9** (137/364)<br>**1** (136/364)<br>**2** (136/364) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1884)<br>**20** (124/1884)<br>**57** (123/1884)<br>**38** (118/1884)<br>**13** (116/1884) | **B** (88/1884)<br>**R** (85/1884)<br>**M** (84/1884)<br>**N** (82/1884)<br>**P** (81/1884) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (163/1772)<br>**21** (149/1772)<br>**10** (149/1772)<br>**6** (145/1772)<br>**15** (145/1772) | **H** (89/1772)<br>**U** (81/1772)<br>**M** (79/1772)<br>**G** (76/1772)<br>**D** (75/1772) |
| **Lagna Wasana** | **5** (144/1891)<br>**23** (142/1891)<br>**39** (141/1891)<br>**36** (140/1891)<br>**25** (139/1891) | N/A |
| **Sasiri** | **9** (83/1069)<br>**20** (81/1069)<br>**26** (79/1069)<br>**22** (78/1069)<br>**21** (78/1069) | N/A |
| **Super Ball** | **45** (115/1885)<br>**9** (113/1885)<br>**52** (112/1885)<br>**29** (112/1885)<br>**74** (111/1885) | **I** (93/1885)<br>**T** (86/1885)<br>**V** (84/1885)<br>**D** (82/1885)<br>**A** (82/1885) |
| **Supiri Dhana Sampatha** | **0** (526/1043)<br>**2** (519/1043)<br>**3** (517/1043)<br>**7** (516/1043)<br>**8** (497/1043) | **V** (56/1043)<br>**K** (51/1043)<br>**T** (49/1043)<br>**S** (48/1043)<br>**G** (47/1043) |

