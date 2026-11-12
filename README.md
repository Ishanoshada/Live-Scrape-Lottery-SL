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

> **Last Updated (Sri Lanka Time):** `2026-11-13 04:19:36 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 392 Rows | 18.94 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 32 Rows | 1.33 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 400 Rows | 17.16 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 399 Rows | 16.92 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 399 Rows | 16.50 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 399 Rows | 16.99 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 399 Rows | 18.07 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 390 Rows | 15.24 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 399 Rows | 18.17 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1918 Rows | 73.35 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1806 Rows | 73.82 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1925 Rows | 71.74 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1103 Rows | 36.63 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1919 Rows | 73.39 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1077 Rows | 40.12 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-13 04:19:36 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (143/392)<br>**3** (139/392)<br>**6** (138/392)<br>**5** (137/392)<br>**4** (137/392) | **D** (25/392)<br>**G** (24/392)<br>**N** (23/392)<br>**J** (23/392)<br>**Q** (22/392) |
| **Ayubo** | **7** (15/32)<br>**9** (15/32)<br>**5** (14/32)<br>**8** (14/32)<br>**2** (11/32) | **K** (2/32)<br>**J** (2/32)<br>**V** (2/32)<br>**A** (2/32)<br>**W** (2/32) |
| **Dhana Nidhanaya** | **9** (34/400)<br>**4** (31/400)<br>**7** (30/400)<br>**80** (29/400)<br>**19** (29/400) | **U** (23/400)<br>**W** (21/400)<br>**M** (21/400)<br>**Z** (20/400)<br>**F** (20/400) |
| **Govisetha** | **55** (30/399)<br>**10** (29/399)<br>**32** (27/399)<br>**45** (27/399)<br>**44** (26/399) | **P** (21/399)<br>**I** (20/399)<br>**W** (19/399)<br>**D** (18/399)<br>**A** (18/399) |
| **Handahana** | **6** (36/399)<br>**58** (35/399)<br>**55** (35/399)<br>**11** (34/399)<br>**56** (33/399) | N/A |
| **Mahajana Sampatha** | **2** (200/399)<br>**1** (196/399)<br>**3** (195/399)<br>**5** (194/399)<br>**9** (191/399) | **D** (25/399)<br>**G** (24/399)<br>**J** (23/399)<br>**N** (22/399)<br>**Q** (22/399) |
| **Mega Power** | **13** (45/399)<br>**11** (44/399)<br>**3** (42/399)<br>**26** (41/399)<br>**22** (40/399) | **U** (27/399)<br>**V** (24/399)<br>**T** (23/399)<br>**K** (20/399)<br>**J** (19/399) |
| **Nlb Jaya** | **5** (166/390)<br>**2** (149/390)<br>**3** (145/390)<br>**6** (145/390)<br>**0** (144/390) | **T** (23/390)<br>**I** (22/390)<br>**G** (20/390)<br>**O** (20/390)<br>**P** (18/390) |
| **Suba Dawasak** | **4** (150/399)<br>**3** (143/399)<br>**9** (141/399)<br>**1** (138/399)<br>**2** (138/399) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1918)<br>**20** (126/1918)<br>**57** (125/1918)<br>**29** (119/1918)<br>**13** (119/1918) | **B** (90/1918)<br>**R** (85/1918)<br>**M** (85/1918)<br>**P** (84/1918)<br>**N** (83/1918) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1806)<br>**21** (153/1806)<br>**10** (152/1806)<br>**15** (149/1806)<br>**16** (148/1806) | **H** (90/1806)<br>**U** (82/1806)<br>**M** (80/1806)<br>**S** (77/1806)<br>**X** (77/1806) |
| **Lagna Wasana** | **23** (146/1925)<br>**5** (145/1925)<br>**25** (143/1925)<br>**39** (142/1925)<br>**36** (142/1925) | N/A |
| **Sasiri** | **9** (86/1103)<br>**20** (84/1103)<br>**19** (81/1103)<br>**22** (80/1103)<br>**26** (79/1103) | N/A |
| **Super Ball** | **52** (116/1919)<br>**45** (116/1919)<br>**9** (115/1919)<br>**74** (114/1919)<br>**29** (114/1919) | **I** (96/1919)<br>**V** (86/1919)<br>**T** (86/1919)<br>**D** (84/1919)<br>**A** (83/1919) |
| **Supiri Dhana Sampatha** | **0** (542/1077)<br>**2** (536/1077)<br>**3** (533/1077)<br>**7** (527/1077)<br>**5** (510/1077) | **V** (58/1077)<br>**K** (53/1077)<br>**T** (50/1077)<br>**S** (49/1077)<br>**A** (48/1077) |

