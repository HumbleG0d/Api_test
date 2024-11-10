import requests
import requests_mock
from app.api.api_client import APIClient


# Mock
def test_get_todo_sucessful_response():
    with requests_mock.Mocker() as m:
        m.get(
            "https://example.com/todos/1",
            json={"id": 1, "title": "Test todo", "completed": False},
            status_code=200,
        )
        client = APIClient("https://example.com")
        result = client.get_todo(1)
        assert result == {"id": 1, "title": "Test todo", "completed": False}


# Stup
class FakeSesseion:
    def get(self, url):
        class Response:
            status_code = 200

            def json(self):
                return {"id": 1, "title": "Test todo", "completed": False}

            def raise_for_status(self):
                pass

        return Response()


# Uso de Stup
def test_get_todo_fake_session():
    # Arrange
    fake_session = FakeSesseion()

    # Act
    client = APIClient("https://example.com", fake_session)
    result = client.get_todo(1)

    # Assert
    assert result["title"] == "Test todo"


# Spy
def test_get_todo_calls_get_method(mocker):
    mock_session = mocker.Mock()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "title": "Test Todo",
        "completed": False,
    }
    mock_session.get.return_value = mock_response

    client = APIClient("https://example.com", session=mock_session)
    todo = client.get_todo(1)

    mock_session.get.assert_called_once_with("https://example.com/todos/1")
    assert todo["title"] == "Test Todo"


# Fake : Simulamos una respuesta falsa
class FakeRequestSession(requests.Session):
    def get(self, url, **kwargs):
        response = requests.Response()
        response.status_code = 200
        response._content = b'{"id": 1, "title": "Test Todo", "completed": false}'
        return response


def test_get_todo_with_fake_requests_session():
    # Arrange
    fake_request = FakeRequestSession()
    cliente = APIClient("https://example.com", fake_request)
    # Act
    result = cliente.get_todo(1)
    # Assert
    assert result["title"] == "Test Todo"


# Prueba de integración: Realizamos una llamada real a la API REST
def test_get_todo_integration():
    client = APIClient("https://jsonplaceholder.typicode.com")
    todo = client.get_todo(1)
    assert todo["id"] == 1
