from datetime import datetime
from app import db


class UploadFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)
    data_uploaded = db.Column(db.DateTime, nullable=False ,default=datetime.utcnow)