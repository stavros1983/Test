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


class EventList:

    def __init__(self, event):
        self.events = {}
        self.events[len(self.events) + 1] = event

    def add_event(self, event):
        self.events[len(self.events) + 1] = event

    def show_ballance_detail(self):
        t_sum_minus = 0
        t_sum_plus = 0
        t_sum = 0
        for i in self.events:
            if self.events[i].category == 'Расход':
                t_sum_minus = t_sum_minus + self.events[i].money_sum
                t_sum = t_sum - self.events[i].money_sum
            if self.events[i].category == 'Доход':
                t_sum_plus = t_sum_plus + self.events[i].money_sum
                t_sum = t_sum + self.events[i].money_sum

        print(f"Балланс: {t_sum}\n"
              f"Расход: {t_sum_minus}\n"
              f"Доход: {t_sum_plus}")

    def search_category(self, category):
        for i in self.events:
            if self.events[i].category == category:
                print(f'ID записи: {i}\n{self.events[i]}')

    def search_date(self, date):
        for i in self.events:
            if self.events[i].date == date:
                print(f'ID записи: {i}\n{self.events[i]}')

    def search_money_sum(self, money_sum):
        for i in self.events:
            if self.events[i].money_sum == money_sum:
                print(f'ID записи: {i}\n{self.events[i]}')


el1 = Event( '22-05-01', 'Расход', 1000, 'зарплата')
el2 = Event( '22-05-02', 'Доход', 2, 'зарплата')
el3 = Event( '22-05-01', 'Доход', 5000, 'зарплата')
p = EventList(el1)
p.add_event(el2)
p.add_event(el3)
# print(p.events['pay'].category)
p.show_ballance_detail()
print(p.events)
p.search_money_sum(5000)
