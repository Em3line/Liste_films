from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    annee = db.Column(db.Integer(), nullable=False)

    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

db.create_all()
