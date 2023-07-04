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
        with DatabaseManager("mydb.db") as conn:
            if conn:
                cur = conn.cursor()
                sql_query = "SELECT * FROM users WHERE username == ?"
                sql_data = self.ui.username_value
                try:
                    query = cur.fetchall(sql_query, sql_data)
                    print(query)
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