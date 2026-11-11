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

> **Last Updated (Sri Lanka Time):** `2026-11-12 05:06:52 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 391 Rows | 18.89 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 31 Rows | 1.29 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 399 Rows | 17.11 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 398 Rows | 16.88 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 398 Rows | 16.45 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 398 Rows | 16.94 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 398 Rows | 18.02 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 389 Rows | 15.20 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 398 Rows | 18.11 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1917 Rows | 73.31 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1805 Rows | 73.78 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1924 Rows | 71.70 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1102 Rows | 36.60 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1918 Rows | 73.35 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1076 Rows | 40.08 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-12 05:06:53 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (143/391)<br>**3** (139/391)<br>**5** (137/391)<br>**6** (137/391)<br>**4** (136/391) | **D** (25/391)<br>**G** (24/391)<br>**N** (23/391)<br>**J** (23/391)<br>**Q** (22/391) |
| **Ayubo** | **7** (15/31)<br>**5** (14/31)<br>**9** (14/31)<br>**8** (13/31)<br>**2** (11/31) | **K** (2/31)<br>**J** (2/31)<br>**V** (2/31)<br>**W** (2/31)<br>**T** (2/31) |
| **Dhana Nidhanaya** | **9** (34/399)<br>**4** (31/399)<br>**7** (30/399)<br>**80** (29/399)<br>**19** (29/399) | **U** (23/399)<br>**W** (21/399)<br>**M** (21/399)<br>**Z** (20/399)<br>**F** (20/399) |
| **Govisetha** | **55** (30/398)<br>**10** (29/398)<br>**32** (27/398)<br>**45** (27/398)<br>**44** (26/398) | **P** (21/398)<br>**I** (20/398)<br>**W** (19/398)<br>**D** (18/398)<br>**A** (18/398) |
| **Handahana** | **6** (36/398)<br>**58** (35/398)<br>**55** (35/398)<br>**11** (34/398)<br>**56** (33/398) | N/A |
| **Mahajana Sampatha** | **2** (200/398)<br>**1** (196/398)<br>**3** (194/398)<br>**5** (193/398)<br>**9** (190/398) | **D** (25/398)<br>**G** (24/398)<br>**J** (23/398)<br>**N** (22/398)<br>**Q** (22/398) |
| **Mega Power** | **13** (45/398)<br>**11** (43/398)<br>**3** (41/398)<br>**26** (41/398)<br>**22** (40/398) | **U** (27/398)<br>**V** (24/398)<br>**T** (23/398)<br>**K** (20/398)<br>**J** (19/398) |
| **Nlb Jaya** | **5** (166/389)<br>**2** (149/389)<br>**6** (145/389)<br>**3** (144/389)<br>**0** (144/389) | **T** (23/389)<br>**I** (22/389)<br>**G** (20/389)<br>**O** (20/389)<br>**P** (18/389) |
| **Suba Dawasak** | **4** (149/398)<br>**3** (143/398)<br>**9** (140/398)<br>**1** (138/398)<br>**2** (137/398) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1917)<br>**20** (126/1917)<br>**57** (125/1917)<br>**29** (119/1917)<br>**13** (119/1917) | **B** (90/1917)<br>**R** (85/1917)<br>**M** (85/1917)<br>**P** (83/1917)<br>**N** (83/1917) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1805)<br>**21** (153/1805)<br>**10** (152/1805)<br>**15** (149/1805)<br>**16** (148/1805) | **H** (90/1805)<br>**U** (82/1805)<br>**M** (80/1805)<br>**S** (77/1805)<br>**X** (77/1805) |
| **Lagna Wasana** | **23** (146/1924)<br>**5** (145/1924)<br>**25** (143/1924)<br>**39** (142/1924)<br>**36** (142/1924) | N/A |
| **Sasiri** | **9** (86/1102)<br>**20** (84/1102)<br>**19** (81/1102)<br>**22** (80/1102)<br>**26** (79/1102) | N/A |
| **Super Ball** | **52** (116/1918)<br>**45** (116/1918)<br>**9** (115/1918)<br>**74** (114/1918)<br>**29** (114/1918) | **I** (96/1918)<br>**V** (86/1918)<br>**T** (86/1918)<br>**D** (84/1918)<br>**A** (83/1918) |
| **Supiri Dhana Sampatha** | **0** (541/1076)<br>**2** (536/1076)<br>**3** (532/1076)<br>**7** (527/1076)<br>**5** (509/1076) | **V** (58/1076)<br>**K** (52/1076)<br>**T** (50/1076)<br>**S** (49/1076)<br>**A** (48/1076) |

