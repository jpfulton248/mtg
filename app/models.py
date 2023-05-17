from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, DECIMAL
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(Integer, primary_key=True, autoincrement=True)
    username = db.Column(String(50), unique=True, nullable=False)
    password_hash = db.Column(String(255), nullable=False)
    email = db.Column(String(100), unique=True, nullable=False)
    reset_token = db.Column(String(100))
    reset_token_expiration = db.Column(DateTime)


class Collection(db.Model):
    __tablename__ = 'collections'

    collection_id = db.Column(Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(Integer, ForeignKey('users.user_id'))
    collection_name = db.Column(String(100), nullable=False)
    creation_date = db.Column(Date, nullable=False)

    user = relationship('User')


class Set(db.Model):
    __tablename__ = 'sets'

    set_id = db.Column(Integer, primary_key=True, autoincrement=True)
    set_name = db.Column(String(100), nullable=False)
    release_date = db.Column(Date)
    expansion_symbol = db.Column(String(10))
    set_image_url = db.Column(String(255))


class Card(db.Model):
    __tablename__ = 'cards'

    card_id = db.Column(Integer, primary_key=True, autoincrement=True)
    set_id = db.Column(Integer, ForeignKey('sets.set_id'))
    card_name = db.Column(String(100), nullable=False)
    multiverse_id = db.Column(Integer)
    rarity = db.Column(String(20))
    color = db.Column(String(20))
    card_type = db.Column(String(50))
    card_image_url = db.Column(String(255))

    card_set = relationship('Set')


class CollectionCard(db.Model):
    __tablename__ = 'collection_cards'

    collection_card_id = db.Column(Integer, primary_key=True, autoincrement=True)
    collection_id = db.Column(Integer, ForeignKey('collections.collection_id'))
    card_id = db.Column(Integer, ForeignKey('cards.card_id'))
    condition = db.Column(String(50))
    price_paid = db.Column(DECIMAL(10, 2))
    purchase_date = db.Column(Date)
    current_value = db.Column(DECIMAL(10, 2))
    foil_status = db.Column(String(10))
    edition = db.Column(String(50))
    language = db.Column(String(50))

    collection = relationship('Collection')
    card = relationship('Card')
