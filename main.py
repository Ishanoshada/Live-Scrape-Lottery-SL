import os
from datetime import datetime, timedelta
from srilanka_lottery import (
    scrape_nlb_active_lottery_names, 
    scrape_nlb_latest_results,
    scrape_dlb_lottery_names,
    scrape_dlb_latest_results
)

LIMIT = 3000
BASE_GITHUB_URL = "https://github.com/Ishanoshada/Live-Scrape-Lottery-SL/blob/main"

def get_sl_time():
    """ශ්‍රී ලංකාවේ වර්තමාන වේලාව (UTC+5:30) ලබා ගනී."""
    # GitHub Actions ක්‍රියාත්මක වන්නේ UTC වේලාවෙන් බැවින් පැය 5 විනාඩි 30ක් එකතු කරයි
    sl_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
    return sl_time.strftime('%Y-%m-%d %I:%M:%S %p')

def get_file_info(folder, filename):
    """ගොනුවේ දත්ත පේළි ගණන සහ ප්‍රමාණය ලබා ගනී."""
    path = os.path.join(folder, filename)
    if not os.path.exists(path):
        return 0, "0 KB"
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        data_count = len(lines) - 1 if len(lines) > 0 else 0
        
    size_bytes = os.path.getsize(path)
    if size_bytes < 1024:
        size_str = f"{size_bytes} Bytes"
    elif size_bytes < 1024 * 1024:
        size_str = f"{size_bytes / 1024:.2f} KB"
    else:
        size_str = f"{size_bytes / (1024 * 1024):.2f} MB"
        
    return data_count, size_str

def generate_readme_table():
    """README සඳහා ලොතරැයි දත්ත වගුව සහ යාවත්කාලීන වේලාව සකස් කරයි."""
    last_update = get_sl_time()
    tables_content = "## 📊 Data Summary\n\n"
    tables_content += f"> **Last Updated (Sri Lanka Time):** `{last_update}`\n\n"
    
    for folder in ["nlb_txt", "dlb_txt"]:
        header_name = "National Lottery Board (NLB)" if folder == "nlb_txt" else "Development Lottery Board (DLB)"
        tables_content += f"### {header_name}\n"
        tables_content += "| Lottery Name | File Link | Data Length | File Size |\n"
        tables_content += "| :--- | :--- | :--- | :--- |\n"
        
        if os.path.exists(folder):
            files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])
            for f in files:
                count, size = get_file_info(folder, f)
                name = f.replace(".txt", "").replace("-", " ").title()
                link = f"[{f}]({BASE_GITHUB_URL}/{folder}/{f})"
                tables_content += f"| {name} | {link} | {count} Rows | {size} |\n"
        tables_content += "\n"
    return tables_content

def update_readme(table_html):
    """README.md ගොනුවේ වගුව සහ වේලාව යාවත්කාලීන කරයි."""
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    marker_start = "## 📊 Data Summary"
    if marker_start in content:
        upper_part = content.split(marker_start)[0]
        new_content = upper_part + table_html
    else:
        new_content = content + "\n\n" + table_html

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def update_txt_file(folder, lottery_id, new_data):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    file_path = os.path.join(folder, f"{lottery_id}.txt")
    existing_draws = set()
    file_content = []

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(",")
                if parts:
                    existing_draws.add(parts[0])
                    file_content.append(line.strip())

    added = 0
    for res in new_data:
        draw_no = str(res['draw'])
        if draw_no not in existing_draws:
            line = f"{draw_no},{res['date']},{res['letter']},{','.join(res['numbers'])}"
            file_content.append(line)
            existing_draws.add(draw_no)
            added += 1

    if file_content:
        file_content.sort(key=lambda x: int(x.split(",")[0]))

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Draw,Date,Letter,Numbers...\n")
        for line in file_content:
            f.write(line + "\n")
            
    return added

def process():
    print(f"=== Starting Scraper at {get_sl_time()} (SL Time) ===")
    
    # NLB
    nlb_active, session = scrape_nlb_active_lottery_names()
    if "NLB_Active" in nlb_active:
        for lot in nlb_active["NLB_Active"]:
            lot_id = lot.lower().replace(" ", "-")
            data = scrape_nlb_latest_results(session, lot_id, limit=LIMIT)
            if "NLB_Results" in data:
                update_txt_file("nlb_txt", lot_id, data["NLB_Results"])

    # DLB
    dlb_names = scrape_dlb_lottery_names()
    if "DLB" in dlb_names:
        for lot in dlb_names["DLB"]:
            data = scrape_dlb_latest_results(lot, limit=LIMIT)
            if "DLB_Results" in data:
                lot_id = lot.lower().replace(" ", "-")
                update_txt_file("dlb_txt", lot_id, data["DLB_Results"])

    # README Table Update
    print("Updating README table and timestamp...")
    table_data = generate_readme_table()
    update_readme(table_data)
    print("Done!")

if __name__ == "__main__":
    process()
