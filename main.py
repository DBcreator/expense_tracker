import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from f import Ui_MainWindow, UI_LoginWindow, Statistics
from pie import pie
import sqlite3 as db
import pandas as pd
from wallet import Wallet

# create app
app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
# init
MainWindow = QtWidgets.QMainWindow()
ui_log = UI_LoginWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui_login = UI_LoginWindow()
# ui_login.show()

user = Wallet()
'''''
w2 = Wallet()
w1.init_user(login ='1', password = '1234',name = 'Test')
w1.init_wallet(value = 10000,name_wallet = 'test')
w2.init_user(login='2',password='1234',name = 'f')
w2.init_wallet(value=1000,name_wallet='u')

w1.written_off(amount=120,category='Food')
w1.written_off(amount=120,category='Food')

w2.written_off(amount=190)
w2.written_off(amount=190)

#print(w1.get_wallet())

w1.refill(value=1000)
w1.refill(value=1000)

#w1.sign_in(login = '1',password='1234')
print(w1.view())
print(w1.total_sum(category='Food'))
'''''


# hook logic
def ViewPng():
    pass


def test():
    user.written_off(name_wallet=ui.Wallet_list.currentText(), amount=int(ui.lineEdit_2.text()),
                     category=str(ui.lineEdit.text()))
    ui.lineEdit_2.clear()
    ui.lineEdit.clear()
    entries = user.view()
    print(entries)
    ui.listwidget.setRowCount(len(entries))
    for i in range(len(entries)):
        for j in range(1, 5):
            ui.listwidget.setItem(i, j - 1, QTableWidgetItem(str(entries[i][j])))
    ui.listwidget.resizeColumnsToContents()


def show_it(the_password):
    Login(the_password)


ui.login.got.connect(show_it)


def statistics(self):
    ui.stat.initUI([user.login,user.password])


def Login(data):
    if not user.sign_in(login=str(data[1]), password=str(data[0])):
        return None
    MainWindow.show()
    ui.login.close()
    entries = user.view()
    print(entries)
    ui.listwidget.setRowCount(len(entries))
    for i in range(len(entries)):
        for j in range(1, 5):
            ui.listwidget.setItem(i, j - 1, QTableWidgetItem(str(entries[i][j])))
    ui.listwidget.resizeColumnsToContents()
    wallet_name()


def wallet_name():
    ui.Wallet_list.clear()
    lst = user.view_wallet()
    for item in lst:
        ui.Wallet_list.addItem(str(item))


def Registration():
    user.init_user(login=str(ui.lineEdit_login.text()), password=str(ui.lineEdit_password.text()), name='Test')
    ui_log.lineEdit_login.clear()
    ui_log.lineEdit_password.clear()


def AddWalet():
    user.init_wallet(value=int(ui.lineEdit_Value.text()), name_wallet=str(ui.lineEdit_name.text()))
    ui.lineEdit_Value.clear()
    ui.lineEdit_name.clear()
    wallet_name()
def Exit():
    MainWindow.close()
    ui.login.show()


db_connection = db.connect('transaction.db')
df1 = pd.read_sql_query('SELECT * FROM users', db_connection)
print(df1)
df2 = pd.read_sql_query('SELECT * FROM wallets', db_connection)
print(df2)
df3 = pd.read_sql_query('SELECT * FROM expenses', db_connection)
print(df3)

ui.pushButton.clicked.connect(test)
ui.pushButton_1.clicked.connect(ViewPng)
ui_log.pushButton_Login.clicked.connect(Login)
ui.pushButton_AddWallet.clicked.connect(AddWalet)
ui.pushButton_Exit.clicked.connect(Exit)
ui_log.pushButton_Sign_up.clicked.connect(Registration)
ui.pushButton_1.clicked.connect(statistics)
# print(w1.get_wallet(login='1',password='1234'))

# main loop
sys.exit(app.exec_())
