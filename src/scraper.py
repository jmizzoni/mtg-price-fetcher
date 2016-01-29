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


def card_page_from_name(name):
    query_url = generate_search_url(name)
    print('QUERYING {}'.format(query_url))
    response = requests.get(query_url, allow_redirects=False)

    if (response.status_code in range(301, 307)):
        query_url = response.headers['Location']
    elif (response.status_code == requests.codes.ok):
        query_url = get_card_url_from_search_results(query_url, name)
    else:
        return None
    
    print(query_url)
    return htmldom.HtmlDom(query_url)

def scrape_price(card_page):
    card_page.createDom() 
    price_keys = ['low', 'avg', 'high']
    price_values = [elem.text() for elem in card_page.find('.priceheader')]
    return dict(zip(price_keys, price_values))
            

def get_card_price(name, set=None):
    
    card_page = card_page_from_name(name)

    result = scrape_price(card_page)
    print(result)
    
    return result

