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

> **Last Updated (Sri Lanka Time):** `2026-11-09 02:48:07 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 388 Rows | 18.74 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 28 Rows | 1.17 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 396 Rows | 16.98 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 395 Rows | 16.74 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 395 Rows | 16.32 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 395 Rows | 16.81 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 395 Rows | 17.88 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 386 Rows | 15.08 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 395 Rows | 17.95 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1914 Rows | 73.20 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1802 Rows | 73.65 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1921 Rows | 71.59 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1099 Rows | 36.50 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1915 Rows | 73.24 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1073 Rows | 39.97 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-09 02:48:07 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (142/388)<br>**3** (139/388)<br>**5** (136/388)<br>**6** (135/388)<br>**4** (134/388) | **D** (25/388)<br>**G** (24/388)<br>**J** (23/388)<br>**N** (22/388)<br>**Q** (22/388) |
| **Ayubo** | **7** (14/28)<br>**5** (13/28)<br>**9** (13/28)<br>**8** (11/28)<br>**2** (10/28) | **K** (2/28)<br>**V** (2/28)<br>**W** (2/28)<br>**F** (2/28)<br>**S** (2/28) |
| **Dhana Nidhanaya** | **9** (34/396)<br>**4** (31/396)<br>**7** (30/396)<br>**80** (29/396)<br>**19** (29/396) | **U** (23/396)<br>**W** (21/396)<br>**M** (21/396)<br>**Z** (20/396)<br>**F** (19/396) |
| **Govisetha** | **55** (30/395)<br>**10** (29/395)<br>**32** (27/395)<br>**44** (26/395)<br>**14** (26/395) | **P** (21/395)<br>**I** (20/395)<br>**W** (19/395)<br>**D** (18/395)<br>**A** (18/395) |
| **Handahana** | **6** (36/395)<br>**58** (35/395)<br>**55** (35/395)<br>**11** (34/395)<br>**56** (33/395) | N/A |
| **Mahajana Sampatha** | **2** (199/395)<br>**1** (196/395)<br>**3** (194/395)<br>**5** (191/395)<br>**8** (188/395) | **D** (25/395)<br>**G** (24/395)<br>**J** (23/395)<br>**Q** (22/395)<br>**N** (21/395) |
| **Mega Power** | **13** (45/395)<br>**11** (43/395)<br>**3** (41/395)<br>**26** (41/395)<br>**22** (40/395) | **U** (26/395)<br>**V** (24/395)<br>**T** (23/395)<br>**K** (20/395)<br>**J** (19/395) |
| **Nlb Jaya** | **5** (166/386)<br>**2** (147/386)<br>**3** (144/386)<br>**6** (143/386)<br>**0** (142/386) | **T** (23/386)<br>**I** (22/386)<br>**G** (20/386)<br>**O** (20/386)<br>**P** (18/386) |
| **Suba Dawasak** | **4** (148/395)<br>**3** (142/395)<br>**9** (139/395)<br>**1** (138/395)<br>**2** (136/395) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1914)<br>**20** (126/1914)<br>**57** (125/1914)<br>**13** (119/1914)<br>**29** (118/1914) | **B** (90/1914)<br>**R** (85/1914)<br>**M** (85/1914)<br>**P** (83/1914)<br>**N** (83/1914) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1802)<br>**21** (153/1802)<br>**10** (152/1802)<br>**15** (149/1802)<br>**16** (148/1802) | **H** (90/1802)<br>**U** (82/1802)<br>**M** (80/1802)<br>**S** (77/1802)<br>**X** (77/1802) |
| **Lagna Wasana** | **23** (146/1921)<br>**5** (145/1921)<br>**25** (143/1921)<br>**39** (142/1921)<br>**36** (142/1921) | N/A |
| **Sasiri** | **9** (86/1099)<br>**20** (82/1099)<br>**19** (81/1099)<br>**22** (80/1099)<br>**26** (79/1099) | N/A |
| **Super Ball** | **52** (116/1915)<br>**45** (116/1915)<br>**9** (115/1915)<br>**29** (114/1915)<br>**3** (113/1915) | **I** (96/1915)<br>**T** (86/1915)<br>**V** (85/1915)<br>**D** (84/1915)<br>**A** (83/1915) |
| **Supiri Dhana Sampatha** | **0** (539/1073)<br>**2** (534/1073)<br>**3** (531/1073)<br>**7** (527/1073)<br>**5** (508/1073) | **V** (57/1073)<br>**K** (52/1073)<br>**T** (50/1073)<br>**S** (49/1073)<br>**G** (47/1073) |

