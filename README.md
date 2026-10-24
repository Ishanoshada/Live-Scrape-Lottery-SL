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

> **Last Updated (Sri Lanka Time):** `2026-10-25 01:09:21 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 373 Rows | 18.00 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 13 Rows | 585 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 381 Rows | 16.33 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 380 Rows | 16.09 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 380 Rows | 15.69 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 380 Rows | 16.16 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 380 Rows | 17.19 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 371 Rows | 14.48 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 380 Rows | 17.36 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1899 Rows | 72.63 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1787 Rows | 73.04 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1906 Rows | 71.03 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1084 Rows | 35.98 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1900 Rows | 72.66 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1058 Rows | 39.40 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-25 01:09:22 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (135/373)<br>**2** (135/373)<br>**3** (131/373)<br>**4** (131/373)<br>**6** (130/373) | **D** (24/373)<br>**Q** (22/373)<br>**J** (21/373)<br>**G** (21/373)<br>**N** (20/373) |
| **Ayubo** | **5** (7/13)<br>**9** (7/13)<br>**8** (6/13)<br>**2** (6/13)<br>**7** (6/13) | **K** (2/13)<br>**V** (2/13)<br>**J** (1/13)<br>**A** (1/13)<br>**W** (1/13) |
| **Dhana Nidhanaya** | **9** (33/381)<br>**4** (30/381)<br>**7** (30/381)<br>**19** (28/381)<br>**3** (28/381) | **U** (21/381)<br>**W** (21/381)<br>**M** (20/381)<br>**Z** (19/381)<br>**F** (18/381) |
| **Govisetha** | **55** (29/380)<br>**10** (28/380)<br>**32** (26/380)<br>**44** (26/380)<br>**45** (26/380) | **P** (20/380)<br>**I** (20/380)<br>**Y** (18/380)<br>**C** (18/380)<br>**X** (18/380) |
| **Handahana** | **58** (33/380)<br>**55** (33/380)<br>**6** (33/380)<br>**60** (32/380)<br>**11** (32/380) | N/A |
| **Mahajana Sampatha** | **2** (190/380)<br>**5** (189/380)<br>**1** (187/380)<br>**3** (184/380)<br>**4** (182/380) | **D** (24/380)<br>**Q** (22/380)<br>**J** (21/380)<br>**G** (21/380)<br>**W** (21/380) |
| **Mega Power** | **13** (43/380)<br>**11** (42/380)<br>**3** (41/380)<br>**22** (40/380)<br>**26** (40/380) | **U** (26/380)<br>**V** (24/380)<br>**T** (23/380)<br>**K** (20/380)<br>**J** (19/380) |
| **Nlb Jaya** | **5** (159/371)<br>**2** (140/371)<br>**0** (139/371)<br>**3** (138/371)<br>**6** (138/371) | **T** (22/371)<br>**I** (20/371)<br>**G** (20/371)<br>**P** (18/371)<br>**Y** (17/371) |
| **Suba Dawasak** | **4** (147/380)<br>**3** (142/380)<br>**9** (138/380)<br>**1** (136/380)<br>**2** (136/380) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1899)<br>**20** (125/1899)<br>**57** (124/1899)<br>**38** (118/1899)<br>**13** (117/1899) | **B** (89/1899)<br>**R** (85/1899)<br>**M** (84/1899)<br>**N** (82/1899)<br>**P** (81/1899) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (166/1787)<br>**21** (151/1787)<br>**10** (150/1787)<br>**15** (148/1787)<br>**16** (147/1787) | **H** (90/1787)<br>**U** (81/1787)<br>**M** (79/1787)<br>**G** (76/1787)<br>**S** (75/1787) |
| **Lagna Wasana** | **5** (144/1906)<br>**23** (143/1906)<br>**39** (142/1906)<br>**25** (142/1906)<br>**36** (141/1906) | N/A |
| **Sasiri** | **9** (86/1084)<br>**20** (81/1084)<br>**19** (81/1084)<br>**22** (79/1084)<br>**26** (79/1084) | N/A |
| **Super Ball** | **45** (116/1900)<br>**9** (114/1900)<br>**52** (113/1900)<br>**74** (113/1900)<br>**29** (113/1900) | **I** (95/1900)<br>**T** (86/1900)<br>**V** (84/1900)<br>**D** (84/1900)<br>**A** (82/1900) |
| **Supiri Dhana Sampatha** | **0** (534/1058)<br>**2** (526/1058)<br>**3** (526/1058)<br>**7** (523/1058)<br>**8** (502/1058) | **V** (56/1058)<br>**K** (51/1058)<br>**T** (50/1058)<br>**S** (48/1058)<br>**G** (47/1058) |

