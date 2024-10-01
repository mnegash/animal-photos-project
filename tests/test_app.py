import pytest
from app import app, db, AnimalPicture

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_save_pictures(client):
    print("inside save pictures:  ")
    response = client.post('/save_pictures', json={
        'animal_type': 'cat',
        'num_pictures': 1
    })
    assert response.status_code == 201
    assert b'Successfully saved 1 pictures of cat' in response.data

def test_get_last_picture(client):
    client.post('/save_pictures', json={
        'animal_type': 'dog',
        'num_pictures': 1
    })
    response = client.get('/last_picture/dog')
    assert response.status_code == 200

