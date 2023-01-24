

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    """A user."""

    __tablename__ = 'user'

    username = db.Column(db.String, primary_key=True, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    cards = db.relationship("Card", secondary='collection', back_populates="users")

    def __repr__(self):
        return f'<User username={self.username} email={self.email}>'




class Collection(db.Model):
    """A users card collection."""

    __tablename__ = 'collection'

    collection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_name = db.Column(db.String, db.ForeignKey('card.name'), nullable=False)
    username = db.Column(db.String, db.ForeignKey('user.username'), nullable=False)


    def __repr__(self):
        return f'<Collection name={self.card_name} username={self.username}>'


class Card(db.Model):
    """Each card"""

    __tablename__ = 'card'

    name = db.Column(db.String, primary_key=True, unique=True)
    manaCost = db.Column(db.String)
    cmc = db.Column(db.Integer)
    colors = db.Column(db.String)
    colorIdentity = db.Column(db.String)
    types = db.Column(db.String)
    rarity = db.Column(db.String)
    setName = db.Column(db.String)
    text = db.Column(db.String)
    artist = db.Column(db.String)
    imageurl = db.Column(db.String)
    

    users = db.relationship("User", secondary="collection", back_populates="cards")

    def __repr__(self):
        return f"<Card name={self.name} manaCost={self.manaCost} cmc={self.cmc} colors={self.colors} colorIdentity={self.colorIdentity} types={self.types} rarity={self.rarity} setName={self.setName} text={self.text} artist={self.artist} imageUrl={self.imageurl}"

class CardHandler(db.Model):
    """Handles the cards between decks."""

    __tablename__ = 'cardhandler'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_name = db.Column(db.String, db.ForeignKey('card.name'), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable=False)

    def __repr__(self):
        return f"<CardHandler name={self.card_name} deck_id={self.deck_id}>"

class Deck(db.Model):
    """Deck List."""

    __tablename__ = 'deck'

    deck_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_name = db.Column(db.String)
    username = db.Column(db.String, db.ForeignKey('user.username'), nullable=False)

    def __repr__(self):
        return f"<Deck deck_id={self.deck_id} deck_name={self.deck_name}>"


def connect_to_db(flask_app, db_uri="postgresql:///cards", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)