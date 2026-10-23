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

> **Last Updated (Sri Lanka Time):** `2026-10-24 02:04:27 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 372 Rows | 17.95 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 12 Rows | 544 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 380 Rows | 16.29 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 379 Rows | 16.05 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 379 Rows | 15.64 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 379 Rows | 16.11 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 379 Rows | 17.14 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 370 Rows | 14.44 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 379 Rows | 17.32 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1898 Rows | 72.59 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1786 Rows | 73.00 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1905 Rows | 71.00 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1083 Rows | 35.95 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1899 Rows | 72.62 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1057 Rows | 39.36 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-24 02:04:27 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/372)<br>**2** (135/372)<br>**3** (131/372)<br>**4** (131/372)<br>**6** (130/372) | **D** (24/372)<br>**Q** (22/372)<br>**J** (21/372)<br>**G** (21/372)<br>**N** (20/372) |
| **Ayubo** | **5** (7/12)<br>**7** (6/12)<br>**9** (6/12)<br>**2** (5/12)<br>**8** (5/12) | **K** (2/12)<br>**V** (2/12)<br>**J** (1/12)<br>**A** (1/12)<br>**W** (1/12) |
| **Dhana Nidhanaya** | **9** (33/380)<br>**4** (30/380)<br>**7** (30/380)<br>**19** (28/380)<br>**3** (28/380) | **U** (21/380)<br>**W** (21/380)<br>**M** (20/380)<br>**Z** (19/380)<br>**F** (18/380) |
| **Govisetha** | **55** (29/379)<br>**10** (28/379)<br>**32** (26/379)<br>**44** (26/379)<br>**45** (26/379) | **P** (20/379)<br>**I** (20/379)<br>**Y** (18/379)<br>**C** (18/379)<br>**X** (18/379) |
| **Handahana** | **58** (33/379)<br>**55** (33/379)<br>**6** (33/379)<br>**60** (32/379)<br>**11** (31/379) | N/A |
| **Mahajana Sampatha** | **2** (189/379)<br>**5** (189/379)<br>**1** (187/379)<br>**3** (184/379)<br>**4** (182/379) | **D** (24/379)<br>**Q** (22/379)<br>**J** (21/379)<br>**G** (21/379)<br>**W** (21/379) |
| **Mega Power** | **13** (43/379)<br>**11** (42/379)<br>**3** (41/379)<br>**22** (40/379)<br>**26** (40/379) | **U** (26/379)<br>**V** (24/379)<br>**T** (23/379)<br>**K** (19/379)<br>**J** (19/379) |
| **Nlb Jaya** | **5** (158/370)<br>**2** (139/370)<br>**0** (139/370)<br>**3** (138/370)<br>**6** (138/370) | **T** (22/370)<br>**I** (20/370)<br>**G** (20/370)<br>**P** (18/370)<br>**Y** (17/370) |
| **Suba Dawasak** | **4** (147/379)<br>**3** (142/379)<br>**9** (138/379)<br>**1** (136/379)<br>**2** (136/379) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1898)<br>**20** (125/1898)<br>**57** (124/1898)<br>**38** (118/1898)<br>**29** (116/1898) | **B** (89/1898)<br>**R** (85/1898)<br>**M** (84/1898)<br>**N** (82/1898)<br>**P** (81/1898) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (165/1786)<br>**21** (150/1786)<br>**10** (150/1786)<br>**15** (148/1786)<br>**16** (147/1786) | **H** (90/1786)<br>**U** (81/1786)<br>**M** (79/1786)<br>**G** (76/1786)<br>**S** (75/1786) |
| **Lagna Wasana** | **5** (144/1905)<br>**23** (143/1905)<br>**25** (142/1905)<br>**39** (141/1905)<br>**36** (141/1905) | N/A |
| **Sasiri** | **9** (86/1083)<br>**20** (81/1083)<br>**19** (80/1083)<br>**22** (79/1083)<br>**26** (79/1083) | N/A |
| **Super Ball** | **45** (116/1899)<br>**9** (114/1899)<br>**52** (113/1899)<br>**74** (113/1899)<br>**29** (113/1899) | **I** (95/1899)<br>**T** (86/1899)<br>**V** (84/1899)<br>**D** (84/1899)<br>**A** (82/1899) |
| **Supiri Dhana Sampatha** | **0** (534/1057)<br>**2** (526/1057)<br>**3** (526/1057)<br>**7** (522/1057)<br>**8** (502/1057) | **V** (56/1057)<br>**K** (51/1057)<br>**T** (50/1057)<br>**S** (48/1057)<br>**G** (47/1057) |

