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

> **Last Updated (Sri Lanka Time):** `2026-10-28 02:55:59 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 376 Rows | 18.14 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 16 Rows | 703 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 384 Rows | 16.46 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 383 Rows | 16.22 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 383 Rows | 15.81 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 383 Rows | 16.29 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 383 Rows | 17.32 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 374 Rows | 14.60 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 383 Rows | 17.47 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1902 Rows | 72.74 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1790 Rows | 73.16 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1909 Rows | 71.14 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1087 Rows | 36.08 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1903 Rows | 72.78 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1061 Rows | 39.51 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-10-28 02:55:59 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (136/376)<br>**5** (135/376)<br>**3** (132/376)<br>**4** (132/376)<br>**6** (131/376) | **D** (24/376)<br>**Q** (22/376)<br>**J** (22/376)<br>**N** (21/376)<br>**G** (21/376) |
| **Ayubo** | **9** (8/16)<br>**7** (7/16)<br>**2** (7/16)<br>**5** (7/16)<br>**0** (7/16) | **K** (2/16)<br>**V** (2/16)<br>**W** (2/16)<br>**J** (1/16)<br>**A** (1/16) |
| **Dhana Nidhanaya** | **9** (33/384)<br>**4** (30/384)<br>**7** (30/384)<br>**19** (28/384)<br>**3** (28/384) | **U** (21/384)<br>**W** (21/384)<br>**M** (20/384)<br>**Z** (19/384)<br>**F** (19/384) |
| **Govisetha** | **55** (29/383)<br>**10** (28/383)<br>**32** (27/383)<br>**44** (26/383)<br>**14** (26/383) | **P** (20/383)<br>**I** (20/383)<br>**W** (18/383)<br>**Y** (18/383)<br>**C** (18/383) |
| **Handahana** | **58** (34/383)<br>**11** (34/383)<br>**6** (34/383)<br>**55** (33/383)<br>**60** (32/383) | N/A |
| **Mahajana Sampatha** | **2** (192/383)<br>**5** (189/383)<br>**1** (189/383)<br>**3** (185/383)<br>**4** (183/383) | **D** (24/383)<br>**Q** (22/383)<br>**J** (22/383)<br>**G** (21/383)<br>**W** (21/383) |
| **Mega Power** | **13** (43/383)<br>**11** (42/383)<br>**3** (41/383)<br>**22** (40/383)<br>**26** (40/383) | **U** (26/383)<br>**V** (24/383)<br>**T** (23/383)<br>**K** (20/383)<br>**J** (19/383) |
| **Nlb Jaya** | **5** (161/374)<br>**2** (141/374)<br>**6** (140/374)<br>**0** (140/374)<br>**3** (139/374) | **T** (22/374)<br>**I** (21/374)<br>**G** (20/374)<br>**P** (18/374)<br>**O** (18/374) |
| **Suba Dawasak** | **4** (147/383)<br>**3** (142/383)<br>**9** (138/383)<br>**1** (136/383)<br>**2** (136/383) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1902)<br>**20** (125/1902)<br>**57** (124/1902)<br>**38** (118/1902)<br>**13** (117/1902) | **B** (89/1902)<br>**R** (85/1902)<br>**M** (84/1902)<br>**N** (82/1902)<br>**P** (81/1902) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (166/1790)<br>**21** (151/1790)<br>**10** (150/1790)<br>**15** (148/1790)<br>**16** (147/1790) | **H** (90/1790)<br>**U** (81/1790)<br>**M** (79/1790)<br>**S** (76/1790)<br>**G** (76/1790) |
| **Lagna Wasana** | **5** (144/1909)<br>**23** (143/1909)<br>**25** (143/1909)<br>**39** (142/1909)<br>**36** (141/1909) | N/A |
| **Sasiri** | **9** (86/1087)<br>**20** (81/1087)<br>**19** (81/1087)<br>**22** (79/1087)<br>**26** (79/1087) | N/A |
| **Super Ball** | **45** (116/1903)<br>**9** (114/1903)<br>**52** (113/1903)<br>**3** (113/1903)<br>**74** (113/1903) | **I** (95/1903)<br>**T** (86/1903)<br>**V** (84/1903)<br>**D** (84/1903)<br>**A** (82/1903) |
| **Supiri Dhana Sampatha** | **0** (534/1061)<br>**2** (527/1061)<br>**3** (527/1061)<br>**7** (523/1061)<br>**8** (503/1061) | **V** (56/1061)<br>**K** (51/1061)<br>**T** (50/1061)<br>**S** (48/1061)<br>**G** (47/1061) |

