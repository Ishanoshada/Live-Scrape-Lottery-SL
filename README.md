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

> **Last Updated (Sri Lanka Time):** `2026-05-19 11:04:48 PM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 217 Rows | 10.55 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 225 Rows | 9.69 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 224 Rows | 9.57 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 224 Rows | 9.33 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 224 Rows | 9.62 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 224 Rows | 10.23 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 215 Rows | 8.44 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 224 Rows | 10.41 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1743 Rows | 66.66 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1631 Rows | 66.62 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1750 Rows | 65.22 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 928 Rows | 30.63 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1744 Rows | 66.70 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 902 Rows | 33.52 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-19 11:04:48 PM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (84/217)<br>**5** (80/217)<br>**2** (79/217)<br>**7** (76/217)<br>**4** (75/217) | **N** (14/217)<br>**D** (14/217)<br>**J** (14/217)<br>**Q** (12/217)<br>**Y** (12/217) |
| **Dhana Nidhanaya** | **28** (22/225)<br>**9** (21/225)<br>**6** (19/225)<br>**7** (18/225)<br>**16** (18/225) | **U** (14/225)<br>**W** (13/225)<br>**T** (12/225)<br>**M** (12/225)<br>**F** (11/225) |
| **Govisetha** | **44** (19/224)<br>**19** (17/224)<br>**55** (17/224)<br>**23** (16/224)<br>**58** (16/224) | **P** (13/224)<br>**D** (11/224)<br>**W** (11/224)<br>**O** (11/224)<br>**K** (11/224) |
| **Handahana** | **58** (22/224)<br>**61** (22/224)<br>**21** (21/224)<br>**6** (21/224)<br>**60** (20/224) | N/A |
| **Mahajana Sampatha** | **6** (112/224)<br>**2** (111/224)<br>**3** (109/224)<br>**5** (109/224)<br>**1** (109/224) | **D** (14/224)<br>**J** (14/224)<br>**N** (13/224)<br>**Q** (12/224)<br>**Y** (12/224) |
| **Mega Power** | **3** (27/224)<br>**6** (26/224)<br>**13** (26/224)<br>**11** (26/224)<br>**22** (25/224) | **V** (17/224)<br>**T** (13/224)<br>**K** (13/224)<br>**U** (13/224)<br>**J** (12/224) |
| **Nlb Jaya** | **5** (92/215)<br>**3** (85/215)<br>**0** (83/215)<br>**2** (81/215)<br>**1** (77/215) | **T** (14/215)<br>**M** (13/215)<br>**P** (13/215)<br>**I** (13/215)<br>**G** (13/215) |
| **Suba Dawasak** | **3** (93/224)<br>**1** (90/224)<br>**4** (89/224)<br>**9** (84/224)<br>**5** (81/224) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1743)<br>**57** (115/1743)<br>**20** (113/1743)<br>**13** (109/1743)<br>**38** (107/1743) | **B** (81/1743)<br>**R** (78/1743)<br>**M** (78/1743)<br>**P** (77/1743)<br>**I** (75/1743) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1631)<br>**10** (142/1631)<br>**29** (133/1631)<br>**21** (133/1631)<br>**22** (132/1631) | **H** (88/1631)<br>**U** (75/1631)<br>**W** (71/1631)<br>**G** (70/1631)<br>**X** (70/1631) |
| **Lagna Wasana** | **5** (135/1750)<br>**28** (133/1750)<br>**36** (130/1750)<br>**25** (130/1750)<br>**23** (129/1750) | N/A |
| **Sasiri** | **20** (70/928)<br>**9** (69/928)<br>**22** (68/928)<br>**26** (68/928)<br>**19** (67/928) | N/A |
| **Super Ball** | **45** (109/1744)<br>**3** (105/1744)<br>**74** (105/1744)<br>**29** (105/1744)<br>**43** (105/1744) | **I** (87/1744)<br>**D** (80/1744)<br>**T** (78/1744)<br>**V** (77/1744)<br>**A** (77/1744) |
| **Supiri Dhana Sampatha** | **2** (456/902)<br>**0** (456/902)<br>**3** (451/902)<br>**7** (447/902)<br>**5** (431/902) | **K** (44/902)<br>**V** (43/902)<br>**T** (43/902)<br>**J** (42/902)<br>**C** (42/902) |

