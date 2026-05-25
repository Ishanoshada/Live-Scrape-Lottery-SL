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

> **Last Updated (Sri Lanka Time):** `2026-05-26 02:28:01 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 223 Rows | 10.82 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 231 Rows | 9.94 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 230 Rows | 9.80 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 230 Rows | 9.56 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 230 Rows | 9.85 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 230 Rows | 10.48 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 221 Rows | 8.66 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 230 Rows | 10.67 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1749 Rows | 66.89 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1637 Rows | 66.86 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1756 Rows | 65.44 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 934 Rows | 30.83 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1750 Rows | 66.93 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 908 Rows | 33.75 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-26 02:28:01 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (86/223)<br>**5** (82/223)<br>**2** (80/223)<br>**0** (78/223)<br>**4** (77/223) | **N** (14/223)<br>**D** (14/223)<br>**J** (14/223)<br>**Q** (13/223)<br>**Y** (12/223) |
| **Dhana Nidhanaya** | **28** (22/231)<br>**9** (22/231)<br>**6** (20/231)<br>**7** (18/231)<br>**16** (18/231) | **U** (14/231)<br>**W** (13/231)<br>**Z** (12/231)<br>**T** (12/231)<br>**M** (12/231) |
| **Govisetha** | **44** (19/230)<br>**10** (18/230)<br>**19** (17/230)<br>**58** (17/230)<br>**55** (17/230) | **P** (13/230)<br>**O** (12/230)<br>**D** (11/230)<br>**W** (11/230)<br>**K** (11/230) |
| **Handahana** | **58** (22/230)<br>**61** (22/230)<br>**6** (22/230)<br>**21** (21/230)<br>**55** (21/230) | N/A |
| **Mahajana Sampatha** | **6** (115/230)<br>**2** (114/230)<br>**1** (114/230)<br>**3** (112/230)<br>**5** (112/230) | **D** (14/230)<br>**J** (14/230)<br>**N** (13/230)<br>**Q** (13/230)<br>**Y** (12/230) |
| **Mega Power** | **3** (28/230)<br>**11** (28/230)<br>**22** (26/230)<br>**6** (26/230)<br>**13** (26/230) | **V** (17/230)<br>**T** (14/230)<br>**K** (13/230)<br>**U** (13/230)<br>**J** (12/230) |
| **Nlb Jaya** | **5** (96/221)<br>**0** (88/221)<br>**3** (87/221)<br>**2** (82/221)<br>**1** (79/221) | **P** (14/221)<br>**T** (14/221)<br>**M** (13/221)<br>**I** (13/221)<br>**G** (13/221) |
| **Suba Dawasak** | **3** (97/230)<br>**1** (92/230)<br>**4** (90/230)<br>**9** (86/230)<br>**5** (84/230) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1749)<br>**57** (115/1749)<br>**20** (114/1749)<br>**13** (109/1749)<br>**38** (107/1749) | **B** (82/1749)<br>**R** (78/1749)<br>**P** (78/1749)<br>**M** (78/1749)<br>**I** (75/1749) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1637)<br>**10** (142/1637)<br>**29** (134/1637)<br>**21** (133/1637)<br>**38** (133/1637) | **H** (88/1637)<br>**U** (75/1637)<br>**W** (72/1637)<br>**G** (70/1637)<br>**X** (70/1637) |
| **Lagna Wasana** | **5** (135/1756)<br>**28** (133/1756)<br>**36** (130/1756)<br>**23** (130/1756)<br>**25** (130/1756) | N/A |
| **Sasiri** | **9** (70/934)<br>**20** (70/934)<br>**22** (68/934)<br>**26** (68/934)<br>**19** (67/934) | N/A |
| **Super Ball** | **45** (109/1750)<br>**74** (106/1750)<br>**29** (106/1750)<br>**52** (105/1750)<br>**3** (105/1750) | **I** (87/1750)<br>**D** (80/1750)<br>**T** (79/1750)<br>**V** (77/1750)<br>**A** (77/1750) |
| **Supiri Dhana Sampatha** | **0** (459/908)<br>**2** (458/908)<br>**3** (453/908)<br>**7** (448/908)<br>**5** (436/908) | **K** (44/908)<br>**V** (44/908)<br>**T** (43/908)<br>**S** (42/908)<br>**J** (42/908) |

