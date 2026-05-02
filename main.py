import os
from srilanka_lottery import (
    scrape_nlb_active_lottery_names, 
    scrape_nlb_latest_results,
    scrape_dlb_lottery_names,
    scrape_dlb_latest_results
)

# එක වරකදී ලබා ගන්නා උපරිම දත්ත ප්‍රමාණය
LIMIT = 100

def update_txt_file(folder, lottery_id, new_data):
    """දත්ත TXT ගොනුවට ඇතුළත් කර Duplicate ඉවත් කරයි."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    file_path = os.path.join(folder, f"{lottery_id}.txt")
    existing_draws = set()
    file_content = []

    # 1. පවතින ගොනුව කියවා දැනටමත් ඇති Draw Numbers හඳුනා ගැනීම
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Header එක හැර අනෙක් පේළි කියවීම
            for line in lines[1:]:
                parts = line.strip().split(",")
                if parts:
                    existing_draws.add(parts[0])
                    file_content.append(line.strip())

    # 2. අලුත් දත්ත පරීක්ෂා කර Duplicate නැති ඒවා පමණක් එකතු කිරීම
    added_count = 0
    for res in new_data:
        draw_no = str(res['draw'])
        if draw_no not in existing_draws:
            # දත්ත පේළිය සකස් කිරීම: Draw,Date,Letter,Num1,Num2...
            numbers_str = ",".join(res['numbers'])
            line = f"{draw_no},{res['date']},{res['letter']},{numbers_str}"
            file_content.append(line)
            existing_draws.add(draw_no)
            added_count += 1

    # 3. Draw Number එක අනුව Sort කිරීම (පිළිවෙළට තැබීම)
    if file_content:
        file_content.sort(key=lambda x: int(x.split(",")[0]))

    # 4. ගොනුව සුරැකීම
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Draw,Date,Letter,Numbers...\n")
        for line in file_content:
            f.write(line + "\n")
            
    return len(file_content), added_count

def process():
    print("=== Starting Lottery Scraper Automation ===")
    
    # --- National Lottery Board (NLB) ---
    print("\n--- Processing NLB ---")
    try:
        nlb_active, session = scrape_nlb_active_lottery_names()
        if "NLB_Active" in nlb_active:
            for lot in nlb_active["NLB_Active"]:
                # API එකට ගැළපෙන ලෙස නම සකස් කිරීම
                lot_id = lot.lower().replace(" ", "-")
                try:
                    data = scrape_nlb_latest_results(session, lot_id, limit=LIMIT)
                    if "NLB_Results" in data and data["NLB_Results"]:
                        total, added = update_txt_file("nlb_txt", lot_id, data["NLB_Results"])
                        print(f"[{lot}] Added: {added} | Total Records: {total}")
                    else:
                        print(f"[{lot}] No new results found.")
                except Exception as e:
                    print(f"[{lot}] Scrape Error: {e}")
    except Exception as e:
        print(f"NLB Session Error: {e}")

    # --- Development Lottery Board (DLB) ---
    print("\n--- Processing DLB ---")
    try:
        dlb_names = scrape_dlb_lottery_names()
        if "DLB" in dlb_names:
            for lot in dlb_names["DLB"]:
                try:
                    data = scrape_dlb_latest_results(lot, limit=LIMIT)
                    if "DLB_Results" in data and data["DLB_Results"]:
                        # DLB සඳහා ID එක නමෙන්ම සකසා ගැනීම
                        lot_id = lot.lower().replace(" ", "-")
                        total, added = update_txt_file("dlb_txt", lot_id, data["DLB_Results"])
                        print(f"[{lot}] Added: {added} | Total Records: {total}")
                    else:
                        print(f"[{lot}] No new results found.")
                except Exception as e:
                    print(f"[{lot}] Scrape Error: {e}")
    except Exception as e:
        print(f"DLB Names Error: {e}")

    print("\n=== Update Completed ===")

if __name__ == "__main__":
    process()
