from datetime import datetime
from models import db

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships - use viewonly for post to avoid conflicts
    author = db.relationship('User', foreign_keys=[author_id], back_populates='user_comments')
    post = db.relationship('Post', foreign_keys=[post_id], viewonly=True)
    
    def __repr__(self):
        return f'<Comment {self.id}>'