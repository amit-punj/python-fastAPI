from fastapi import FastAPI
from routers.routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}



