from fastapi import FastAPI
import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from os import getenv, path
from dotenv import load_dotenv
from typing import Annotated

load_dotenv('../.env')

DB_NAME = getenv('')
DB_USER = getenv('')
DB_PASSWORD = getenv('')
DB_HOST = getenv('')

HASH_SALT = getenv('')

VARCHAR_MIN_LENGTH = getenv('')
VARCHAR_MAX_LENGTH = getenv('')
VARCHAR_MAX_TEXT_LENGTH = 255

app = FastAPI()

# SessionDep = Annotated[AsyncSession, Depends(get_session)]

# @app.get("/", summary="Начало проекта")
# def root():
#     return "hello world"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)