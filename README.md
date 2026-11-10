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

> **Last Updated (Sri Lanka Time):** `2026-11-10 06:18:18 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 389 Rows | 18.79 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 29 Rows | 1.21 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 397 Rows | 17.03 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 396 Rows | 16.79 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 396 Rows | 16.37 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 396 Rows | 16.85 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 396 Rows | 17.93 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 387 Rows | 15.12 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 396 Rows | 18.00 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1915 Rows | 73.24 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1803 Rows | 73.69 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1922 Rows | 71.63 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1100 Rows | 36.53 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1916 Rows | 73.27 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1074 Rows | 40.00 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-10 06:18:18 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (142/389)<br>**3** (139/389)<br>**5** (136/389)<br>**6** (135/389)<br>**4** (135/389) | **D** (25/389)<br>**G** (24/389)<br>**N** (23/389)<br>**J** (23/389)<br>**Q** (22/389) |
| **Ayubo** | **7** (14/29)<br>**5** (14/29)<br>**9** (13/29)<br>**8** (12/29)<br>**2** (10/29) | **K** (2/29)<br>**V** (2/29)<br>**W** (2/29)<br>**T** (2/29)<br>**F** (2/29) |
| **Dhana Nidhanaya** | **9** (34/397)<br>**4** (31/397)<br>**7** (30/397)<br>**80** (29/397)<br>**19** (29/397) | **U** (23/397)<br>**W** (21/397)<br>**M** (21/397)<br>**Z** (20/397)<br>**F** (19/397) |
| **Govisetha** | **55** (30/396)<br>**10** (29/396)<br>**32** (27/396)<br>**44** (26/396)<br>**14** (26/396) | **P** (21/396)<br>**I** (20/396)<br>**W** (19/396)<br>**D** (18/396)<br>**A** (18/396) |
| **Handahana** | **6** (36/396)<br>**58** (35/396)<br>**55** (35/396)<br>**11** (34/396)<br>**56** (33/396) | N/A |
| **Mahajana Sampatha** | **2** (199/396)<br>**1** (196/396)<br>**3** (194/396)<br>**5** (192/396)<br>**9** (189/396) | **D** (25/396)<br>**G** (24/396)<br>**J** (23/396)<br>**N** (22/396)<br>**Q** (22/396) |
| **Mega Power** | **13** (45/396)<br>**11** (43/396)<br>**3** (41/396)<br>**26** (41/396)<br>**22** (40/396) | **U** (27/396)<br>**V** (24/396)<br>**T** (23/396)<br>**K** (20/396)<br>**J** (19/396) |
| **Nlb Jaya** | **5** (166/387)<br>**2** (148/387)<br>**3** (144/387)<br>**6** (143/387)<br>**0** (143/387) | **T** (23/387)<br>**I** (22/387)<br>**G** (20/387)<br>**O** (20/387)<br>**P** (18/387) |
| **Suba Dawasak** | **4** (148/396)<br>**3** (143/396)<br>**9** (139/396)<br>**1** (138/396)<br>**2** (136/396) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1915)<br>**20** (126/1915)<br>**57** (125/1915)<br>**13** (119/1915)<br>**29** (118/1915) | **B** (90/1915)<br>**R** (85/1915)<br>**M** (85/1915)<br>**P** (83/1915)<br>**N** (83/1915) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1803)<br>**21** (153/1803)<br>**10** (152/1803)<br>**15** (149/1803)<br>**16** (148/1803) | **H** (90/1803)<br>**U** (82/1803)<br>**M** (80/1803)<br>**S** (77/1803)<br>**X** (77/1803) |
| **Lagna Wasana** | **23** (146/1922)<br>**5** (145/1922)<br>**25** (143/1922)<br>**39** (142/1922)<br>**36** (142/1922) | N/A |
| **Sasiri** | **9** (86/1100)<br>**20** (83/1100)<br>**19** (81/1100)<br>**22** (80/1100)<br>**26** (79/1100) | N/A |
| **Super Ball** | **52** (116/1916)<br>**45** (116/1916)<br>**9** (115/1916)<br>**29** (114/1916)<br>**3** (113/1916) | **I** (96/1916)<br>**T** (86/1916)<br>**V** (85/1916)<br>**D** (84/1916)<br>**A** (83/1916) |
| **Supiri Dhana Sampatha** | **0** (540/1074)<br>**2** (535/1074)<br>**3** (531/1074)<br>**7** (527/1074)<br>**5** (508/1074) | **V** (57/1074)<br>**K** (52/1074)<br>**T** (50/1074)<br>**S** (49/1074)<br>**G** (47/1074) |

