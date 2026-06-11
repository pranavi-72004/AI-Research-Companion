# 📚 AI Research Paper Assistant

An AI-powered web application that helps users quickly search, understand, and summarize research papers in a simple and user-friendly way.

---

## 🚀 Live Demo
🔗 https://your-deployment-link.onrender.com

---

## 📌 Features

- 🔍 Search research papers easily
- 🧠 AI-based summarization of content
- 📄 Clean and simple UI for reading papers
- ⚡ Fast responses using API integration
- 🌐 Web-based interface (no installation needed)

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- HTML, CSS, JavaScript 🎨
- REST APIs (for AI integration)
- Gunicorn (deployment server)

---

## 📁 Project Structure

```
AI-Research-Companion/
│
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Research-Companion.git
cd AI-Research-Companion
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate environment
```bash
venv\Scripts\activate    # Windows
source venv/bin/activate  # Mac/Linux
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up Environment Variables

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> 🔑 Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)


### 6. Run the app
```bash
python app.py
```

Then open:
```
http://127.0.0.1:5000
```

---

## 📈 Future Improvements

- 📊 Add research paper recommendation system
- 🤖 Improve AI summarization accuracy
- 💬 Add chatbot-style interface
- 🌙 Dark mode UI
- 📱 Mobile responsive design

---

## 👩‍💻 Author

**Pranavi S**
Computer Science & Engineering Student

---

## 📜 License
This project is licensed under the MIT License - feel free to use and modify it with credits
