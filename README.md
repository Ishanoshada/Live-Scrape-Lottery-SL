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

> **Last Updated (Sri Lanka Time):** `2026-10-21 02:17:00 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 369 Rows | 17.80 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 9 Rows | 422 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 377 Rows | 16.16 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 376 Rows | 15.92 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 376 Rows | 15.52 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 376 Rows | 15.98 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 376 Rows | 17.00 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 367 Rows | 14.32 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 376 Rows | 17.20 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1895 Rows | 72.47 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1783 Rows | 72.87 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1902 Rows | 70.88 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1080 Rows | 35.84 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1896 Rows | 72.51 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1054 Rows | 39.24 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-21 02:17:00 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/369)<br>**2** (135/369)<br>**3** (130/369)<br>**4** (129/369)<br>**6** (128/369) | **D** (23/369)<br>**Q** (22/369)<br>**G** (21/369)<br>**N** (20/369)<br>**J** (20/369) |
| **Ayubo** | **5** (6/9)<br>**8** (5/9)<br>**9** (5/9)<br>**7** (4/9)<br>**2** (4/9) | **V** (2/9)<br>**K** (1/9)<br>**J** (1/9)<br>**A** (1/9)<br>**W** (1/9) |
| **Dhana Nidhanaya** | **9** (33/377)<br>**4** (30/377)<br>**7** (30/377)<br>**3** (28/377)<br>**80** (27/377) | **U** (21/377)<br>**W** (21/377)<br>**M** (20/377)<br>**Z** (19/377)<br>**F** (18/377) |
| **Govisetha** | **55** (29/376)<br>**10** (27/376)<br>**32** (26/376)<br>**44** (26/376)<br>**45** (26/376) | **P** (20/376)<br>**I** (20/376)<br>**Y** (18/376)<br>**C** (18/376)<br>**X** (18/376) |
| **Handahana** | **58** (33/376)<br>**55** (33/376)<br>**6** (33/376)<br>**60** (31/376)<br>**11** (31/376) | N/A |
| **Mahajana Sampatha** | **5** (189/376)<br>**2** (188/376)<br>**1** (185/376)<br>**3** (183/376)<br>**4** (180/376) | **D** (23/376)<br>**Q** (22/376)<br>**G** (21/376)<br>**J** (20/376)<br>**W** (20/376) |
| **Mega Power** | **13** (42/376)<br>**11** (42/376)<br>**3** (41/376)<br>**22** (40/376)<br>**26** (40/376) | **U** (25/376)<br>**V** (24/376)<br>**T** (23/376)<br>**K** (19/376)<br>**J** (19/376) |
| **Nlb Jaya** | **5** (156/367)<br>**0** (139/367)<br>**2** (138/367)<br>**3** (137/367)<br>**6** (137/367) | **T** (22/367)<br>**I** (20/367)<br>**G** (20/367)<br>**P** (17/367)<br>**Y** (17/367) |
| **Suba Dawasak** | **4** (146/376)<br>**3** (142/376)<br>**9** (138/376)<br>**1** (136/376)<br>**2** (136/376) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1895)<br>**20** (125/1895)<br>**57** (124/1895)<br>**38** (118/1895)<br>**29** (116/1895) | **B** (89/1895)<br>**R** (85/1895)<br>**M** (84/1895)<br>**N** (82/1895)<br>**P** (81/1895) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (165/1783)<br>**21** (150/1783)<br>**10** (150/1783)<br>**16** (147/1783)<br>**15** (147/1783) | **H** (90/1783)<br>**U** (81/1783)<br>**M** (79/1783)<br>**G** (76/1783)<br>**S** (75/1783) |
| **Lagna Wasana** | **5** (144/1902)<br>**23** (143/1902)<br>**25** (142/1902)<br>**39** (141/1902)<br>**36** (141/1902) | N/A |
| **Sasiri** | **9** (85/1080)<br>**20** (81/1080)<br>**19** (80/1080)<br>**26** (79/1080)<br>**22** (78/1080) | N/A |
| **Super Ball** | **45** (116/1896)<br>**9** (114/1896)<br>**52** (113/1896)<br>**29** (113/1896)<br>**3** (112/1896) | **I** (93/1896)<br>**T** (86/1896)<br>**V** (84/1896)<br>**D** (84/1896)<br>**A** (82/1896) |
| **Supiri Dhana Sampatha** | **0** (533/1054)<br>**2** (525/1054)<br>**3** (525/1054)<br>**7** (521/1054)<br>**8** (502/1054) | **V** (56/1054)<br>**K** (51/1054)<br>**T** (50/1054)<br>**S** (48/1054)<br>**G** (47/1054) |

