from fastapi import FastAPI, status

from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION
    )
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World"}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    return {"healthcheck": "Everything OK!"}
