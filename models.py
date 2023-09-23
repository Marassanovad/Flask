from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  surname = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(20), nullable=False, unique=True)
  password = db.Column(db.String(20), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return f'Book("{self.name}", {self.surname}, {self.email})'
