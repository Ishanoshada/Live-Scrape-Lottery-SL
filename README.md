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

> **Last Updated (Sri Lanka Time):** `2026-06-17 01:53:48 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 242 Rows | 11.69 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 250 Rows | 10.71 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 249 Rows | 10.56 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 249 Rows | 10.30 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 249 Rows | 10.61 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 248 Rows | 11.25 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 239 Rows | 9.33 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 248 Rows | 11.46 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1768 Rows | 67.62 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1656 Rows | 67.64 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1775 Rows | 66.15 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 953 Rows | 31.48 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1769 Rows | 67.65 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 927 Rows | 34.46 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-06-17 01:53:48 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (91/242)<br>**5** (90/242)<br>**0** (88/242)<br>**7** (85/242)<br>**2** (83/242) | **J** (15/242)<br>**N** (14/242)<br>**Q** (14/242)<br>**D** (14/242)<br>**Y** (12/242) |
| **Dhana Nidhanaya** | **28** (24/250)<br>**9** (23/250)<br>**6** (21/250)<br>**16** (20/250)<br>**4** (19/250) | **U** (16/250)<br>**W** (13/250)<br>**Z** (12/250)<br>**T** (12/250)<br>**S** (12/250) |
| **Govisetha** | **55** (21/249)<br>**10** (20/249)<br>**44** (19/249)<br>**33** (19/249)<br>**23** (18/249) | **P** (15/249)<br>**C** (14/249)<br>**D** (12/249)<br>**O** (12/249)<br>**M** (12/249) |
| **Handahana** | **21** (25/249)<br>**6** (25/249)<br>**11** (23/249)<br>**55** (23/249)<br>**58** (22/249) | N/A |
| **Mahajana Sampatha** | **1** (124/249)<br>**5** (121/249)<br>**6** (121/249)<br>**4** (120/249)<br>**2** (120/249) | **J** (15/249)<br>**Q** (14/249)<br>**D** (14/249)<br>**N** (13/249)<br>**Y** (12/249) |
| **Mega Power** | **11** (32/248)<br>**3** (29/248)<br>**6** (27/248)<br>**22** (27/248)<br>**19** (27/248) | **V** (18/248)<br>**U** (15/248)<br>**T** (14/248)<br>**K** (14/248)<br>**J** (14/248) |
| **Nlb Jaya** | **5** (104/239)<br>**0** (94/239)<br>**3** (93/239)<br>**2** (90/239)<br>**1** (85/239) | **T** (15/239)<br>**P** (14/239)<br>**I** (14/239)<br>**Y** (14/239)<br>**M** (13/239) |
| **Suba Dawasak** | **3** (104/248)<br>**4** (100/248)<br>**1** (98/248)<br>**9** (93/248)<br>**5** (90/248) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1768)<br>**20** (117/1768)<br>**57** (115/1768)<br>**75** (109/1768)<br>**38** (109/1768) | **B** (82/1768)<br>**P** (79/1768)<br>**M** (79/1768)<br>**R** (78/1768)<br>**I** (76/1768) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1656)<br>**10** (142/1656)<br>**27** (135/1656)<br>**29** (134/1656)<br>**21** (134/1656) | **H** (88/1656)<br>**U** (76/1656)<br>**W** (72/1656)<br>**G** (71/1656)<br>**X** (71/1656) |
| **Lagna Wasana** | **28** (135/1775)<br>**5** (135/1775)<br>**36** (133/1775)<br>**23** (132/1775)<br>**2** (131/1775) | N/A |
| **Sasiri** | **9** (72/953)<br>**20** (71/953)<br>**26** (70/953)<br>**22** (69/953)<br>**19** (67/953) | N/A |
| **Super Ball** | **45** (110/1769)<br>**52** (107/1769)<br>**74** (107/1769)<br>**3** (106/1769)<br>**57** (106/1769) | **I** (89/1769)<br>**D** (81/1769)<br>**V** (80/1769)<br>**T** (79/1769)<br>**A** (79/1769) |
| **Supiri Dhana Sampatha** | **2** (468/927)<br>**0** (468/927)<br>**3** (464/927)<br>**7** (454/927)<br>**5** (444/927) | **K** (46/927)<br>**V** (45/927)<br>**S** (43/927)<br>**M** (43/927)<br>**T** (43/927) |

