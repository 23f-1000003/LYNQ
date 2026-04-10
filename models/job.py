from models import db
from datetime import datetime

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location = db.Column(db.String(255))
    salary_min = db.Column(db.Float)
    salary_max = db.Column(db.Float)
    job_type = db.Column(db.String(50))
    posted_at = db.Column(db.DateTime, default=datetime.now)
    deadline = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    
    # ✅ Use back_populates - NOT backref
    company = db.relationship('User', back_populates='company_jobs', foreign_keys=[company_id])
    job_applications = db.relationship('Application', back_populates='job', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Job {self.title}>'