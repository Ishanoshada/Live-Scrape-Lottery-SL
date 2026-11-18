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

> **Last Updated (Sri Lanka Time):** `2026-11-19 04:59:07 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 398 Rows | 19.24 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 38 Rows | 1.57 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 406 Rows | 17.42 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 405 Rows | 17.18 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 405 Rows | 16.75 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 405 Rows | 17.25 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 405 Rows | 18.35 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 396 Rows | 15.48 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 405 Rows | 18.49 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1924 Rows | 73.58 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1812 Rows | 74.07 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1931 Rows | 71.96 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1109 Rows | 36.84 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1925 Rows | 73.62 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1083 Rows | 40.35 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-19 04:59:07 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (145/398)<br>**6** (140/398)<br>**3** (140/398)<br>**8** (139/398)<br>**5** (139/398) | **D** (26/398)<br>**G** (25/398)<br>**N** (23/398)<br>**J** (23/398)<br>**Q** (22/398) |
| **Ayubo** | **9** (18/38)<br>**8** (17/38)<br>**7** (16/38)<br>**5** (16/38)<br>**4** (14/38) | **T** (3/38)<br>**U** (3/38)<br>**K** (2/38)<br>**J** (2/38)<br>**V** (2/38) |
| **Dhana Nidhanaya** | **9** (35/406)<br>**4** (31/406)<br>**7** (30/406)<br>**19** (30/406)<br>**80** (29/406) | **U** (24/406)<br>**W** (21/406)<br>**M** (21/406)<br>**Z** (20/406)<br>**F** (20/406) |
| **Govisetha** | **55** (30/405)<br>**10** (29/405)<br>**32** (27/405)<br>**45** (27/405)<br>**60** (26/405) | **P** (21/405)<br>**I** (20/405)<br>**W** (19/405)<br>**C** (19/405)<br>**D** (18/405) |
| **Handahana** | **55** (37/405)<br>**6** (37/405)<br>**58** (36/405)<br>**11** (34/405)<br>**56** (33/405) | N/A |
| **Mahajana Sampatha** | **2** (202/405)<br>**1** (201/405)<br>**3** (196/405)<br>**5** (196/405)<br>**8** (194/405) | **D** (26/405)<br>**G** (25/405)<br>**J** (23/405)<br>**N** (22/405)<br>**Q** (22/405) |
| **Mega Power** | **13** (46/405)<br>**11** (44/405)<br>**3** (42/405)<br>**26** (41/405)<br>**4** (41/405) | **U** (27/405)<br>**V** (24/405)<br>**T** (23/405)<br>**K** (20/405)<br>**J** (20/405) |
| **Nlb Jaya** | **5** (169/396)<br>**2** (150/396)<br>**6** (148/396)<br>**0** (147/396)<br>**3** (146/396) | **T** (23/396)<br>**I** (22/396)<br>**G** (22/396)<br>**O** (21/396)<br>**P** (19/396) |
| **Suba Dawasak** | **4** (154/405)<br>**3** (143/405)<br>**1** (142/405)<br>**9** (142/405)<br>**2** (140/405) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1924)<br>**20** (127/1924)<br>**57** (125/1924)<br>**29** (120/1924)<br>**13** (119/1924) | **B** (91/1924)<br>**R** (86/1924)<br>**M** (85/1924)<br>**P** (84/1924)<br>**N** (83/1924) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1812)<br>**21** (154/1812)<br>**10** (152/1812)<br>**16** (150/1812)<br>**15** (149/1812) | **H** (90/1812)<br>**U** (82/1812)<br>**M** (80/1812)<br>**S** (77/1812)<br>**X** (77/1812) |
| **Lagna Wasana** | **23** (146/1931)<br>**5** (145/1931)<br>**36** (143/1931)<br>**25** (143/1931)<br>**39** (142/1931) | N/A |
| **Sasiri** | **9** (87/1109)<br>**20** (84/1109)<br>**19** (83/1109)<br>**22** (80/1109)<br>**26** (79/1109) | N/A |
| **Super Ball** | **52** (116/1925)<br>**9** (116/1925)<br>**45** (116/1925)<br>**3** (114/1925)<br>**74** (114/1925) | **I** (96/1925)<br>**V** (86/1925)<br>**T** (86/1925)<br>**A** (85/1925)<br>**D** (84/1925) |
| **Supiri Dhana Sampatha** | **0** (546/1083)<br>**2** (538/1083)<br>**3** (535/1083)<br>**7** (530/1083)<br>**5** (512/1083) | **V** (58/1083)<br>**K** (54/1083)<br>**T** (51/1083)<br>**S** (50/1083)<br>**A** (48/1083) |

