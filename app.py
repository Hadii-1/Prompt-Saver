"""
AI Prompt Saver - Flask Backend
A simple web app to save and view AI prompts using a CSV file as storage.
"""

import csv
import os
from datetime import datetime   
# type: ignore 
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "prompt-saver-secret-key"  # Required for flash messages

# Path to the CSV data file
DATA_FILE = "data.csv"
CSV_HEADERS = ["id", "title", "prompt", "timestamp"]


def init_csv():
    """Create data.csv with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)


def get_next_id():
    """Read all rows and return the next auto-incremented ID."""
    rows = read_all_prompts()
    if not rows:
        return 1
    return max(int(row["id"]) for row in rows) + 1


def save_prompt(title, prompt_text):
    """Append a new prompt entry to the CSV file."""
    new_id = get_next_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, title, prompt_text, timestamp])


def read_all_prompts():
    """Read and return all prompts from the CSV file as a list of dicts."""
    prompts = []
    try:
        with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                prompts.append(row)
    except FileNotFoundError:
        pass
    return prompts


# ──────────────────────────────────────────────
#  ROUTES
# ──────────────────────────────────────────────

@app.route("/", methods=["GET", "POST"])
def index():
    """Home page — shows the submission form."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        prompt_text = request.form.get("prompt", "").strip()

        # Basic server-side validation
        if not title or not prompt_text:
            flash("Both fields are required. Please fill in the title and prompt.", "error")
            return render_template("index.html", title=title, prompt=prompt_text)

        save_prompt(title, prompt_text)
        flash("Prompt saved successfully! ✓", "success")
        # Redirect to clear the form (Post/Redirect/Get pattern)
        return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/prompts")
def prompts():
    """View prompts page — displays all saved prompts, newest first."""
    all_prompts = read_all_prompts()
    # Reverse to show newest first
    all_prompts.reverse()
    return render_template("prompts.html", prompts=all_prompts)


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────

if __name__ == "__main__":
    init_csv()  # Ensure CSV file exists before starting
    app.run(debug=True)
