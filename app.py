from flask import Flask, request, render_template_string
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk

nltk.download("punkt")

app = Flask(__name__)


def summarize_text(text, sentences_count=3, language="french", algorithm="lsa"):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    stemmer = Stemmer(language)

    if algorithm == "lsa":
        summarizer = LsaSummarizer(stemmer)
    elif algorithm == "textrank":
        summarizer = TextRankSummarizer(stemmer)
    elif algorithm == "lexrank":
        summarizer = LexRankSummarizer(stemmer)
    else:
        raise ValueError("Algorithme non supporté")

    summarizer.stop_words = get_stop_words(language)

    summary = summarizer(parser.document, sentences_count)
    return " ".join([str(sentence) for sentence in summary])


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    original_text = ""
    if request.method == "POST":
        original_text = request.form.get("text", "")
        sentences_count = int(request.form.get("sentences", 3))
        language = request.form.get("language", "french")
        algorithm = request.form.get("algorithm", "lsa")
        summary = summarize_text(original_text, sentences_count, language, algorithm)

    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TextDistill - Résumeur de Texte Intelligent</title>
            <style>
                :root {
                    --bg-color: #ffffff;
                    --text-color: #333333;
                    --button-color: #4CAF50;
                    --button-hover-color: #45a049;
                    --input-border-color: #ccc;
                    --result-bg-color: #f9f9f9;
                    --result-border-color: #ddd;
                    --font-family: Arial, sans-serif;
                }

                body {
                    background-color: var(--bg-color);
                    color: var(--text-color);
                    font-family: var(--font-family);
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }

                .container {
                    max-width: 800px;
                    margin: 20px;
                    padding: 20px;
                    border: 1px solid var(--input-border-color);
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }

                h1 {
                    font-size: 2em;
                    margin-bottom: 20px;
                }

                form {
                    display: flex;
                    flex-direction: column;
                }

                textarea, select, input[type="number"] {
                    margin-bottom: 10px;
                    padding: 10px;
                    border: 1px solid var(--input-border-color);
                    border-radius: 4px;
                    font-size: 1em;
                }

                button {
                    background-color: var(--button-color);
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 1em;
                }

                button:hover {
                    background-color: var(--button-hover-color);
                }

                .result {
                    margin-top: 20px;
                    padding: 10px;
                    border: 1px solid var(--result-border-color);
                    background-color: var(--result-bg-color);
                    border-radius: 4px;
                    display: none;
                }

                .result.show {
                    display: block;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>TextDistill - Résumeur de Texte Intelligent</h1>
                <form method="post" id="summarize-form">
                    <textarea name="text" rows="10" placeholder="Collez votre texte ici...">{{ original_text }}</textarea>
                    <select name="language">
                        <option value="french">Français</option>
                        <option value="english">Anglais</option>
                    </select>
                    <select name="algorithm">
                        <option value="lsa">LSA</option>
                        <option value="textrank">TextRank</option>
                        <option value="lexrank">LexRank</option>
                    </select>
                    <input type="number" name="sentences" min="1" max="10" value="3" placeholder="Nombre de phrases">
                    <button type="submit">Résumer</button>
                </form>
                <div id="result" class="result {% if summary %}show{% endif %}">
                    <h2>Résumé:</h2>
                    <p>{{ summary }}</p>
                </div>
            </div>

            <script>
                // Toggle dark mode
                const themeToggle = document.getElementById('theme-toggle');
                themeToggle.addEventListener('click', () => {
                    document.body.classList.toggle('dark-mode');
                });

                // Show result with animation
                const form = document.getElementById('summarize-form');
                const result = document.getElementById('result');
                form.addEventListener('submit', (e) => {
                    e.preventDefault();
                    fetch('/', {
                        method: 'POST',
                        body: new FormData(form)
                    })
                    .then(response => response.text())
                    .then(html => {
                        const parser = new DOMParser();
                        const doc = parser.parseFromString(html, 'text/html');
                        const newResult = doc.getElementById('result');
                        result.innerHTML = newResult.innerHTML;
                        result.classList.add('show');
                    });
                });
            </script>
        </body>
        </html>
    """,
        summary=summary,
        original_text=original_text,
    )


if __name__ == "__main__":
    app.run(debug=True)
