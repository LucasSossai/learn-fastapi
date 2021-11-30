import random as rng
import string

from sqlalchemy.orm import Session

from db.repository.users import create_new_user
from schemas.users import UserCreate


def random_lower_string() -> str:
    return "".join(rng.choices(string.ascii_lowercase, k=32))


def create_random_owner(db: Session):
    username = random_lower_string()
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    user_schema = UserCreate(username=username, email=email, password=password)
    return create_new_user(user=user_schema, db=db)
