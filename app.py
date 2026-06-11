from flask import Flask, render_template, request
from pdf_processor import extract_text
from summarizer import analyze_paper
from rag import build_vector_store, search_chunks
from chat_paper import answer_question
import os


app = Flask(__name__)

# Store paper data globally
paper_index = None
paper_chunks = None
latest_result = None

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template(
    "index.html",
    summary=None,
    answer=None,
    scroll=False
)


@app.route("/upload", methods=["POST"])
def upload():
    global paper_index, paper_chunks

    file = request.files["pdf"]
    feature = request.form.get("feature", "summary")

    print("=" * 50)
    print("Selected Feature:", feature)
    print("=" * 50)

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    text = extract_text(path)

    # ✅ Only build vector store for chat feature
    if feature == "chat":
        paper_index, paper_chunks = build_vector_store(text)

    global latest_result
    result = analyze_paper(text, feature)
    latest_result = result

    return render_template(
        "index.html",
        summary=latest_result,
        answer=None,
        scroll=True
    )
@app.route("/ask", methods=["POST"])
def ask():

    global paper_index
    global paper_chunks
    global latest_result

    if paper_index is None:
        return render_template(
            "index.html",
            summary=latest_result,
            answer="Please upload a research paper first."
        )

    question = request.form["question"]

    context = search_chunks(
        question,
        paper_index,
        paper_chunks
    )

    answer = answer_question(
        question,
        context
    )

    return render_template(
    "index.html",
    summary=latest_result,
    answer=answer,
    scroll=True
)

if __name__ == "__main__":
    app.run(debug=True)