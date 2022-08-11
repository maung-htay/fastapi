from app import schemas
from .database import client, session

def test_root(client):
    response = client.get('/')
    # print(response.json())
    assert response.json().get('message') == 'Hello World Docker BindMouth Ok'
    assert response.status_code == 200
    
def test_create_user(client):
    response = client.post("/user/", json={"email": "hello123@gmail.com",
                                           "password": "password123"})
    new_user = schemas.User(**response.json())
    assert response.status_code == 201    
    assert new_user.email == 'hello123@gmail.com'
    
def test_login(client):
   response = client.post("/login", data={"username": "hello123@gmail.com",
                                           "password": "password123"})
   # json -> json
   # form -> data
   assert response.status_code == 200
        

