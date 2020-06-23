import json

import pytest


@pytest.fixture
def create_reservation(test_app_with_db):
    payload = {
        "restaurant_id": 1,
        "table_id": 1,
        "start": "2021-06-22 20:11:30",
        "end": "2021-06-22 20:11:30",
        "guests": 3,
    }
    response = test_app_with_db.post("/reservations", data=json.dumps(payload))
    assert response.status_code == 201
    return payload, response.json()


def test_create_note_without_mandatory_fields(test_app_with_db):
    response = test_app_with_db.post("/reservations", data=json.dumps({"restaurant_id": 1}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "payload", "table_id"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "start"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "end"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "guests"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_create_reservation(create_reservation):
    payload, response = create_reservation
    assert "id" in response
    assert response["restaurant_id"] == payload["restaurant_id"]
    assert response["guests"] == payload["guests"]


def test_get_reservation(create_reservation, test_app_with_db):
    _, response = create_reservation
    assert "id" in response
    reservation_id = response["id"]
    get_response = test_app_with_db.get(f"/reservations/{reservation_id}")
    assert get_response.status_code == 200
    reservation = get_response.json()
    assert reservation == response
