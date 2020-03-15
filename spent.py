import _sqlite3 as db

class Transaction():

    def __init__(self):
        '''
           Инициализируем новую базу данных для хранения транзакций
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
           create table if not exists expenses(
               id integer primary key autoincrement,
               amount number,
               category string,
               date string,
               message string
           )
        '''
        self.cursor.execute(sql_query)
        # сохраняем изменения
        self.conn.commit()

    def log(self,amount, category = None, message=None):
        '''
        Логируем наши транзакции
        :param amount: число
        :param category: категория расходов
        :param message: (опиционально) описание транзакции где была совершена, на что конкретно были потрачены деньги и т.д
        :return:
        '''
        from datetime import datetime
        date = str(datetime.now())  # сохраняем сегодняшнюю дату
        data = (amount, category, date, message)
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = 'INSERT INTO expenses VALUES (?, ?, ?, ?)'
        self.cursor.execute(sql_query, data)
        # сохраняем изменения
        self.conn.commit()

    def delete_all_database(self):
        # удаляет всю базу данных
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
        delete from expenses
        '''
        self.cursor.execute(sql_query)
        self.conn.commit()


    '''
    Пока не знаю как сделать
    def delete_from_category(self,category):
        #удаляет все транзакции из выбранной категории
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = 
        delete from expenses where category = '{}'
        self.cursor.execute(sql_query)
        self.conn.commit()'''

    def delete_transaction(self,id):
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
        delete from expenses where id = ?
        '''
        self.cursor.execute(sql_query)
        self.conn.commit()


    def view(self, category = None):
        '''
        Функция которая показывает все траты на выбранную категорию,
        если категория не выюрана, то показывает все совершенные транзакции
        :param category:  категория расходов
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        if category: # если задана категория, то показываем общую сумму в категории
            sql_query1 = '''
            select * from expenses where category = '{}'
            '''.format(category)
            sql_query2 = '''
            select sum(amount) from expenses where category = '{}'
            '''.format(category)
        else: #иначе показываем все транзакции и общую сумму по всем транзакциям
            sql_query1 = '''
            select * from expenses  
            '''.format(category)
            sql_query2 = '''
            select sum(amount) from expenses
            '''.format(category)

        self.cursor.execute(sql_query1)
        result = self.cursor.fetchall()
        self.cursor.execute(sql_query2)
        total_sum = self.cursor.fetchone()[0]
        return total_sum, result

t1 = Transaction()
t1.log(2000,'food')
t1.log(1000,'food')