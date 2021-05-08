from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from knowing.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(254), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(30))
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(254), unique=True, index=True)
    confirmed = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

class KnowledgeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(254), unique=True, index=True)
    content = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)





