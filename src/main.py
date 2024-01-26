from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "first page"}


@app.on_event("startup")
async def startup_event():
    print("application is started")

