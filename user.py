import _sqlite3 as db

class User():
    def __init__(self):
        self.login = None
        self.password = None
        self.user_id = None
        '''
           Инициализируем новую базу данных для хранения юзеров
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query1 = '''
              create table if not exists users( 
                  user_id integer primary key UNIQUE ,
                  login string UNIQUE,
                  password string,
                  name string
              )
        '''
        self.cursor.execute(sql_query1)
        # сохраняем изменения
        self.conn.commit()

    def delete_transaction_users(self, user_id):
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
        delete from users where wallet_id = ?
        '''
        self.cursor.execute(sql_query)
        self.conn.commit()

    def delete_all_database_users(self):
        # удаляет всю базу данных
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query = '''
                delete from users
                '''
        self.cursor.execute(sql_query)
        self.conn.commit()

    def get_id(self, login, password):

        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query1 = '''
                    select user_id from users where login = '{}' and password = '{}'
                    '''.format(login, password)

        self.cursor.execute(sql_query1)
        id = self.cursor.fetchone()[0]
        return id

    def init_user(self,login,password,name):
        '''
        Метод для регистрации пользователя
        :param login:
        :param password:
        :param name:
        :return:
        '''

        data1 = (login,password,name)
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query3 = '''
                            select * from users where login = '{}' 
                            '''.format(login)

        self.cursor.execute(sql_query3)
        res = self.cursor.fetchone()
        if res == None:
            sql_query1 = 'INSERT INTO users(login,password,name) VALUES (?, ?, ?)'
            self.cursor.execute(sql_query1, data1)
            sql_query2 = '''
                                        select * from users where login = '{}' and password = '{}' 
                                        '''.format(login, password)
            self.cursor.execute(sql_query2)
            res = self.cursor.fetchone()
            self.user_id = res[0]
            self.login = res[1]
            self.password = res[2]

            self.conn.commit()
            return True
        else:
            return False

    def init_wallet(self, value, name_wallet):
        '''
        Метод для регистрации кошелька пользователя
        :param value:
        :param name_wallet:
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        # id = self.get_id(self.login,self.password)
        data = (self.user_id, value, name_wallet)
        sql_query = 'INSERT INTO wallets(user_id,value,name_wallet) VALUES (?,?,?)'
        # сохраняем изменения
        self.cursor.execute(sql_query, data)
        self.conn.commit()

    def sign_in(self,login,password):
        '''
        Метод, который реалтзует вход пользователя
        :param login:
        :param password:
        :return:
        '''
        self.conn = db.connect('transaction.db')
        self.cursor = self.conn.cursor()
        sql_query1 = '''
                        select * from users where login = '{}' and password = '{}' 
                        '''.format(login, password)
        self.cursor.execute(sql_query1)
        res = self.cursor.fetchone()
        if res:
            self.user_id = res[0]
            self.login = res[1]
            self.password = res[2]
            self.conn.commit()
            return True
        else:
            #print('Wrong login or passsword')
            return False

    def exit(self):
        '''
        Метод для выхода пользователя
        :return:
        '''
        self.login = None
        self.password = None


#u1 = User()


