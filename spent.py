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
               transaction_id integer primary key,
               user_id integer,
               amount number,
               category string,
               date string,
               message string
           )
        '''
        self.cursor.execute(sql_query)
        # сохраняем изменения
        self.conn.commit()

    def delete_users(self):
        # удаляет всю базу данных
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
        delete from expenses
        '''
        self.cursor.execute(sql_query)
        self.conn.commit()

    def delete_transaction(self, id):
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
        delete from expenses where id = ?
        '''
        self.cursor.execute(sql_query)
        self.conn.commit()
