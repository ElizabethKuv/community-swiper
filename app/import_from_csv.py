import csv
from sqlalchemy.orm import Session
from .db import SessionLocal, engine
from . import models

models.Base.metadata.create_all(bind=engine)

def import_csv(path: str):
    db: Session = SessionLocal()
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = models.User(
                telegram_id=int(row['telegram_id']),
                name=row['name'],
                username=row.get('username'),
                city=row.get('city'),
                sphere=row.get('sphere'),
                description=row.get('description'),
                category=row.get('category'),
            )
            db.add(user)
        db.commit()
    db.close()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    args = parser.parse_args()
    import_csv(args.csv_path)
