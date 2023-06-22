import requests

from src.api_worker import ApiWorker
from src.vacancies import Vacancies


class HHApi(ApiWorker):
    """"Класс для работы с сайтом hh.ru"""

    def __init__(self):
        self.api_url = 'https://api.hh.ru/vacancies'
        self.keyword = None
        self.per_page = 50

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def get_vacancies(self):
        """Возвращает список вакансий"""

        vacancies = []
        params = {
            "text": self.keyword,
            "per_page": self.per_page
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
                    responsibility = item['snippet']['responsibility'].replace('<highlighttext>', '').replace(
                        '</highlighttext>', '')

                area = item['area']['name']

                # проверка на наличие указания зарплаты и корректировка написания с api superjob
                if item['salary'] is None:
                    salary_from = 0
                    salary_to = 0
                    currency = None
                elif not item['salary']['from']:
                    salary_from = 0
                    salary_to = item['salary']['to']
                    currency = item['salary']['currency']
                elif not item['salary']['to']:
                    salary_from = item['salary']['from']
                    salary_to = 0
                    currency = item['salary']['currency']
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
