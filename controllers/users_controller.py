from google import genai
import json
from pathlib import Path

DATA_FILE = Path("models/users.json")
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists

# initialize file if it doesn't exist
if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")

def users():
    clint = genai.Client(api_key="AIzaSyCsvNedRp4iXIXxNJbTM7OLrIFt9hHC51U")
    print('inside get users controller')
     # Example of generating content using Gemini
    response = clint.models.generate_content(
        model="gemini-1.5-flash",
        contents="difference bw state and props in react",
    )
    print('response.candidates', response)
     # Gemini returns an object; extract text from it
    if response.candidates:
        text = response.candidates[0].content.parts[0].text
        return {"users": text.split(",")}
    
    # Fallback if no response
    return {"users": ["amit", "sumit", "rahul"]}
    
    users = ['amit', 'sumit', 'rahul']
    return {"users": users }

def get_users():
    try:
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []  # in case file is corrupted

    return {"message": "Users fetched successfully", "users": users }

def UserbyID(user_id: int):
    try:
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []  # in case file is corrupted

    result = []
    for user in users:
        if user.get("username") == "amit sharma":
            result.append(user)
            break

    return {"message": "User fetched successfully", "user": result }

def create_user(request, user):
    """Insert new user into users.json"""

    # read existing users
    try:
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []  # in case file is corrupted
    print('users', users)
    # append new user
    users.append(user.dict())
    print('users after append', users)

    # save back
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return {"message": "User created successfully", "users": users}

def update_user(username):
    try:
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []  # in case file is corrupted

    updated_user = {}
    for i, user in enumerate(users):
        if user.get("username") == username:
            user["username"] = "anjna sharma"
            user["role"] = "student"
            users[i].update(user)
            updated_user = users[i]
            break
    
    print('users after append', users)

    # save back
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)
    
    print('inside update user controller')
    return {"message": "User updated successfully", "user": updated_user}

def delete_user():
    print('inside delete user controller')
    return {"message": "User deleted successfully"}