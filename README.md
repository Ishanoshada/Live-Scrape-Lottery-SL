
# 🎰 Sri Lanka Lottery Results Archive (Automated)

This repository provides an automated, up-to-date archive of lottery results from the **National Lottery Board (NLB)** and the **Development Lottery Board (DLB)** of Sri Lanka. Data is extracted using the [srilanka-lottery](https://pypi.org/project/srilanka-lottery/) Python package.

## 🚀 How it Works
*   **Automation:** A GitHub Action runs every few minutes to check for new draw results.
*   **Extraction:** It uses the `srilanka-lottery` library to scrape official data.
*   **Storage:** Results are stored in clean `.txt` files within the `nlb_txt/` and `dlb_txt/` directories.
*   **Deduplication:** The system automatically ensures no duplicate draw entries are recorded, keeping the data clean and sorted.

## 📁 Data Structure
The results are saved in a Comma-Separated Values (CSV) compatible text format:
`Draw_Number, Date, Winning_Letter, Numbers...`

### Folders:
*   `/nlb_txt`: Contains results for Mega Power, Mahajana Sampatha, Govisetha, Dhana Nidhanaya, etc.
*   `/dlb_txt`: Contains results for Ada Kotipathi, Jayoda, Lagna Wasana, Kapruka, etc.

## 🛠 Usage for Developers
If you want to use this data in your own projects, you can fetch the raw text files directly from this repository or use the core scraping package:

```bash
pip install srilanka-lottery
```

## ⚖️ License
This project is licensed under the **MIT License**.

## 👨‍💻 Author
Developed and maintained by **Ishan Oshada**.
*   **GitHub:** [@Ishanoshada](https://github.com/Ishanoshada)
*   **PyPI:** [srilanka-lottery](https://pypi.org/project/srilanka-lottery/)


![Views](https://dynamic-repo-badges.vercel.app/svg/count/7/Repository%20Views/lotterylive2)

