from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return "444"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
