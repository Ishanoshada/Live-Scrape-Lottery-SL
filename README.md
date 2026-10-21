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

> **Last Updated (Sri Lanka Time):** `2026-10-22 02:17:50 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 370 Rows | 17.85 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 10 Rows | 464 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 378 Rows | 16.20 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 377 Rows | 15.96 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 377 Rows | 15.56 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 377 Rows | 16.03 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 377 Rows | 17.05 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 368 Rows | 14.36 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 377 Rows | 17.24 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1896 Rows | 72.51 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1784 Rows | 72.91 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1903 Rows | 70.92 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1081 Rows | 35.88 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1897 Rows | 72.55 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1055 Rows | 39.28 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-22 02:17:51 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/370)<br>**2** (135/370)<br>**3** (130/370)<br>**4** (130/370)<br>**6** (128/370) | **D** (23/370)<br>**Q** (22/370)<br>**J** (21/370)<br>**G** (21/370)<br>**N** (20/370) |
| **Ayubo** | **5** (7/10)<br>**7** (5/10)<br>**8** (5/10)<br>**9** (5/10)<br>**2** (4/10) | **V** (2/10)<br>**K** (1/10)<br>**J** (1/10)<br>**A** (1/10)<br>**W** (1/10) |
| **Dhana Nidhanaya** | **9** (33/378)<br>**4** (30/378)<br>**7** (30/378)<br>**19** (28/378)<br>**3** (28/378) | **U** (21/378)<br>**W** (21/378)<br>**M** (20/378)<br>**Z** (19/378)<br>**F** (18/378) |
| **Govisetha** | **55** (29/377)<br>**10** (27/377)<br>**32** (26/377)<br>**44** (26/377)<br>**45** (26/377) | **P** (20/377)<br>**I** (20/377)<br>**Y** (18/377)<br>**C** (18/377)<br>**X** (18/377) |
| **Handahana** | **58** (33/377)<br>**55** (33/377)<br>**6** (33/377)<br>**60** (31/377)<br>**11** (31/377) | N/A |
| **Mahajana Sampatha** | **5** (189/377)<br>**2** (188/377)<br>**1** (186/377)<br>**3** (183/377)<br>**4** (181/377) | **D** (23/377)<br>**Q** (22/377)<br>**J** (21/377)<br>**G** (21/377)<br>**W** (20/377) |
| **Mega Power** | **13** (42/377)<br>**11** (42/377)<br>**3** (41/377)<br>**22** (40/377)<br>**26** (40/377) | **U** (26/377)<br>**V** (24/377)<br>**T** (23/377)<br>**K** (19/377)<br>**J** (19/377) |
| **Nlb Jaya** | **5** (157/368)<br>**0** (139/368)<br>**3** (138/368)<br>**6** (138/368)<br>**2** (138/368) | **T** (22/368)<br>**I** (20/368)<br>**G** (20/368)<br>**P** (17/368)<br>**Y** (17/368) |
| **Suba Dawasak** | **4** (146/377)<br>**3** (142/377)<br>**9** (138/377)<br>**1** (136/377)<br>**2** (136/377) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1896)<br>**20** (125/1896)<br>**57** (124/1896)<br>**38** (118/1896)<br>**29** (116/1896) | **B** (89/1896)<br>**R** (85/1896)<br>**M** (84/1896)<br>**N** (82/1896)<br>**P** (81/1896) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (165/1784)<br>**21** (150/1784)<br>**10** (150/1784)<br>**15** (148/1784)<br>**16** (147/1784) | **H** (90/1784)<br>**U** (81/1784)<br>**M** (79/1784)<br>**G** (76/1784)<br>**S** (75/1784) |
| **Lagna Wasana** | **5** (144/1903)<br>**23** (143/1903)<br>**25** (142/1903)<br>**39** (141/1903)<br>**36** (141/1903) | N/A |
| **Sasiri** | **9** (86/1081)<br>**20** (81/1081)<br>**19** (80/1081)<br>**26** (79/1081)<br>**22** (78/1081) | N/A |
| **Super Ball** | **45** (116/1897)<br>**9** (114/1897)<br>**52** (113/1897)<br>**74** (113/1897)<br>**29** (113/1897) | **I** (93/1897)<br>**T** (86/1897)<br>**V** (84/1897)<br>**D** (84/1897)<br>**A** (82/1897) |
| **Supiri Dhana Sampatha** | **0** (533/1055)<br>**2** (526/1055)<br>**3** (525/1055)<br>**7** (522/1055)<br>**8** (502/1055) | **V** (56/1055)<br>**K** (51/1055)<br>**T** (50/1055)<br>**S** (48/1055)<br>**G** (47/1055) |

