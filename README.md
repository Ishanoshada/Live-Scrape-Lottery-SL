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

> **Last Updated (Sri Lanka Time):** `2026-05-18 07:08:42 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 215 Rows | 10.46 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 223 Rows | 9.62 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 222 Rows | 9.49 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 222 Rows | 9.25 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 222 Rows | 9.54 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 222 Rows | 10.14 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 213 Rows | 8.37 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 222 Rows | 10.32 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1741 Rows | 66.58 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1629 Rows | 66.53 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1748 Rows | 65.15 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 926 Rows | 30.56 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1742 Rows | 66.62 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 900 Rows | 33.45 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-18 07:08:42 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (83/215)<br>**5** (79/215)<br>**2** (78/215)<br>**7** (76/215)<br>**4** (74/215) | **N** (14/215)<br>**D** (14/215)<br>**J** (14/215)<br>**Q** (12/215)<br>**Y** (12/215) |
| **Dhana Nidhanaya** | **28** (22/223)<br>**9** (21/223)<br>**6** (19/223)<br>**7** (18/223)<br>**16** (18/223) | **U** (14/223)<br>**W** (13/223)<br>**T** (12/223)<br>**M** (12/223)<br>**Q** (11/223) |
| **Govisetha** | **44** (19/222)<br>**19** (17/222)<br>**55** (17/222)<br>**23** (16/222)<br>**58** (16/222) | **P** (13/222)<br>**D** (11/222)<br>**W** (11/222)<br>**O** (11/222)<br>**C** (11/222) |
| **Handahana** | **58** (22/222)<br>**21** (21/222)<br>**6** (21/222)<br>**60** (20/222)<br>**11** (20/222) | N/A |
| **Mahajana Sampatha** | **2** (110/222)<br>**6** (110/222)<br>**1** (109/222)<br>**3** (108/222)<br>**5** (108/222) | **D** (14/222)<br>**J** (14/222)<br>**N** (13/222)<br>**Q** (12/222)<br>**Y** (12/222) |
| **Mega Power** | **3** (27/222)<br>**6** (26/222)<br>**13** (26/222)<br>**22** (25/222)<br>**19** (25/222) | **V** (17/222)<br>**T** (13/222)<br>**K** (13/222)<br>**U** (13/222)<br>**J** (12/222) |
| **Nlb Jaya** | **5** (92/213)<br>**3** (84/213)<br>**0** (82/213)<br>**2** (80/213)<br>**4** (76/213) | **T** (14/213)<br>**M** (13/213)<br>**P** (13/213)<br>**I** (13/213)<br>**G** (13/213) |
| **Suba Dawasak** | **3** (91/222)<br>**1** (89/222)<br>**4** (88/222)<br>**9** (84/222)<br>**5** (79/222) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1741)<br>**57** (115/1741)<br>**20** (112/1741)<br>**13** (109/1741)<br>**38** (106/1741) | **B** (81/1741)<br>**M** (78/1741)<br>**R** (77/1741)<br>**P** (77/1741)<br>**I** (75/1741) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1629)<br>**10** (142/1629)<br>**29** (133/1629)<br>**21** (133/1629)<br>**22** (132/1629) | **H** (88/1629)<br>**U** (75/1629)<br>**W** (71/1629)<br>**G** (70/1629)<br>**D** (69/1629) |
| **Lagna Wasana** | **5** (135/1748)<br>**28** (133/1748)<br>**36** (130/1748)<br>**25** (130/1748)<br>**23** (129/1748) | N/A |
| **Sasiri** | **20** (70/926)<br>**9** (69/926)<br>**22** (68/926)<br>**26** (68/926)<br>**19** (67/926) | N/A |
| **Super Ball** | **45** (109/1742)<br>**3** (105/1742)<br>**29** (105/1742)<br>**43** (105/1742)<br>**52** (104/1742) | **I** (87/1742)<br>**D** (80/1742)<br>**T** (78/1742)<br>**V** (77/1742)<br>**A** (77/1742) |
| **Supiri Dhana Sampatha** | **2** (455/900)<br>**0** (454/900)<br>**3** (450/900)<br>**7** (445/900)<br>**5** (430/900) | **K** (44/900)<br>**V** (43/900)<br>**T** (43/900)<br>**J** (42/900)<br>**C** (42/900) |

