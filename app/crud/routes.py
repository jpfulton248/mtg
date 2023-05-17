from flask import render_template, redirect, url_for, request, Blueprint
from models import Collection, CollectionCard

crud = Blueprint('crud', __name__, template_folder='templates', static_folder='../static')

@crud.route('/')
def index():
    # Display a list of collections
    collections = Collection.query.all()
    return render_template('index.html', collections=collections)

@crud.route('/collection/<int:collection_id>')
def view_collection(collection_id):
    # Display the details of a specific collection
    collection = Collection.query.get(collection_id)
    if not collection:
        # Handle the case where the collection is not found
        return redirect(url_for('crud.index'))
    return render_template('collection.html', collection=collection)

@crud.route('/collection/<int:collection_id>/add_card', methods=['GET', 'POST'])
def add_card(collection_id):
    # Add a card to a collection
    if request.method == 'POST':
        # Process form data and create a new CollectionCard entry
        # Redirect to the collection view
        return redirect(url_for('crud.view_collection', collection_id=collection_id))
    else:
        # Display the form for adding a card
        return render_template('add_card.html', collection_id=collection_id)

@crud.route('/collection/<int:collection_id>/edit_card/<int:card_id>', methods=['GET', 'POST'])
def edit_card(collection_id, card_id):
    # Edit details of a specific card in a collection
    collection_card = CollectionCard.query.get(card_id)
    if not collection_card:
        # Handle the case where the collection card is not found
        return redirect(url_for('crud.view_collection', collection_id=collection_id))
    if request.method == 'POST':
        # Process form data and update the CollectionCard entry
        # Redirect to the collection view
        return redirect(url_for('crud.view_collection', collection_id=collection_id))
    else:
        # Display the form for editing the card details
        return render_template('edit_card.html', collection_card=collection_card)

@crud.route('/collection/<int:collection_id>/delete_card/<int:card_id>', methods=['POST'])
def delete_card(collection_id, card_id):
    # Delete a specific card from a collection
    collection_card = CollectionCard.query.get(card_id)
    if collection_card:
        # Delete the collection_card from the database
        # Redirect to the collection view
        return redirect(url_for('crud.view_collection', collection_id=collection_id))
    else:
        # Handle the case where the collection card is not found
        return redirect(url_for('crud.view_collection', collection_id=collection_id))