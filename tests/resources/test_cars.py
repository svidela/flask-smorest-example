
def test_get_cars(client):
    response = client.get('/api/cars/')

    assert response.status_code == 200


def test_post_cars(client):
    response = client.post('/api/cars/')

    assert response.status_code == 201



def test_get_cars_by_id(client):
    response = client.get('/api/cars/10')

    assert response.status_code == 200


def test_put_cars_by_id(client):
    response = client.put('/api/cars/10')

    assert response.status_code == 200


def test_delete_cars_by_id(client):
    response = client.delete('/api/cars/10')

    assert response.status_code == 404
