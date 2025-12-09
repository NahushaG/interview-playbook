import os

# summary.py is inside scripts-tool → go one level up to reach repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def summarize_problems(folder):
    folder_path = os.path.join(REPO_ROOT, folder)

    if not os.path.exists(folder_path):
        print(f"[WARN] Folder not found: {folder_path}")
        return {}

    items = os.listdir(folder_path)

    # Detect subfolders
    subfolders = [
        item for item in items 
        if os.path.isdir(os.path.join(folder_path, item))
    ]

    # CASE 1: Folder contains subfolders
    if subfolders:
        summary = {}
        for sub in subfolders:
            sub_path = os.path.join(folder_path, sub)
            files = [
                f for f in os.listdir(sub_path)
                if os.path.isfile(os.path.join(sub_path, f))
            ]
            summary[sub] = files   # show folder even if empty
        return summary

    # CASE 2: Folder contains direct files
    files = [
        item for item in items 
        if os.path.isfile(os.path.join(folder_path, item))
    ]

    return files  # may be empty, but folder still shown


def load_folders(file_path="folders.txt"):
    folders_file_path = os.path.join(REPO_ROOT, file_path)

    if not os.path.exists(folders_file_path):
        print(f"[ERROR] folders.txt not found at: {folders_file_path}")
        return []

    with open(folders_file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def generate_html(results):
    html_path = os.path.join(REPO_ROOT, "dashboard.html")

    html = """
    <html>
    <head>
        <title>Interview Playbook Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f4; }
            h1 { color: #333; }
            .folder-section { background: white; padding: 15px; margin-bottom: 20px; border-radius: 8px; }
            .sub-item { margin-left: 20px; font-size: 16px; }
            .subfolder { font-weight: bold; color: #222; }
            .file-list { margin-left: 40px; color: #555; }
        </style>
    </head>
    <body>
        <h1>📘 Interview Playbook Dashboard</h1>
    """

    for folder, content in results.items():
        html += f"<div class='folder-section'><h2>📂 {folder}</h2>"

        # CASE A — Subfolders
        if isinstance(content, dict):
            for subfolder, files in content.items():
                html += f"<p class='sub-item'><span class='subfolder'>{subfolder}</span>:</p>"
                html += "<div class='file-list'>"
                for file in files:   # print nothing if empty
                    html += f"<p>📄 {file}</p>"
                html += "</div>"

        # CASE B — Direct files
        elif isinstance(content, list):
            html += "<div class='file-list'>"
            for file in content:  # print nothing if empty
                html += f"<p>📄 {file}</p>"
            html += "</div>"

        html += "</div>"

    html += "</body></html>"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✅ HTML Dashboard created at: {html_path}")


if __name__ == "__main__":
    folders = load_folders()

    print("📁 Scanning folders...\n")

    results = {}
    for folder in folders:
        results[folder] = summarize_problems(folder)

    generate_html(results)
