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

> **Last Updated (Sri Lanka Time):** `2026-11-08 02:30:43 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 387 Rows | 18.69 KB |
| Ayubo | [ayubo.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ayubo.txt) | 27 Rows | 1.13 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 395 Rows | 16.94 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 394 Rows | 16.70 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 394 Rows | 16.28 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 394 Rows | 16.77 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 394 Rows | 17.84 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 385 Rows | 15.04 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 394 Rows | 17.91 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1913 Rows | 73.16 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1801 Rows | 73.61 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1920 Rows | 71.55 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 1098 Rows | 36.46 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1914 Rows | 73.20 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 1072 Rows | 39.93 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-11-08 02:30:43 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **2** (142/387)<br>**3** (138/387)<br>**5** (136/387)<br>**6** (135/387)<br>**8** (133/387) | **D** (25/387)<br>**J** (23/387)<br>**G** (23/387)<br>**N** (22/387)<br>**Q** (22/387) |
| **Ayubo** | **7** (13/27)<br>**5** (12/27)<br>**9** (12/27)<br>**0** (10/27)<br>**2** (10/27) | **K** (2/27)<br>**V** (2/27)<br>**W** (2/27)<br>**F** (2/27)<br>**U** (2/27) |
| **Dhana Nidhanaya** | **9** (34/395)<br>**4** (31/395)<br>**7** (30/395)<br>**80** (28/395)<br>**28** (28/395) | **U** (23/395)<br>**W** (21/395)<br>**M** (21/395)<br>**Z** (19/395)<br>**F** (19/395) |
| **Govisetha** | **55** (30/394)<br>**10** (29/394)<br>**32** (27/394)<br>**44** (26/394)<br>**14** (26/394) | **P** (21/394)<br>**I** (20/394)<br>**W** (19/394)<br>**D** (18/394)<br>**Y** (18/394) |
| **Handahana** | **6** (36/394)<br>**55** (35/394)<br>**11** (34/394)<br>**58** (34/394)<br>**56** (33/394) | N/A |
| **Mahajana Sampatha** | **2** (199/394)<br>**1** (195/394)<br>**3** (193/394)<br>**5** (191/394)<br>**8** (188/394) | **D** (25/394)<br>**J** (23/394)<br>**G** (23/394)<br>**Q** (22/394)<br>**N** (21/394) |
| **Mega Power** | **13** (45/394)<br>**11** (43/394)<br>**3** (41/394)<br>**26** (41/394)<br>**22** (40/394) | **U** (26/394)<br>**V** (24/394)<br>**T** (23/394)<br>**K** (20/394)<br>**J** (19/394) |
| **Nlb Jaya** | **5** (165/385)<br>**2** (146/385)<br>**3** (144/385)<br>**6** (142/385)<br>**0** (142/385) | **T** (23/385)<br>**I** (22/385)<br>**G** (20/385)<br>**O** (20/385)<br>**P** (18/385) |
| **Suba Dawasak** | **4** (148/394)<br>**3** (142/394)<br>**9** (139/394)<br>**1** (138/394)<br>**2** (136/394) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (128/1913)<br>**20** (125/1913)<br>**57** (125/1913)<br>**13** (119/1913)<br>**29** (118/1913) | **B** (90/1913)<br>**R** (85/1913)<br>**M** (85/1913)<br>**P** (83/1913)<br>**N** (83/1913) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (167/1801)<br>**21** (153/1801)<br>**10** (152/1801)<br>**15** (149/1801)<br>**16** (148/1801) | **H** (90/1801)<br>**U** (82/1801)<br>**M** (80/1801)<br>**S** (77/1801)<br>**D** (76/1801) |
| **Lagna Wasana** | **23** (146/1920)<br>**5** (145/1920)<br>**25** (143/1920)<br>**39** (142/1920)<br>**36** (142/1920) | N/A |
| **Sasiri** | **9** (86/1098)<br>**20** (82/1098)<br>**19** (81/1098)<br>**22** (79/1098)<br>**26** (79/1098) | N/A |
| **Super Ball** | **52** (116/1914)<br>**45** (116/1914)<br>**9** (115/1914)<br>**29** (114/1914)<br>**3** (113/1914) | **I** (96/1914)<br>**T** (86/1914)<br>**V** (85/1914)<br>**D** (84/1914)<br>**A** (83/1914) |
| **Supiri Dhana Sampatha** | **0** (539/1072)<br>**2** (533/1072)<br>**3** (531/1072)<br>**7** (527/1072)<br>**5** (508/1072) | **V** (57/1072)<br>**K** (52/1072)<br>**T** (50/1072)<br>**S** (49/1072)<br>**G** (47/1072) |

