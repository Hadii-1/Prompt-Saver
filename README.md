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
git clone [https://github.com/your-username/prompt-saver.git](https://github.com/Hadii-1/Prompt-Saver.git)
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
