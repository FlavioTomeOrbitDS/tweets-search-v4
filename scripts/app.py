from flask import Flask, jsonify
from index import tweetSearch, config_driver
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return "hello world"

@app.route("/tweetSearch", methods = ["GET","POST"] )
def main():
    
    r = tweetSearch("https://twitter.com/search?q=Angular%20lang%3Apt%20until%3A2024-01-02%20since%3A2024-01-01&src=recent_search_click", 3)
    
    return jsonify(r)

if __name__ == "__main__":
    app.run(debug = True, port=8080)