def test_ping(client):
    response = client.get("/api/ping")
    assert response.status_code == 200, f"{response.status_code=} {response.text=}"
