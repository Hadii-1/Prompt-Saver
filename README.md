# 🚀 AI Prompt Saver

A minimal and clean web application built with **Flask (Python)** that allows users to save and manage AI prompts using a simple CSV file as storage.

---

## 📌 Features

* 📝 Save AI prompts with title and description
* 📂 Store data using CSV (no database required)
* 📊 View all saved prompts (newest first)
* ✅ Form validation (client + server side)
* 🔔 Flash messages for user feedback
* 📋 Copy prompt to clipboard
* 🎨 Clean, professional light UI
* 📱 Responsive design

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, minimal JavaScript
* **Storage:** CSV file

---
# Prompt : 

Create a minimal but professional full-stack web application using Flask (Python) with the following requirements:

PROJECT NAME: AI Prompt Saver

GOAL:
Build a simple web app where users can submit AI prompts and view previously saved prompts. Use a CSV file as storage instead of a database.

TECH STACK:

* Backend: Python with Flask
* Frontend: HTML, CSS (no frameworks like React)
* Optional: minimal JavaScript (only if necessary)
* Data storage: CSV file

FEATURES:

1. HOME PAGE ("/")

* A clean, modern UI with a centered card layout
* Form with:

  * Input field for "Prompt Title"
  * Textarea for "Prompt"
  * Submit button
* After submission, show a success message

2. SAVE FUNCTIONALITY

* On form submission (POST request):

  * Save data into a CSV file (data.csv)
  * Columns: id, title, prompt, timestamp
  * Auto-increment ID

3. VIEW PROMPTS PAGE ("/prompts")

* Display all saved prompts in a clean layout
* Each prompt shown as a card:

  * Title
  * Prompt text
  * Timestamp
* Show newest prompts first

4. UI DESIGN (IMPORTANT)

* Use a LIGHT theme (NOT dark)
* Color palette:

  * Background: soft off-white or light grey (#f5f7fa)
  * Primary: soft blue (#4a90e2)
  * Accent: muted teal or green
* Clean spacing, rounded corners, subtle shadows
* Professional font (like Arial, Inter, or system font)
* Responsive design (works on mobile)

5. STRUCTURE:

* app.py
* data.csv (create if not exists)
* templates/

  * index.html
  * prompts.html
* static/

  * style.css

6. FLASK REQUIREMENTS:

* Use render_template
* Use POST and GET methods correctly
* Separate routes:

  * "/" → form page
  * "/prompts" → display page

7. CODE QUALITY:

* Keep code simple and readable
* Add comments explaining key parts
* Do not overcomplicate

8. EXTRA (if easy):

* Clear form after submission
* Basic validation (no empty input)

OUTPUT:
Provide complete working code for:

* app.py
* HTML templates
* CSS file

Ensure the app runs with:
python app.py

And works locally on http://127.0.0.1:5000/

IMPORTANT:
Keep everything minimal, clean, and professional — suitable for a student internship project.


## 📁 Project Structure

```
prompt-saver/
│
├── app.py
├── data.csv
│
├── templates/
│   ├── index.html
│   └── prompts.html
│
├── static/
│   └── style.css
│
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Hadii-1/Prompt-Saver.git
cd prompt-saver
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the app

```
python app.py
```

---

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

* Users submit prompts through a form
* Flask handles the request and saves data into a CSV file
* Data is retrieved and displayed dynamically using Jinja templates

---

## 📸 Future Improvements

* ✏️ Edit prompts
* ❌ Delete prompts
* 🔍 Search functionality
* 🌐 Deploy online

---

## 👨‍💻 Author

**Muhammad Hadi**
Computer Science Student

---

## ⭐ Acknowledgment

Built as part of an internship task to demonstrate understanding of:

* Flask APIs
* Backend-Frontend integration
* File-based data handling
