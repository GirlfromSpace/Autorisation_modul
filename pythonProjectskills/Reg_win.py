import sqlite3

from regwin import Ui_RegWin
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from SQliteManager import DatabaseManager

class RegWin(QWidget):
    def __init__(self):
        super(RegWin, self).__init__()
        self.ui = Ui_RegWin()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.registr)
        if self.ui.password_value.text():
        self.password = self.ui.password_value

    def registr(self):
        #записываем значения в БД
        with DatabaseManager("mydb.db") as conn:
            if conn:
                cur = conn.cursor()
                sql_query = "INSERT INTO users VALUES (?, ?, ?, ?, ?);"
                sql_data = (self.ui.name.text(), self.ui.birth_date.text(), self.ui.otdel_num.text(), self.ui.username_value.text(), self.ui.password_value.text())
                print(sql_data)
                try:
                    cur.execute(sql_query, sql_data)
                    QMessageBox.information(self, 'Успешно','Регистрация успешно завершена!')
                except NameError:
                    cur.execute("""
                        CREATE TABLE users (
                            name VARCHAR(20) PRIMARY KEY,
                            birth_date INTEGER,
                            otdel_num INTEGER,
                            username VARCHAR(20),
                            hashed_pass VARCHAR(20)
                     );
                        """)
                    cur.execute(sql_query, sql_data)
                    QMessageBox.information(self, 'Успешно', 'Регистрация успешно завершена!')
                except sqlite3.IntegrityError:
                    QMessageBox.information(self, 'Ошибка', 'Такой пользователь уже есть в системе!')
                conn.commit()


