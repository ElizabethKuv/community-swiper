from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Community Swiper")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@ app.post('/auth', response_model=schemas.User)
def auth(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_telegram_id(db, user.telegram_id)
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=403, detail="Access denied")


@ app.get('/profiles/random', response_model=schemas.User)
def random_profile(user_id: int, db: Session = Depends(get_db)):
    profile = crud.get_random_profile(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="No profiles available")
    return profile


@ app.post('/swipe')
def swipe(user_id: int, swipe: schemas.SwipeCreate, db: Session = Depends(get_db)):
    return crud.create_swipe(db, user_id, swipe)


@ app.get('/matches', response_model=list[schemas.User])
def matches(user_id: int, db: Session = Depends(get_db)):
    return crud.get_matches(db, user_id)
