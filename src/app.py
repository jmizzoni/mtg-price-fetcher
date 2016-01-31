from flask import Flask, jsonify
from .scraper import *


app = Flask('mtg-price-fetcher')

@app.route('/cards/<cardname>') 
def fetch_card_price(cardname):
    result = get_card_price(cardname)
    print(result)

    return jsonify(result)
