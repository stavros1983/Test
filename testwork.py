import sys
import pathlib


class Event:

    def __init__(self, date, category, money_sum, description):
        self.date = date
        self.category = category
        self.money_sum = money_sum
        self.description = description

    def __str__(self):
        return (f'Дата: {self.date}\n'
                f'Категория: {self.category}\n'
                f'Сумма: {self.money_sum}\n'
                f'Описание: {self.description}\n')

    def validate_event_date_form(self):
        if len(self.date) == 10 and self.date[0:4].isdigit() and self.date[5:7].isdigit() and self.date[8:].isdigit()\
                and self.date[4] == '-' and self.date[7] == '-':
            return True
        else:
            return False

    def validate_event(self):
        if not len(self.date) == 10 or not self.date[0:4].isdigit() or not self.date[5:7].isdigit() \
          or not self.date[8:].isdigit() or not self.date[4] == '-' or not self.date[7] == '-':
            return False
        if not self.money_sum.isdigit():
            return False
        return True

    def validate_event_money_sum(self):
        if self.money_sum.isdigit():
            return True
        else:
            return False


class EventList:

    def __init__(self):
        self.events = {}
#        self.events[len(self.events) + 1] = event

    def add_event(self, event):
        self.events[str(len(self.events) + 1)] = event
        print(self.events[str(len(self.events))])

    def show_ballance_detail(self):
        t_sum_minus = 0
        t_sum_plus = 0
        t_sum = 0
        for i in self.events:
            if self.events[i].category == 'Расход':
                t_sum_minus = t_sum_minus + int(self.events[i].money_sum)
                t_sum = t_sum - int(self.events[i].money_sum)
            if self.events[i].category == 'Доход':
                t_sum_plus = t_sum_plus + int(self.events[i].money_sum)
                t_sum = t_sum + int(self.events[i].money_sum)

        print(f"Балланс: {t_sum}\n"
              f"Расход: {t_sum_minus}\n"
              f"Доход: {t_sum_plus}\n")

    def search_category(self, category):
        counter = 0
        for i in self.events:
            if self.events[i].category == category:
                counter += 1
                print(f'ID записи: {i}\n{self.events[i]}')
        if counter == 0:
            print("Не найдено")

    def search_date(self, date):
        counter = 0
        for i in self.events:
            if self.events[i].date == date:
                counter += 1
                print(f'ID записи: {i}\n{self.events[i]}')
        if counter == 0:
            print("Не найдено")

    def search_money_sum(self, money_sum):
        counter = 0
        for i in self.events:
            if self.events[i].money_sum == money_sum:
                counter += 1
                print(f'ID записи: {i}\n{self.events[i]}')
        if counter == 0:
            print("Не найдено")

    def update_event(self, id, event):
        self.events[id] = event
        print(f'Запись с ID: {id} обновлена\n{self.events[id]}')


def task_choice():
    flag_task_choice = True
    while flag_task_choice:
        command_start = input('Введите 1 для вывода балланса,\n'
                              'Введите 2 для добавления новой записи,\n'
                              'Введите 3 для редактирования записи,\n'
                              'Введите 4 для поиска записи по категории\n'
                              'Введите 5 для завершения\n')
        if command_start.isdigit() is False:
            print("Неправильно введено число\n")
            continue
        if 1 > int(command_start) or 5 < int(command_start):
            print("Неправильно введено число\n")
        else:
            return int(command_start)


def task_activation(command, personal_wallet):
    if command == 1:
        personal_wallet.show_ballance_detail()
    if command == 2:
        personal_wallet = EventList()
        flag = True
        while flag:
            try:
                date, category, money_sum, description = (input('Введите данные через пробел без запятой в формате:'
                                                                ' Дата(формат строки 1111-11-11),'
                                                                ' Категория,'
                                                                ' Сумма(числовой формат),'
                                                                ' Описание\n').split())
                event = Event(date, category, money_sum, description)
                if event.validate_event():
                    flag = False
                else:
                    print('Неправильный формат ввода данных')
            except:
                print('Неправильный формат ввода данных')

        personal_wallet.add_event(event)
    if command == 3:
        flag_id = True
        while flag_id:
            id = input('Введите ID записи для изменения\n')
            if id in personal_wallet.events:
                flag_id = False
            else:
                print(f'Запись с ID: {id} отсутствует\n'
                      f'Всего {len(personal_wallet.events)} записи.\n'
                      f'ID начинается с 1\n')

        flag = True
        while flag:
            try:
                date, category, money_sum, description = (input('Введите данные через пробел без запятой в формате:'
                                                                ' Дата(формат строки 1111-11-11),'
                                                                ' Категория,'
                                                                ' Сумма(числовой формат),'
                                                                ' Описание\n').split())
                new_event = Event(date, category, money_sum, description)
                if new_event.validate_event():
                    flag = False
                else:
                    print('Неправильный формат ввода данных')
            except:
                print('Неправильный формат ввода данных')

        personal_wallet.update_event(id, new_event)

    if command == 4:
        search_criteria = input('Выберите критерий поиска записи\n'
                                'Нажмите 1 для поиска по дате\n'
                                'Нажмите 2 для поиска по сумме\n'
                                'Нажмите 3 для поиска по категории\n')
        if search_criteria == '1':
            date = input('Введите дату в формате(1111-11-11)\n')
            personal_wallet.search_date(date)
        elif search_criteria == '2':
            money_sum = input('Введите сумму в числовом формате\n')
            personal_wallet.search_money_sum(money_sum)
        elif search_criteria == '3':
            category = input('Введите название категории\n')
            personal_wallet.search_category(category)
        else:
            print('Неверные критерии поиска')
    if command == 5:
        info_write_into_txt_file(personal_wallet)
        sys.exit()


def info_write_into_txt_file(event_list):
    path = pathlib.Path('D:/Pathtest/test.txt')
    with path.open(mode='w', encoding='utf-8') as file:
        for i in event_list.events.keys():
            file.write(f'ID записи: {i}\n'
                       f'{event_list.events[i].date}\n'
                       f'{event_list.events[i].category}\n'
                       f'{event_list.events[i].money_sum}\n'
                       f'{event_list.events[i].description}\n'
                       f'\n')


def info_receive_from_txt_file():
    path = pathlib.Path('D:/Pathtest/test.txt')
    with path.open(mode='r', encoding='utf-8') as file:
        p = EventList()
        counter = 1
        for line in file.readlines():
            if counter == 1:
                id = line
                counter += 1
                continue
            if counter == 2:
                date = line[:-1]
                counter += 1
                continue
            if counter == 3:
                category = line[:-1]
                counter += 1
                continue
            if counter == 4:
                money_sum = line[:-1]
                counter += 1
                continue
            if counter == 5:
                description = line[:-1]
                counter += 1
                p.add_event(Event(date, category, money_sum, description))
                continue
            if counter == 6:
                counter = 1

    return p


def data_from_file_or_new_data():
    data_choice = input('Введите 1 для работы с данными из файла.\n'
                        'Введите 2, если данные из файла не актуальны и не нужны для дальнейшей работы.\n'
                        'Введите 3 для завершения работы.\n')
    if data_choice == '1':
        p = info_receive_from_txt_file()
        print('Данные из файла успешно получены\n')
        return p
    if data_choice == '2':
        print('Начинаем работу с новыми данными. При сохранении их в файл, данные из файла будут утеряны!!!\n')
        p = EventList()
        return p
    if data_choice == '3':
        sys.exit()


def main():
    data = data_from_file_or_new_data()
    while True:
        command_start = task_choice()
        task_activation(command_start, data)


if __name__ == '__main__':
    main()
