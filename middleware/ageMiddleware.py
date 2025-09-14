from fastapi import Request
from fastapi.responses import JSONResponse
async def check_age_middleware (request: Request, call_next):
    age = request.headers.get("x-age")

    if age is None:
        return JSONResponse(content = {"error": "age header is required"}, status_code=400)
    try:
        age =int(age)
    except ValueError:
        return JSONResponse(content = {"erroe": "age must be a number"}, status_code=400)
    if age < 18 :
        return JSONResponse(content= {"error": "age must be greater than 18"},status_code=400)
    
    response = await call_next(request)
    return response


