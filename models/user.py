from datetime import datetime
from models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    usertag = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    profile_picture = db.Column(db.String(500))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # Relationships
    user_comments = db.relationship('Comment', foreign_keys='Comment.author_id', lazy=True, cascade='all, delete-orphan')
    applications = db.relationship('Application', foreign_keys='Application.user_id', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User {self.usertag}>'
    
    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture
        return '/static/default-avatar.png'
    
    def get_stats(self):
        from models.post import Post
        from models.comment import Comment
        posts = Post.query.filter_by(author_id=self.id).count()
        comments = Comment.query.filter_by(author_id=self.id).count()
        return {
            'total_posts': posts,
            'total_comments': comments,
            'total_applications': len(self.applications)
        }