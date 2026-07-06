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

> **Last Updated (Sri Lanka Time):** `2026-07-07 12:45:27 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 263 Rows | 12.66 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 271 Rows | 11.57 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 270 Rows | 11.40 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 270 Rows | 11.12 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 270 Rows | 11.46 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 270 Rows | 12.19 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 261 Rows | 10.15 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 270 Rows | 12.42 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1789 Rows | 68.42 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1677 Rows | 68.51 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1796 Rows | 66.93 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 974 Rows | 32.21 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1790 Rows | 68.46 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 948 Rows | 35.24 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-07-07 12:45:27 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **5** (97/263)<br>**6** (96/263)<br>**2** (94/263)<br>**7** (93/263)<br>**0** (91/263) | **N** (16/263)<br>**D** (16/263)<br>**Q** (15/263)<br>**J** (15/263)<br>**G** (15/263) |
| **Dhana Nidhanaya** | **9** (26/271)<br>**28** (24/271)<br>**7** (24/271)<br>**4** (23/271)<br>**6** (21/271) | **U** (17/271)<br>**F** (15/271)<br>**W** (14/271)<br>**Z** (13/271)<br>**E** (13/271) |
| **Govisetha** | **55** (22/270)<br>**10** (21/270)<br>**23** (20/270)<br>**29** (20/270)<br>**19** (19/270) | **P** (15/270)<br>**C** (14/270)<br>**D** (13/270)<br>**A** (13/270)<br>**O** (12/270) |
| **Handahana** | **58** (27/270)<br>**21** (27/270)<br>**11** (26/270)<br>**6** (26/270)<br>**55** (24/270) | N/A |
| **Mahajana Sampatha** | **2** (133/270)<br>**5** (133/270)<br>**1** (132/270)<br>**6** (132/270)<br>**4** (131/270) | **D** (16/270)<br>**N** (15/270)<br>**Q** (15/270)<br>**J** (15/270)<br>**G** (15/270) |
| **Mega Power** | **11** (36/270)<br>**6** (31/270)<br>**3** (31/270)<br>**19** (30/270)<br>**13** (29/270) | **V** (19/270)<br>**U** (19/270)<br>**T** (18/270)<br>**K** (15/270)<br>**J** (15/270) |
| **Nlb Jaya** | **5** (117/261)<br>**0** (102/261)<br>**3** (100/261)<br>**2** (100/261)<br>**7** (93/261) | **I** (16/261)<br>**T** (16/261)<br>**G** (16/261)<br>**P** (14/261)<br>**Y** (14/261) |
| **Suba Dawasak** | **3** (111/270)<br>**4** (110/270)<br>**1** (106/270)<br>**9** (98/270)<br>**5** (97/270) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (120/1789)<br>**20** (119/1789)<br>**57** (116/1789)<br>**75** (111/1789)<br>**38** (110/1789) | **B** (82/1789)<br>**R** (81/1789)<br>**P** (79/1789)<br>**M** (79/1789)<br>**I** (77/1789) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (156/1677)<br>**10** (143/1677)<br>**27** (138/1677)<br>**29** (137/1677)<br>**15** (137/1677) | **H** (88/1677)<br>**U** (77/1677)<br>**M** (73/1677)<br>**X** (72/1677)<br>**W** (72/1677) |
| **Lagna Wasana** | **5** (137/1796)<br>**28** (136/1796)<br>**36** (134/1796)<br>**25** (133/1796)<br>**23** (132/1796) | N/A |
| **Sasiri** | **9** (73/974)<br>**22** (71/974)<br>**20** (71/974)<br>**26** (71/974)<br>**5** (69/974) | N/A |
| **Super Ball** | **52** (110/1790)<br>**45** (110/1790)<br>**29** (109/1790)<br>**74** (107/1790)<br>**43** (107/1790) | **I** (90/1790)<br>**D** (81/1790)<br>**V** (80/1790)<br>**T** (80/1790)<br>**A** (79/1790) |
| **Supiri Dhana Sampatha** | **2** (479/948)<br>**0** (475/948)<br>**3** (475/948)<br>**7** (466/948)<br>**5** (451/948) | **V** (48/948)<br>**K** (46/948)<br>**S** (43/948)<br>**J** (43/948)<br>**M** (43/948) |

