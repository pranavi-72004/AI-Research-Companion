# 🧠 AI RESEARCH COMAPNION

AI Research Companion is an AI-powered web application that simplifies research paper analysis by transforming complex academic papers into actionable insights.

The platform enables users to upload research papers and instantly generate summaries, project ideas, implementation roadmaps, research gap analysis, literature reviews, citations, and interactive question-answering. It combines Google Gemini AI with Retrieval-Augmented Generation (RAG) techniques to provide context-aware responses directly from uploaded documents.

Designed for students, researchers, and developers, ResearchMind AI reduces the time required to understand and extract valuable information from research publications.

---

## 🚀 Live Demo
🔗 https://ai-research-companion-otqy.onrender.com

---

## 📌 Features

- 📄 Generate research paper summaries
- 💡 Generate project ideas from research papers
- 🗺️ Create implementation roadmaps
- 🔍 Identify research gaps
- 📚 Generate literature reviews
- 📝 Generate citations (APA, IEEE, MLA)
- 💬 Chat with uploaded research papers using RAG

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- Google Gemini API 🤖
- PyPDF2 📄
- HTML, CSS, JavaScript 🎨

---

## 📁 Project Structure

```
AI-Research-Companion/
│
├── app.py
├── summarizer.py
├── chat_paper.py
├── rag.py
├── pdf_processor.py
├── requirements.txt
├── Procfile
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── uploads/
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Research-Companion.git
cd AI-Research-Companion
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the environment
```bash
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
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


### 6. Run the application
```bash
python app.py
```

Then open:
```
http://127.0.0.1:5000
```

---

## 👩‍💻 Author

**Pranavi S**  

---

## 📜 License

This project is licensed under the MIT License - feel free to use and modify it with credits.
