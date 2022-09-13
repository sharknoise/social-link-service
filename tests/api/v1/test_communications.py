def test_send_communication(client):
    response = client.post("/api/v1/communications/send", json={"user_ids": [1, 2]})
    assert response.status_code == 200, f"{response.status_code=} {response.text=}"
    assert response.json()["communication_id"]


def test_get_social_graph(client):
    response = client.get("/api/v1/communications/")
    assert response.status_code == 200, f"{response.status_code=} {response.text=}"
    assert "average_communication_count" in response.json()["statistics"]
