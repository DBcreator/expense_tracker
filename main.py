import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from f import Ui_MainWindow, UI_LoginWindow
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


# hook logic
def ViewPng():
    pass


def test():
    user.written_off(name_wallet=ui.Wallet_list.currentText(), amount=int(ui.lineEdit_2.text()),
                     category=str(ui.lineEdit.text()), message=str(ui.lineEdit_comments.text()))
    ui.lineEdit_2.clear()
    ui.lineEdit.clear()
    entries = user.view()
    print(entries)
    ui.listwidget.setRowCount(len(entries))
    for i in range(len(entries)):
        f = 0
        for j in range(2, 6):
            ui.listwidget.setItem(i, f, QTableWidgetItem(str(entries[i][j])))
            f+=1
    ui.listwidget.resizeColumnsToContents()
    wallet_list = user.get_wallet()
    print(wallet_list)
    ui.Tabel_view.setRowCount(len(wallet_list))
    for i in range(len(wallet_list)):
        for j in range(2):
            ui.Tabel_view.setItem(i, j, QTableWidgetItem(str(wallet_list[i][j])))
    ui.listwidget.resizeColumnsToContents()


def show_it(the_password):
    Login(the_password)


ui.login.got.connect(show_it)


def statistic(self):
    ui.stat.initUI([user.login, user.password])


def Login(data):
    if not user.sign_in(login=str(data[1]), password=str(data[0])):
        return None
    MainWindow.show()
    ui.login.close()
    entries = user.view()
    ui.listwidget.setRowCount(len(entries))
    for i in range(len(entries)):
        f = 0
        for j in range(2, 6):

            ui.listwidget.setItem(i, f, QTableWidgetItem(str(entries[i][j])))
            f+=1
    wallet_list = user.get_wallet()
    print(wallet_list)
    ui.Tabel_view.setRowCount(len(wallet_list))
    for i in range(len(wallet_list)):
        for j in range(2):
            ui.Tabel_view.setItem(i, j, QTableWidgetItem(str(wallet_list[i][j])))
    ui.listwidget.resizeColumnsToContents()
    wallet_name()


def wallet_name():
    ui.Wallet_list.clear()
    ui.QComboBox_lst.clear()
    lst = user.view_wallet()
    for item in lst:
        ui.Wallet_list.addItem(str(item))
        ui.QComboBox_lst.addItem(str(item))


def Registration():
    user.init_user(login=str(ui.lineEdit_login.text()), password=str(ui.lineEdit_password.text()), name='Test')
    ui_log.lineEdit_login.clear()
    ui_log.lineEdit_password.clear()


def refill():
    user.refill(value=int(ui.lineEdit_Sum.text()), name_wallet=str(ui.QComboBox_lst.currentText()))
    ui.lineEdit_Sum.clear()
    wallet_list = user.get_wallet()
    ui.Tabel_view.setRowCount(len(wallet_list))
    for i in range(len(wallet_list)):
        for j in range(2):
            ui.Tabel_view.setItem(i, j, QTableWidgetItem(str(wallet_list[i][j])))


def AddWalet():
    user.init_wallet(value=int(ui.lineEdit_Value.text()), name_wallet=str(ui.lineEdit_name.text()))
    ui.lineEdit_Value.clear()
    ui.lineEdit_name.clear()
    wallet_list = user.get_wallet()
    ui.Tabel_view.setRowCount(len(wallet_list))
    for i in range(len(wallet_list)):
        for j in range(2):
            ui.Tabel_view.setItem(i, j, QTableWidgetItem(str(wallet_list[i][j])))
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
ui.pushButton_1.clicked.connect(statistic)
ui.pushButton_refill.clicked.connect(refill)

# main loop
sys.exit(app.exec_())
