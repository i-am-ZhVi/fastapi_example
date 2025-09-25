from datetime import datetime
from fastapi import FastAPI
from schemas import UserGet
import uvicorn


app = FastAPI()


@app.get("/")
def index():

    return UserGet(
        **{
            "id": 1,
            "username": "135",
            "avatarfileid": 1,
            "statusmessage": "sda",
            "createdat": datetime.now(),
            "updatedat": datetime.now(),
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
