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

> **Last Updated (Sri Lanka Time):** `2026-11-26 06:36:16 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 405 Rows | 19.59 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 45 Rows | 1.85 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 413 Rows | 17.73 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 412 Rows | 17.49 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 412 Rows | 17.05 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 412 Rows | 17.56 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 412 Rows | 18.68 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 403 Rows | 15.76 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 412 Rows | 18.86 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1931 Rows | 73.85 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1819 Rows | 74.35 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1938 Rows | 72.22 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1116 Rows | 37.08 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1932 Rows | 73.89 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1090 Rows | 40.62 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-26 06:36:16 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (147/405)<br>**6** (146/405)<br>**8** (143/405)<br>**3** (141/405)<br>**5** (141/405) | **D** (27/405)<br>**G** (25/405)<br>**N** (23/405)<br>**J** (23/405)<br>**Q** (22/405) |
| **Ayubo** | **8** (21/45)<br>**9** (20/45)<br>**5** (19/45)<br>**7** (19/45)<br>**0** (15/45) | **U** (4/45)<br>**Z** (3/45)<br>**T** (3/45)<br>**I** (3/45)<br>**K** (2/45) |
| **Dhana Nidhanaya** | **9** (35/413)<br>**4** (31/413)<br>**7** (31/413)<br>**19** (31/413)<br>**80** (29/413) | **U** (24/413)<br>**W** (22/413)<br>**M** (21/413)<br>**Z** (20/413)<br>**F** (20/413) |
| **Govisetha** | **55** (32/412)<br>**10** (29/412)<br>**32** (27/412)<br>**44** (27/412)<br>**45** (27/412) | **P** (21/412)<br>**I** (20/412)<br>**A** (19/412)<br>**W** (19/412)<br>**C** (19/412) |
| **Handahana** | **58** (37/412)<br>**55** (37/412)<br>**6** (37/412)<br>**11** (34/412)<br>**53** (33/412) | N/A |
| **Mahajana Sampatha** | **2** (204/412)<br>**1** (204/412)<br>**8** (198/412)<br>**5** (198/412)<br>**3** (197/412) | **D** (27/412)<br>**G** (25/412)<br>**J** (23/412)<br>**N** (22/412)<br>**Q** (22/412) |
| **Mega Power** | **13** (47/412)<br>**11** (44/412)<br>**3** (42/412)<br>**26** (42/412)<br>**4** (41/412) | **U** (27/412)<br>**V** (24/412)<br>**T** (23/412)<br>**K** (20/412)<br>**J** (20/412) |
| **Nlb Jaya** | **5** (170/403)<br>**6** (153/403)<br>**2** (153/403)<br>**0** (151/403)<br>**3** (149/403) | **G** (24/403)<br>**T** (23/403)<br>**O** (23/403)<br>**I** (22/403)<br>**P** (19/403) |
| **Suba Dawasak** | **4** (158/412)<br>**3** (147/412)<br>**1** (143/412)<br>**2** (143/412)<br>**9** (142/412) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (129/1931)<br>**20** (127/1931)<br>**57** (126/1931)<br>**29** (120/1931)<br>**13** (120/1931) | **B** (91/1931)<br>**R** (87/1931)<br>**M** (85/1931)<br>**P** (84/1931)<br>**N** (84/1931) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1819)<br>**21** (154/1819)<br>**10** (152/1819)<br>**16** (150/1819)<br>**15** (150/1819) | **H** (90/1819)<br>**U** (82/1819)<br>**M** (80/1819)<br>**S** (77/1819)<br>**X** (77/1819) |
| **Lagna Wasana** | **23** (147/1938)<br>**5** (145/1938)<br>**39** (143/1938)<br>**36** (143/1938)<br>**25** (143/1938) | N/A |
| **Sasiri** | **9** (87/1116)<br>**20** (84/1116)<br>**19** (83/1116)<br>**22** (82/1116)<br>**26** (79/1116) | N/A |
| **Super Ball** | **52** (117/1932)<br>**9** (116/1932)<br>**45** (116/1932)<br>**74** (115/1932)<br>**3** (114/1932) | **I** (97/1932)<br>**V** (86/1932)<br>**T** (86/1932)<br>**A** (85/1932)<br>**D** (84/1932) |
| **Supiri Dhana Sampatha** | **0** (549/1090)<br>**3** (540/1090)<br>**2** (539/1090)<br>**7** (532/1090)<br>**5** (515/1090) | **V** (58/1090)<br>**K** (54/1090)<br>**S** (51/1090)<br>**T** (51/1090)<br>**A** (49/1090) |

