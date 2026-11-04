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

> **Last Updated (Sri Lanka Time):** `2026-11-05 04:15:50 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 384 Rows | 18.54 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 24 Rows | 1.01 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 392 Rows | 16.81 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 391 Rows | 16.57 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 391 Rows | 16.15 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 391 Rows | 16.64 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 391 Rows | 17.70 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 382 Rows | 14.92 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 391 Rows | 17.79 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1910 Rows | 73.05 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1798 Rows | 73.49 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1917 Rows | 71.44 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1095 Rows | 36.36 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1911 Rows | 73.08 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1069 Rows | 39.82 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-05 04:15:51 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (140/384)<br>**3** (137/384)<br>**5** (135/384)<br>**6** (134/384)<br>**8** (132/384) | **D** (25/384)<br>**J** (23/384)<br>**N** (22/384)<br>**Q** (22/384)<br>**G** (22/384) |
| **Ayubo** | **5** (12/24)<br>**7** (10/24)<br>**9** (10/24)<br>**2** (9/24)<br>**8** (9/24) | **K** (2/24)<br>**V** (2/24)<br>**W** (2/24)<br>**F** (2/24)<br>**U** (2/24) |
| **Dhana Nidhanaya** | **9** (34/392)<br>**4** (31/392)<br>**7** (30/392)<br>**80** (28/392)<br>**6** (28/392) | **U** (22/392)<br>**W** (21/392)<br>**M** (21/392)<br>**Z** (19/392)<br>**F** (19/392) |
| **Govisetha** | **55** (30/391)<br>**10** (28/391)<br>**32** (27/391)<br>**44** (26/391)<br>**14** (26/391) | **P** (21/391)<br>**I** (20/391)<br>**W** (19/391)<br>**Y** (18/391)<br>**C** (18/391) |
| **Handahana** | **55** (35/391)<br>**6** (35/391)<br>**11** (34/391)<br>**58** (34/391)<br>**56** (33/391) | N/A |
| **Mahajana Sampatha** | **2** (197/391)<br>**3** (192/391)<br>**1** (192/391)<br>**5** (190/391)<br>**8** (187/391) | **D** (25/391)<br>**J** (23/391)<br>**Q** (22/391)<br>**G** (22/391)<br>**N** (21/391) |
| **Mega Power** | **13** (45/391)<br>**11** (43/391)<br>**3** (41/391)<br>**26** (41/391)<br>**22** (40/391) | **U** (26/391)<br>**V** (24/391)<br>**T** (23/391)<br>**K** (20/391)<br>**J** (19/391) |
| **Nlb Jaya** | **5** (164/382)<br>**2** (145/382)<br>**3** (142/382)<br>**0** (142/382)<br>**6** (141/382) | **T** (23/382)<br>**I** (22/382)<br>**G** (20/382)<br>**O** (19/382)<br>**P** (18/382) |
| **Suba Dawasak** | **4** (148/391)<br>**3** (142/391)<br>**9** (139/391)<br>**1** (138/391)<br>**2** (136/391) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1910)<br>**20** (125/1910)<br>**57** (125/1910)<br>**29** (118/1910)<br>**38** (118/1910) | **B** (89/1910)<br>**R** (85/1910)<br>**M** (85/1910)<br>**N** (83/1910)<br>**P** (82/1910) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1798)<br>**21** (153/1798)<br>**10** (152/1798)<br>**15** (149/1798)<br>**16** (148/1798) | **H** (90/1798)<br>**U** (81/1798)<br>**M** (80/1798)<br>**S** (77/1798)<br>**G** (76/1798) |
| **Lagna Wasana** | **23** (145/1917)<br>**5** (145/1917)<br>**25** (143/1917)<br>**39** (142/1917)<br>**36** (142/1917) | N/A |
| **Sasiri** | **9** (86/1095)<br>**20** (82/1095)<br>**19** (81/1095)<br>**22** (79/1095)<br>**26** (79/1095) | N/A |
| **Super Ball** | **45** (116/1911)<br>**52** (115/1911)<br>**9** (115/1911)<br>**29** (114/1911)<br>**3** (113/1911) | **I** (96/1911)<br>**T** (86/1911)<br>**V** (85/1911)<br>**D** (84/1911)<br>**A** (83/1911) |
| **Supiri Dhana Sampatha** | **0** (539/1069)<br>**2** (532/1069)<br>**3** (530/1069)<br>**7** (524/1069)<br>**5** (506/1069) | **V** (57/1069)<br>**K** (51/1069)<br>**T** (50/1069)<br>**S** (48/1069)<br>**G** (47/1069) |

