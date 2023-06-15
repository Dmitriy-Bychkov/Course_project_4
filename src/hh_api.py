import requests

from src.api_worker import ApiWorker
from src.vacancies import Vacancies


class HHApi(ApiWorker):
    """"Класс для работы с сайтом hh.ru"""

    def __init__(self):
        self.api_url = 'https://api.hh.ru/vacancies'
        self.keyword = None
        self.vacancy_url = None
        self.__experience = None
        self.__salary = None
        self.__area = None
        self.__only_with_salary = False
        self.__currency = None
        self.__page = 0
        self.__per_page = 20

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def get_vacancies(self):
        """Возвращает список вакансий"""

        vacancies = []
        params = {
            "text": self.keyword,
            "experience": self.__experience,
            "salary": self.__salary,
            "area": self.__area,
            "only_with_salary": self.__only_with_salary,
            "currency": self.__currency,
            "page": self.__page,
            "per_page": self.__per_page
        }

        hh_response = requests.get(self.api_url, params)

        if hh_response.status_code == 200:
            data = hh_response.json()

            # Цикл для перебора всех вакансий по параметрам
            for item in data['items']:
                name = item['name']

                # Проверяем наличие требований у вакансии
                if item['snippet']['requirement'] is None:
                    requirement = ''
                else:
                    requirement = item['snippet']['requirement'].replace('<highlighttext>', '').replace(
                        '</highlighttext>', '')

                # Проверяем наличие обязанностей у вакансии
                if item['snippet']['responsibility'] is None:
                    responsibility = ''
                else:
                    responsibility = item['snippet']['responsibility']

                area = item['area']['name']

                # проверка на наличие указания зарплаты
                if item['salary'] is None:
                    salary_from = 0
                    salary_to = 0
                    currency = None
                else:
                    salary_from = item['salary']['from']
                    salary_to = item['salary']['to']
                    currency = item['salary']['currency']

                experience = item['experience']['name']
                employer = item['employer']['name']
                employment = item['employment']['name']
                vacancy_url = item['alternate_url']

                # Создаем экземпляр класса - Vacancies
                vacancy = Vacancies(
                    name,
                    requirement,
                    responsibility,
                    salary_from,
                    salary_to,
                    currency,
                    experience,
                    employer,
                    employment,
                    area,
                    vacancy_url
                )

                # Добавляем вакансию в список
                vacancies.append(vacancy)

            return vacancies

        else:
            print(f'Ошибка подключения к серверу - {hh_response.status_code}')


a = HHApi()
a.keyword = 'python'
b = a.get_vacancies()
#print(b)
# c = b.write_json
#for i in b:
    #print(i)
    # print(i.description)
    # print(i.salary)
    # print(i.experience)
    # print(i.area)
    # print(i.vac_url())
    # print(i.vac_employer)
    # print(i.vac_employment)
    #print(i.all_vacancy_information())
