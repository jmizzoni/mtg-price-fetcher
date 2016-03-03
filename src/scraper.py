from htmldom import htmldom
from fuzzywuzzy import process
from html import unescape
import requests
import urllib

MTGSTOCKS_BASE_URL = 'http://www.mtgstocks.com'
QUERY_STRING = '/cards/search?utf8=%E2%9C%93&print%5Bcard%5D={}&button='
SETS_PATH = MTGSTOCKS_BASE_URL + '/sets'

def generate_search_url(name):
    formatted_name = urllib.parse.quote('+'.join(name.split(' ')), '/+')
    return MTGSTOCKS_BASE_URL + QUERY_STRING.format(formatted_name)

# searches all items on the given page matching the given selector
# and returns the one closes
def get_matching_item_on_page(url, text, selector):
    page = htmldom.HtmlDom(url)
    page.createDom()
    elems = page.find(selector)

    possible_matches = [elem.text() for elem in elems]
    best_match = process.extractOne(text, possible_matches)

    match_index = possible_matches.index(best_match[0])
    return elems[match_index]

def get_card_url_from_search_results(search_url, name):
    card_link = get_matching_item_on_page(search_url, name, '.table > tbody > tr > td > a')

    return MTGSTOCKS_BASE_URL + card_link.attr('href')

def card_url_from_name(name):
    query_url = generate_search_url(name)
    response = requests.get(query_url, allow_redirects=False)

    if (response.status_code in range(301, 307)):
        return response.headers['Location']
    elif (response.status_code == requests.codes.ok):
        return get_card_url_from_search_results(query_url, name)

    return None

def card_url_from_set(name, card_set):
    set_link = get_matching_item_on_page(SETS_PATH, card_set, '.list > a')

    card_link = get_matching_item_on_page(
        MTGSTOCKS_BASE_URL + set_link.attr('href'),
        name,
        '.table tr > td > a'
    )

    return MTGSTOCKS_BASE_URL + card_link.attr('href')

def scrape_price(card_url):
    card_page = htmldom.HtmlDom(card_url)
    card_page.createDom()
    card_name = card_page.find('h2 > a').text()
    card_set = card_page.find('h5 > a').text()
    price_values = [elem.text() for elem in card_page.find('.priceheader')]
    price_keys = ['avg']

    if len(price_values) > 1:
        price_keys.insert(0, 'low')
        price_keys.append('high')

    return {
        'name': unescape(card_name),
        'set': unescape(card_set),
        'link': card_url,
        'promo': len(price_keys) == 1,
        'prices' : dict(zip(price_keys, price_values))
    }



def get_card_price(name, card_set=None):
    if card_set is not None:
        card_url = card_url_from_set(name, card_set)
    else:
        card_url = card_url_from_name(name)

    return scrape_price(card_url)


