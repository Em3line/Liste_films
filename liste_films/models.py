from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    deja_vu = db.Column(db.Boolean(), nullable=False)
    annee = db.Column(db.Integer(), nullable=True)
    realisateur = db.Column(db.String(200), nullable=True)
    acteur = db.Column(db.String(200), nullable=True)
    actrice = db.Column(db.String(200), nullable=True)
    note = db.Column(db.Integer(), nullable=True)
    remarque = db.Column(db.String(200), nullable=True)


    def __init__(self, titre, deja_vu = False, annee = None, realisateur = None,
                     acteur = None, actrice = None, note = None, remarque = None):
        self.titre = titre
        self.deja_vu = deja_vu
        self.annee = annee
        self.realisateur = realisateur
        self.acteur = acteur
        self.actrice = actrice
        self.note = note
        self.remarque = remarque


db.create_all()
