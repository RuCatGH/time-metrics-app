import requests

def test_time_route():
    response = requests.get("http://localhost:5000/time")
    assert response.status_code == 200
    assert response.json()["time"] != 0
