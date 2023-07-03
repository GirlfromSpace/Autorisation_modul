import sys
import hashlib
from auth import Ui_autorisation
from PyQt5.QtWidgets import QApplication, QWidget
from SQliteManager import DatabaseManager

class AutoriseWin(QWidget):
    def __init__(self):
        super(AutoriseWin, self).__init__()
        self.ui = Ui_autorisation()
        self.ui.setupUi(self)
        # кнопка входа
        self.ui.login_btn.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.username_value, self.ui.password_value]

    def auth(self):
        with DatabaseManager("mydb.db") as conn:
            if conn:
                cur = conn.cursor()
                sql_query = "SELECT * FROM users WHERE username == (?)"
                sql_data = self.ui.username_value
                cur.fetchall(sql_query, sql_data)
                print(sql_query)
                conn.commit()

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywin = AutoriseWin()
    mywin.show()
    sys.exit(app.exec_())