from src.class_vacancy import Vacancy


def test_vacancy_init() -> None:
    vacancy = Vacancy(
        "Software Engineer",
        {"from": 50000, "to": 70000, "currency": "RUR"},
        "http://example.com",
        "Example Inc",
        "Python skills",
        "Writing code",
    )
    assert vacancy.name == "Software Engineer"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 70000
    assert vacancy.url == "http://example.com"
    assert vacancy.employer == "Example Inc"
    assert vacancy.requirement == "Python skills"
    assert vacancy.responsibility == "Writing code"


def test_vacancy_comparison() -> None:
    vacancy1 = Vacancy(
        "Software Developer",
        {"from": 50000, "to": 70000, "currency": "RUR"},
        "http://example.com",
        "Example Inc.",
        "Python, SQL",
        "Writing code",
    )
    vacancy2 = Vacancy(
        "Data Scientist",
        {"from": 60000, "to": 80000, "currency": "RUR"},
        "http://example2.com",
        "Example2 Inc.",
        "Machine Learning, Statistics",
        "Writing code",
    )

    assert vacancy1.salary_to < vacancy2.salary_to
    assert vacancy2.salary_to > vacancy1.salary_to


def test_vacancy_with_missing_salary() -> None:
    vacancy = Vacancy("Software Engineer", None, "http://example.com", "Example Inc", "Python skills", "Writing code")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.salary_currency == "валюта не указана"


def test_vacancy_sorting() -> None:
    vacancy1 = Vacancy(
        "Software Developer",
        {"from": 50000, "to": 70000, "currency": "RUR"},
        "http://example.com",
        "Example Inc.",
        "Python, SQL",
        "Writing code",
    )
    vacancy2 = Vacancy(
        "Data Scientist",
        {"from": 60000, "to": 80000, "currency": "RUR"},
        "http://example2.com",
        "Example2 Inc.",
        "Machine Learning, Statistics",
        "Writing code",
    )
    vacancies = [vacancy1, vacancy2]
    vacancies.sort()
    assert vacancies == [vacancy2, vacancy1]


def test_vacancy_repr() -> None:
    vacancy = Vacancy(
        "Software Engineer",
        {"from": 50000, "to": 70000, "currency": "RUR"},
        "http://example.com",
        "Example Inc",
        "Python skills",
        "Writing code",
    )
    expected_output = (
        "Vacancy(Software Engineer, 50000, 70000, http://example.com, Example Inc, " "Python skills, Writing code)"
    )
    assert repr(vacancy) == expected_output


def test_vacancy_str() -> None:
    vacancy = Vacancy(
        "Software Engineer",
        {"from": 50000, "to": 70000, "currency": "RUR"},
        "http://example.com",
        "Example Inc",
        "Python skills",
        "Writing code",
    )
    expected_output = (
        "Название: Software Engineer\n"
        "Зарплата: от 50000 до 70000 RUR\n"
        "Ссылка: http://example.com\n"
        "Название компании: Example Inc\n"
        "Требования: Python skills\n"
        "Обязанности: Writing code\n"
    )
    assert str(vacancy) == expected_output
