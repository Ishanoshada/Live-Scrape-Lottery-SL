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

> **Last Updated (Sri Lanka Time):** `2026-10-19 01:02:16 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 367 Rows | 17.70 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 7 Rows | 343 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 375 Rows | 16.07 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 373 Rows | 15.79 KB |
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
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1893 Rows | 72.40 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1781 Rows | 72.79 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1900 Rows | 70.81 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1078 Rows | 35.78 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1894 Rows | 72.43 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1052 Rows | 39.17 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-19 01:02:16 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/367)<br>**2** (134/367)<br>**3** (129/367)<br>**4** (129/367)<br>**6** (126/367) | **D** (23/367)<br>**Q** (22/367)<br>**G** (21/367)<br>**N** (20/367)<br>**J** (20/367) |
| **Ayubo** | **5** (5/7)<br>**7** (4/7)<br>**8** (4/7)<br>**2** (3/7)<br>**3** (3/7) | **V** (2/7)<br>**K** (1/7)<br>**J** (1/7)<br>**A** (1/7)<br>**W** (1/7) |
| **Dhana Nidhanaya** | **9** (33/375)<br>**4** (30/375)<br>**7** (30/375)<br>**80** (27/375)<br>**3** (27/375) | **U** (21/375)<br>**W** (21/375)<br>**M** (20/375)<br>**Z** (19/375)<br>**F** (18/375) |
| **Govisetha** | **55** (29/373)<br>**10** (27/373)<br>**32** (26/373)<br>**44** (26/373)<br>**29** (25/373) | **P** (20/373)<br>**I** (20/373)<br>**Y** (18/373)<br>**C** (18/373)<br>**X** (18/373) |
| **Handahana** | **58** (33/372)<br>**60** (31/372)<br>**11** (31/372)<br>**55** (31/372)<br>**6** (31/372) | N/A |
| **Mahajana Sampatha** | **5** (187/372)<br>**2** (186/372)<br>**1** (183/372)<br>**3** (182/372)<br>**4** (178/372) | **D** (23/372)<br>**Q** (22/372)<br>**G** (21/372)<br>**J** (20/372)<br>**W** (20/372) |
| **Mega Power** | **13** (42/372)<br>**11** (42/372)<br>**26** (40/372)<br>**3** (39/372)<br>**22** (38/372) | **V** (24/372)<br>**U** (24/372)<br>**T** (23/372)<br>**K** (19/372)<br>**J** (18/372) |
| **Nlb Jaya** | **5** (154/363)<br>**0** (139/363)<br>**3** (137/363)<br>**2** (137/363)<br>**6** (135/363) | **T** (22/363)<br>**I** (20/363)<br>**G** (19/363)<br>**P** (17/363)<br>**Y** (17/363) |
| **Suba Dawasak** | **4** (146/372)<br>**3** (142/372)<br>**9** (138/372)<br>**1** (136/372)<br>**2** (136/372) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1893)<br>**20** (125/1893)<br>**57** (124/1893)<br>**38** (118/1893)<br>**75** (116/1893) | **B** (88/1893)<br>**R** (85/1893)<br>**M** (84/1893)<br>**N** (82/1893)<br>**P** (81/1893) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (164/1781)<br>**21** (150/1781)<br>**10** (150/1781)<br>**15** (147/1781)<br>**16** (146/1781) | **H** (90/1781)<br>**U** (81/1781)<br>**M** (79/1781)<br>**G** (76/1781)<br>**D** (75/1781) |
| **Lagna Wasana** | **5** (144/1900)<br>**23** (143/1900)<br>**39** (141/1900)<br>**25** (141/1900)<br>**36** (140/1900) | N/A |
| **Sasiri** | **9** (85/1078)<br>**20** (81/1078)<br>**19** (79/1078)<br>**26** (79/1078)<br>**22** (78/1078) | N/A |
| **Super Ball** | **45** (115/1894)<br>**9** (114/1894)<br>**52** (113/1894)<br>**29** (113/1894)<br>**3** (112/1894) | **I** (93/1894)<br>**T** (86/1894)<br>**V** (84/1894)<br>**D** (83/1894)<br>**A** (82/1894) |
| **Supiri Dhana Sampatha** | **0** (532/1052)<br>**2** (523/1052)<br>**3** (523/1052)<br>**7** (520/1052)<br>**8** (501/1052) | **V** (56/1052)<br>**K** (51/1052)<br>**T** (50/1052)<br>**S** (48/1052)<br>**G** (47/1052) |

