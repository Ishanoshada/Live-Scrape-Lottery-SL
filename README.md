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

> **Last Updated (Sri Lanka Time):** `2026-11-07 03:45:11 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 386 Rows | 18.64 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 26 Rows | 1.09 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 394 Rows | 16.89 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 393 Rows | 16.66 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 393 Rows | 16.24 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 393 Rows | 16.72 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 393 Rows | 17.79 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 383 Rows | 14.96 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 392 Rows | 17.83 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1912 Rows | 73.12 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1800 Rows | 73.57 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1919 Rows | 71.52 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1097 Rows | 36.43 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1913 Rows | 73.16 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1071 Rows | 39.89 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-07 03:45:11 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (141/386)<br>**3** (137/386)<br>**5** (136/386)<br>**6** (135/386)<br>**4** (133/386) | **D** (25/386)<br>**J** (23/386)<br>**N** (22/386)<br>**Q** (22/386)<br>**G** (22/386) |
| **Ayubo** | **5** (12/26)<br>**7** (12/26)<br>**9** (11/26)<br>**4** (10/26)<br>**2** (10/26) | **K** (2/26)<br>**V** (2/26)<br>**W** (2/26)<br>**F** (2/26)<br>**U** (2/26) |
| **Dhana Nidhanaya** | **9** (34/394)<br>**4** (31/394)<br>**7** (30/394)<br>**80** (28/394)<br>**28** (28/394) | **U** (23/394)<br>**W** (21/394)<br>**M** (21/394)<br>**Z** (19/394)<br>**F** (19/394) |
| **Govisetha** | **55** (30/393)<br>**10** (28/393)<br>**32** (27/393)<br>**44** (26/393)<br>**14** (26/393) | **P** (21/393)<br>**I** (20/393)<br>**W** (19/393)<br>**D** (18/393)<br>**Y** (18/393) |
| **Handahana** | **55** (35/393)<br>**6** (35/393)<br>**11** (34/393)<br>**58** (34/393)<br>**56** (33/393) | N/A |
| **Mahajana Sampatha** | **2** (198/393)<br>**1** (194/393)<br>**3** (192/393)<br>**5** (191/393)<br>**8** (187/393) | **D** (25/393)<br>**J** (23/393)<br>**Q** (22/393)<br>**G** (22/393)<br>**N** (21/393) |
| **Mega Power** | **13** (45/393)<br>**11** (43/393)<br>**3** (41/393)<br>**26** (41/393)<br>**22** (40/393) | **U** (26/393)<br>**V** (24/393)<br>**T** (23/393)<br>**K** (20/393)<br>**J** (19/393) |
| **Nlb Jaya** | **5** (164/383)<br>**2** (145/383)<br>**3** (142/383)<br>**0** (142/383)<br>**6** (141/383) | **T** (23/383)<br>**I** (22/383)<br>**G** (20/383)<br>**O** (19/383)<br>**P** (18/383) |
| **Suba Dawasak** | **4** (148/392)<br>**3** (142/392)<br>**9** (139/392)<br>**1** (138/392)<br>**2** (136/392) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1912)<br>**20** (125/1912)<br>**57** (125/1912)<br>**29** (118/1912)<br>**38** (118/1912) | **B** (90/1912)<br>**R** (85/1912)<br>**M** (85/1912)<br>**N** (83/1912)<br>**P** (82/1912) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1800)<br>**21** (153/1800)<br>**10** (152/1800)<br>**15** (149/1800)<br>**16** (148/1800) | **H** (90/1800)<br>**U** (82/1800)<br>**M** (80/1800)<br>**S** (77/1800)<br>**D** (76/1800) |
| **Lagna Wasana** | **23** (145/1919)<br>**5** (145/1919)<br>**25** (143/1919)<br>**39** (142/1919)<br>**36** (142/1919) | N/A |
| **Sasiri** | **9** (86/1097)<br>**20** (82/1097)<br>**19** (81/1097)<br>**22** (79/1097)<br>**26** (79/1097) | N/A |
| **Super Ball** | **52** (116/1913)<br>**45** (116/1913)<br>**9** (115/1913)<br>**29** (114/1913)<br>**3** (113/1913) | **I** (96/1913)<br>**T** (86/1913)<br>**V** (85/1913)<br>**D** (84/1913)<br>**A** (83/1913) |
| **Supiri Dhana Sampatha** | **0** (539/1071)<br>**2** (533/1071)<br>**3** (531/1071)<br>**7** (526/1071)<br>**5** (507/1071) | **V** (57/1071)<br>**K** (52/1071)<br>**T** (50/1071)<br>**S** (49/1071)<br>**G** (47/1071) |

