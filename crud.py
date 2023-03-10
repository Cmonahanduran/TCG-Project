"""Crud operations"""

from model import db, User, Collection, Card, CardHandler, Deck,Post, connect_to_db

# User functions
def create_user(username, email, password):
    """Create and return a new user."""
    user = User(username=username,email=email,password=password)

    return user

def get_user_by_username(username):

    return User.query.filter(User.username == username).first()


#Card functions


def get_card_by_color(colors):

    return Card.query.get(colors)

def create_card(name, manaCost,cmc, colors, colorIdentity,type,rarity,setName, text, flavor, artist, imageUrl):

    card = Card(name=name, manaCost=manaCost,cmc=cmc, colors=colors, colorIdentity=colorIdentity,type=type,rarity=rarity,setName=setName, text=text, flavor=flavor, artist=artist, imageUrl=imageUrl)
    return card

def create_card_list():
    #returns a list of all cards
    return Card.query.filter(Card.imageUrl != '').all()

def get_card_by_rarity(rarity):

    return Card.query.get(rarity)

def get_card_by_set(setName):

    return Card.query.get(setName)

def get_card_by_cost(manaCost):

    return Card.query.get(manaCost)

def get_card_by_id(id):

    return Card.query.get(id)

def get_card_by_name(name):
    
    return Card.query.filter(Card.name == name).first()

#deck functions

def create_deck(deck_name, username):

    deck = Deck(deck_name=deck_name, username=username)

    return deck

def get_deck_by_card_id(card_id):

    deck = Deck.query.filter(Deck.name == card_id).first()

def get_deck(deck_id):

    return Deck.query.get(deck_id)


def add_card_to_deck(id,deck_name):

    card = Card.query.get(id)
    deck = Deck.query.filter(Deck.deck_name == deck_name).first()

    deck.cards.append(card)
    return deck

def remove_card_from_deck(id,deck_name):
    deck = Deck.query.filter(Deck.deck_name == deck_name).first()
    card = Card.query.get(id)
    print(deck_name)
    print(deck)
    deck.cards.remove(card)
    return deck

def trade_cards(deck, owned_card, trade_card):

    deck.cards.remove(owned_card)
    deck.cards.append(trade_card)
    return deck
#post functions

def create_post(username,post_title,post_text, owned_card_id, trade_card_id):

    post = Post(username=username, post_title=post_title, post_text=post_text, owned_card_id=owned_card_id, trade_card_id=trade_card_id)

    return post

def create_post_list():
    
    return Post.query.filter().all()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)