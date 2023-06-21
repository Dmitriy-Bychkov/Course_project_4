from src.hh_api import HHApi
from src.json_saver import JsonSaver
from src.sj_api import SJApi


def main():
    print('Добро пожаловать в парсер вакансий!\n'
          'Я помогу подобрать нужные вам вакансии с таких платформ как:\n'
          '"Headhunter.ru" и "Superjob.ru"')
    print('.' * 50)

    saver = JsonSaver()

    while True:
        platform = input('Введите соответствующую цифру, где искать вакансии:\n'
                         '1 - искать на "Headhunter.ru"\n'
                         '2 - искать на "Superjob.ru"\n'
                         '3 - искать на обеих платформах\n'
                         )
        # keyword = input('Введите ключевое слово для поиска (например: "python" или "java")\n')
        # city = input('В каком городе искать?\n')
        # number_vacancies = int(input('Сколько ваканcий загрузить?\n'))
        print()

        if platform == '1':
            hh_api = HHApi()
            hh_api.keyword = 'python'
            hh_api.per_page = 3
            vacancies_list = hh_api.get_vacancies()
            saver.write_json('src/vacancies.json', vacancies_list)

            # for i in vacancies_list:
            #     print(i.all_vacancy_information())
            #     print('.' * 50)
            # hh_api.write_json()
            break

        elif platform == '2':
            sj_api = SJApi()
            sj_api.keyword = 'python'
            sj_api.count = 5
            vacancies_list = sj_api.get_vacancies()
            saver.write_json('src/vacancies.json', vacancies_list)
            break

        elif platform == '3':
            hh_api = HHApi()
            hh_api.keyword = 'java'
            hh_api.per_page = 2
            vacancies_list = hh_api.get_vacancies()

            sj_api = SJApi()
            sj_api.keyword = 'java'
            sj_api.count = 2
            sj_vacancies_list = sj_api.get_vacancies()
            vacancies_list.extend(sj_vacancies_list)

            saver.write_json('src/vacancies.json', vacancies_list)
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
            vacancies = saver.load_from_file('src/vacancies.json')
            for i in vacancies:
                print(i.all_vacancy_information())
                print('.' * 50)
            break

        elif user_answer == '2':
            vacancies = saver.load_from_file('src/vacancies.json')
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


if __name__ == '__main__':
    main()
