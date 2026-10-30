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

> **Last Updated (Sri Lanka Time):** `2026-10-31 03:09:28 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 379 Rows | 18.29 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 19 Rows | 825 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 387 Rows | 16.59 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 386 Rows | 16.35 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 386 Rows | 15.94 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 386 Rows | 16.42 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 386 Rows | 17.46 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 377 Rows | 14.72 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 386 Rows | 17.59 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1905 Rows | 72.85 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1793 Rows | 73.28 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1912 Rows | 71.26 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1090 Rows | 36.19 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1906 Rows | 72.89 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1064 Rows | 39.62 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-31 03:09:28 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (138/379)<br>**5** (135/379)<br>**3** (133/379)<br>**4** (132/379)<br>**6** (131/379) | **D** (24/379)<br>**J** (23/379)<br>**Q** (22/379)<br>**N** (21/379)<br>**G** (21/379) |
| **Ayubo** | **5** (9/19)<br>**0** (8/19)<br>**2** (8/19)<br>**7** (8/19)<br>**4** (8/19) | **K** (2/19)<br>**V** (2/19)<br>**W** (2/19)<br>**J** (1/19)<br>**A** (1/19) |
| **Dhana Nidhanaya** | **9** (34/387)<br>**4** (30/387)<br>**7** (30/387)<br>**80** (28/387)<br>**19** (28/387) | **U** (21/387)<br>**W** (21/387)<br>**M** (21/387)<br>**Z** (19/387)<br>**F** (19/387) |
| **Govisetha** | **55** (29/386)<br>**10** (28/386)<br>**32** (27/386)<br>**44** (26/386)<br>**14** (26/386) | **P** (20/386)<br>**I** (20/386)<br>**W** (18/386)<br>**Y** (18/386)<br>**C** (18/386) |
| **Handahana** | **58** (34/386)<br>**11** (34/386)<br>**55** (34/386)<br>**6** (34/386)<br>**60** (32/386) | N/A |
| **Mahajana Sampatha** | **2** (194/386)<br>**1** (190/386)<br>**5** (189/386)<br>**3** (187/386)<br>**8** (184/386) | **D** (24/386)<br>**J** (23/386)<br>**Q** (22/386)<br>**G** (21/386)<br>**W** (21/386) |
| **Mega Power** | **13** (43/386)<br>**11** (43/386)<br>**3** (41/386)<br>**26** (41/386)<br>**22** (40/386) | **U** (26/386)<br>**V** (24/386)<br>**T** (23/386)<br>**K** (20/386)<br>**J** (19/386) |
| **Nlb Jaya** | **5** (162/377)<br>**2** (144/377)<br>**0** (141/377)<br>**3** (140/377)<br>**6** (140/377) | **T** (22/377)<br>**I** (21/377)<br>**G** (20/377)<br>**O** (19/377)<br>**P** (18/377) |
| **Suba Dawasak** | **4** (147/386)<br>**3** (142/386)<br>**9** (138/386)<br>**1** (137/386)<br>**2** (136/386) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1905)<br>**20** (125/1905)<br>**57** (125/1905)<br>**38** (118/1905)<br>**29** (117/1905) | **B** (89/1905)<br>**R** (85/1905)<br>**M** (84/1905)<br>**N** (83/1905)<br>**P** (81/1905) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (166/1793)<br>**21** (151/1793)<br>**10** (150/1793)<br>**15** (148/1793)<br>**16** (147/1793) | **H** (90/1793)<br>**U** (81/1793)<br>**M** (79/1793)<br>**S** (76/1793)<br>**G** (76/1793) |
| **Lagna Wasana** | **23** (144/1912)<br>**5** (144/1912)<br>**25** (143/1912)<br>**39** (142/1912)<br>**36** (141/1912) | N/A |
| **Sasiri** | **9** (86/1090)<br>**20** (81/1090)<br>**19** (81/1090)<br>**22** (79/1090)<br>**26** (79/1090) | N/A |
| **Super Ball** | **45** (116/1906)<br>**9** (114/1906)<br>**29** (114/1906)<br>**52** (113/1906)<br>**3** (113/1906) | **I** (95/1906)<br>**T** (86/1906)<br>**V** (84/1906)<br>**D** (84/1906)<br>**A** (83/1906) |
| **Supiri Dhana Sampatha** | **0** (537/1064)<br>**2** (528/1064)<br>**3** (528/1064)<br>**7** (523/1064)<br>**5** (504/1064) | **V** (56/1064)<br>**K** (51/1064)<br>**T** (50/1064)<br>**S** (48/1064)<br>**G** (47/1064) |

