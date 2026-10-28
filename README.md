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

> **Last Updated (Sri Lanka Time):** `2026-10-29 03:19:20 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 377 Rows | 18.19 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 17 Rows | 745 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 385 Rows | 16.50 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 384 Rows | 16.26 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 384 Rows | 15.85 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 384 Rows | 16.33 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 384 Rows | 17.37 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 375 Rows | 14.64 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 384 Rows | 17.51 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1903 Rows | 72.78 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1791 Rows | 73.20 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1910 Rows | 71.18 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1088 Rows | 36.12 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1904 Rows | 72.82 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1062 Rows | 39.55 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-29 03:19:20 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (137/377)<br>**5** (135/377)<br>**3** (132/377)<br>**4** (132/377)<br>**6** (131/377) | **D** (24/377)<br>**Q** (22/377)<br>**J** (22/377)<br>**N** (21/377)<br>**G** (21/377) |
| **Ayubo** | **5** (8/17)<br>**9** (8/17)<br>**7** (7/17)<br>**0** (7/17)<br>**2** (7/17) | **K** (2/17)<br>**V** (2/17)<br>**W** (2/17)<br>**J** (1/17)<br>**A** (1/17) |
| **Dhana Nidhanaya** | **9** (33/385)<br>**4** (30/385)<br>**7** (30/385)<br>**80** (28/385)<br>**19** (28/385) | **U** (21/385)<br>**W** (21/385)<br>**M** (20/385)<br>**Z** (19/385)<br>**F** (19/385) |
| **Govisetha** | **55** (29/384)<br>**10** (28/384)<br>**32** (27/384)<br>**44** (26/384)<br>**14** (26/384) | **P** (20/384)<br>**I** (20/384)<br>**W** (18/384)<br>**Y** (18/384)<br>**C** (18/384) |
| **Handahana** | **58** (34/384)<br>**11** (34/384)<br>**55** (34/384)<br>**6** (34/384)<br>**60** (32/384) | N/A |
| **Mahajana Sampatha** | **2** (193/384)<br>**5** (189/384)<br>**1** (189/384)<br>**3** (185/384)<br>**4** (183/384) | **D** (24/384)<br>**Q** (22/384)<br>**J** (22/384)<br>**G** (21/384)<br>**W** (21/384) |
| **Mega Power** | **13** (43/384)<br>**11** (42/384)<br>**3** (41/384)<br>**22** (40/384)<br>**26** (40/384) | **U** (26/384)<br>**V** (24/384)<br>**T** (23/384)<br>**K** (20/384)<br>**J** (19/384) |
| **Nlb Jaya** | **5** (161/375)<br>**2** (142/375)<br>**0** (141/375)<br>**3** (140/375)<br>**6** (140/375) | **T** (22/375)<br>**I** (21/375)<br>**G** (20/375)<br>**P** (18/375)<br>**O** (18/375) |
| **Suba Dawasak** | **4** (147/384)<br>**3** (142/384)<br>**9** (138/384)<br>**1** (136/384)<br>**2** (136/384) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1903)<br>**20** (125/1903)<br>**57** (125/1903)<br>**38** (118/1903)<br>**29** (117/1903) | **B** (89/1903)<br>**R** (85/1903)<br>**M** (84/1903)<br>**N** (83/1903)<br>**P** (81/1903) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (166/1791)<br>**21** (151/1791)<br>**10** (150/1791)<br>**15** (148/1791)<br>**16** (147/1791) | **H** (90/1791)<br>**U** (81/1791)<br>**M** (79/1791)<br>**S** (76/1791)<br>**G** (76/1791) |
| **Lagna Wasana** | **23** (144/1910)<br>**5** (144/1910)<br>**25** (143/1910)<br>**39** (142/1910)<br>**36** (141/1910) | N/A |
| **Sasiri** | **9** (86/1088)<br>**20** (81/1088)<br>**19** (81/1088)<br>**22** (79/1088)<br>**26** (79/1088) | N/A |
| **Super Ball** | **45** (116/1904)<br>**9** (114/1904)<br>**52** (113/1904)<br>**3** (113/1904)<br>**74** (113/1904) | **I** (95/1904)<br>**T** (86/1904)<br>**V** (84/1904)<br>**D** (84/1904)<br>**A** (82/1904) |
| **Supiri Dhana Sampatha** | **0** (535/1062)<br>**2** (528/1062)<br>**3** (527/1062)<br>**7** (523/1062)<br>**8** (503/1062) | **V** (56/1062)<br>**K** (51/1062)<br>**T** (50/1062)<br>**S** (48/1062)<br>**G** (47/1062) |

