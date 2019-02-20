import json


def test_get_spec(client):
    response = client.get('/openapi/openapi.json')

    assert response.status_code == 200
    spec = json.loads(response.data)

    assert len(spec['components']['schemas']) == 3
