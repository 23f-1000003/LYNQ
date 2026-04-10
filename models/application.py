from models import db
from datetime import datetime

class Application(db.Model):
    __tablename__ = 'applications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    resume_filename = db.Column(db.String(255))
    cover_letter = db.Column(db.Text)
    status = db.Column(db.String(50), default='pending')
    applied_at = db.Column(db.DateTime, default=datetime.now)
    
    # ✅ Use unique backref names
    user = db.relationship('User', backref='user_applications', foreign_keys=[user_id])
    job = db.relationship('Job', backref='job_applications', foreign_keys=[job_id])
    
    def __repr__(self):
        return f'<Application {self.id}>'