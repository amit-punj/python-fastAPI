from fastapi import FastAPI
from routers.routes import router
from middleware.ageMiddleware import check_age_middleware

app = FastAPI()
app.middleware("http")(check_age_middleware)
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}



