# mtg-price-fetcher

## Description

A simple REST API for fetching pricing data on Magic: The Gathering Cards from MTGStocks.com

## Usage

Arguments aare provided by way of URL query paramteters

### Search by card name

```
http://host.url/cards?name=<cardname>
```
Return Format (JSON):
```
{
    "name": "Card Name",
    "set":  "Card Set",
    "link": "http://mtgstocks.com/prints/<card-id>"
    "promo": false
    "prices": {
        "avg":  "$00.00"
        "high": "$00.00"
        "low":  "$00.00"
    }
```

### Specify a Printing

```
http://host.url/cards?name=<cardname>&set=<setname>
```

The `promo` field indicates whether or not the card returned by the search is a printing that is only available in foil, such as a Duel Deck or FTV foil. In this case, the `high` and `low` fields will be blank. Why MTGStocks does this eludes me.

**More to come!** 

## Todos
- Add foil pricing

## Disclaimer

Magic: the Gathering is copyrighted by  Wizards of the Coast. This project is not affiliated with Wizards or MTGStocks.com in any way.
