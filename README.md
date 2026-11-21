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

> **Last Updated (Sri Lanka Time):** `2026-11-22 03:47:56 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 401 Rows | 19.39 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 41 Rows | 1.69 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 409 Rows | 17.55 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 408 Rows | 17.32 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 408 Rows | 16.88 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 408 Rows | 17.39 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 408 Rows | 18.49 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 399 Rows | 15.60 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 408 Rows | 18.65 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1927 Rows | 73.70 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1815 Rows | 74.19 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1934 Rows | 72.08 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1112 Rows | 36.94 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1928 Rows | 73.73 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1086 Rows | 40.47 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-22 03:47:56 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (146/401)<br>**6** (142/401)<br>**3** (141/401)<br>**5** (140/401)<br>**8** (140/401) | **D** (27/401)<br>**G** (25/401)<br>**N** (23/401)<br>**J** (23/401)<br>**Q** (22/401) |
| **Ayubo** | **9** (20/41)<br>**8** (19/41)<br>**7** (18/41)<br>**5** (17/41)<br>**4** (15/41) | **U** (4/41)<br>**T** (3/41)<br>**K** (2/41)<br>**J** (2/41)<br>**V** (2/41) |
| **Dhana Nidhanaya** | **9** (35/409)<br>**4** (31/409)<br>**7** (30/409)<br>**19** (30/409)<br>**80** (29/409) | **U** (24/409)<br>**W** (22/409)<br>**M** (21/409)<br>**Z** (20/409)<br>**F** (20/409) |
| **Govisetha** | **55** (30/408)<br>**10** (29/408)<br>**32** (27/408)<br>**45** (27/408)<br>**60** (26/408) | **P** (21/408)<br>**I** (20/408)<br>**W** (19/408)<br>**C** (19/408)<br>**D** (18/408) |
| **Handahana** | **58** (37/408)<br>**55** (37/408)<br>**6** (37/408)<br>**11** (34/408)<br>**53** (33/408) | N/A |
| **Mahajana Sampatha** | **2** (203/408)<br>**1** (202/408)<br>**3** (197/408)<br>**5** (197/408)<br>**8** (195/408) | **D** (27/408)<br>**G** (25/408)<br>**J** (23/408)<br>**N** (22/408)<br>**Q** (22/408) |
| **Mega Power** | **13** (46/408)<br>**11** (44/408)<br>**3** (42/408)<br>**26** (42/408)<br>**4** (41/408) | **U** (27/408)<br>**V** (24/408)<br>**T** (23/408)<br>**K** (20/408)<br>**J** (20/408) |
| **Nlb Jaya** | **5** (170/399)<br>**2** (150/399)<br>**0** (150/399)<br>**6** (149/399)<br>**3** (148/399) | **T** (23/399)<br>**G** (23/399)<br>**I** (22/399)<br>**O** (21/399)<br>**P** (19/399) |
| **Suba Dawasak** | **4** (156/408)<br>**3** (145/408)<br>**1** (142/408)<br>**9** (142/408)<br>**2** (141/408) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1927)<br>**20** (127/1927)<br>**57** (125/1927)<br>**29** (120/1927)<br>**13** (119/1927) | **B** (91/1927)<br>**R** (87/1927)<br>**M** (85/1927)<br>**P** (84/1927)<br>**N** (84/1927) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1815)<br>**21** (154/1815)<br>**10** (152/1815)<br>**16** (150/1815)<br>**15** (149/1815) | **H** (90/1815)<br>**U** (82/1815)<br>**M** (80/1815)<br>**S** (77/1815)<br>**X** (77/1815) |
| **Lagna Wasana** | **23** (147/1934)<br>**5** (145/1934)<br>**36** (143/1934)<br>**25** (143/1934)<br>**39** (142/1934) | N/A |
| **Sasiri** | **9** (87/1112)<br>**20** (84/1112)<br>**19** (83/1112)<br>**22** (81/1112)<br>**26** (79/1112) | N/A |
| **Super Ball** | **52** (116/1928)<br>**9** (116/1928)<br>**45** (116/1928)<br>**74** (115/1928)<br>**3** (114/1928) | **I** (96/1928)<br>**V** (86/1928)<br>**T** (86/1928)<br>**A** (85/1928)<br>**D** (84/1928) |
| **Supiri Dhana Sampatha** | **0** (547/1086)<br>**2** (538/1086)<br>**3** (537/1086)<br>**7** (532/1086)<br>**5** (513/1086) | **V** (58/1086)<br>**K** (54/1086)<br>**S** (51/1086)<br>**T** (51/1086)<br>**G** (48/1086) |

