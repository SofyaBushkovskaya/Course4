from src.class_hh_api import HH
from src.class_json import JSONSaver
from src.utils import get_salary, get_vacancies_by_salary


def main() -> None:
    """Главная функция работы с пользователем"""
    print("Добрый день! С помощью этого приложения поиск вакансий на hh.ru упростится.")
    hh = HH()
    print("Получаем вакансии с сайта")
    text: str = input("Введите слова для поиска вакансий: ").lower()
    per_page: int = int(input("Введите количество вакансий которое вы хотите вывести на экран: "))
    vacancies: list[dict] = hh.get_vacancies_response(text, per_page)

    print("Сохраняем вакансии в файл")
    saver = JSONSaver()
    saver.write_data(vacancies)

    min_salary, max_salary = get_salary()
    choice = input("Выберите, сортировать список да или нет: ")
    vacancies = get_vacancies_by_salary(min_salary, max_salary, choice)
    counter_vacancy = 0
    for vacancy in vacancies:
        counter_vacancy += 1
        print(f"№ вакансии: {counter_vacancy}")
        print(vacancy)

    del_choise = input("Выберите очистить список вакансий да или нет: ")
    if del_choise.lower() == "да":
        saver.delete_vacancy()
        print("Файл vacancies.json очищен, работа программы завершена.")
    else:
        print("Программа завершена")


main()
