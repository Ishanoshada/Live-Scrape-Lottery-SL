import os
from collections import Counter
from datetime import datetime, timedelta

FOLDERS = ["nlb_txt", "dlb_txt"]
README_FILE = "README.md"
MARKER = "## 📈 Lottery Data Analytic Report"

def get_sl_time():
    """ශ්‍රී ලංකාවේ වර්තමාන වේලාව (UTC+5:30) ලබා ගනී."""
    sl_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
    return sl_time.strftime('%Y-%m-%d %I:%M:%S %p')

def analyze_lottery_files():
    print("=== 📊 Starting Lottery Data Analysis ===")
    
    # වාර්තාවේ ආරම්භය සහ වේලාව සැකසීම
    report_md = f"{MARKER}\n\n"
    report_md += f"> **Analytic Report Last Updated:** `{get_sl_time()}` (Sri Lanka Time)\n>\n"
    report_md += "> *This table is auto-generated based on the current dataset. It displays the top 5 most frequently drawn numbers and letters (Hits / Total Draws).*\n\n"

    for folder in FOLDERS:
        if not os.path.exists(folder):
            continue

        folder_title = "National Lottery Board (NLB)" if folder == "nlb_txt" else "Development Lottery Board (DLB)"
        report_md += f"### 🏢 {folder_title}\n\n"
        
        # Table Header එක නිර්මාණය කිරීම
        report_md += "| Lottery Name | 🔥 Top 5 Numbers (Hits/Total) | 🔠 Top 5 Letters (Hits/Total) |\n"
        report_md += "| :--- | :--- | :--- |\n"
        
        print(f"--- Analyzing {folder.upper()} Files ---")
        files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])

        for filename in files:
            file_path = os.path.join(folder, filename)
            
            all_numbers = []
            all_letters = []
            total_draws = 0
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if len(lines) <= 1:
                        continue 
                    
                    for line in lines[1:]:
                        parts = line.strip().split(",")
                        if len(parts) < 4:
                            continue
                        
                        total_draws += 1
                        
                        # Date එක කමාවකින් වෙන් වී ඇත්දැයි පරීක්ෂා කිරීම (උදා: '2026' වෙන්වීම වැළැක්වීමට)
                        if parts[2].strip().isdigit() and len(parts[2].strip()) == 4:
                            letter = parts[3].strip()
                            numbers = parts[4:]
                        else:
                            letter = parts[2].strip()
                            numbers = parts[3:]
                        
                        # අකුරු පෙරීම
                        if letter and letter.isalpha():
                            all_letters.append(letter.upper())
                        
                        # අංක පෙරීම (එකම පේළියේ duplicate වීම වැළැක්වීම සඳහා Set එකක් භාවිතා කිරීම)
                        draw_numbers = set()
                        for num in numbers:
                            n = num.strip()
                            if n.isdigit():
                                draw_numbers.add(str(int(n))) 
                        
                        # Set එකේ අගයන් ප්‍රධාන ලැයිස්තුවට එක් කිරීම
                        all_numbers.extend(draw_numbers)

                if total_draws == 0:
                    continue

                # වැඩිම වාර ගණනක් ආ Top 5 ලබා ගැනීම
                top_numbers = Counter(all_numbers).most_common(5)
                top_letters = Counter(all_letters).most_common(5)

                lottery_name = filename.replace(".txt", "").replace("-", " ").title()
                
                # Table එකට දත්ත ඇතුළත් කිරීම සඳහා Format කිරීම (HTML <br> ටැග් භාවිතා කිරීම)
                if top_numbers:
                    num_str = "<br>".join([f"**{n}** ({c}/{total_draws})" for n, c in top_numbers])
                else:
                    num_str = "N/A"
                    
                if top_letters:
                    let_str = "<br>".join([f"**{l}** ({c}/{total_draws})" for l, c in top_letters])
                else:
                    let_str = "N/A"
                
                # Markdown Table පේළිය
                report_md += f"| **{lottery_name}** | {num_str} | {let_str} |\n"
                print(f"Analyzed: {lottery_name} ({total_draws} draws)")

            except Exception as e:
                print(f"Error analyzing {filename}: {e}")
        
        report_md += "\n" # ඊළඟ ෆෝල්ඩරයට පෙර හිස් පේළියක්

    # README එක යාවත්කාලීන කිරීම සඳහා ශ්‍රිතය ඇමතීම
    update_readme_file(report_md)

def update_readme_file(new_report_content):
    if not os.path.exists(README_FILE):
        print(f"Error: {README_FILE} not found. Analytics report not saved.")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # කලින් තිබූ වාර්තාව (MARKER එකෙන් පහළ කොටස) කපා ඉවත් කරයි
    if MARKER in content:
        # MARKER එකට ඉහළින් ඇති කොටස පමණක් ලබා ගනී
        base_content = content.split(MARKER)[0].strip()
    else:
        # පළමු වතාවට ධාවනය කරන්නේ නම් සම්පූර්ණ content එකම ලබා ගනී
        base_content = content.strip()

    # අලුත් වාර්තාව වෙන් කරන ඉරක් (---) සමඟ සම්බන්ධ කරයි
    updated_readme = base_content + "\n\n---\n\n" + new_report_content

    # අලුත් content එක ගොනුවට ලිවීම
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated_readme)
        
    print(f"\n✅ Successfully updated {README_FILE} with the latest Analytic Report Table!")

if __name__ == "__main__":
    analyze_lottery_files()