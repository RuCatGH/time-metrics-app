import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_v1 import app
import pytest

def test_metrics_route():
    with app.test_client() as client:
        # Сначала сделаем несколько запросов к /time, чтобы увеличить счётчик
        for _ in range(5):
            client.get("/time")

        # Теперь проверим /metrics
        response = client.get("/metrics")
        assert response.status_code == 200

        data = response.get_json()
        assert "count" in data, "Отсутствует ключ 'count' в ответе"
        assert isinstance(data["count"], int), "Значение 'count' должно быть числом"
        assert data["count"] >= 5, "Счётчик должен быть как минимум 5 после 5 запросов"
