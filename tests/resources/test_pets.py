
def test_get_pets(client):
    response = client.get('/api/pets/')

    assert response.status_code == 200


def test_post_pets(client):
    response = client.post('/api/pets/')

    assert response.status_code == 201



def test_get_pets_by_id(client):
    response = client.get('/api/pets/10')

    assert response.status_code == 200


def test_put_pets_by_id(client):
    response = client.put('/api/pets/10')

    assert response.status_code == 200


def test_delete_pets_by_id(client):
    response = client.delete('/api/pets/10')

    assert response.status_code == 404
