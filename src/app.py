from flask import Flask, jsonify, request
from .scraper import *


app = Flask('mtg-price-fetcher')

@app.route('/cards')
def fetch_card_price():
    cardname = request.args.get('name')
    setname = request.args.get('set')

    result = get_card_price(cardname, setname)

    return jsonify(result)
