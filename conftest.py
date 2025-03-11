import pytest
import requests

from const import URL
from models import Pet

@pytest.fixture(scope="session", name="pet")
def prepare_pet():
    data = {
        "id": 123,
        "name": "kitty",
        "status": "available"
    }
    return Pet(**data)

@pytest.fixture(scope="function")
def create_pet():
    _pet_id = None
    _delete_after = None

    def wrapper(pet: Pet, delete_after: bool = True):
        nonlocal _pet_id, _delete_after
        _delete_after = delete_after

        response = requests.post(f"{URL}/pet", json=pet.model_dump())
        _pet_id = pet.id
        return response

    yield wrapper

    if _pet_id and _delete_after:
        requests.delete(f"{URL}/pet/{_pet_id}")