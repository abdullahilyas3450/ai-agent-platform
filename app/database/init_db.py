from app.database.connection import engine
from app.database.models.base import Base

# Import models so they are registered with Base.metadata
from app.database.models.users import User
from app.database.models.agents import Agent


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")