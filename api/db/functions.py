from .base import engine
from sqlmodel import Session,select
from .models import User

def create_user(name : str):
    with Session(engine) as session:
        user = User(name=name)
        session.add(user)
        try:
            session.commit()
            return user
        except:
            return None

def get_users():
    with Session(engine) as session:
        stmt = select(User)
        user = session.exec(stmt).all()
        return user