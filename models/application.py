from models import db
from datetime import datetime

class Application(db.Model):
    __tablename__ = 'applications'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Contact Info
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    linkedin_url = db.Column(db.String(255))
    portfolio_url = db.Column(db.String(255))
    
    # Application Details
    resume_filename = db.Column(db.String(255))
    cover_letter = db.Column(db.Text)
    
    # Status
    status = db.Column(db.String(50), default='pending')
    applied_at = db.Column(db.DateTime, default=datetime.now)
    reviewed_at = db.Column(db.DateTime)
    review_notes = db.Column(db.Text)
    
    # Relationships
    job = db.relationship('Job', foreign_keys=[job_id], backref='job_applications')
    user = db.relationship('User', foreign_keys=[user_id], backref='user_applications')
    
    def to_dict(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'user_id': self.user_id,
            'phone': self.phone,
            'email': self.email,
            'linkedin_url': self.linkedin_url,
            'portfolio_url': self.portfolio_url,
            'resume_filename': self.resume_filename,
            'cover_letter': self.cover_letter,
            'status': self.status,
            'applied_at': self.applied_at.strftime('%Y-%m-%d %H:%M:%S'),
            'reviewed_at': self.reviewed_at.strftime('%Y-%m-%d %H:%M:%S') if self.reviewed_at else None,
            'review_notes': self.review_notes
        }
    
    def __repr__(self):
        return f'<Application {self.job_id}-{self.user_id}>'