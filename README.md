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

> **Last Updated (Sri Lanka Time):** `2026-10-26 01:21:27 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 374 Rows | 18.05 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 14 Rows | 624 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 382 Rows | 16.37 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 381 Rows | 16.13 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 381 Rows | 15.73 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 381 Rows | 16.20 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 381 Rows | 17.23 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 372 Rows | 14.52 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 381 Rows | 17.39 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1900 Rows | 72.66 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1788 Rows | 73.08 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1907 Rows | 71.07 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1085 Rows | 36.02 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1901 Rows | 72.70 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1059 Rows | 39.43 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-26 01:21:27 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/374)<br>**2** (135/374)<br>**4** (132/374)<br>**3** (131/374)<br>**6** (130/374) | **D** (24/374)<br>**Q** (22/374)<br>**J** (22/374)<br>**G** (21/374)<br>**N** (20/374) |
| **Ayubo** | **9** (8/14)<br>**5** (7/14)<br>**7** (7/14)<br>**2** (6/14)<br>**8** (6/14) | **K** (2/14)<br>**V** (2/14)<br>**W** (2/14)<br>**J** (1/14)<br>**A** (1/14) |
| **Dhana Nidhanaya** | **9** (33/382)<br>**4** (30/382)<br>**7** (30/382)<br>**19** (28/382)<br>**3** (28/382) | **U** (21/382)<br>**W** (21/382)<br>**M** (20/382)<br>**Z** (19/382)<br>**F** (18/382) |
| **Govisetha** | **55** (29/381)<br>**10** (28/381)<br>**32** (26/381)<br>**44** (26/381)<br>**14** (26/381) | **P** (20/381)<br>**I** (20/381)<br>**Y** (18/381)<br>**C** (18/381)<br>**X** (18/381) |
| **Handahana** | **6** (34/381)<br>**58** (33/381)<br>**11** (33/381)<br>**55** (33/381)<br>**60** (32/381) | N/A |
| **Mahajana Sampatha** | **2** (191/381)<br>**5** (189/381)<br>**1** (187/381)<br>**3** (184/381)<br>**4** (183/381) | **D** (24/381)<br>**Q** (22/381)<br>**J** (22/381)<br>**G** (21/381)<br>**W** (21/381) |
| **Mega Power** | **13** (43/381)<br>**11** (42/381)<br>**3** (41/381)<br>**22** (40/381)<br>**26** (40/381) | **U** (26/381)<br>**V** (24/381)<br>**T** (23/381)<br>**K** (20/381)<br>**J** (19/381) |
| **Nlb Jaya** | **5** (160/372)<br>**2** (141/372)<br>**3** (139/372)<br>**0** (139/372)<br>**6** (138/372) | **T** (22/372)<br>**I** (20/372)<br>**G** (20/372)<br>**P** (18/372)<br>**Y** (17/372) |
| **Suba Dawasak** | **4** (147/381)<br>**3** (142/381)<br>**9** (138/381)<br>**1** (136/381)<br>**2** (136/381) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1900)<br>**20** (125/1900)<br>**57** (124/1900)<br>**38** (118/1900)<br>**13** (117/1900) | **B** (89/1900)<br>**R** (85/1900)<br>**M** (84/1900)<br>**N** (82/1900)<br>**P** (81/1900) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (166/1788)<br>**21** (151/1788)<br>**10** (150/1788)<br>**15** (148/1788)<br>**16** (147/1788) | **H** (90/1788)<br>**U** (81/1788)<br>**M** (79/1788)<br>**S** (76/1788)<br>**G** (76/1788) |
| **Lagna Wasana** | **5** (144/1907)<br>**23** (143/1907)<br>**39** (142/1907)<br>**25** (142/1907)<br>**36** (141/1907) | N/A |
| **Sasiri** | **9** (86/1085)<br>**20** (81/1085)<br>**19** (81/1085)<br>**22** (79/1085)<br>**26** (79/1085) | N/A |
| **Super Ball** | **45** (116/1901)<br>**9** (114/1901)<br>**52** (113/1901)<br>**3** (113/1901)<br>**74** (113/1901) | **I** (95/1901)<br>**T** (86/1901)<br>**V** (84/1901)<br>**D** (84/1901)<br>**A** (82/1901) |
| **Supiri Dhana Sampatha** | **0** (534/1059)<br>**2** (526/1059)<br>**3** (526/1059)<br>**7** (523/1059)<br>**8** (503/1059) | **V** (56/1059)<br>**K** (51/1059)<br>**T** (50/1059)<br>**S** (48/1059)<br>**G** (47/1059) |

