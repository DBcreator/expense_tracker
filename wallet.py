import _sqlite3 as db
from user import User
import matplotlib.pyplot as plt
import pandas as pd
import os


class Wallet(User):
    def __init__(self):
        '''
           Инициализируем новую базу данных для хранения кошельков пользователей
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
           create table if not exists wallets(
               wallet_id integer primary key, 
               user_id integer,
               value number,
               name_wallet string
           )

        '''
        self.cursor.execute(sql_query)
        # сохраняем изменения
        self.conn.commit()

    def get_id(self,login,password):
        '''
        Получаем id пользователя по логину и паролю
        :param login:
        :param password:
        :return:
        '''

        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        # select user_id
        sql_query1 = '''
                    select user_id from users where login = '{}' and password = '{}' 
                    '''.format(login,password)

        self.cursor.execute(sql_query1)
        id = self.cursor.fetchone()[0]
        return id

    def get_wallet(self):
        '''
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        id = self.get_id(self.login, self.password)

        sql_query2 = '''
                            select * from wallets where user_id = '{}'
                            '''.format(id)
        self.cursor.execute(sql_query2)

        res = self.cursor.fetchall()
        return res

    def written_off(self, name_wallet, amount, category = None, message=None,date = None):
        '''
        Метод для логирования наших транзакций и снятие денег с соответсвующего кошелька пользователя
        :param amount: число
        :param category: категория расходов
        :param message: (опиционально) описание транзакции где была совершена, на что конкретно были потрачены деньги и т.д
        :return:
        '''
        from datetime import datetime
        if date == None:
            date = str(datetime.now())  # сохраняем сегодняшнюю дату

        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()

        id = self.get_id(self.login, self.password)
        data = (id, amount, category, date, message)
        sql_query1 = 'INSERT INTO expenses(user_id,amount,category,date,message) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(sql_query1, data)


        sql_query2 = '''
                    select * from wallets where user_id = '{}' and name_wallet = '{}'
                    '''.format(id,name_wallet)
        self.cursor.execute(sql_query2)
        res = self.cursor.fetchall()[-1]
        wallet_id = res[0]
        wallet = res[2]
        name = res[3]

        new_wallet = wallet - amount

        new_data = (wallet_id,id, new_wallet,name)

        sql_query3 = '''
                    replace into wallets(wallet_id,user_id,value,name_wallet) values (?, ?, ?, ?)
                    '''
        self.cursor.execute(sql_query3,new_data)

        # сохраняем изменения
        self.conn.commit()

    def refill(self,value,name_wallet):
        '''
        Пополнение кошелька на введенную сумму
        :param value: сумма, на которую пополняем
        :param name_wallet:  имя кошелька, на который совершается пополнение
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()

        id = self.get_id(self.login, self.password)

        sql_query2 = '''
                           select * from wallets where user_id = '{}' and name_wallet = '{}'
                           '''.format(id,name_wallet)

        self.cursor.execute(sql_query2)
        res = self.cursor.fetchall()[-1]
        wallet_id = res[0]
        wallet = res[2]
        name = res[3]

        new_wallet = wallet + value

        new_data = (wallet_id,id, new_wallet,name)

        sql_query3 = '''
                           replace into wallets(wallet_id,user_id,value,name_wallet) values (?, ?, ?,?)
                           '''
        self.cursor.execute(sql_query3, new_data)

        # сохраняем изменения
        self.conn.commit()

    def delete_transaction_wallets(self, wallet_id):
        '''
        Удаление определенного кошелька по id кошелька
        :param wallet_id:
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
        delete from wallets where user_id = ?
        '''
        self.cursor.execute(sql_query,wallet_id)
        self.conn.commit()

    def delete_all_database_wallets(self):
        # удаляет всю базу данных
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
                delete from wallets
                '''
        self.cursor.execute(sql_query)
        self.conn.commit()

    def view(self, category=None):
        '''
        Функция которая показывает все траты на выбранную категорию,
        если категория не выюрана, то показывает все совершенные транзакции
        :param category:  категория расходов
        :return:
        '''
        id = self.get_id(self.login,self.password)
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        if category:  # если задана категория, то показываем общую сумму в категории
            sql_query1 = '''
            select * from expenses where user_id = '{}' and category = '{}'
            '''.format(id,category)
            sql_query2 = '''
            select sum(amount) from expenses where user_id = '{}' and category = '{}'
            '''.format(id,category)
        else:  # иначе показываем все транзакции и общую сумму по всем транзакциям
            sql_query1 = '''
            select * from expenses where user_id = '{}'
            '''.format(id,category)
            sql_query2 = '''
            select sum(amount) from expenses where user_id = '{}'
            '''.format(id,category)

        self.cursor.execute(sql_query1)
        result = self.cursor.fetchall()
        result = [list(row) for row in result]
        self.cursor.execute(sql_query2)
        return result

    def total_sum(self, category=None):
        '''
        Функция которая выводит сумму за категорию
        :param category:  категория расходов
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        id = self.get_id(self.login,self.password)
        if category:  # если задана категория, то показываем общую сумму в категории
            sql_query2 = '''
            select sum(amount) from expenses where user_id and category = '{}'
            '''.format(id,category)
        else:  # иначе показываем все транзакции и общую сумму по всем транзакциям
            sql_query2 = '''
                        select sum(amount) from expenses where user_id = '{}'
                        '''.format(id,category)


        self.cursor.execute(sql_query2)
        sum = self.cursor.fetchone()[0]
        return sum

    def view_wallet(self):
        '''
        Метод, который возвращеает список кошельков пользователя
        :return:
        '''
        self.conn = db.connect('transaction.db')
        id = self.get_id(self.login, self.password)
        sql_query = '''
                    SELECT name_wallet FROM wallets where user_id = '{}'
        '''.format(id)
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        result = [list(row) for row in result]
        res = []
        for row in result:
            temp = row[0]
            res.append(temp)
        return res

    def pie(self):
        '''
        Метод, который реализует диаграмму трат пользователя по категориям
        :return:
        '''
        db_connection = db.connect('transaction.db')
        id = self.get_id(self.login,self.password)
        df = pd.read_sql_query('''SELECT * FROM expenses where user_id = '{}' '''.format(id), db_connection)
        new_df = df.groupby(['category']).sum()
        diagram = new_df.plot.pie(y='amount', figsize=(9, 9), autopct='%1.1f%%', startangle=90)
        name = 'diagram.png'
        plt.savefig(os.path.join(name), dpi=200)



#w1 = Wallet()
