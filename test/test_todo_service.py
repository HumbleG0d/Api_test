from app.services.todo_service import TodoService
from app.api.api_client import APIClient

def test_get_todo_details(mocker):
    mock_api_client = mocker.Mock(spec = APIClient)
    mock_api_client.get_todo.return_value = {
        "id" : 1,
        "title" : "Test Todo",
        "completed" : False
    }

    service = TodoService(mock_api_client)
    result = service.get_todo_details(1)
    assert result["title"] == "Test Todo"
    mock_api_client.get_todo.assert_called_once_with(1)


class FakeApiClient:
    def get_todo(self , todo_id):
        return {
            "id" : todo_id,
            "title" : "fake todo",
            "completed" : False
        }

def test_get_todo_details_with_fake_client():
    fake_api = FakeApiClient()
    service = TodoService(fake_api)

    result = service.get_todo_details(1)

    assert result["title"] == "Fake Todo"


def test_add_todo_calls_create_todo(mocker):
    mock_api_client = mocker.Mock(spec = APIClient)
    mock_api_client.create_todo.return_value = {
        "id": 101,
        "title": "New Todo",
        "completed": False
    }

    service = TodoService(mock_api_client)

    result = service.add_todo("New Todo")

    assert result['title'] == "New Todo"