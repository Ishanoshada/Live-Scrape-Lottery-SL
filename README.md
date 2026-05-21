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

> **Last Updated (Sri Lanka Time):** `2026-05-21 01:57:55 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 218 Rows | 10.59 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 226 Rows | 9.73 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 225 Rows | 9.61 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 225 Rows | 9.37 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 225 Rows | 9.66 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 225 Rows | 10.27 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 216 Rows | 8.48 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 225 Rows | 10.45 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1744 Rows | 66.70 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1632 Rows | 66.66 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1751 Rows | 65.26 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 929 Rows | 30.66 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1745 Rows | 66.74 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 903 Rows | 33.56 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-21 01:57:55 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (85/218)<br>**5** (80/218)<br>**2** (80/218)<br>**0** (76/218)<br>**7** (76/218) | **N** (14/218)<br>**D** (14/218)<br>**J** (14/218)<br>**Q** (12/218)<br>**Y** (12/218) |
| **Dhana Nidhanaya** | **28** (22/226)<br>**9** (21/226)<br>**6** (19/226)<br>**7** (18/226)<br>**16** (18/226) | **U** (14/226)<br>**W** (13/226)<br>**T** (12/226)<br>**M** (12/226)<br>**Z** (11/226) |
| **Govisetha** | **44** (19/225)<br>**19** (17/225)<br>**55** (17/225)<br>**23** (16/225)<br>**58** (16/225) | **P** (13/225)<br>**D** (11/225)<br>**W** (11/225)<br>**O** (11/225)<br>**K** (11/225) |
| **Handahana** | **58** (22/225)<br>**61** (22/225)<br>**21** (21/225)<br>**6** (21/225)<br>**60** (20/225) | N/A |
| **Mahajana Sampatha** | **6** (113/225)<br>**2** (112/225)<br>**3** (110/225)<br>**5** (109/225)<br>**1** (109/225) | **D** (14/225)<br>**J** (14/225)<br>**N** (13/225)<br>**Q** (12/225)<br>**Y** (12/225) |
| **Mega Power** | **3** (27/225)<br>**6** (26/225)<br>**13** (26/225)<br>**11** (26/225)<br>**22** (25/225) | **V** (17/225)<br>**T** (13/225)<br>**K** (13/225)<br>**U** (13/225)<br>**J** (12/225) |
| **Nlb Jaya** | **5** (92/216)<br>**3** (86/216)<br>**0** (83/216)<br>**2** (81/216)<br>**1** (77/216) | **P** (14/216)<br>**T** (14/216)<br>**M** (13/216)<br>**I** (13/216)<br>**G** (13/216) |
| **Suba Dawasak** | **3** (94/225)<br>**1** (91/225)<br>**4** (89/225)<br>**9** (85/225)<br>**5** (81/225) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1744)<br>**57** (115/1744)<br>**20** (113/1744)<br>**13** (109/1744)<br>**38** (107/1744) | **B** (82/1744)<br>**R** (78/1744)<br>**M** (78/1744)<br>**P** (77/1744)<br>**I** (75/1744) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1632)<br>**10** (142/1632)<br>**29** (133/1632)<br>**21** (133/1632)<br>**22** (132/1632) | **H** (88/1632)<br>**U** (75/1632)<br>**W** (71/1632)<br>**G** (70/1632)<br>**X** (70/1632) |
| **Lagna Wasana** | **5** (135/1751)<br>**28** (133/1751)<br>**36** (130/1751)<br>**25** (130/1751)<br>**23** (129/1751) | N/A |
| **Sasiri** | **9** (70/929)<br>**20** (70/929)<br>**22** (68/929)<br>**26** (68/929)<br>**19** (67/929) | N/A |
| **Super Ball** | **45** (109/1745)<br>**3** (105/1745)<br>**74** (105/1745)<br>**29** (105/1745)<br>**43** (105/1745) | **I** (87/1745)<br>**D** (80/1745)<br>**T** (78/1745)<br>**V** (77/1745)<br>**A** (77/1745) |
| **Supiri Dhana Sampatha** | **2** (457/903)<br>**0** (456/903)<br>**3** (452/903)<br>**7** (447/903)<br>**5** (432/903) | **K** (44/903)<br>**V** (43/903)<br>**T** (43/903)<br>**J** (42/903)<br>**C** (42/903) |

