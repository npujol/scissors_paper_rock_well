from fastapi.testclient import TestClient
from scissors_paper_rock_well.api import app
from scissors_paper_rock_well.models import Throw, Result

VALID_THROWS = [t.value for t in Throw]
VALID_RESULTS = [r.value for r in Result]

client = TestClient(app)

# Check if the endpoint get a correct answer for a valid input
def test_create_play_with_correct_input():
    response = client.post(
        "/play/",
        json={"throw": "scissors"},
    )
    assert response.status_code == 200
    response_json = response.json()
    assert (
        response_json["computer_throw"] in VALID_THROWS
        and response_json["result"] in VALID_RESULTS
    )


# Check if the endpoint throw an error for an invalid input
def test_create_play_without_correct_input():
    response = client.post(
        "/play/",
        json={"throw": "other"},
    )
    assert response.status_code == 422
