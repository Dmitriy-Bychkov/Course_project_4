import json

from src.vacancies import Vacancies


class JsonSaver:
    """Работа с файлом json"""

    @staticmethod
    def write_json(filename, vacancies):
        """Запись вакансий в файл json"""

        with open(filename, 'w', encoding='utf-8') as file:
            json_file = []

            # Создаем словарь, который запишется в файл
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

            # Создаем экземпляр класса Vacancies
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

    @staticmethod
    def sort_by_max_salary(vacancies):
        """Сортировка вакансий по наибольшей зарплате"""

        max_salary_list = sorted(vacancies,
                                 key=lambda
                                 vacancy: vacancy.salary_to if vacancy.salary_to != 0 else vacancy.salary_from,
                                 reverse=True)

        return max_salary_list
