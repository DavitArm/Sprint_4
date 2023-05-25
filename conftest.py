import pytest
from selenium import webdriver
from faker import Faker
import random as rd


# добавлен фикстура browser
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def name():
    faker = Faker('ru_RU')
    first_name = faker.first_name()
    return first_name


@pytest.fixture()
def last_name():
    faker = Faker('ru_RU')
    last_name = faker.last_name()
    return last_name


@pytest.fixture()
def address():
    faker = Faker('ru_RU')
    address = faker.street_name()
    return address


@pytest.fixture()
def phone():
    country_code = '+7'
    digits = rd.randint(1000000000,9999999999)
    tel_number = country_code + str(digits)
    return tel_number
