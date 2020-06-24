import json

from app.api import crud


def test_create_reservation_unit(test_app, monkeypatch):
    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    request_payload = {
        "restaurant_id": 1,
        "table_id": 1,
        "start": "2021-06-22 20:11:30",
        "end": "2021-06-22 20:11:30",
        "guests": 3,
    }
    response_payload = {
        "restaurant_id": 1,
        "table_id": 1,
        "start": "2021-06-22T20:11:30",
        "end": "2021-06-22T20:11:30",
        "guests": 3,
        "id": 1,
    }
    response = test_app.post("/reservations", data=json.dumps(request_payload))
    assert response.status_code == 201
    assert response.json() == response_payload
