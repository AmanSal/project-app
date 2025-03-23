from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Azure Web App Backend!</h1>"

@app.route("/api/data")
def api_data():
    return jsonify({"message": "This is a sample API response from Azure Web App."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)