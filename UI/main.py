from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


# фронт-энд
# не трогать
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.show()
        self.UIElements()

    # можно трогать
    def UIElements(self):
        acmp_ = QLabel("acmp-\nsolver", self)
        acmp_.setFont(QFont('Times', 20))
        acmp_.setGeometry(27, 23, 271, 128)
        acmp_.setStyleSheet("letter-spacing:2px;font-weight:bold;")

        account_label = QLabel("аккаунт", self)
        account_label.setFont(QFont('Times', 20))
        account_label.setGeometry(30, 197, 320, 54)
        account_label.setStyleSheet("letter-spacing:2px;")

        nickname_field = QLineEdit("", self)
        nickname_field.setPlaceholderText("Никнейм")
        nickname_field.setFont(QFont('Times', 20))
        nickname_field.setGeometry(30, 268, 320, 56)
        nickname_field.setStyleSheet("letter-spacing:2px;")

        password_field = QLineEdit("", self)
        password_field.setPlaceholderText("Пароль")
        password_field.setFont(QFont('Times', 20))
        password_field.setGeometry(30, 341, 320, 56)
        password_field.setStyleSheet("letter-spacing:2px;")

        log_label = QLabel("Лог:", self)
        log_label.setFont(QFont('Times', 15))
        log_label.setGeometry(30, 443, 300, 40)
        log_label.setStyleSheet("letter-spacing:2px;font-weight:500;")

        clientsatus_label = QLabel("Клиент Запущен", self)
        clientsatus_label.setFont(QFont('Times', 12))
        clientsatus_label.setGeometry(30, 475, 300, 22)
        clientsatus_label.setStyleSheet("letter-spacing:2px;font-weight:lighter;")
        if client_status:
            clientsatus_label.setText("Клиент Запущен")
        else:
            clientsatus_label.setText("Клиент Отключен")

        completed_label = QLabel("Решено " + str(completed) + " задач", self)
        completed_label.setFont(QFont('Times', 12))
        completed_label.setGeometry(30, 496, 300, 21)
        completed_label.setStyleSheet("letter-spacing:2px;font-weight:lighter;")

        notfound_label = QLabel("Не найдено: " + " ".join(not_found), self)
        notfound_label.setFont(QFont('Times', 12))
        notfound_label.setGeometry(30, 518, 300, 22)
        notfound_label.setStyleSheet("letter-spacing:2px;font-weight:lighter;")

        errors_label = QLabel("Ошибки", self)
        errors_label.setFont(QFont('Times', 12))
        errors_label.setGeometry(30, 539, 300, 21)
        errors_label.setStyleSheet("letter-spacing:2px;font-weight:lighter;")
        if errors:
            errors_label.setText("Ошибки есть")
        else:
            errors_label.setText("Ошибок нет")

        minimize_button = QPushButton("-", self)
        minimize_button.setFont(QFont('Times', 20))
        minimize_button.setGeometry(702, 42, 32, 32)
        minimize_button.setStyleSheet("border-radius : 16;border : 2px solid black;")

        close_button = QPushButton("x", self)
        close_button.setFont(QFont('Times', 10))
        close_button.setGeometry(739, 42, 32, 32)
        close_button.setStyleSheet("border-radius : 16;border : 2px solid black;")

        exercises_label = QLabel("задачи", self)
        exercises_label.setFont(QFont('Times', 20))
        exercises_label.setGeometry(451, 197, 319, 54)
        exercises_label.setStyleSheet("letter-spacing:2px;")

        choose_exercise = QPushButton("Решить задачу", self)
        choose_exercise.setFont(QFont('Times', 10))
        choose_exercise.setGeometry(450, 268, 160, 56)
        choose_exercise.setStyleSheet("letter-spacing:2px;font-weight:lighter")

        choose_topic = QPushButton("Решить тему", self)
        choose_topic.setFont(QFont('Times', 10))
        choose_topic.setGeometry(609, 268, 160, 56)
        choose_topic.setStyleSheet("letter-spacing:2px;font-weight:lighter")

        answer_textfield = QLineEdit("", self)
        answer_textfield.setPlaceholderText("Поиск")
        answer_textfield.setFont(QFont('Times', 10))
        answer_textfield.setGeometry(451, 341, 319, 56)
        answer_textfield.setStyleSheet("letter-spacing:2px;font-weight:lighter")

        # короче, копаться в твоем коде я не буду, поэтому сам делай вывод правильного названия
        chosen_exercise = QLabel("выбранная задача: " + exercise_name, self)
        chosen_exercise.setFont(QFont('Times', 7))
        chosen_exercise.setGeometry(451, 415, 319, 58)
        chosen_exercise.setStyleSheet("letter-spacing:2px;")

        start_button = QPushButton("Запуск", self)
        start_button.setFont(QFont('Times', 10))
        start_button.setGeometry(451, 497, 349, 103)
        start_button.setStyleSheet("letter-spacing:2px;font-weight:lighter")

        start_button.show()
        chosen_exercise.show()
        answer_textfield.show()
        choose_topic.show()
        choose_exercise.show()
        exercises_label.show()
        close_button.show()
        close_button.clicked.connect(self.closeApp)
        minimize_button.show()
        minimize_button.clicked.connect(self.minimizeApp)
        clientsatus_label.show()
        errors_label.show()
        notfound_label.show()
        completed_label.show()
        log_label.show()
        password_field.show()
        nickname_field.show()
        account_label.show()
        acmp_.show()

    def closeApp(self):
        self.close()

    def minimizeApp(self):
        window.setWindowState(window.windowState() | Qt.WindowMinimized)


# остальное
not_found = ["144", "123"]
completed = 10
errors = False
client_status = True
exercise_name = "A+B (№1)"


# не трогать
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
