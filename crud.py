"""Crud operations"""

from model import db, User, Collection, Card, CardHandler, Deck, connect_to_db


def create_user(username, email, password):
    """Create and return a new user."""
    user = User(username=username,email=email,password=password)

    return user

def get_user_by_username(username):

    return User.query.filter(User.username == username).first()

def get_card_by_color(colors):

    return Card.query.get(colors)

def create_card(name, manaCost,cmc, colors, colorIdentity,type,rarity,setName, text, flavor, artist, imageUrl):

    card = Card(name=name, manaCost=manaCost,cmc=cmc, colors=colors, colorIdentity=colorIdentity,type=type,rarity=rarity,setName=setName, text=text, flavor=flavor, artist=artist, imageUrl=imageUrl)
    return card


def create_card_list():
    #returns a list of all cards
    return Card.query.all()

def get_card_by_rarity(rarity):

    return Card.query.get(rarity)

def get_card_by_set(setName):

    return Card.query.get(setName)

def get_card_by_cost(manaCost):

    return Card.query.get(manaCost)


def create_deck(deck_name, username):

    deck = Deck(deck_name=deck_name, username=username)

    return deck

def get_deck(deck_id):

    return Deck.query.get(deck_id)


def get_card_by_id(id):

    return Card.query.get(id)

def add_card_to_deck(id,deck_name):

    card = Card.query.get(id)
    deck = Deck.query.filter(Deck.deck_name == deck_name).first()

    deck.cards.append(card)
    return deck


def add_card_to_user(id,collection_id):

    card = Card.query.get(id)
    collection = Collection.query.get(collection_id)
    user.cards.append(card)
    #pass in user_id
    return collection

if __name__ == '__main__':
    from server import app
    connect_to_db(app)