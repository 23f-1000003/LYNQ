from models import db
from datetime import datetime

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    certification = db.Column(db.String(200))
    verification_link = db.Column(db.String(500))
    certificate_file = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # ✅ Use backref='user_skills' to avoid conflicts
    user = db.relationship('User', backref='user_skills', foreign_keys=[user_id])
    
    def __repr__(self):
        return f'<Skill {self.name}>'