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

> **Last Updated (Sri Lanka Time):** `2026-10-15 02:22:26 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 363 Rows | 17.51 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 3 Rows | 183 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 371 Rows | 15.90 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 370 Rows | 15.66 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 370 Rows | 15.27 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 370 Rows | 15.73 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 370 Rows | 16.73 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 361 Rows | 14.09 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 370 Rows | 16.96 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1889 Rows | 72.24 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1777 Rows | 72.63 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1896 Rows | 70.66 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1074 Rows | 35.64 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1890 Rows | 72.28 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1048 Rows | 39.01 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-15 02:22:26 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (132/363)<br>**2** (132/363)<br>**3** (128/363)<br>**4** (126/363)<br>**6** (125/363) | **D** (23/363)<br>**Q** (21/363)<br>**G** (21/363)<br>**N** (20/363)<br>**J** (20/363) |
| **Ayubo** | **1** (2/3)<br>**0** (2/3)<br>**5** (2/3)<br>**2** (2/3)<br>**7** (2/3) | **K** (1/3)<br>**J** (1/3)<br>**V** (1/3) |
| **Dhana Nidhanaya** | **9** (33/371)<br>**4** (30/371)<br>**7** (30/371)<br>**3** (27/371)<br>**80** (26/371) | **U** (21/371)<br>**W** (21/371)<br>**M** (20/371)<br>**Z** (19/371)<br>**F** (18/371) |
| **Govisetha** | **55** (28/370)<br>**10** (27/370)<br>**44** (26/370)<br>**32** (25/370)<br>**29** (25/370) | **P** (20/370)<br>**I** (19/370)<br>**Y** (18/370)<br>**C** (18/370)<br>**X** (18/370) |
| **Handahana** | **58** (33/370)<br>**60** (31/370)<br>**11** (31/370)<br>**55** (31/370)<br>**6** (31/370) | N/A |
| **Mahajana Sampatha** | **5** (185/370)<br>**2** (184/370)<br>**1** (183/370)<br>**3** (181/370)<br>**4** (177/370) | **D** (23/370)<br>**Q** (21/370)<br>**G** (21/370)<br>**J** (20/370)<br>**W** (20/370) |
| **Mega Power** | **13** (42/370)<br>**11** (42/370)<br>**26** (40/370)<br>**3** (39/370)<br>**22** (38/370) | **V** (24/370)<br>**U** (24/370)<br>**T** (23/370)<br>**K** (19/370)<br>**J** (18/370) |
| **Nlb Jaya** | **5** (154/361)<br>**0** (139/361)<br>**3** (137/361)<br>**2** (135/361)<br>**6** (134/361) | **T** (21/361)<br>**I** (20/361)<br>**G** (19/361)<br>**P** (17/361)<br>**Y** (17/361) |
| **Suba Dawasak** | **4** (146/370)<br>**3** (142/370)<br>**9** (138/370)<br>**1** (136/370)<br>**2** (136/370) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1889)<br>**20** (124/1889)<br>**57** (124/1889)<br>**38** (118/1889)<br>**75** (116/1889) | **B** (88/1889)<br>**R** (85/1889)<br>**M** (84/1889)<br>**N** (82/1889)<br>**P** (81/1889) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (164/1777)<br>**10** (150/1777)<br>**21** (149/1777)<br>**15** (147/1777)<br>**6** (145/1777) | **H** (90/1777)<br>**U** (81/1777)<br>**M** (79/1777)<br>**G** (76/1777)<br>**D** (75/1777) |
| **Lagna Wasana** | **5** (144/1896)<br>**23** (142/1896)<br>**39** (141/1896)<br>**25** (141/1896)<br>**36** (140/1896) | N/A |
| **Sasiri** | **9** (84/1074)<br>**20** (81/1074)<br>**19** (79/1074)<br>**26** (79/1074)<br>**22** (78/1074) | N/A |
| **Super Ball** | **45** (115/1890)<br>**52** (113/1890)<br>**9** (113/1890)<br>**29** (113/1890)<br>**43** (112/1890) | **I** (93/1890)<br>**T** (86/1890)<br>**V** (84/1890)<br>**D** (82/1890)<br>**A** (82/1890) |
| **Supiri Dhana Sampatha** | **0** (530/1048)<br>**2** (523/1048)<br>**7** (519/1048)<br>**3** (519/1048)<br>**8** (500/1048) | **V** (56/1048)<br>**K** (51/1048)<br>**T** (50/1048)<br>**S** (48/1048)<br>**G** (47/1048) |

