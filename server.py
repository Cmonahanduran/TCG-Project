from flask import Flask, render_template,request, flash, session, redirect

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
    

    user = crud.get_user_by_username(username)
    if user:
        if user.password == password:
            session['username'] = username
            return render_template('user_page.html')
        else:
            flash("Incorrect password")
            return redirect('/')
    else:
        flash("Account doesn't exist")
        return redirect('/')

    
@app.route('/usersPage', methods=['POST'])
def user_page():
    """Display deck/create deck"""
   
    deck_name = request.form.get("deckName")

    username = session['username']

    deck = crud.create_deck(deck_name,username)
    db.session.add(deck)
    db.session.commit()
    flash("Deck creation succesful!")
    user = crud.get_user_by_username(username)
    user_decks = user.decks


    return render_template('user_page.html', user_decks=user_decks)




@app.route('/cards')
def view_cards():

    cards = crud.create_card_list()

    return render_template('card_list.html', cards=cards)

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

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)