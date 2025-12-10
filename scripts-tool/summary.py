import os
import sys

# --- Fix Windows Unicode Output (CP1252 issue) ---
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
FOLDERS_FILE = os.path.join(REPO_ROOT, "folders.txt")


# ------------------------------------------------
# Load folders from folders.txt
# ------------------------------------------------
def load_folders():
    if not os.path.exists(FOLDERS_FILE):
        print(f"[ERROR] folders.txt not found at: {FOLDERS_FILE}")
        return []
    with open(FOLDERS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


# ------------------------------------------------
# Produce a hierarchical tree list
# ------------------------------------------------
def summarize_folder(folder):
    folder_path = os.path.join(REPO_ROOT, folder)

    if not os.path.exists(folder_path):
        print(f"[WARN] Folder not found: {folder_path}")
        return []

    tree_output = []

    for root, dirs, files in os.walk(folder_path):
        rel_root = os.path.relpath(root, folder_path)

        # Convert Windows \ to /
        rel_root = rel_root.replace("\\", "/")

        indent_level = rel_root.count("/") if rel_root != "." else 0
        indent = " " * 4 * indent_level

        # Print folder (except root)
        if rel_root != ".":
            tree_output.append(f"{indent}• {rel_root}/")

        # Print files
        for f in files:
            file_indent = " " * 4 * (indent_level + 1)
            path = f"{rel_root}/{f}" if rel_root != "." else f
            path = path.replace("\\", "/")
            tree_output.append(f"{file_indent}• {path}")

    return tree_output


# ------------------------------------------------
# Generate dashboard.html
# ------------------------------------------------
def generate_dashboard(results):
    dashboard_path = os.path.join(REPO_ROOT, "dashboard.html")

    html = """
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Repository Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f4; }
        h1 { color: #333; }
        h2 { color: #444; margin-top: 30px; }
        pre { background: white; padding: 15px; border-radius: 8px; }
    </style>
    </head>
    <body>
        <h1>📘 Repository Dashboard</h1>
    """

    for folder, content in results.items():
        html += f"<h2>📁 {folder}</h2><pre>"
        for item in content:
            html += item + "\n"
        html += "</pre>"

    html += "</body></html>"

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✅ Dashboard generated at: {dashboard_path}")


# ------------------------------------------------
# MAIN
# ------------------------------------------------
if __name__ == "__main__":
    print("📁 Scanning folders...\n")

    folders = load_folders()
    results = {}

    for folder in folders:
        tree = summarize_folder(folder)
        results[folder] = tree

        # Console output
        print(f"📂 {folder}:")
        for line in tree:
            print(line)
        print()

    generate_dashboard(results)
