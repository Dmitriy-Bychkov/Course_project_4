import requests

from src.api_worker import ApiWorker
from src.sj_api_token import sj_api_token
from src.vacancies import Vacancies


class SJApi(ApiWorker):
    """"Класс для работы с сайтом superjob.ru"""

    def __init__(self):
        self.sj_api_token = sj_api_token
        self.api_url = 'https://api.superjob.ru/2.0/vacancies/'
        self.keyword = None
        self.count = 50

    def get_vacancies(self):
        """Возвращает список вакансий"""

        vacancies = []
        params = {
            "keyword": self.keyword,
            "count": self.count,
        }

        sj_response = requests.get(self.api_url, params, headers=self.sj_api_token)

        if sj_response.status_code == 200:
            data = sj_response.json()

            # Цикл для перебора всех вакансий по параметрам
            for item in data['objects']:
                name = item['profession']

                # Проверяем наличие требований у вакансии
                if item['candidat'] is None:
                    requirement = ''
                else:
                    requirement = item['candidat']

                # Проверяем наличие обязанностей у вакансии
                if item['work'] is None:
                    responsibility = ''
                else:
                    responsibility = item['work']

                area = item['town']['title']
                salary_from = item['payment_from']
                salary_to = item['payment_to']

                # Корректировка соответствия написания валюты с hh.ru
                if not item['payment_from'] and not item['payment_to']:
                    currency = None
                elif item['currency'] == 'rub':
                    currency = 'RUR'
                else:
                    currency = item['currency']

                experience = item['experience']['title']
                employer = item['client']['title']
                employment = item['type_of_work']['title']
                vacancy_url = item['link']

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
            print(f'Ошибка подключения к серверу - {sj_response.status_code}')
