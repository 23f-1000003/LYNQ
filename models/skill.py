from models import db
from datetime import datetime

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    certification = db.Column(db.String(255))  # Certification name
    verification_link = db.Column(db.String(500))  # Link to certificate or verification
    certificate_file = db.Column(db.String(255))  # Uploaded certificate image
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'certification': self.certification,
            'verification_link': self.verification_link,
            'certificate_file': self.certificate_file,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }
    
    def __repr__(self):
        return f'<Skill {self.name}>'