from models import db
from datetime import datetime

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(200), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location = db.Column(db.String(200))
    salary_range = db.Column(db.String(200))  # ✅ Added - allows currency symbols
    job_type = db.Column(db.String(50))
    requirements = db.Column(db.Text)
    status = db.Column(db.String(50), default='active')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships
    company_obj = db.relationship('User', foreign_keys=[company_id])
    applications = db.relationship('Application', backref='job', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Job {self.title}>'