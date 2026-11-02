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

> **Last Updated (Sri Lanka Time):** `2026-11-03 05:28:44 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 382 Rows | 18.44 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 22 Rows | 946 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 390 Rows | 16.72 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 389 Rows | 16.48 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 389 Rows | 16.06 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 389 Rows | 16.55 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 389 Rows | 17.60 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 380 Rows | 14.83 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 389 Rows | 17.71 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1908 Rows | 72.97 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1796 Rows | 73.41 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1915 Rows | 71.37 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1093 Rows | 36.29 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1909 Rows | 73.00 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1067 Rows | 39.74 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-03 05:28:45 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (139/382)<br>**3** (136/382)<br>**5** (135/382)<br>**6** (132/382)<br>**4** (132/382) | **D** (25/382)<br>**J** (23/382)<br>**Q** (22/382)<br>**N** (21/382)<br>**G** (21/382) |
| **Ayubo** | **5** (11/22)<br>**7** (9/22)<br>**2** (9/22)<br>**9** (9/22)<br>**8** (8/22) | **K** (2/22)<br>**V** (2/22)<br>**W** (2/22)<br>**U** (2/22)<br>**I** (2/22) |
| **Dhana Nidhanaya** | **9** (34/390)<br>**4** (30/390)<br>**7** (30/390)<br>**80** (28/390)<br>**6** (28/390) | **U** (21/390)<br>**W** (21/390)<br>**M** (21/390)<br>**Z** (19/390)<br>**F** (19/390) |
| **Govisetha** | **55** (30/389)<br>**10** (28/389)<br>**32** (27/389)<br>**44** (26/389)<br>**14** (26/389) | **P** (20/389)<br>**I** (20/389)<br>**W** (19/389)<br>**Y** (18/389)<br>**C** (18/389) |
| **Handahana** | **55** (35/389)<br>**58** (34/389)<br>**11** (34/389)<br>**6** (34/389)<br>**60** (32/389) | N/A |
| **Mahajana Sampatha** | **2** (196/389)<br>**3** (190/389)<br>**5** (190/389)<br>**1** (190/389)<br>**8** (186/389) | **D** (25/389)<br>**J** (23/389)<br>**Q** (22/389)<br>**G** (21/389)<br>**W** (21/389) |
| **Mega Power** | **13** (44/389)<br>**11** (43/389)<br>**3** (41/389)<br>**26** (41/389)<br>**22** (40/389) | **U** (26/389)<br>**V** (24/389)<br>**T** (23/389)<br>**K** (20/389)<br>**J** (19/389) |
| **Nlb Jaya** | **5** (162/380)<br>**2** (145/380)<br>**0** (142/380)<br>**6** (141/380)<br>**3** (140/380) | **I** (22/380)<br>**T** (22/380)<br>**G** (20/380)<br>**O** (19/380)<br>**P** (18/380) |
| **Suba Dawasak** | **4** (148/389)<br>**3** (142/389)<br>**9** (139/389)<br>**1** (138/389)<br>**2** (136/389) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1908)<br>**20** (125/1908)<br>**57** (125/1908)<br>**29** (118/1908)<br>**38** (118/1908) | **B** (89/1908)<br>**R** (85/1908)<br>**M** (84/1908)<br>**N** (83/1908)<br>**P** (82/1908) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1796)<br>**21** (152/1796)<br>**10** (152/1796)<br>**15** (148/1796)<br>**16** (147/1796) | **H** (90/1796)<br>**U** (81/1796)<br>**M** (80/1796)<br>**S** (76/1796)<br>**G** (76/1796) |
| **Lagna Wasana** | **5** (145/1915)<br>**23** (144/1915)<br>**25** (143/1915)<br>**39** (142/1915)<br>**36** (142/1915) | N/A |
| **Sasiri** | **9** (86/1093)<br>**20** (82/1093)<br>**19** (81/1093)<br>**22** (79/1093)<br>**26** (79/1093) | N/A |
| **Super Ball** | **45** (116/1909)<br>**52** (115/1909)<br>**9** (115/1909)<br>**29** (114/1909)<br>**3** (113/1909) | **I** (96/1909)<br>**T** (86/1909)<br>**V** (84/1909)<br>**D** (84/1909)<br>**A** (83/1909) |
| **Supiri Dhana Sampatha** | **0** (539/1067)<br>**2** (530/1067)<br>**3** (528/1067)<br>**7** (524/1067)<br>**5** (505/1067) | **V** (57/1067)<br>**K** (51/1067)<br>**T** (50/1067)<br>**S** (48/1067)<br>**G** (47/1067) |

