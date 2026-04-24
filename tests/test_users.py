from fastapi.testclient import TestClient
from app.main import app
from app import schemas

#request object 

client = TestClient(app)

def test_root() : 
    res = client.get("/") 
    print(res.json().get('message'))
    assert res.json().get('message') == 'rudra here'
    assert res.status_code == 200

def test_create_user() :
    res = client.post("/users/", json = {"email" : "hello123@gmail.com", "password" : "pass123"})

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201