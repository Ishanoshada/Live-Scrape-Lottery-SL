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

> **Last Updated (Sri Lanka Time):** `2026-11-17 06:26:53 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 396 Rows | 19.14 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 36 Rows | 1.49 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 404 Rows | 17.33 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 403 Rows | 17.09 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 403 Rows | 16.67 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 403 Rows | 17.16 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 403 Rows | 18.25 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 394 Rows | 15.40 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 403 Rows | 18.38 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1922 Rows | 73.50 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1810 Rows | 73.98 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1929 Rows | 71.89 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1107 Rows | 36.77 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1923 Rows | 73.54 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1081 Rows | 40.27 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-17 06:26:53 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (145/396)<br>**3** (139/396)<br>**6** (139/396)<br>**4** (138/396)<br>**8** (137/396) | **D** (26/396)<br>**G** (25/396)<br>**N** (23/396)<br>**J** (23/396)<br>**Q** (22/396) |
| **Ayubo** | **8** (17/36)<br>**9** (17/36)<br>**5** (16/36)<br>**7** (16/36)<br>**4** (13/36) | **U** (3/36)<br>**K** (2/36)<br>**J** (2/36)<br>**V** (2/36)<br>**A** (2/36) |
| **Dhana Nidhanaya** | **9** (35/404)<br>**4** (31/404)<br>**7** (30/404)<br>**80** (29/404)<br>**19** (29/404) | **U** (23/404)<br>**W** (21/404)<br>**M** (21/404)<br>**Z** (20/404)<br>**F** (20/404) |
| **Govisetha** | **55** (30/403)<br>**10** (29/403)<br>**32** (27/403)<br>**45** (27/403)<br>**60** (26/403) | **P** (21/403)<br>**I** (20/403)<br>**W** (19/403)<br>**C** (19/403)<br>**D** (18/403) |
| **Handahana** | **6** (37/403)<br>**58** (36/403)<br>**55** (36/403)<br>**11** (34/403)<br>**56** (33/403) | N/A |
| **Mahajana Sampatha** | **2** (202/403)<br>**1** (200/403)<br>**3** (195/403)<br>**5** (194/403)<br>**8** (192/403) | **D** (26/403)<br>**G** (25/403)<br>**J** (23/403)<br>**N** (22/403)<br>**Q** (22/403) |
| **Mega Power** | **13** (46/403)<br>**11** (44/403)<br>**3** (42/403)<br>**26** (41/403)<br>**22** (40/403) | **U** (27/403)<br>**V** (24/403)<br>**T** (23/403)<br>**K** (20/403)<br>**J** (19/403) |
| **Nlb Jaya** | **5** (169/394)<br>**2** (149/394)<br>**0** (147/394)<br>**6** (146/394)<br>**3** (145/394) | **T** (23/394)<br>**I** (22/394)<br>**G** (21/394)<br>**O** (21/394)<br>**P** (18/394) |
| **Suba Dawasak** | **4** (152/403)<br>**3** (143/403)<br>**9** (142/403)<br>**1** (140/403)<br>**2** (139/403) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1922)<br>**20** (126/1922)<br>**57** (125/1922)<br>**29** (120/1922)<br>**13** (119/1922) | **B** (91/1922)<br>**R** (86/1922)<br>**M** (85/1922)<br>**P** (84/1922)<br>**N** (83/1922) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1810)<br>**21** (153/1810)<br>**10** (152/1810)<br>**16** (149/1810)<br>**15** (149/1810) | **H** (90/1810)<br>**U** (82/1810)<br>**M** (80/1810)<br>**S** (77/1810)<br>**X** (77/1810) |
| **Lagna Wasana** | **23** (146/1929)<br>**5** (145/1929)<br>**36** (143/1929)<br>**25** (143/1929)<br>**39** (142/1929) | N/A |
| **Sasiri** | **9** (87/1107)<br>**20** (84/1107)<br>**19** (82/1107)<br>**22** (80/1107)<br>**26** (79/1107) | N/A |
| **Super Ball** | **52** (116/1923)<br>**9** (116/1923)<br>**45** (116/1923)<br>**3** (114/1923)<br>**74** (114/1923) | **I** (96/1923)<br>**V** (86/1923)<br>**T** (86/1923)<br>**D** (84/1923)<br>**A** (84/1923) |
| **Supiri Dhana Sampatha** | **0** (545/1081)<br>**2** (537/1081)<br>**3** (534/1081)<br>**7** (528/1081)<br>**5** (510/1081) | **V** (58/1081)<br>**K** (54/1081)<br>**S** (50/1081)<br>**T** (50/1081)<br>**A** (48/1081) |

