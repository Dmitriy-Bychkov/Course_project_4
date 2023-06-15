from abc import ABC, abstractmethod


class ApiWorker(ABC):
    """Абстрактный класс для работы с платформами через Api"""

    def __init__(self):
        self.api_url = None
        self.keyword = None
        self.vacancy_url = None
        self.__experience = None
        self.__salary = None
        self.__area = None
        self.__only_with_salary = False
        self.__currency = None
        self.__page = 0
        self.__per_page = 100

    @abstractmethod
    def get_vacancies(self):
        """Возвращает список вакансий"""

        pass
