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

> **Last Updated (Sri Lanka Time):** `2026-11-14 04:15:22 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 393 Rows | 18.99 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 33 Rows | 1.37 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 401 Rows | 17.20 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 400 Rows | 16.96 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 400 Rows | 16.54 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 400 Rows | 17.03 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 400 Rows | 18.12 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 391 Rows | 15.28 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 400 Rows | 18.22 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1919 Rows | 73.39 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1807 Rows | 73.86 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1926 Rows | 71.78 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1104 Rows | 36.67 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1920 Rows | 73.43 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1078 Rows | 40.16 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-14 04:15:22 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (144/393)<br>**3** (139/393)<br>**6** (138/393)<br>**5** (137/393)<br>**4** (137/393) | **D** (25/393)<br>**G** (24/393)<br>**N** (23/393)<br>**J** (23/393)<br>**Q** (22/393) |
| **Ayubo** | **9** (16/33)<br>**8** (15/33)<br>**7** (15/33)<br>**5** (14/33)<br>**4** (12/33) | **U** (3/33)<br>**K** (2/33)<br>**J** (2/33)<br>**V** (2/33)<br>**A** (2/33) |
| **Dhana Nidhanaya** | **9** (35/401)<br>**4** (31/401)<br>**7** (30/401)<br>**80** (29/401)<br>**19** (29/401) | **U** (23/401)<br>**W** (21/401)<br>**M** (21/401)<br>**Z** (20/401)<br>**F** (20/401) |
| **Govisetha** | **55** (30/400)<br>**10** (29/400)<br>**32** (27/400)<br>**45** (27/400)<br>**44** (26/400) | **P** (21/400)<br>**I** (20/400)<br>**W** (19/400)<br>**D** (18/400)<br>**A** (18/400) |
| **Handahana** | **6** (36/400)<br>**58** (35/400)<br>**55** (35/400)<br>**11** (34/400)<br>**56** (33/400) | N/A |
| **Mahajana Sampatha** | **2** (201/400)<br>**1** (197/400)<br>**3** (195/400)<br>**5** (194/400)<br>**4** (191/400) | **D** (25/400)<br>**G** (24/400)<br>**J** (23/400)<br>**N** (22/400)<br>**Q** (22/400) |
| **Mega Power** | **13** (45/400)<br>**11** (44/400)<br>**3** (42/400)<br>**26** (41/400)<br>**22** (40/400) | **U** (27/400)<br>**V** (24/400)<br>**T** (23/400)<br>**K** (20/400)<br>**J** (19/400) |
| **Nlb Jaya** | **5** (167/391)<br>**2** (149/391)<br>**6** (146/391)<br>**3** (145/391)<br>**0** (144/391) | **T** (23/391)<br>**I** (22/391)<br>**G** (20/391)<br>**O** (20/391)<br>**P** (18/391) |
| **Suba Dawasak** | **4** (151/400)<br>**3** (143/400)<br>**9** (141/400)<br>**1** (139/400)<br>**2** (138/400) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1919)<br>**20** (126/1919)<br>**57** (125/1919)<br>**29** (119/1919)<br>**13** (119/1919) | **B** (90/1919)<br>**R** (85/1919)<br>**M** (85/1919)<br>**P** (84/1919)<br>**N** (83/1919) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1807)<br>**21** (153/1807)<br>**10** (152/1807)<br>**15** (149/1807)<br>**16** (148/1807) | **H** (90/1807)<br>**U** (82/1807)<br>**M** (80/1807)<br>**S** (77/1807)<br>**X** (77/1807) |
| **Lagna Wasana** | **23** (146/1926)<br>**5** (145/1926)<br>**36** (143/1926)<br>**25** (143/1926)<br>**39** (142/1926) | N/A |
| **Sasiri** | **9** (86/1104)<br>**20** (84/1104)<br>**19** (82/1104)<br>**22** (80/1104)<br>**26** (79/1104) | N/A |
| **Super Ball** | **52** (116/1920)<br>**45** (116/1920)<br>**9** (115/1920)<br>**74** (114/1920)<br>**29** (114/1920) | **I** (96/1920)<br>**V** (86/1920)<br>**T** (86/1920)<br>**D** (84/1920)<br>**A** (83/1920) |
| **Supiri Dhana Sampatha** | **0** (543/1078)<br>**2** (536/1078)<br>**3** (533/1078)<br>**7** (527/1078)<br>**5** (510/1078) | **V** (58/1078)<br>**K** (53/1078)<br>**S** (50/1078)<br>**T** (50/1078)<br>**A** (48/1078) |

