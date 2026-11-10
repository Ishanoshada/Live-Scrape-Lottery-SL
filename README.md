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

> **Last Updated (Sri Lanka Time):** `2026-11-11 03:58:11 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 390 Rows | 18.84 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 30 Rows | 1.25 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 398 Rows | 17.07 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 397 Rows | 16.83 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 397 Rows | 16.41 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 397 Rows | 16.90 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 397 Rows | 17.98 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 388 Rows | 15.16 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 397 Rows | 18.06 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1916 Rows | 73.27 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1804 Rows | 73.74 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1923 Rows | 71.66 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1101 Rows | 36.56 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1917 Rows | 73.31 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1075 Rows | 40.04 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-11 03:58:11 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (142/390)<br>**3** (139/390)<br>**5** (137/390)<br>**6** (136/390)<br>**4** (136/390) | **D** (25/390)<br>**G** (24/390)<br>**N** (23/390)<br>**J** (23/390)<br>**Q** (22/390) |
| **Ayubo** | **5** (14/30)<br>**7** (14/30)<br>**8** (13/30)<br>**9** (13/30)<br>**4** (11/30) | **K** (2/30)<br>**J** (2/30)<br>**V** (2/30)<br>**W** (2/30)<br>**T** (2/30) |
| **Dhana Nidhanaya** | **9** (34/398)<br>**4** (31/398)<br>**7** (30/398)<br>**80** (29/398)<br>**19** (29/398) | **U** (23/398)<br>**W** (21/398)<br>**M** (21/398)<br>**Z** (20/398)<br>**F** (20/398) |
| **Govisetha** | **55** (30/397)<br>**10** (29/397)<br>**32** (27/397)<br>**44** (26/397)<br>**14** (26/397) | **P** (21/397)<br>**I** (20/397)<br>**W** (19/397)<br>**D** (18/397)<br>**A** (18/397) |
| **Handahana** | **6** (36/397)<br>**58** (35/397)<br>**55** (35/397)<br>**11** (34/397)<br>**56** (33/397) | N/A |
| **Mahajana Sampatha** | **2** (199/397)<br>**1** (196/397)<br>**3** (194/397)<br>**5** (193/397)<br>**8** (189/397) | **D** (25/397)<br>**G** (24/397)<br>**J** (23/397)<br>**N** (22/397)<br>**Q** (22/397) |
| **Mega Power** | **13** (45/397)<br>**11** (43/397)<br>**3** (41/397)<br>**26** (41/397)<br>**22** (40/397) | **U** (27/397)<br>**V** (24/397)<br>**T** (23/397)<br>**K** (20/397)<br>**J** (19/397) |
| **Nlb Jaya** | **5** (166/388)<br>**2** (148/388)<br>**3** (144/388)<br>**6** (144/388)<br>**0** (144/388) | **T** (23/388)<br>**I** (22/388)<br>**G** (20/388)<br>**O** (20/388)<br>**P** (18/388) |
| **Suba Dawasak** | **4** (148/397)<br>**3** (143/397)<br>**9** (140/397)<br>**1** (138/397)<br>**2** (137/397) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1916)<br>**20** (126/1916)<br>**57** (125/1916)<br>**29** (119/1916)<br>**13** (119/1916) | **B** (90/1916)<br>**R** (85/1916)<br>**M** (85/1916)<br>**P** (83/1916)<br>**N** (83/1916) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1804)<br>**21** (153/1804)<br>**10** (152/1804)<br>**15** (149/1804)<br>**16** (148/1804) | **H** (90/1804)<br>**U** (82/1804)<br>**M** (80/1804)<br>**S** (77/1804)<br>**X** (77/1804) |
| **Lagna Wasana** | **23** (146/1923)<br>**5** (145/1923)<br>**25** (143/1923)<br>**39** (142/1923)<br>**36** (142/1923) | N/A |
| **Sasiri** | **9** (86/1101)<br>**20** (83/1101)<br>**19** (81/1101)<br>**22** (80/1101)<br>**26** (79/1101) | N/A |
| **Super Ball** | **52** (116/1917)<br>**45** (116/1917)<br>**9** (115/1917)<br>**74** (114/1917)<br>**29** (114/1917) | **I** (96/1917)<br>**T** (86/1917)<br>**V** (85/1917)<br>**D** (84/1917)<br>**A** (83/1917) |
| **Supiri Dhana Sampatha** | **0** (540/1075)<br>**2** (536/1075)<br>**3** (532/1075)<br>**7** (527/1075)<br>**5** (509/1075) | **V** (58/1075)<br>**K** (52/1075)<br>**T** (50/1075)<br>**S** (49/1075)<br>**G** (47/1075) |

