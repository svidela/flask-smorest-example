import json
from app import create_app

def test_create_multiple_apps(app):
    response = app.test_client().get('/api/cars/1')
    assert response.status_code == 200
    
    body = response.get_data(as_text=True)
    rv = json.loads(body)
    rv['name'] == 'foo'

    prod_app = create_app('production')

    response = prod_app.test_client().get('/api/cars/1')
    assert response.status_code == 200

    body = response.get_data(as_text=True)
    rv = json.loads(body)
    rv['name'] == 'bar'
