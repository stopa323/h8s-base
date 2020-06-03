import pytest

from mongoengine import connect, disconnect

from base.db import pancake as db
from base.provider import pancake as provider


@pytest.fixture(scope="function")
def mongo():
    db = connect("testdb", host="mongomock://localhost")
    yield db
    db.drop_database("testdb")
    db.close()
    disconnect()


def test_is_there_something_to_eat(mongo):
    db.PancakeTypeObj(name="TastyOunce").save()

    my_lunch = provider.list_pancakes()

    assert 1 == len(my_lunch)
    assert "TastyOunce" == my_lunch[0].name
    assert my_lunch[0].description is None

    print("Umumum...")


def test_pancake_lust(mongo):
    my_lunch = provider.list_pancakes()

    assert 0 == len(my_lunch)
