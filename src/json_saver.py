import json

from src.vacancies import Vacancies


class JsonSaver:
    """Работа с файлом json"""

    @staticmethod
    def write_json(filename, vacancies):
        """Запись вакансий в файл json"""

        with open(filename, 'w', encoding='utf-8') as file:
            json_file = []

            for vac in vacancies:
                vacancies_dict = {'name': vac.name,
                                  'salary': vac.salary(),
                                  'salary_min': vac.salary_from,
                                  'salary_max': vac.salary_to,
                                  'currency': vac.currency,
                                  'experience': vac.experience,
                                  'employment': vac.employment,
                                  'requirement': vac.requirement,
                                  'responsibility': vac.responsibility,
                                  'description': vac.description(),
                                  'area': vac.area,
                                  'employer': vac.employer,
                                  'vacancy_url': vac.vac_url()
                                  }

                json_file.append(vacancies_dict)
            file.write(json.dumps(json_file, sort_keys=False, indent=4, ensure_ascii=False))

    @staticmethod
    def load_from_file(filename):
        """Чтение вакансий из файл json"""

        with open(filename, 'r', encoding='UTF-8') as file:
            json_data = file.read()
            data = json.loads(json_data)
        vacancies = []
        for i in data:
            name = i["name"]
            requirement = i["requirement"]
            responsibility = i["responsibility"]
            salary_from = i["salary_min"]
            salary_to = i["salary_max"]
            currency = i["currency"]
            experience = i["experience"]
            employer = i["employer"]
            employment = i["employment"]
            area = i["area"]
            vacancy_url = i["vacancy_url"]

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
            vacancies.append(vacancy)

        return vacancies

    def sort_by_max_salary(self, vacancies):
        """Сортировка вакансий по наибольшей зарплате"""

        max_salary_list = sorted(vacancies,
                                 key=lambda x: x.get('salary_max') if x.get('salary_max') != 0 else x.get('salary_min'),
                                 reverse=True)
        # max_salary_list = sorted(vacancies, reverse=True)

        return max_salary_list

# a = JsonSaver()
# b = a.load_from_file()
# c = a.sort_by_max_salary()
# print(b)
# print(c)
# for res in c:
#     print(res["name"], '-', res["salary"])
# a = HHApi()
# a.per_page = 3
# a.keyword = 'java'
# a.get_vacancies()
# # print(b)
# #c = Vacancies.vacancies
# # print('-----')
# # print(c)
# # print('-----')
# write_json()
