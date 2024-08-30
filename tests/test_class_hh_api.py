import pytest
from src.class_hh_api import HH


@pytest.fixture
def headhunter_instance() -> HH:
    return HH()


def test_get_response(headhunter_instance: HH) -> None:
    response = headhunter_instance.get_response("python", 5)
    assert response.status_code == 200


def test_get_vacancies(headhunter_instance: HH) -> None:
    vacancies = headhunter_instance.get_vacancies_response("python", 5)
    assert isinstance(vacancies, list)
