from app import app

def test_time_route():
    with app.test_client() as client:
        response = client.get("/time")
        assert response.status_code == 200
        data = response.get_json()
        assert "time" in data
        assert data["time"] > 0
