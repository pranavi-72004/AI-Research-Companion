from flask import Flask, render_template, request
from pdf_processor import extract_text
from summarizer import analyze_paper
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template(
        "index.html",
        summary=None
    )


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["pdf"]

    feature = request.form.get("feature", "summary")

    print("=" * 50)
    print("Selected Feature:", feature)
    print("=" * 50)

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(path)

    text = extract_text(path)

    result = analyze_paper(
        text,
        feature
    )

    return render_template(
        "index.html",
        summary=result
    )


if __name__ == "__main__":
    app.run(debug=True)