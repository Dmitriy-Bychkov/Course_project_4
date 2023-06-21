class Vacancies:
    vacancies = []

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
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.experience = experience
        self.employer = employer
        self.employment = employment
        self.area = area

        Vacancies.vacancies.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.vacancy_url}, {self.requirement},' \
               f'{self.responsibility}, {self.salary_from}, {self.salary_to},' \
               f'{self.currency}, {self.experience}, {self.employer},' \
               f'{self.employment}, {self.area})'

    def __str__(self):
        return f'Вакансия: {self.name}'

    def __gt__(self, other):
        return int(self.salary_from) > int(other.salary_from)

    def __ge__(self, other):
        return int(self.salary_from) >= int(other.salary_from)

    def __lt__(self, other):
        return int(self.salary_from) < int(other.salary_from)

    def __le__(self, other):
        return int(self.salary_from) <= int(other.salary_from)

    def __eq__(self, other):
        return int(self.salary_from) == int(other.salary_from)

    def requirement(self):
        """Возвращает требования вакансии"""

        return self.requirement

    def responsibility(self):
        """Возвращает обязанности вакансии"""

        return self.responsibility

    def description(self):
        """Возвращает подробную информацию о вакансии"""

        return f'{self.requirement}' \
               f' {self.responsibility}'

    def salary(self):
        """Возвращает диапазон зарплат у вакансии"""

        if self.salary_from == 0 and self.salary_to == 0:
            return "Зарплата не указана"

        elif self.salary_from is None:
            return f'{self.salary_to} {self.currency}'

        elif self.salary_to is None or self.salary_to == 0:
            return f'{self.salary_from} {self.currency}'

        elif self.salary_from == self.salary_to:
            return f'{self.salary_from} {self.currency}'

        else:
            return f'{self.salary_from}-{self.salary_to} {self.currency}'

    def currency(self):
        """Возвращает валюту зарплаты"""

        return self.currency

    def experience(self):
        """Возвращает опыт для вакансии"""

        return self.experience

    def vac_url(self):
        """Возвращает ссылку на вакансию"""

        return self.vacancy_url

    def area(self):
        """Возвращает город вакансии"""

        return self.area

    def employer(self):
        """Возвращает работодателя"""

        return self.employer

    def employment(self):
        """Возвращает занятость"""

        return self.employment

    def all_vacancy_information(self):
        """Возвращает всю информацию о вакансии"""

        return f'Вакансия:\n{self.name}, с з/п: {self.salary()}\n' \
               f'Опыт работы: {self.experience}\nГород: {self.area}\n' \
               f'Описание и требования: {self.description()}\nЗанятость: {self.employment}\n' \
               f'Работодатель: {self.employer}\nСсылка на вакансию: {self.vac_url()}'
