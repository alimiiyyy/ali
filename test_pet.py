import requests

from const import URL


def test_pet_create(create_pet, pet):
    response = create_pet(pet=pet)
    assert response.status_code == 200

def test_pet_get(create_pet, pet):
    create_pet(pet=pet)
    response = requests.get(f"{URL}/pet/{pet.id}")
    assert response.status_code == 200

def test_pet_delete(create_pet, pet):
    create_pet(pet=pet, delete_after=False)

    response = requests.delete(f"{URL}/pet/{pet.id}")

    assert response.status_code == 200, response.status_code

def test_pet_update(create_pet, pet):
    create_pet(pet=pet)

    update_data = pet.model_copy()
    update_data.name = "Sonya"

    response = requests.put(f"{URL}/pet", json=update_data.model_dump())

    assert response.status_code == 200, response.status_code
    updated_pet = response.json()
    assert updated_pet["name"] == "Sonya"