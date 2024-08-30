import os
from typing import MutableMapping
from unittest.mock import MagicMock

import pytest
from src.class_json import JSONSaver
from src.class_vacancy import Vacancy

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data", "test_vacancies.json")


@pytest.fixture
def json_saver() -> JSONSaver:

    return JSONSaver(filename=file_path)


def test_write_data(json_saver: JSONSaver) -> None:
    vacancies = [
        {
            "name": "Software Engineer",
            "salary": {"from": 10000, "to": 100000, "currency": "RUR"},
            "alternate_url": "https://vacancy.ru/103285189",
            "employer": {"name": "Example Inc"},
            "snippet": {"requirement": "Python, Java, C++"},
        },
        {
            "name": "Data Scientist",
            "salary": {"from": 10000, "to": 120000, "currency": "RUR"},
            "alternate_url": "https://vacancy.ru/102734485",
            "employer": {"name": "Test Corp"},
            "snippet": {"requirement": "Python, SQL, Machine Learning"},
        },
    ]
    json_saver.write_data(vacancies)
    assert os.path.exists(json_saver.filename)


def test_get_vacancies(json_saver: JSONSaver) -> None:
    vacancies = [
        {
            "name": "Software Engineer",
            "salary": {"from": 10000, "to": 100000, "currency": "RUR"},
            "alternate_url": "https://vacancy.ru/103285189",
            "employer": {"name": "Example Inc"},
            "snippet": {"requirement": "Python, Java, C++", "responsibility": "Writing code"},
        },
        {
            "name": "Data Scientist",
            "salary": {"from": 10000, "to": 120000, "currency": "RUR"},
            "alternate_url": "https://vacancy.ru/102734485",
            "employer": {"name": "Test Corp"},
            "snippet": {"requirement": "Python, SQL, Machine Learning", "responsibility": "Writing code"},
        },
    ]
    json_saver.write_data(vacancies)
    expected_vacancies = {
        Vacancy(
            name="Software Engineer",
            salary={"from": 10000, "to": 100000, "currency": "RUR"},
            url="https://vacancy.ru/103285189",
            employer="Example Inc",
            requirement="Python, Java, C++",
            responsibility="Writing code",
        ),
        Vacancy(
            name="Data Scientist",
            salary={"from": 10000, "to": 120000, "currency": "RUR"},
            url="https://vacancy.ru/102734485",
            employer="Test Corp",
            requirement="Python, SQL, Machine Learning",
            responsibility="Writing code",
        ),
    }
    set(json_saver.get_vacancies()) == expected_vacancies


def test_delete_vacancy(json_saver: JSONSaver) -> None:
    # Добавляем данные в файл
    vacancies = [
        {
            "name": "Software Engineer",
            "salary": {"from": 10000, "to": 100000, "currency": "RUR"},
            "alternate_url": "https://vacancy.ru/103285189",
            "employer": {"name": "Example Inc"},
            "snippet": {"requirement": "Python, Java, C++", "responsibility": "Writing code"},
        },
        {
            "name": "Data Scientist",
            "salary": {"from": 10000, "to": 120000, "currency": "RUR"},
            "alternate_url": "https://vacancy.ru/102734485",
            "employer": {"name": "Test Corp"},
            "snippet": {"requirement": "Python, SQL, Machine Learning", "responsibility": "Writing code"},
        },
    ]
    json_saver.write_data(vacancies)

    # Удаляем данные из файла
    json_saver.delete_vacancy()

    # Проверяем, что файл пустой
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 0


def test_write_data_exception(json_saver: JSONSaver, monkeypatch: MagicMock) -> None:
    def mock_open(*args: tuple, **kwargs: MutableMapping[str, str]) -> MagicMock:
        raise IOError("Test exception")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(IOError):
        json_saver.write_data([])


def test_get_vacancies_exception(json_saver: JSONSaver, monkeypatch: MagicMock) -> None:
    def mock_open(*args: tuple, **kwargs: MutableMapping[str, str]) -> MagicMock:
        raise IOError("Test exception")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(IOError):
        json_saver.get_vacancies()
