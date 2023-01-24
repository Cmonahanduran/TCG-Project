"""Script to seed database."""

import os
import json

import crud
import model
import server

os.system("dropdb cards")
os.system("createdb cards")

model.connect_to_db(server.app)
model.db.create_all()

# load card data from JSON file
with open('data/cards.json') as f:
    card_data = json.loads(f.read())

cards_in_db = []

# get all the relevant card info for each card from the card dictionary

for card in card_data:
    name, manaCost, cmc, colors, colorIdentity, types, rarity, setName, text, artist, imageUrl = (
        card["name"],
        card["manaCost"],
        card["cmc"],
        card["colors"],
        card["colorIdentity"],
        card["types"],
        card["rarity"],
        card["setName"],
        card["text"],
        card["artist"],
        card["imageUrl"],

    )

    db_card = crud.create_card(name, manaCost,cmc, colors, colorIdentity,types,rarity,setName, text, artist, imageUrl)
    cards_in_db.append(db_card)


model.db.session.add_all(cards_in_db)
model.db.session.commit()