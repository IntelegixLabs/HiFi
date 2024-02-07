import mongomock
import pytest
from fastapi.testclient import TestClient

from config.settings import create_app


@pytest.fixture
def client():
    app = create_app("hifi_test")
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def mock_mongodb_connection(client):
    return mongomock.MongoClient()


@pytest.fixture
def mock_db(client, mock_mongodb_connection):
    return mock_mongodb_connection.db
