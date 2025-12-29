from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

JAMENDO_API_URL = "https://api.jamendo.com/v3.0/tracks"
JAMENDO_API_KEY = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<query>')
def search(query):
    params = {
        'client_id': JAMENDO_API_KEY,
        'format': 'json',
        'limit': 10,
        'namesearch': query,
        'tags': 'hindi',  
        'order': 'popularity_total'
    }
    response = requests.get(JAMENDO_API_URL, params=params)
    data = response.json()
    return jsonify(data['results'])

if __name__ == '__main__':
    app.run(debug=True)

