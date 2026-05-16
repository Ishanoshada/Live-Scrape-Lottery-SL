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

> **Last Updated (Sri Lanka Time):** `2026-05-17 02:09:28 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 214 Rows | 10.41 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 222 Rows | 9.57 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 221 Rows | 9.45 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 221 Rows | 9.22 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 221 Rows | 9.50 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 221 Rows | 10.10 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 212 Rows | 8.33 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 221 Rows | 10.28 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1740 Rows | 66.55 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1628 Rows | 66.49 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1747 Rows | 65.11 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 925 Rows | 30.53 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1741 Rows | 66.58 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 899 Rows | 33.42 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-17 02:09:28 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (82/214)<br>**5** (79/214)<br>**2** (77/214)<br>**7** (76/214)<br>**4** (74/214) | **D** (14/214)<br>**J** (14/214)<br>**N** (13/214)<br>**Q** (12/214)<br>**Y** (12/214) |
| **Dhana Nidhanaya** | **28** (22/222)<br>**9** (20/222)<br>**6** (19/222)<br>**7** (18/222)<br>**16** (18/222) | **U** (14/222)<br>**W** (13/222)<br>**T** (12/222)<br>**M** (12/222)<br>**Q** (11/222) |
| **Govisetha** | **44** (19/221)<br>**19** (17/221)<br>**55** (17/221)<br>**23** (16/221)<br>**58** (16/221) | **P** (13/221)<br>**D** (11/221)<br>**W** (11/221)<br>**O** (11/221)<br>**C** (11/221) |
| **Handahana** | **58** (22/221)<br>**21** (21/221)<br>**6** (21/221)<br>**60** (20/221)<br>**11** (20/221) | N/A |
| **Mahajana Sampatha** | **2** (109/221)<br>**1** (109/221)<br>**6** (109/221)<br>**3** (108/221)<br>**5** (107/221) | **D** (14/221)<br>**J** (14/221)<br>**N** (12/221)<br>**Q** (12/221)<br>**Y** (12/221) |
| **Mega Power** | **3** (27/221)<br>**6** (26/221)<br>**13** (26/221)<br>**22** (25/221)<br>**11** (25/221) | **V** (17/221)<br>**T** (13/221)<br>**K** (13/221)<br>**U** (13/221)<br>**J** (11/221) |
| **Nlb Jaya** | **5** (92/212)<br>**3** (84/212)<br>**0** (81/212)<br>**2** (79/212)<br>**4** (76/212) | **T** (14/212)<br>**M** (13/212)<br>**P** (13/212)<br>**I** (13/212)<br>**G** (13/212) |
| **Suba Dawasak** | **3** (91/221)<br>**1** (89/221)<br>**4** (88/221)<br>**9** (83/221)<br>**5** (78/221) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1740)<br>**57** (115/1740)<br>**20** (111/1740)<br>**13** (109/1740)<br>**38** (106/1740) | **B** (81/1740)<br>**M** (78/1740)<br>**R** (77/1740)<br>**P** (77/1740)<br>**I** (75/1740) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1628)<br>**10** (142/1628)<br>**29** (133/1628)<br>**21** (133/1628)<br>**22** (132/1628) | **H** (88/1628)<br>**U** (75/1628)<br>**W** (71/1628)<br>**G** (70/1628)<br>**D** (69/1628) |
| **Lagna Wasana** | **5** (135/1747)<br>**28** (133/1747)<br>**36** (130/1747)<br>**25** (130/1747)<br>**23** (129/1747) | N/A |
| **Sasiri** | **20** (70/925)<br>**9** (69/925)<br>**22** (68/925)<br>**26** (68/925)<br>**19** (67/925) | N/A |
| **Super Ball** | **45** (109/1741)<br>**3** (105/1741)<br>**29** (105/1741)<br>**43** (105/1741)<br>**52** (104/1741) | **I** (87/1741)<br>**D** (80/1741)<br>**T** (78/1741)<br>**V** (77/1741)<br>**A** (77/1741) |
| **Supiri Dhana Sampatha** | **2** (454/899)<br>**0** (454/899)<br>**3** (450/899)<br>**7** (444/899)<br>**5** (429/899) | **K** (44/899)<br>**V** (43/899)<br>**T** (43/899)<br>**J** (42/899)<br>**S** (41/899) |

