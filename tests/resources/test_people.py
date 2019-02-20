
def test_get_people(client):
    response = client.get('/api/people/')

    assert response.status_code == 200
    

def test_post_people(client):
    response = client.post('/api/people/')

    assert response.status_code == 201



def test_get_people_by_id(client):
    response = client.get('/api/people/10')

    assert response.status_code == 200


def test_put_people_by_id(client):
    response = client.put('/api/people/10')

    assert response.status_code == 200


def test_delete_people_by_id(client):
    response = client.delete('/api/people/10')

    assert response.status_code == 404
