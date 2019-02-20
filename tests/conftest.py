import pytest
from app import create_app

@pytest.fixture(scope="session")
def app():
    app = create_app('testing')
    ctx = app.app_context()

    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
