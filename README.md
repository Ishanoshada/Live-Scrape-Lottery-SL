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

> **Last Updated (Sri Lanka Time):** `2026-11-02 02:49:23 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 381 Rows | 18.39 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 21 Rows | 906 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 389 Rows | 16.67 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 388 Rows | 16.44 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 388 Rows | 16.02 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 388 Rows | 16.50 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 388 Rows | 17.55 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 379 Rows | 14.80 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 388 Rows | 17.67 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1907 Rows | 72.93 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1795 Rows | 73.37 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1914 Rows | 71.33 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1092 Rows | 36.26 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1908 Rows | 72.97 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1066 Rows | 39.70 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-02 02:49:23 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (139/381)<br>**3** (135/381)<br>**5** (135/381)<br>**6** (132/381)<br>**4** (132/381) | **D** (25/381)<br>**J** (23/381)<br>**Q** (22/381)<br>**N** (21/381)<br>**G** (21/381) |
| **Ayubo** | **5** (10/21)<br>**2** (9/21)<br>**7** (9/21)<br>**8** (8/21)<br>**4** (8/21) | **K** (2/21)<br>**V** (2/21)<br>**W** (2/21)<br>**U** (2/21)<br>**J** (1/21) |
| **Dhana Nidhanaya** | **9** (34/389)<br>**4** (30/389)<br>**7** (30/389)<br>**80** (28/389)<br>**6** (28/389) | **U** (21/389)<br>**W** (21/389)<br>**M** (21/389)<br>**Z** (19/389)<br>**F** (19/389) |
| **Govisetha** | **55** (30/388)<br>**10** (28/388)<br>**32** (27/388)<br>**44** (26/388)<br>**14** (26/388) | **P** (20/388)<br>**I** (20/388)<br>**W** (19/388)<br>**Y** (18/388)<br>**C** (18/388) |
| **Handahana** | **55** (35/388)<br>**11** (34/388)<br>**58** (34/388)<br>**6** (34/388)<br>**60** (32/388) | N/A |
| **Mahajana Sampatha** | **2** (195/388)<br>**5** (190/388)<br>**1** (190/388)<br>**3** (189/388)<br>**8** (185/388) | **D** (25/388)<br>**J** (23/388)<br>**Q** (22/388)<br>**G** (21/388)<br>**W** (21/388) |
| **Mega Power** | **13** (43/388)<br>**11** (43/388)<br>**3** (41/388)<br>**26** (41/388)<br>**22** (40/388) | **U** (26/388)<br>**V** (24/388)<br>**T** (23/388)<br>**K** (20/388)<br>**J** (19/388) |
| **Nlb Jaya** | **5** (162/379)<br>**2** (145/379)<br>**0** (142/379)<br>**6** (141/379)<br>**3** (140/379) | **T** (22/379)<br>**I** (21/379)<br>**G** (20/379)<br>**O** (19/379)<br>**P** (18/379) |
| **Suba Dawasak** | **4** (148/388)<br>**3** (142/388)<br>**9** (139/388)<br>**1** (137/388)<br>**2** (136/388) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1907)<br>**20** (125/1907)<br>**57** (125/1907)<br>**29** (118/1907)<br>**38** (118/1907) | **B** (89/1907)<br>**R** (85/1907)<br>**M** (84/1907)<br>**N** (83/1907)<br>**P** (81/1907) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1795)<br>**21** (152/1795)<br>**10** (151/1795)<br>**15** (148/1795)<br>**16** (147/1795) | **H** (90/1795)<br>**U** (81/1795)<br>**M** (80/1795)<br>**S** (76/1795)<br>**G** (76/1795) |
| **Lagna Wasana** | **23** (144/1914)<br>**5** (144/1914)<br>**25** (143/1914)<br>**39** (142/1914)<br>**36** (142/1914) | N/A |
| **Sasiri** | **9** (86/1092)<br>**20** (81/1092)<br>**19** (81/1092)<br>**22** (79/1092)<br>**26** (79/1092) | N/A |
| **Super Ball** | **45** (116/1908)<br>**9** (115/1908)<br>**52** (114/1908)<br>**29** (114/1908)<br>**3** (113/1908) | **I** (96/1908)<br>**T** (86/1908)<br>**V** (84/1908)<br>**D** (84/1908)<br>**A** (83/1908) |
| **Supiri Dhana Sampatha** | **0** (539/1066)<br>**2** (530/1066)<br>**3** (528/1066)<br>**7** (523/1066)<br>**5** (505/1066) | **V** (57/1066)<br>**K** (51/1066)<br>**T** (50/1066)<br>**S** (48/1066)<br>**G** (47/1066) |

