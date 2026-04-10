from models import db
from datetime import datetime
import time
from werkzeug.security import generate_password_hash, check_password_hash

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
    
    # ✅ All use back_populates
    user_posts = db.relationship('Post', back_populates='author', foreign_keys='Post.author_id', cascade='all, delete-orphan')
    user_comments = db.relationship('Comment', back_populates='author', foreign_keys='Comment.author_id', cascade='all, delete-orphan')
    user_post_likes = db.relationship('PostLike', back_populates='user', foreign_keys='PostLike.user_id', cascade='all, delete-orphan')
    user_skills = db.relationship('Skill', back_populates='user', foreign_keys='Skill.user_id', cascade='all, delete-orphan')
    user_applications = db.relationship('Application', back_populates='user', foreign_keys='Application.user_id', cascade='all, delete-orphan')
    company_jobs = db.relationship('Job', back_populates='company', foreign_keys='Job.company_id')
    
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
    
    def get_stats(self):
        """Return a dict of stats for the user's profile page"""
        return {
            'total_posts': len(self.user_posts),
            'total_comments': len(self.user_comments),
            'total_skills': len(self.user_skills),
            'total_applications': len(self.user_applications) if not self.is_admin else 0,
            'total_jobs_posted': len(self.company_jobs) if self.is_admin else 0,
        }
    
    def __repr__(self):
        return f'<User {self.email}>'