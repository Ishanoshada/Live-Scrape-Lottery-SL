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

> **Last Updated (Sri Lanka Time):** `2026-05-16 04:26:18 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 213 Rows | 10.37 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 221 Rows | 9.53 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 220 Rows | 9.41 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 220 Rows | 9.18 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 220 Rows | 9.46 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 220 Rows | 10.06 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 211 Rows | 8.29 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 220 Rows | 10.24 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1739 Rows | 66.51 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1627 Rows | 66.45 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1746 Rows | 65.07 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 924 Rows | 30.50 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1740 Rows | 66.55 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 898 Rows | 33.38 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-16 04:26:18 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (81/213)<br>**5** (79/213)<br>**2** (76/213)<br>**7** (76/213)<br>**4** (74/213) | **D** (14/213)<br>**J** (14/213)<br>**N** (13/213)<br>**Q** (12/213)<br>**Y** (12/213) |
| **Dhana Nidhanaya** | **28** (21/221)<br>**9** (20/221)<br>**6** (19/221)<br>**7** (18/221)<br>**16** (18/221) | **U** (14/221)<br>**W** (13/221)<br>**T** (12/221)<br>**M** (12/221)<br>**Q** (11/221) |
| **Govisetha** | **44** (19/220)<br>**19** (17/220)<br>**55** (17/220)<br>**23** (16/220)<br>**58** (16/220) | **P** (13/220)<br>**D** (11/220)<br>**W** (11/220)<br>**O** (11/220)<br>**X** (11/220) |
| **Handahana** | **58** (22/220)<br>**21** (21/220)<br>**6** (21/220)<br>**60** (20/220)<br>**11** (20/220) | N/A |
| **Mahajana Sampatha** | **2** (108/220)<br>**1** (108/220)<br>**6** (108/220)<br>**3** (107/220)<br>**5** (107/220) | **D** (14/220)<br>**J** (14/220)<br>**N** (12/220)<br>**Q** (12/220)<br>**Y** (12/220) |
| **Mega Power** | **3** (27/220)<br>**6** (26/220)<br>**13** (26/220)<br>**22** (25/220)<br>**11** (25/220) | **V** (17/220)<br>**T** (13/220)<br>**K** (13/220)<br>**U** (13/220)<br>**J** (11/220) |
| **Nlb Jaya** | **5** (91/211)<br>**3** (84/211)<br>**0** (81/211)<br>**2** (79/211)<br>**4** (75/211) | **T** (14/211)<br>**M** (13/211)<br>**P** (13/211)<br>**I** (13/211)<br>**G** (13/211) |
| **Suba Dawasak** | **3** (90/220)<br>**1** (89/220)<br>**4** (87/220)<br>**9** (83/220)<br>**5** (78/220) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1739)<br>**57** (115/1739)<br>**20** (111/1739)<br>**13** (109/1739)<br>**38** (106/1739) | **B** (81/1739)<br>**M** (78/1739)<br>**R** (77/1739)<br>**P** (77/1739)<br>**I** (75/1739) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1627)<br>**10** (142/1627)<br>**29** (133/1627)<br>**21** (133/1627)<br>**22** (132/1627) | **H** (88/1627)<br>**U** (75/1627)<br>**W** (71/1627)<br>**G** (70/1627)<br>**D** (69/1627) |
| **Lagna Wasana** | **5** (135/1746)<br>**28** (133/1746)<br>**36** (130/1746)<br>**25** (130/1746)<br>**23** (129/1746) | N/A |
| **Sasiri** | **20** (70/924)<br>**9** (69/924)<br>**22** (68/924)<br>**26** (68/924)<br>**19** (67/924) | N/A |
| **Super Ball** | **45** (109/1740)<br>**3** (105/1740)<br>**29** (105/1740)<br>**43** (105/1740)<br>**52** (104/1740) | **I** (87/1740)<br>**D** (80/1740)<br>**T** (78/1740)<br>**V** (77/1740)<br>**A** (77/1740) |
| **Supiri Dhana Sampatha** | **2** (454/898)<br>**0** (453/898)<br>**3** (450/898)<br>**7** (444/898)<br>**5** (429/898) | **K** (44/898)<br>**V** (43/898)<br>**T** (43/898)<br>**J** (42/898)<br>**S** (41/898) |

