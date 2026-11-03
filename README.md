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

> **Last Updated (Sri Lanka Time):** `2026-11-04 03:56:51 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 383 Rows | 18.49 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 23 Rows | 987 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 391 Rows | 16.76 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 390 Rows | 16.52 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 390 Rows | 16.11 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 390 Rows | 16.59 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 390 Rows | 17.65 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 381 Rows | 14.88 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 390 Rows | 17.75 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1909 Rows | 73.01 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1797 Rows | 73.45 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1916 Rows | 71.40 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1094 Rows | 36.32 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1910 Rows | 73.04 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1068 Rows | 39.78 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-04 03:56:51 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (140/383)<br>**3** (137/383)<br>**5** (135/383)<br>**6** (133/383)<br>**4** (132/383) | **D** (25/383)<br>**J** (23/383)<br>**N** (22/383)<br>**Q** (22/383)<br>**G** (21/383) |
| **Ayubo** | **5** (12/23)<br>**9** (10/23)<br>**7** (9/23)<br>**4** (9/23)<br>**2** (9/23) | **K** (2/23)<br>**V** (2/23)<br>**W** (2/23)<br>**F** (2/23)<br>**U** (2/23) |
| **Dhana Nidhanaya** | **9** (34/391)<br>**4** (30/391)<br>**7** (30/391)<br>**80** (28/391)<br>**6** (28/391) | **U** (21/391)<br>**W** (21/391)<br>**M** (21/391)<br>**Z** (19/391)<br>**F** (19/391) |
| **Govisetha** | **55** (30/390)<br>**10** (28/390)<br>**32** (27/390)<br>**44** (26/390)<br>**14** (26/390) | **P** (20/390)<br>**I** (20/390)<br>**W** (19/390)<br>**Y** (18/390)<br>**C** (18/390) |
| **Handahana** | **55** (35/390)<br>**6** (35/390)<br>**58** (34/390)<br>**11** (34/390)<br>**60** (32/390) | N/A |
| **Mahajana Sampatha** | **2** (197/390)<br>**3** (191/390)<br>**1** (191/390)<br>**5** (190/390)<br>**8** (186/390) | **D** (25/390)<br>**J** (23/390)<br>**Q** (22/390)<br>**N** (21/390)<br>**G** (21/390) |
| **Mega Power** | **13** (45/390)<br>**11** (43/390)<br>**3** (41/390)<br>**26** (41/390)<br>**22** (40/390) | **U** (26/390)<br>**V** (24/390)<br>**T** (23/390)<br>**K** (20/390)<br>**J** (19/390) |
| **Nlb Jaya** | **5** (163/381)<br>**2** (145/381)<br>**0** (142/381)<br>**3** (141/381)<br>**6** (141/381) | **I** (22/381)<br>**T** (22/381)<br>**G** (20/381)<br>**O** (19/381)<br>**P** (18/381) |
| **Suba Dawasak** | **4** (148/390)<br>**3** (142/390)<br>**9** (139/390)<br>**1** (138/390)<br>**2** (136/390) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1909)<br>**20** (125/1909)<br>**57** (125/1909)<br>**29** (118/1909)<br>**38** (118/1909) | **B** (89/1909)<br>**R** (85/1909)<br>**M** (84/1909)<br>**N** (83/1909)<br>**P** (82/1909) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1797)<br>**21** (153/1797)<br>**10** (152/1797)<br>**15** (148/1797)<br>**16** (147/1797) | **H** (90/1797)<br>**U** (81/1797)<br>**M** (80/1797)<br>**S** (76/1797)<br>**G** (76/1797) |
| **Lagna Wasana** | **5** (145/1916)<br>**23** (144/1916)<br>**25** (143/1916)<br>**39** (142/1916)<br>**36** (142/1916) | N/A |
| **Sasiri** | **9** (86/1094)<br>**20** (82/1094)<br>**19** (81/1094)<br>**22** (79/1094)<br>**26** (79/1094) | N/A |
| **Super Ball** | **45** (116/1910)<br>**52** (115/1910)<br>**9** (115/1910)<br>**29** (114/1910)<br>**3** (113/1910) | **I** (96/1910)<br>**T** (86/1910)<br>**V** (84/1910)<br>**D** (84/1910)<br>**A** (83/1910) |
| **Supiri Dhana Sampatha** | **0** (539/1068)<br>**2** (531/1068)<br>**3** (529/1068)<br>**7** (524/1068)<br>**5** (506/1068) | **V** (57/1068)<br>**K** (51/1068)<br>**T** (50/1068)<br>**S** (48/1068)<br>**G** (47/1068) |

