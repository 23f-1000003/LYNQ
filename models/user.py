from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import time
from models import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    usertag = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.Text)
    age = db.Column(db.Integer)
    company_name = db.Column(db.String(120))
    cgpa = db.Column(db.Float)
    is_admin = db.Column(db.Boolean, default=False)
    profile_picture = db.Column(db.String(255), default='default_profile.png')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    # ✅ NO relationships defined here - avoid conflicts
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_profile_picture(self):
        """Get profile picture URL with cache busting"""
        if self.profile_picture and self.profile_picture != 'default_profile.png':
            cache_bust = int(time.time())
            return f'/static/uploads/profiles/{self.profile_picture}?t={cache_bust}'
        return f'https://ui-avatars.com/api/?name={self.full_name.replace(" ", "+")}&background=random'
    
    def __repr__(self):
        return f'<User {self.email}>'