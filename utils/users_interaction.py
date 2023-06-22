from src.hh_api import HHApi
from src.json_saver import JsonSaver
from src.sj_api import SJApi


def users_interaction_logic():
    """
    Функция основной логики взаимодействия с пользователем.
    Исподьзуется для вызова в главном файле запуска - main
    """

    filename = 'src/vacancies.json'
    saver = JsonSaver()

    while True:
        platform = input('Введите соответствующую цифру, где искать вакансии:\n'
                         '1 - искать на "Headhunter.ru"\n'
                         '2 - искать на "Superjob.ru"\n'
                         '3 - искать на обеих платформах\n'
                         )
        keyword = input('Введите ключевое слово для поиска (например: "python" или "java"):\n')
        city = input('Укажите город в котором искать вакансии:\n')
        number_vacancies = int(input('Сколько ваканcий нужно загрузить с сайта:\n'))
        search_phrase = f'{keyword} {city}'
        print()

        if platform == '1':
            hh_api = HHApi()
            hh_api.keyword = search_phrase
            hh_api.per_page = number_vacancies
            vacancies_list = hh_api.get_vacancies()
            saver.write_json(filename, vacancies_list)

            break

        elif platform == '2':
            sj_api = SJApi()
            sj_api.keyword = search_phrase
            sj_api.count = number_vacancies
            vacancies_list = sj_api.get_vacancies()
            saver.write_json(filename, vacancies_list)
            break

        elif platform == '3':
            hh_api = HHApi()
            hh_api.keyword = search_phrase
            hh_api.per_page = number_vacancies
            vacancies_list = hh_api.get_vacancies()

            sj_api = SJApi()
            sj_api.keyword = search_phrase
            sj_api.count = number_vacancies
            sj_vacancies_list = sj_api.get_vacancies()
            vacancies_list.extend(sj_vacancies_list)

            saver.write_json(filename, vacancies_list)
            break

        else:
            print('Вы ввели некорректный номер!\n'
                  'Повторите ввод снова.\n'
                  )
            continue

    print(f'{len(vacancies_list)} вакансий загружено успешно!')

    while True:
        user_answer = input('Выберите вариант вывода на экран загруженных ваканссий:\n'
                            '1 - Показать все загруженные вакансии\n'
                            '2 - Показать отсортированные вакансии по максимальной зарплате\n'
                            )
        print('.' * 50)

        if user_answer == '1':
            vacancies = saver.load_from_file(filename)
            for i in vacancies:
                print(i.all_vacancy_information())
                print('.' * 50)
            break

        elif user_answer == '2':
            vacancies = saver.load_from_file(filename)
            sorted_vacancies = saver.sort_by_max_salary(vacancies)
            for i in sorted_vacancies:
                print(i.all_vacancy_information())
                print('.' * 50)
            break

        else:
            print('Вы ввели некорректный номер\n'
                  'Повторите ввод снова.\n'
                  )
            continue
