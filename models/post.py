from datetime import datetime
from models import db

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    likes_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships - NO BACKREF to avoid conflicts
    author = db.relationship('User', foreign_keys=[author_id], backref='posts')
    comments = db.relationship('Comment', foreign_keys='Comment.post_id', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Post {self.id}>'