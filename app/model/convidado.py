from app import db

class Convidado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200))
    telefone = db.Column(db.Integer)