import json

def test_create_user(client):
    data = {"username":"irina", "email":"dfdfd@test.com", "password":"gfdg"}
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "dfdfd@test.com"
    assert response.json()["is_active"] == True