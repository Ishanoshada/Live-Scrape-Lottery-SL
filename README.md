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

> **Last Updated (Sri Lanka Time):** `2026-11-01 02:05:03 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 380 Rows | 18.34 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 20 Rows | 866 Bytes |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 388 Rows | 16.63 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 387 Rows | 16.39 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 387 Rows | 15.98 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 387 Rows | 16.46 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 387 Rows | 17.51 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 378 Rows | 14.76 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 387 Rows | 17.63 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1906 Rows | 72.89 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1794 Rows | 73.33 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1913 Rows | 71.29 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1091 Rows | 36.22 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1907 Rows | 72.93 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1065 Rows | 39.66 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-01 02:05:03 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (139/380)<br>**5** (135/380)<br>**3** (134/380)<br>**4** (132/380)<br>**6** (131/380) | **D** (24/380)<br>**J** (23/380)<br>**Q** (22/380)<br>**N** (21/380)<br>**G** (21/380) |
| **Ayubo** | **5** (10/20)<br>**7** (9/20)<br>**2** (8/20)<br>**4** (8/20)<br>**0** (8/20) | **K** (2/20)<br>**V** (2/20)<br>**W** (2/20)<br>**J** (1/20)<br>**A** (1/20) |
| **Dhana Nidhanaya** | **9** (34/388)<br>**4** (30/388)<br>**7** (30/388)<br>**80** (28/388)<br>**19** (28/388) | **U** (21/388)<br>**W** (21/388)<br>**M** (21/388)<br>**Z** (19/388)<br>**F** (19/388) |
| **Govisetha** | **55** (29/387)<br>**10** (28/387)<br>**32** (27/387)<br>**44** (26/387)<br>**14** (26/387) | **P** (20/387)<br>**I** (20/387)<br>**W** (19/387)<br>**Y** (18/387)<br>**C** (18/387) |
| **Handahana** | **55** (35/387)<br>**11** (34/387)<br>**58** (34/387)<br>**6** (34/387)<br>**60** (32/387) | N/A |
| **Mahajana Sampatha** | **2** (195/387)<br>**5** (190/387)<br>**1** (190/387)<br>**3** (188/387)<br>**8** (184/387) | **D** (24/387)<br>**J** (23/387)<br>**Q** (22/387)<br>**G** (21/387)<br>**W** (21/387) |
| **Mega Power** | **13** (43/387)<br>**11** (43/387)<br>**3** (41/387)<br>**26** (41/387)<br>**22** (40/387) | **U** (26/387)<br>**V** (24/387)<br>**T** (23/387)<br>**K** (20/387)<br>**J** (19/387) |
| **Nlb Jaya** | **5** (162/378)<br>**2** (144/378)<br>**0** (142/378)<br>**6** (141/378)<br>**3** (140/378) | **T** (22/378)<br>**I** (21/378)<br>**G** (20/378)<br>**O** (19/378)<br>**P** (18/378) |
| **Suba Dawasak** | **4** (148/387)<br>**3** (142/387)<br>**9** (138/387)<br>**1** (137/387)<br>**2** (136/387) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1906)<br>**20** (125/1906)<br>**57** (125/1906)<br>**29** (118/1906)<br>**38** (118/1906) | **B** (89/1906)<br>**R** (85/1906)<br>**M** (84/1906)<br>**N** (83/1906)<br>**P** (81/1906) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1794)<br>**21** (152/1794)<br>**10** (151/1794)<br>**15** (148/1794)<br>**16** (147/1794) | **H** (90/1794)<br>**U** (81/1794)<br>**M** (80/1794)<br>**S** (76/1794)<br>**G** (76/1794) |
| **Lagna Wasana** | **23** (144/1913)<br>**5** (144/1913)<br>**25** (143/1913)<br>**39** (142/1913)<br>**36** (142/1913) | N/A |
| **Sasiri** | **9** (86/1091)<br>**20** (81/1091)<br>**19** (81/1091)<br>**22** (79/1091)<br>**26** (79/1091) | N/A |
| **Super Ball** | **45** (116/1907)<br>**9** (115/1907)<br>**29** (114/1907)<br>**52** (113/1907)<br>**3** (113/1907) | **I** (96/1907)<br>**T** (86/1907)<br>**V** (84/1907)<br>**D** (84/1907)<br>**A** (83/1907) |
| **Supiri Dhana Sampatha** | **0** (538/1065)<br>**2** (529/1065)<br>**3** (528/1065)<br>**7** (523/1065)<br>**5** (505/1065) | **V** (56/1065)<br>**K** (51/1065)<br>**T** (50/1065)<br>**S** (48/1065)<br>**G** (47/1065) |

