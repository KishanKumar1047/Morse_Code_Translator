from flask import Flask, render_template, request, jsonify
from morse_utils import text_to_morse, morse_to_text, suggest_words, MORSE_CODE_DICT
import os
import nltk
from nltk.corpus import words

# Download words dataset if not already available
nltk.download("words", quiet=True)
ENGLISH_WORDS = set(words.words())

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    input_text = data.get("text", "").strip()
    mode = data.get("mode", "eng")  # eng or morse

    if not input_text:
        return jsonify({"error": "Empty input"})

    if mode == "eng":
        morse_code = text_to_morse(input_text)
        suggestions = []
        if input_text.lower() not in [w.lower() for w in ENGLISH_WORDS]:
            suggestions = suggest_words(input_text.lower(), ENGLISH_WORDS)
        return jsonify({"output": morse_code, "suggestions": suggestions})

    elif mode == "morse":
        english_text = morse_to_text(input_text)
        return jsonify({"output": english_text, "suggestions": []})

    return jsonify({"error": "Invalid mode"})


# Run locally or on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render injects PORT
    app.run(host="0.0.0.0", port=port, debug=True)
