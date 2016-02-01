# mtg-price-fetcher

## Description

A simple REST API for fetching pricing data on Magic: The Gathering Cards from MTGStocks.com

## Usage

### Search by card name

```
http://host.url/cards/<cardname>
```
Return Format (JSON):
```
{
    "name": "Card Name",
    "set":  "Card Set",
    "link": "http://mtgstocks.com/prints/<card-id>"
    "prices": {
        "avg":  "$00.00"
        "high": "$00.00"
        "low":  "$00.00"
        "foil": ""
    }
```

The `foil` field will be blank in most cases. When it is not, it means that the card found is a printing only available in foil, such as an FTV or Duel Deck. MTGStocks doesn't list high, average and low prices in this case, so those fields will be blank instead. 
**More to come!** 


## Disclaimer

Magic: the Gathering is copyrighted by  Wizards of the Coast. This project is not affiliated with Wizards or MTGStocks.com in any way.
