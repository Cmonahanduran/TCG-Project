import json

with open('data/cards.json') as f:
    card_data = json.loads(f.read())
    
with open('data/cards2.json') as f:
    card_data2 = json.loads(f.read())
    card_data.extend(card_data2['cards']) 

with open('data/cards2x2.json') as f:
    card_data2x2 = json.loads(f.read())
    card_data.extend(card_data2x2['cards']) 

with open('data/cards40K.json') as f:
    card_data40K = json.loads(f.read())
    card_data.extend(card_data40K['cards']) 

with open('data/cardsBRO.json') as f:
    card_dataBRO = json.loads(f.read())
    card_data.extend(card_dataBRO['cards']) 



cards_in_db = []
print(len(card_data))