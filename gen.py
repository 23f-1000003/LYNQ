from app import create_app
from models import db
from sqlalchemy import text

app = create_app()

with app.app_context():
    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute('ALTER TABLE users ADD COLUMN age INTEGER')
        print("✅ Added age column")
    except Exception as e:
        print(f"⚠️ age: {e}")

    try:
        cursor.execute('ALTER TABLE users ADD COLUMN company_name VARCHAR(200)')
        print("✅ Added company_name column")
    except Exception as e:
        print(f"⚠️ company_name: {e}")

    try:
        cursor.execute('ALTER TABLE users ADD COLUMN cgpa FLOAT')
        print("✅ Added cgpa column")
    except Exception as e:
        print(f"⚠️ cgpa: {e}")
    
    connection.commit()
    cursor.close()
    connection.close()

print("\n✅ Migration complete!")