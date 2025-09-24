from fastapi import FastAPI
from core import db_helper
import uvicorn


app = FastAPI()


@app.get("/")
def index():

    return "444"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
