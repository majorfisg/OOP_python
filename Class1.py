
# объект - единица информации в памяти
# экземпляр - конкретный объект какогото класса
# класс - инструкция по созданию объектов одного типа
# метод - функция в классе для воздействия на объект

class Purse:
    def __init__(self, valute, name='Unknown'):
        if valute not in ('ERO', 'USD'):
            raise ValueError
        self.money = 0.00
        self.valute = valute
        self.name = name

    def top_up_balance(self, howmany):
        self.money += howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.money - howmany < 0:
            print('Недостаточно средств')
            raise ValueError('Недостаточно средств')
        self.money -= howmany
        return howmany

    def info(self):
        print(self.money)

    def __del__(self):
        print('Кошелек удален')

x = Purse('USD')
y = Purse('ERO', 'Linda')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
