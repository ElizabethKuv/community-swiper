from sqlalchemy.orm import Session
from . import models, schemas


def get_user_by_telegram_id(db: Session, telegram_id: int):
    return db.query(models.User).filter(models.User.telegram_id == telegram_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_random_profile(db: Session, exclude_id: int):
    return (
        db.query(models.User)
        .filter(models.User.id != exclude_id)
        .order_by(models.User.id)
        .first()
    )


def create_swipe(db: Session, from_user_id: int, swipe: schemas.SwipeCreate):
    db_swipe = models.Swipe(from_user_id=from_user_id, **swipe.dict())
    db.add(db_swipe)
    db.commit()
    db.refresh(db_swipe)
    return db_swipe


def get_matches(db: Session, user_id: int):
    return (
        db.query(models.User)
        .join(models.Swipe, models.Swipe.to_user_id == models.User.id)
        .filter(models.Swipe.from_user_id == user_id, models.Swipe.is_like == True)
        .join(
            models.Swipe,
            (models.Swipe.from_user_id == models.User.id) & (models.Swipe.to_user_id == user_id) & (models.Swipe.is_like == True),
            isouter=False,
        )
        .all()
    )
