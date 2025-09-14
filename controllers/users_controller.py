from google import genai
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
    users = ['amit', 'sumit', 'rahul']
    return {"users": users }

def UserbyID(user_id: int):
    print('inside get user by id controller')
    if user_id == 1:
        user = {'id': 1, 'name': 'amit', 'age': 24}
        return {"user": user }
    else:
        return "there is no user"
    
    return {"user": user }  


def create_user(request, name: str, age: int):
    print('inside create user controller')
    print('user', request.json())
    return {"message": "User created successfully", "name": name, "age": age}

def update_user():
    print('inside update user controller')
    return {"message": "User updated successfully"}

def delete_user():
    print('inside delete user controller')
    return {"message": "User deleted successfully"}