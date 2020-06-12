import json


def test_create_note_invalid_json(test_app):
    response = test_app.post("/reservations", data=json.dumps({"title": "something"}))
    assert response.status_code == 422
