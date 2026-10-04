def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_create_and_get_user(client):
    payload = {"name": "Aman", "email": "aman@test.com"}

    res = client.post("/users", json=payload)
    assert res.status_code == 201

    res2 = client.get("/users/aman@test.com")
    data = res2.get_json()
    assert data["name"] == "Aman"
    assert data["email"] == "aman@test.com"


def test_user_not_found(client):
    res = client.get("/users/unknown@test.com")
    assert res.status_code == 404
