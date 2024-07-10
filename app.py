from flask import Flask, request, render_template_string
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
import os
from googletrans import Translator

# Configuration de NLTK pour utiliser le répertoire local
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

app = Flask(__name__)
translator = Translator()


def summarize_text(
    text,
    sentences_count=3,
    language="french",
    algorithm="lsa",
    target_language="english",
):
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
    summary_text = " ".join([str(sentence) for sentence in summary])

    # Traduire le résumé si la langue cible est différente de la langue source
    if target_language != language:
        summary_text = translator.translate(
            summary_text, src=language, dest=target_language
        ).text

    return summary_text


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    original_text = ""
    if request.method == "POST":
        try:
            original_text = request.form.get("text", "")
            sentences_count = int(request.form.get("sentences", 3))
            language = request.form.get("language", "french")
            algorithm = request.form.get("algorithm", "lsa")
            target_language = request.form.get("target_language", "english")
            summary = summarize_text(
                original_text, sentences_count, language, algorithm, target_language
            )
        except Exception as e:
            summary = f"Erreur: {str(e)}"

    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Synthèse AI - Résumeur de Texte Intelligent</title>
            <style>
                :root {
                    --bg-color: #ffffff;
                    --text-color: #333333;
                    --primary-color: #3498db;
                    --secondary-color: #ecf0f1;
                }
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    padding: 20px;
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: var(--bg-color);
                    color: var(--text-color);
                    transition: background-color 0.3s, color 0.3s;
                }
                h1 {
                    color: var(--primary-color);
                    text-align: center;
                }
                textarea, select, input, button {
                    margin-bottom: 10px;
                    width: 100%;
                    padding: 10px;
                    box-sizing: border-box;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    transition: all 0.3s ease;
                }
                textarea {
                    height: 200px;
                    resize: vertical;
                }
                button {
                    background-color: var(--primary-color);
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #2980b9;
                    transform: translateY(-2px);
                    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                }
                .result {
                    background-color: var(--secondary-color);
                    padding: 15px;
                    border-radius: 5px;
                    margin-top: 20px;
                    opacity: 0;
                    transform: translateY(20px);
                    transition: opacity 0.5s, transform 0.5s;
                }
                .result.show {
                    opacity: 1;
                    transform: translateY(0);
                }

                #theme-toggle-container {
                    display: flex;
                    justify-content: center;
                    width: 100%;
                    margin-bottom: 20px;
                }
                #theme-toggle {
                    width: 30%;
                    position: static;
                    padding: 10px;
                    border-radius: 15px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    font-size: 16px;
                }
                .dark-mode {
                    --bg-color: #2c3e50;
                    --text-color: #ecf0f1;
                    --primary-color: #3498db;
                    --secondary-color: #34495e;
                }
                @media (max-width: 600px) {
                    body {
                        padding: 10px;
                    }
                    textarea {
                        height: 150px;
                    }
                }
            </style>
        </head>
        <body>
            <div id="theme-toggle-container">
                <button id="theme-toggle">🌓 Changer de thème</button>
            </div>
            <h1>Synthèse AI</h1>
            <form method="post" id="summarize-form">
                <textarea name="text" placeholder="Entrez votre texte ici" required>{{ original_text }}</textarea>
                <select name="algorithm">
                    <option value="lsa">LSA</option>
                    <option value="textrank">TextRank</option>
                    <option value="lexrank">LexRank</option>
                </select>
                <input type="number" name="sentences" min="1" max="10" value="3" placeholder="Nombre de phrases">
                <select name="target_language">
                    <option value="english">Anglais</option>
                    <option value="french">Français</option>
                </select>
                <button type="submit">Résumer</button>
            </form>
            <div id="result" class="result {% if summary %}show{% endif %}">
                <h2>Résumé:</h2>
                <p>{{ summary }}</p>
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
