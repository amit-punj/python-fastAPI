# from fastapi import requests
from database import db
from datetime import datetime, timedelta
from bson import ObjectId
from jose import JWTError, jwt, ExpiredSignatureError
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import utils.helpers as helpers

# Secret key (keep safe, normally from .env)
SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

user_collection = db["users"]

# password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="sign_in")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        print("raw token before cleaning:", token)

        # If token starts with "Bearer ", remove it
        if token.startswith("Bearer "):
            token = token.split(" ")[1]

        # print("token in decode_access_token (cleaned):", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print('payload in decode_access_token', payload)
        return payload
    except ExpiredSignatureError:
        # print("❌ Token has expired")
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError as e:
        # print(f"❌ JWT Error: {e}")
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # print('token in get_current_user function', token)
    payload = decode_access_token(token)
    # print('payload in get_current_user function', payload)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = payload.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="User not found in token")
    return user

def profile(user):
    # print('current_user in route', user)
    return {"message": "Profile get successfully","user":user}

def sign_up(request, user):
    # print('user', user)
    if user_collection.find_one({"username": user.username}):
        return {"error": "Username already exists"}
    
    user_dict = user.dict()
    user_dict['_id'] = ObjectId()
    user_dict["password"] = hash_password(user.password)

    # Insert user into MongoDB
    try:
        user_collection.insert_one(user_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    user_dict = helpers.serialize_doc(user_dict)
    user_dict.pop("password", None) # remove password before returning
    user_dict["token"] = create_access_token({"user": user_dict})

    return {"message": "Sign Up successful","user":user_dict}

def sign_in(request, user):
    # print('username, ', user)
    ExistingUser = user_collection.find_one({"username": user.username})
    if not ExistingUser:
        return {'error': 'User not found'}

    if not verify_password(user.password, ExistingUser["password"]):
        return {"error": "Password is incorrect"}
    
    ExistingUser = helpers.serialize_doc(ExistingUser)
    ExistingUser.pop("password", None) # remove password before returning
    ExistingUser["token"] = create_access_token({"user": ExistingUser})
    print('ExistingUser', ExistingUser)

    return {"message": "User signed in successfully", "user": ExistingUser}  
    

