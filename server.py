from flask import Flask, render_template,request, flash, session, redirect, jsonify

from model import connect_to_db, db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'please'
app.jinja_env.undefined = StrictUndefined




@app.route('/')
def homepage():
    """Landing Page"""


    return render_template('homepage.html')

@app.route('/users')
def register():

    return render_template('register.html')
    
@app.route('/users', methods=['POST'])
def create_user():
    """Create new login"""

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)

    if user:
        flash("Account with that username already exists.")
    else:
        user = crud.create_user(username, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account creation succesful.")

    return redirect('/')

@app.route('/login', methods=["POST"])
def login_authentication():
    """Verify username and email"""
    username = request.form.get("username")
    password = request.form.get("password")
    print(password)

    user = crud.get_user_by_username(username)
    if user:
        if user.password == password:
            session['username'] = username
            return redirect('/usersPage')
        else:
            flash("Incorrect password")
            return redirect('/')
    else:
        flash("Account doesn't exist")
        return redirect('/')

    
@app.route('/usersPage')
def user_page():
    """Display deck/create deck"""
   
    username = session['username']
    user = crud.get_user_by_username(username)
    user_decks = user.decks
    

    return render_template('user_page.html', user_decks=user_decks)


@app.route('/create_deck', methods=['POST'])
def create_deck():
    deck_name = request.form.get("deckName")

    username = session['username']

    deck = crud.create_deck(deck_name,username)
    db.session.add(deck)
    db.session.commit()
    flash("Deck creation succesful!")
    return redirect('/usersPage')

@app.route('/cards')
def view_cards():
    
    cards = crud.create_card_list()

    return render_template('card_list.html', cards=cards)

@app.route('/all_posts')
def json_posts():
    posts_json = []
    posts = crud.create_post_list()

    for post in posts:
        posts_json.append(post.get_json())
    
    return jsonify(posts_json)


@app.route('/posts', methods=['POST'])
def create_post():
    username = session['username']
    post_title = request.form.get('post_title')
    post_text= request.form.get('post_text')
    owned_card = request.form.get('owned_card_name')
    trade_card = request.form.get('trade_card_name')

    owned_card_id = crud.get_card_by_name(owned_card).id
    trade_card_id = crud.get_card_by_name(trade_card).id

    post = crud.create_post(username,post_title,post_text, owned_card_id, trade_card_id)


    db.session.add(post)
    db.session.commit()
    flash("Trade Post creation succesful!")
    return redirect('/usersPage')


@app.route('/trade_accepted', methods=['POST'])
def accepted_trade():

    owned_card_name = request.form.get('owned_card')
    trade_card_name = request.form.get('trade_card')
    owned_card = crud.get_card_by_name(owned_card_name)
    trade_card = crud.get_card_by_name(trade_card_name)
    deck = owned_card.decks[0]
    trade = crud.trade_cards(deck, owned_card, trade_card)
    db.session.add(trade)
    db.session.commit()
    flash("Trade Succesful!")
    return redirect('/usersPage')


@app.route('/all_cards')
def json_cards():
    cards_json = []
    cards = crud.create_card_list()
    
    for card in cards:
        cards_json.append(card.get_json())

    return jsonify(cards = cards_json)

@app.route('/cards/<id>')
def show_card(id):
   
    card = crud.get_card_by_id(id)
    username = session['username']
    user = crud.get_user_by_username(username)
    decks = user.decks
    
    return render_template('card_details.html', card=card, decks=decks)

@app.route('/add_to_deck/<id>', methods=['post'])
def add_cards(id):

    deck_name = request.form.get("Deck")

    add = crud.add_card_to_deck(id,deck_name)
    db.session.add(add)
    db.session.commit()
    flash(f"Card added to {deck_name}")
    return redirect(f"/cards/{id}")

@app.route('/remove_card', methods=['POST'])
def remove_card_from_deck():

    id = request.form.get("card_to_remove")
    deck_name = request.form.get("deck_to_remove_from")
    
    remove = crud.remove_card_from_deck(id,deck_name)
    db.session.add(remove)
    db.session.commit()
    flash(f"Card removed from {deck_name}")
    return redirect('/usersPage')


@app.route('/deck', methods=['POST'])
def show_deck_contents():
    deck_id = request.form.get("Deck")
    print(deck_id)
    deck = crud.get_deck(deck_id)
    print(deck)
    cards = deck.cards
    return render_template("deck_details.html", deck=deck, cards=cards)

@app.route('/map')
def store_locator():
    return render_template('map.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)