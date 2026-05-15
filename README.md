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

> **Last Updated (Sri Lanka Time):** `2026-05-15 07:56:11 AM`

### National Lottery Board (NLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Sampatha | [ada-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/ada-sampatha.txt) | 212 Rows | 10.32 KB |
| Dhana Nidhanaya | [dhana-nidhanaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/dhana-nidhanaya.txt) | 220 Rows | 9.49 KB |
| Govisetha | [govisetha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/govisetha.txt) | 219 Rows | 9.37 KB |
| Handahana | [handahana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/handahana.txt) | 219 Rows | 9.14 KB |
| Lucky 7 | [lucky-7.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/lucky-7.txt) | 0 Rows | 28 Bytes |
| Mahajana Sampatha | [mahajana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mahajana-sampatha.txt) | 219 Rows | 9.42 KB |
| Mega Power | [mega-power.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/mega-power.txt) | 219 Rows | 10.02 KB |
| Nlb Jaya | [nlb-jaya.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/nlb-jaya.txt) | 210 Rows | 8.26 KB |
| Samurdhi Scratch Lottery | [samurdhi-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/samurdhi-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Sevana Scratch Lottery | [sevana-scratch-lottery.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/sevana-scratch-lottery.txt) | 0 Rows | 28 Bytes |
| Suba Dawasak | [suba-dawasak.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/nlb_txt/suba-dawasak.txt) | 219 Rows | 10.19 KB |

### Development Lottery Board (DLB)
| Lottery Name | File Link | Data Length | File Size |
| :--- | :--- | :--- | :--- |
| Ada Kotipathi | [ada-kotipathi.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/ada-kotipathi.txt) | 1738 Rows | 66.47 KB |
| Jaya Sampatha | [jaya-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jaya-sampatha.txt) | 0 Rows | 28 Bytes |
| Jayoda | [jayoda.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/jayoda.txt) | 427 Rows | 16.50 KB |
| Kapruka | [kapruka.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/kapruka.txt) | 1626 Rows | 66.41 KB |
| Lagna Wasana | [lagna-wasana.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/lagna-wasana.txt) | 1745 Rows | 65.04 KB |
| Sasiri | [sasiri.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/sasiri.txt) | 923 Rows | 30.46 KB |
| Shanida | [shanida.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/shanida.txt) | 0 Rows | 28 Bytes |
| Super Ball | [super-ball.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/super-ball.txt) | 1739 Rows | 66.51 KB |
| Supiri Dhana Sampatha | [supiri-dhana-sampatha.txt](https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main/dlb_txt/supiri-dhana-sampatha.txt) | 897 Rows | 33.34 KB |

---

## 📈 Lottery Data Analytic Report

> **Analytic Report Last Updated:** `2026-05-15 07:56:11 AM` (Sri Lanka Time)
>
> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*

### 🏢 National Lottery Board (NLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Sampatha** | **6** (81/212)<br>**5** (78/212)<br>**7** (76/212)<br>**2** (76/212)<br>**0** (74/212) | **D** (14/212)<br>**J** (14/212)<br>**N** (13/212)<br>**Q** (12/212)<br>**Y** (12/212) |
| **Dhana Nidhanaya** | **28** (21/220)<br>**9** (20/220)<br>**6** (19/220)<br>**16** (18/220)<br>**7** (17/220) | **U** (14/220)<br>**W** (13/220)<br>**T** (12/220)<br>**M** (12/220)<br>**Q** (11/220) |
| **Govisetha** | **44** (18/219)<br>**19** (17/219)<br>**55** (17/219)<br>**23** (16/219)<br>**58** (16/219) | **P** (13/219)<br>**D** (11/219)<br>**W** (11/219)<br>**O** (11/219)<br>**X** (11/219) |
| **Handahana** | **58** (22/219)<br>**21** (21/219)<br>**6** (21/219)<br>**60** (20/219)<br>**11** (20/219) | N/A |
| **Mahajana Sampatha** | **2** (108/219)<br>**6** (108/219)<br>**1** (107/219)<br>**3** (106/219)<br>**9** (106/219) | **D** (14/219)<br>**J** (14/219)<br>**N** (12/219)<br>**Q** (12/219)<br>**Y** (12/219) |
| **Mega Power** | **6** (26/219)<br>**3** (26/219)<br>**13** (26/219)<br>**22** (25/219)<br>**11** (25/219) | **V** (17/219)<br>**T** (13/219)<br>**K** (13/219)<br>**U** (13/219)<br>**J** (11/219) |
| **Nlb Jaya** | **5** (91/210)<br>**3** (84/210)<br>**0** (81/210)<br>**2** (79/210)<br>**4** (74/210) | **T** (14/210)<br>**M** (13/210)<br>**P** (13/210)<br>**I** (13/210)<br>**G** (13/210) |
| **Suba Dawasak** | **3** (90/219)<br>**1** (89/219)<br>**4** (87/219)<br>**9** (82/219)<br>**5** (78/219) | N/A |

### 🏢 Development Lottery Board (DLB)

| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |
| :--- | :--- | :--- |
| **Ada Kotipathi** | **9** (116/1738)<br>**57** (115/1738)<br>**20** (111/1738)<br>**13** (109/1738)<br>**38** (106/1738) | **B** (81/1738)<br>**M** (78/1738)<br>**R** (77/1738)<br>**P** (77/1738)<br>**I** (75/1738) |
| **Jayoda** | **30** (37/427)<br>**3** (32/427)<br>**16** (32/427)<br>**59** (31/427)<br>**64** (31/427) | **G** (26/427)<br>**C** (21/427)<br>**Y** (21/427)<br>**F** (21/427)<br>**U** (20/427) |
| **Kapruka** | **28** (155/1626)<br>**10** (142/1626)<br>**29** (133/1626)<br>**21** (133/1626)<br>**22** (132/1626) | **H** (87/1626)<br>**U** (75/1626)<br>**W** (71/1626)<br>**G** (70/1626)<br>**D** (69/1626) |
| **Lagna Wasana** | **5** (135/1745)<br>**28** (133/1745)<br>**36** (130/1745)<br>**25** (130/1745)<br>**23** (129/1745) | N/A |
| **Sasiri** | **20** (70/923)<br>**9** (69/923)<br>**22** (68/923)<br>**26** (68/923)<br>**19** (67/923) | N/A |
| **Super Ball** | **45** (109/1739)<br>**3** (105/1739)<br>**29** (105/1739)<br>**43** (105/1739)<br>**52** (104/1739) | **I** (87/1739)<br>**D** (80/1739)<br>**T** (78/1739)<br>**V** (77/1739)<br>**A** (77/1739) |
| **Supiri Dhana Sampatha** | **2** (454/897)<br>**0** (453/897)<br>**3** (450/897)<br>**7** (444/897)<br>**5** (428/897) | **K** (44/897)<br>**V** (43/897)<br>**T** (43/897)<br>**J** (42/897)<br>**S** (41/897) |

