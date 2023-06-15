import json

from src.hh_api import HHApi
from src.vacancies import Vacancies


# class JsonSaver:
#     """Работа с файлом json"""

def write_json():
    """Запись вакансий в файл json"""

    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json_file = []

        for vac in Vacancies.vacancies:
            vacancies_dict = {'name': vac.name,
                              'description': vac.description,
                              'area': vac.area,
                              'salary': vac.salary,
                              'currency': vac.currency,
                              'experience': vac.experience,
                              'employer': vac.employer,
                              'employment': vac.employment,
                              'vacancy_url': vac.vac_url
                              }

            json_file.append(vacancies_dict)
        file.write(json.dumps(json_file, ensure_ascii=False))


a = HHApi()
a.keyword = 'python'
b = a.get_vacancies()
print(b)
c = Vacancies.vacancies
print('-----')
print(c)
print('-----')
d = write_json()
