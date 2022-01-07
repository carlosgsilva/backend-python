from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing input
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing outpu
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(digits=2), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing input
    assert user_repo.insert_user_params == {}

    # Testing outpu
    assert response["Success"] is False
    assert response["Data"] is None
