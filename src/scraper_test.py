from  scraper import *

# Currently just a script to run a few demo cases for anity checking purposes
# TODO: programatically compare results

# Ordinary case
print(get_card_price("tarmogoyf"))

# 'Splinter' is a card with a name that is a substring of another
# this should return the correct card
print(get_card_price("splinter"))

# testing that you can search with random unicode characters
print(get_card_price("jace, vryn's prodigy"))

# testing search-by-set
print(get_card_price('Wasteland', 'Tempest'))
