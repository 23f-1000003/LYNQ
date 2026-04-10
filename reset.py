from models import db
from app import create_app

app = create_app()

with app.app_context():
    # Drop all tables
    db.drop_all()
    print("✅ Dropped all tables")
    
    # Create all tables from scratch
    db.create_all()
    print("✅ Created all tables")
    
    # Create admin user
    from models.user import User
    
    admin = User(
        email='admin@lynqplat.com',
        full_name='Admin User',
        usertag='admin',
        is_admin=True,
        company_name='LYNQ',
        age=30
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    
    print("✅ Admin user created!")

