import sqlite3
import sys
import hashlib
from auth import Ui_autorisation
from Reg_win import RegWin
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from SQliteManager import DatabaseManager

class AutoriseWin(QWidget):
    def __init__(self):
        super(AutoriseWin, self).__init__()
        self.ui = Ui_autorisation()
        self.ui.setupUi(self)
        # кнопка входа
        self.ui.login_btn.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.username_value, self.ui.password_value]
        #кнопка регистрации пользователя
        self.ui.reg_btn.clicked.connect(self.reg)
    #авторизация пользователя
    def auth(self):
        self.passw = self.ui.password_value.text()
        with DatabaseManager("mydb.db") as conn:
            if conn:
                cur = conn.cursor()
                sql_data = self.ui.username_value.text()
                try:
                    cur.execute("SELECT hashed_pass FROM users WHERE username == (?)", (sql_data,))
                    query = cur.fetchone()
                    if query[0]==self.passw:
                        print('вход')
                    else:
                        QMessageBox.information(self, 'Ошибка',
                                                'Неправильно введен логин или пароль!')
                except Exception:#возможно лишнее так как таблица будет в БД
                    QMessageBox.information(self, 'Ошибка', 'Нет данных о пользователе. Проверьте правильность введенных данных')
                conn.commit()
    #регистрация пользователя
    def reg(self):
        self.new = RegWin()
        self.new.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    mywin = AutoriseWin()
    mywin.show()
    sys.exit(app.exec_())