"""Script to seed database."""

import os
import json

import crud
import model
import server

os.system("dropdb cards")
os.system("createdb cards")
server.app.app_context().push()
model.connect_to_db(server.app)
model.db.create_all()

# load card data from JSON file
with open('data/cards.json') as f:
    card_data = json.loads(f.read())
    card_data = card_data['cards']

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
# get all the relevant card info for each card from the card dictionary

for card in card_data:
    print(card)
    name, manaCost, cmc, colors, colorIdentity, type, rarity, setName, text, flavor, artist, imageUrl = (
        card["name"],
        card["manaCost"],
        card["cmc"],
        card.get("colors",""),
        card.get("colorIdentity",""),
        card["type"],
        card["rarity"],
        card["setName"],
        card.get('text',""),
        card.get("flavor",""),
        card["artist"],
        card.get("imageUrl",""),

    )

    db_card = crud.create_card(name, manaCost,cmc, colors, colorIdentity,type,rarity,setName, text, flavor, artist, imageUrl)
    cards_in_db.append(db_card)


model.db.session.add_all(cards_in_db)
model.db.session.commit()