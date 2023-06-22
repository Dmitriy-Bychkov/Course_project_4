from abc import ABC, abstractmethod


class ApiWorker(ABC):
    """Абстрактный класс для работы с платформами через Api"""

    def __init__(self):
        self.api_url = None
        self.keyword = None
        self.vacancy_url = None
        self.experience = None
        self.salary = None
        self.area = None
        self.only_with_salary = False
        self.currency = None
        self.page = 0
        self.per_page = 50

    @abstractmethod
    def get_vacancies(self):
        """Возвращает список вакансий"""

        pass
