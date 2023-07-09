import sqlite3
from regwin import Ui_RegWin
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit
from SQliteManager import DatabaseManager

class RegWin(QWidget):
    def __init__(self):
        super(RegWin, self).__init__()
        self.ui = Ui_RegWin()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.registr)



    def registr(self):
        #проверка сток на пустоту
        lineEdits = self.findChildren(QLineEdit)
        text = ''
        for lineEdit in lineEdits:
            if not lineEdit.text():
                print(f'Заполните {lineEdit.objectName()}')
                text = f'{text}Заполните все поля!\n'
        if text:
            QMessageBox.information(
                self, 'Внимание', text)
        else:
            flag = self.passw_check(self.ui.password_value.text())
            if flag:
                self.password = self.ui.password_value.text()
                self.write_data()
            else:
                QMessageBox.information(self, 'Ошибка','Пароль должен состоять из не менее чем 8 симоволов, содержать заглавные и строчные буквы и цифры!')
    def write_data(self):
        #записываем значения в БД
        with DatabaseManager("mydb.db") as conn:
            if conn:
                cur = conn.cursor()
                sql_query = "INSERT INTO users VALUES (?, ?, ?, ?, ?);"
                sql_data = (self.ui.name.text(), self.ui.birth_date.text(), self.ui.otdel_num.text(),
                            self.ui.username_value.text(), self.password)
                print(sql_data)
                try:
                    cur.execute(sql_query, sql_data)
                    QMessageBox.information(self, 'Успешно', 'Регистрация успешно завершена!')
                #Обрабатывается исключение отсутствия таблицы в базе данных
                except sqlite3.OperationalError:
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

    def passw_check(self, data):
        return not (len(data) < 8 or
                    data.isdigit() or
                    data.isalpha() or
                    data.islower() or
                    data.isupper()) \
            and data.isalnum()



