from fastapi import FastAPI
import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from typing import Annotated


app = FastAPI()

# SessionDep = Annotated[AsyncSession, Depends(get_session)]

# @app.get("/", summary="Начало проекта")
# def root():
#     return "hello world"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)