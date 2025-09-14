from fastapi import FastAPI, Request
from routers.routes import router
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from middleware.ageMiddleware import check_age_middleware

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    messages = []
    for error in errors:
        loc = error.get("loc", [])
        field = loc[-1] if loc else "field"
        msg = error.get("msg", "Invalid input")
        messages.append(f"Error in '{field}': {msg}")
    return JSONResponse(
        status_code=422,
        content={"errors": messages}  # return list of friendly messages
    )



app.middleware("http")(check_age_middleware)
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}



