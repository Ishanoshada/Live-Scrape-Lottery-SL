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

> **Last Updated (Sri Lanka Time):** `2026-05-18 10:56:58 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 216 Rows | 10.50 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 224 Rows | 9.65 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 223 Rows | 9.53 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 223 Rows | 9.29 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 223 Rows | 9.58 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 223 Rows | 10.19 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 214 Rows | 8.41 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 223 Rows | 10.36 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1742 Rows | 66.62 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1630 Rows | 66.57 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1749 Rows | 65.18 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 927 Rows | 30.59 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1743 Rows | 66.66 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 901 Rows | 33.49 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-18 10:56:58 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (83/216)<br>**5** (80/216)<br>**2** (79/216)<br>**7** (76/216)<br>**0** (75/216) | **N** (14/216)<br>**D** (14/216)<br>**J** (14/216)<br>**Q** (12/216)<br>**Y** (12/216) |
| **Dhana Nidhanaya** | **28** (22/224)<br>**9** (21/224)<br>**6** (19/224)<br>**7** (18/224)<br>**16** (18/224) | **U** (14/224)<br>**W** (13/224)<br>**T** (12/224)<br>**M** (12/224)<br>**Q** (11/224) |
| **Govisetha** | **44** (19/223)<br>**19** (17/223)<br>**55** (17/223)<br>**23** (16/223)<br>**58** (16/223) | **P** (13/223)<br>**D** (11/223)<br>**W** (11/223)<br>**O** (11/223)<br>**C** (11/223) |
| **Handahana** | **58** (22/223)<br>**61** (21/223)<br>**21** (21/223)<br>**6** (21/223)<br>**60** (20/223) | N/A |
| **Mahajana Sampatha** | **2** (111/223)<br>**6** (111/223)<br>**3** (109/223)<br>**5** (109/223)<br>**1** (109/223) | **D** (14/223)<br>**J** (14/223)<br>**N** (13/223)<br>**Q** (12/223)<br>**Y** (12/223) |
| **Mega Power** | **3** (27/223)<br>**6** (26/223)<br>**13** (26/223)<br>**22** (25/223)<br>**19** (25/223) | **V** (17/223)<br>**T** (13/223)<br>**K** (13/223)<br>**U** (13/223)<br>**J** (12/223) |
| **Nlb Jaya** | **5** (92/214)<br>**3** (85/214)<br>**0** (82/214)<br>**2** (80/214)<br>**1** (77/214) | **T** (14/214)<br>**M** (13/214)<br>**P** (13/214)<br>**I** (13/214)<br>**G** (13/214) |
| **Suba Dawasak** | **3** (92/223)<br>**1** (90/223)<br>**4** (88/223)<br>**9** (84/223)<br>**5** (80/223) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1742)<br>**57** (115/1742)<br>**20** (113/1742)<br>**13** (109/1742)<br>**38** (106/1742) | **B** (81/1742)<br>**R** (78/1742)<br>**M** (78/1742)<br>**P** (77/1742)<br>**I** (75/1742) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1630)<br>**10** (142/1630)<br>**29** (133/1630)<br>**21** (133/1630)<br>**22** (132/1630) | **H** (88/1630)<br>**U** (75/1630)<br>**W** (71/1630)<br>**G** (70/1630)<br>**D** (69/1630) |
| **Lagna Wasana** | **5** (135/1749)<br>**28** (133/1749)<br>**36** (130/1749)<br>**25** (130/1749)<br>**23** (129/1749) | N/A |
| **Sasiri** | **20** (70/927)<br>**9** (69/927)<br>**22** (68/927)<br>**26** (68/927)<br>**19** (67/927) | N/A |
| **Super Ball** | **45** (109/1743)<br>**3** (105/1743)<br>**29** (105/1743)<br>**43** (105/1743)<br>**52** (104/1743) | **I** (87/1743)<br>**D** (80/1743)<br>**T** (78/1743)<br>**V** (77/1743)<br>**A** (77/1743) |
| **Supiri Dhana Sampatha** | **2** (455/901)<br>**0** (455/901)<br>**3** (450/901)<br>**7** (446/901)<br>**5** (430/901) | **K** (44/901)<br>**V** (43/901)<br>**T** (43/901)<br>**J** (42/901)<br>**C** (42/901) |

