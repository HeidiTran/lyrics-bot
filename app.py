from flask import Flask, request, render_template, jsonify
from lyricsBot import LyricsBot


app = Flask(__name__)
bot = LyricsBot()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        jsonData = request.get_json()
        bot.name = jsonData["username"]
        results = bot.getQuery(jsonData["message"])
        return jsonify(results) 