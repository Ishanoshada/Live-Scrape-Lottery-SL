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

> **Last Updated (Sri Lanka Time):** `2026-10-20 03:09:37 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 368 Rows | 17.75 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 8 Rows | 382 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 376 Rows | 16.11 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 375 Rows | 15.88 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 375 Rows | 15.48 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 375 Rows | 15.94 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 375 Rows | 16.95 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 366 Rows | 14.28 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 375 Rows | 17.16 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1894 Rows | 72.43 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1782 Rows | 72.83 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1901 Rows | 70.84 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1079 Rows | 35.81 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1895 Rows | 72.47 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1053 Rows | 39.20 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-20 03:09:37 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/368)<br>**2** (135/368)<br>**3** (130/368)<br>**4** (129/368)<br>**6** (127/368) | **D** (23/368)<br>**Q** (22/368)<br>**G** (21/368)<br>**N** (20/368)<br>**J** (20/368) |
| **Ayubo** | **5** (5/8)<br>**8** (5/8)<br>**2** (4/8)<br>**7** (4/8)<br>**9** (4/8) | **V** (2/8)<br>**K** (1/8)<br>**J** (1/8)<br>**A** (1/8)<br>**W** (1/8) |
| **Dhana Nidhanaya** | **9** (33/376)<br>**4** (30/376)<br>**7** (30/376)<br>**3** (28/376)<br>**80** (27/376) | **U** (21/376)<br>**W** (21/376)<br>**M** (20/376)<br>**Z** (19/376)<br>**F** (18/376) |
| **Govisetha** | **55** (29/375)<br>**10** (27/375)<br>**32** (26/375)<br>**44** (26/375)<br>**45** (26/375) | **P** (20/375)<br>**I** (20/375)<br>**Y** (18/375)<br>**C** (18/375)<br>**X** (18/375) |
| **Handahana** | **58** (33/375)<br>**55** (32/375)<br>**6** (32/375)<br>**60** (31/375)<br>**11** (31/375) | N/A |
| **Mahajana Sampatha** | **5** (189/375)<br>**2** (188/375)<br>**1** (184/375)<br>**3** (183/375)<br>**4** (180/375) | **D** (23/375)<br>**Q** (22/375)<br>**G** (21/375)<br>**J** (20/375)<br>**W** (20/375) |
| **Mega Power** | **13** (42/375)<br>**11** (42/375)<br>**3** (41/375)<br>**26** (40/375)<br>**22** (39/375) | **U** (25/375)<br>**V** (24/375)<br>**T** (23/375)<br>**K** (19/375)<br>**J** (18/375) |
| **Nlb Jaya** | **5** (155/366)<br>**0** (139/366)<br>**3** (137/366)<br>**6** (137/366)<br>**2** (137/366) | **T** (22/366)<br>**I** (20/366)<br>**G** (20/366)<br>**P** (17/366)<br>**Y** (17/366) |
| **Suba Dawasak** | **4** (146/375)<br>**3** (142/375)<br>**9** (138/375)<br>**1** (136/375)<br>**2** (136/375) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1894)<br>**20** (125/1894)<br>**57** (124/1894)<br>**38** (118/1894)<br>**75** (116/1894) | **B** (88/1894)<br>**R** (85/1894)<br>**M** (84/1894)<br>**N** (82/1894)<br>**P** (81/1894) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (165/1782)<br>**21** (150/1782)<br>**10** (150/1782)<br>**16** (147/1782)<br>**15** (147/1782) | **H** (90/1782)<br>**U** (81/1782)<br>**M** (79/1782)<br>**G** (76/1782)<br>**S** (75/1782) |
| **Lagna Wasana** | **5** (144/1901)<br>**23** (143/1901)<br>**39** (141/1901)<br>**36** (141/1901)<br>**25** (141/1901) | N/A |
| **Sasiri** | **9** (85/1079)<br>**20** (81/1079)<br>**19** (79/1079)<br>**26** (79/1079)<br>**22** (78/1079) | N/A |
| **Super Ball** | **45** (116/1895)<br>**9** (114/1895)<br>**52** (113/1895)<br>**29** (113/1895)<br>**3** (112/1895) | **I** (93/1895)<br>**T** (86/1895)<br>**V** (84/1895)<br>**D** (83/1895)<br>**A** (82/1895) |
| **Supiri Dhana Sampatha** | **0** (532/1053)<br>**2** (524/1053)<br>**3** (524/1053)<br>**7** (521/1053)<br>**8** (502/1053) | **V** (56/1053)<br>**K** (51/1053)<br>**T** (50/1053)<br>**S** (48/1053)<br>**G** (47/1053) |

