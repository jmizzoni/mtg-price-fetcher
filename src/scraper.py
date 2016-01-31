from htmldom import htmldom
import requests
import urllib

MTGSTOCKS_BASE_URL = "http://www.mtgstocks.com"
QUERY_STRING = "/cards/search?utf8=%E2%9C%93&print%5Bcard%5D={}&button="

def generate_search_url(name):
    formatted_name = urllib.parse.quote('+'.join(name.split(' ')), '/+')
    return MTGSTOCKS_BASE_URL + QUERY_STRING.format(formatted_name)


def get_card_url_from_search_results(search_url, name):
    results_page = htmldom.HtmlDom(search_url)
    results_page.createDom()
    result_links = results_page.find('.table > tbody > tr > td > a')

    for result in result_links:
        if result.text().lower() == name.lower():
            return MTGSTOCKS_BASE_URL + result.attr('href')
        
    return MTGSTOCKS_BASE_URL + result_links.first().attr('href')


def card_url_from_name(name):
    query_url = generate_search_url(name)
    response = requests.get(query_url, allow_redirects=False)

    if (response.status_code in range(301, 307)):
        return response.headers['Location']
    elif (response.status_code == requests.codes.ok):
        return get_card_url_from_search_results(query_url, name)

    return None

def scrape_price(card_url):
    card_page = htmldom.HtmlDom(card_url)
    card_page.createDom() 
    card_name = card_page.find('h2 > a').text()
    card_set = card_page.find('h5 > a').text()

    price_keys = ['low', 'avg', 'high']
    price_values = [elem.text() for elem in card_page.find('.priceheader')]
    
    return {
        "name": card_name,
        "set": card_set,
        "link": card_url,
        "prices" : dict(zip(price_keys, price_values))
    }

            

def get_card_price(name, set=None):
    card_url = card_url_from_name(name)

    return scrape_price(card_url)


