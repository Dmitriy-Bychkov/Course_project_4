class Vacancies:

    def __init__(
            self, name, requirement, responsibility,
            salary_from, salary_to, currency, experience,
            employer, employment, area, vacancy_url
    ):
        """
        Класс выбранных вакансий с необходимой информацией
        :param name: Название вакансии
        :param requirement: Требования к работнику
        :param responsibility: Обязанности
        :param salary_from: Зарплата от...
        :param salary_to: Зарплата до.
        :param currency: Валюта зарплаты
        :param experience: Опыт работы
        :param employer: Работодатель
        :param employment: Занятость
        :param area: Город вакансии
        :param vacancy_url: Ссылка на вакансию
        """

        self.name = name
        self.vacancy_url = vacancy_url
        self.__requirement = requirement
        self.__responsibility = responsibility
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__currency = currency
        self.__experience = experience
        self.__employer = employer
        self.__employment = employment
        self.__area = area

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'Вакансия: {self.name}'

    @property
    def description(self):
        """Возвращает подробную информацию о вакансии"""

        return f'Описание вакансии (требования и обязанности):\n{self.__requirement}\n' \
               f'{self.__responsibility}'

    @property
    def salary(self):
        """Возвращает диапазон зарплат у вакансии"""

        if self.__salary_from == 0 and self.__salary_to == 0:
            return "'Зарплата не указана'"

        elif self.__salary_from is None:
            return f'З/п до {self.__salary_to} {self.__currency}'

        elif self.__salary_to is None or self.__salary_to == 0:
            return f'З/п от {self.__salary_from} {self.__currency}'

        elif self.__salary_from == self.__salary_to:
            return f'З/п {self.__salary_from} {self.__currency}'

        else:
            return f'З/п от {self.__salary_from} до {self.__salary_to} {self.__currency}'

    @property
    def experience(self):
        """Возвращает опыт для вакансии"""

        return f'Опыт работы: {self.__experience}'

    def vac_url(self):
        """Возвращает ссылку на вакансию"""

        return f'Ссылка на вакансию: {self.vacancy_url}'

    @property
    def area(self):
        """Возвращает нахождение вакансии"""

        return self.__area

    @property
    def vac_employer(self):
        """Возвращает работодателя"""

        return f'Работодатель: {self.__employer}'

    @property
    def vac_employment(self):
        """Возвращает занятость"""

        return f'Занятость: {self.__employment}'

    def all_vacancy_information(self):
        """Возвращает всю информацию о вакансии"""

        return f'Вакансия:\n{self.name}, {self.salary}\n' \
               f'{self.experience}\nГород: {self.area}\n' \
               f'{self.description}\n{self.vac_employment}\n' \
               f'{self.vac_employer}\n{self.vac_url()}'
