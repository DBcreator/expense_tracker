import _sqlite3 as db
from spent import Transaction

class Wallet(Transaction):
    def __init__(self, value):
        self.value = value

    def written_off(self,amount, category = None, message=None):
        '''
        Логируем наши транзакции
        :param amount: число
        :param category: категория расходов
        :param message: (опиционально) описание транзакции где была совершена, на что конкретно были потрачены деньги и т.д
        :return:
        '''
        self.log(amount,category,message)
        self.value -= amount


    def replenishment(self,value):
        self.value += value

        return self.value
