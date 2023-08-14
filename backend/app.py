from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_random_response
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

app.config.from_object(__name__)

# CORS(app, resources = {r"/*":{'origins':"*"}})
CORS(app, resources = {r"/*":{'origins':"http://localhost:8080", "allow_headers": "Access-Control-Allow-Origin"}})

english_bot = ChatBot(
    "Chatterbot", 
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    logic_adapters = [
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": LevenshteinDistance,
            "response_selection_method": get_random_response,
            "default_response": "Your response is outside of my capacity. Please consult a different entity regarding your concern.",
            "threshold": 0.3,
            "maximum_similarity_threshold": 0.90
        }
    ]
)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train(
    "chatterbot.corpus.english.customer service",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor"
)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/bot")
def get_bot_response():
    userText = request.args.get("msg")
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug = True)