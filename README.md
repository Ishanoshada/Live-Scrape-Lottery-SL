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

> **Last Updated (Sri Lanka Time):** `2026-11-15 03:08:37 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 394 Rows | 19.04 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 34 Rows | 1.41 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 402 Rows | 17.25 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 401 Rows | 17.01 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 401 Rows | 16.58 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 401 Rows | 17.08 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 401 Rows | 18.16 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 392 Rows | 15.32 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 401 Rows | 18.27 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1920 Rows | 73.43 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1808 Rows | 73.90 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1927 Rows | 71.82 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1105 Rows | 36.70 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1921 Rows | 73.47 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1079 Rows | 40.20 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-15 03:08:37 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (145/394)<br>**3** (139/394)<br>**6** (138/394)<br>**5** (137/394)<br>**4** (137/394) | **D** (26/394)<br>**G** (24/394)<br>**N** (23/394)<br>**J** (23/394)<br>**Q** (22/394) |
| **Ayubo** | **7** (16/34)<br>**8** (16/34)<br>**9** (16/34)<br>**5** (15/34)<br>**4** (12/34) | **U** (3/34)<br>**K** (2/34)<br>**J** (2/34)<br>**V** (2/34)<br>**A** (2/34) |
| **Dhana Nidhanaya** | **9** (35/402)<br>**4** (31/402)<br>**7** (30/402)<br>**80** (29/402)<br>**19** (29/402) | **U** (23/402)<br>**W** (21/402)<br>**M** (21/402)<br>**Z** (20/402)<br>**F** (20/402) |
| **Govisetha** | **55** (30/401)<br>**10** (29/401)<br>**32** (27/401)<br>**45** (27/401)<br>**44** (26/401) | **P** (21/401)<br>**I** (20/401)<br>**W** (19/401)<br>**C** (19/401)<br>**D** (18/401) |
| **Handahana** | **6** (36/401)<br>**58** (35/401)<br>**55** (35/401)<br>**11** (34/401)<br>**56** (33/401) | N/A |
| **Mahajana Sampatha** | **2** (202/401)<br>**1** (198/401)<br>**3** (195/401)<br>**5** (194/401)<br>**9** (192/401) | **D** (26/401)<br>**G** (24/401)<br>**J** (23/401)<br>**N** (22/401)<br>**Q** (22/401) |
| **Mega Power** | **13** (45/401)<br>**11** (44/401)<br>**3** (42/401)<br>**26** (41/401)<br>**22** (40/401) | **U** (27/401)<br>**V** (24/401)<br>**T** (23/401)<br>**K** (20/401)<br>**J** (19/401) |
| **Nlb Jaya** | **5** (168/392)<br>**2** (149/392)<br>**6** (146/392)<br>**3** (145/392)<br>**0** (145/392) | **T** (23/392)<br>**I** (22/392)<br>**O** (21/392)<br>**G** (20/392)<br>**P** (18/392) |
| **Suba Dawasak** | **4** (151/401)<br>**3** (143/401)<br>**9** (141/401)<br>**1** (140/401)<br>**2** (138/401) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1920)<br>**20** (126/1920)<br>**57** (125/1920)<br>**29** (119/1920)<br>**13** (119/1920) | **B** (90/1920)<br>**R** (85/1920)<br>**M** (85/1920)<br>**P** (84/1920)<br>**N** (83/1920) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1808)<br>**21** (153/1808)<br>**10** (152/1808)<br>**15** (149/1808)<br>**16** (148/1808) | **H** (90/1808)<br>**U** (82/1808)<br>**M** (80/1808)<br>**S** (77/1808)<br>**X** (77/1808) |
| **Lagna Wasana** | **23** (146/1927)<br>**5** (145/1927)<br>**36** (143/1927)<br>**25** (143/1927)<br>**39** (142/1927) | N/A |
| **Sasiri** | **9** (86/1105)<br>**20** (84/1105)<br>**19** (82/1105)<br>**22** (80/1105)<br>**26** (79/1105) | N/A |
| **Super Ball** | **52** (116/1921)<br>**45** (116/1921)<br>**9** (115/1921)<br>**3** (114/1921)<br>**74** (114/1921) | **I** (96/1921)<br>**V** (86/1921)<br>**T** (86/1921)<br>**D** (84/1921)<br>**A** (84/1921) |
| **Supiri Dhana Sampatha** | **0** (544/1079)<br>**2** (536/1079)<br>**3** (534/1079)<br>**7** (527/1079)<br>**5** (510/1079) | **V** (58/1079)<br>**K** (53/1079)<br>**S** (50/1079)<br>**T** (50/1079)<br>**A** (48/1079) |

