from utils.users_interaction import users_interaction_logic


def main():
    print('Добро пожаловать в парсер вакансий!\n'
          'Я помогу подобрать нужные вам вакансии с таких платформ как:\n'
          '"Headhunter.ru" и "Superjob.ru"')
    print('.' * 50)

    # Вызов функции взаимодействия с пользователем
    users_interaction_logic()


if __name__ == '__main__':
    main()
