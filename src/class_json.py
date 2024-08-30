import json
from abc import ABC, abstractmethod
from typing import Any

from src.class_vacancy import Vacancy


class FileAbstractClass(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def write_data(self, vacancies: list[Vacancy]) -> None:
        """Абстрактный метод записи данных"""
        pass

    @abstractmethod
    def get_vacancies(self) -> None:
        """Абстрактный метод для чтения вакансий из файла json"""
        pass

    @abstractmethod
    def delete_vacancy(self) -> None:
        """Абстрактный метод удаления вакансий"""
        pass


class JSONSaver(FileAbstractClass):
    def __init__(self, filename: str = "../data/vacancies.json") -> None:
        self.filename = filename

    def write_data(self, vacancies: Any) -> None:
        """Метод записи данных в файл json"""
        with open(self.filename, "w", encoding="utf8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> Any:
        """Метод для чтения вакансий из файла json"""
        with open(self.filename, "r", encoding="utf8") as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            vacancies.append(
                Vacancy(
                    name=vacancy["name"],
                    salary=vacancy["salary"],
                    url=vacancy["alternate_url"],
                    employer=vacancy["employer"]["name"],
                    requirement=vacancy["snippet"]["requirement"],
                    responsibility=vacancy["snippet"]["responsibility"],
                )
            )
        return vacancies

    def delete_vacancy(self) -> None:
        """Метод удаления данных из файла"""
        list_vacancies_del: list = []
        list_del = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open(self.filename, "w", encoding="utf8") as f:
            f.write(list_del)
