from flask import Flask, jsonify
from scraper import *


app = Flask(__name__)

@app.route('/cards/<cardname>') 
def fetch_card_price(cardname):
    result = get_card_price(cardname)
    print(result)

    return jsonify(result)

if __name__ == '__main__':
    app.run()
