import requests
import design
from sys import exit as e
# import keyboard as kb
from PySide2.QtWidgets import (QMainWindow,
                               QLineEdit,
                               QApplication,
                               QLabel,
                               QPushButton,
                               QGraphicsView)
from PySide2 import QtWebEngineWidgets as WebEngine
from PySide2 import QtGui, QtCore

class MainWindow(QMainWindow, design.Ui_MainWindow):
    tabs = 1

    def __init__(self):

        super().__init__()
        self.setupUi(self)

        # noinspection PyArgumentList
        self.setGeometry(QtCore.QRect((QApplication.desktop().width() - self.geometry().width()) / 2, 40, self.geometry().width(), self.geometry().height()))
        # noinspection PyArgumentList
        self.setMaximumSize(QtCore.QSize(1024, 650))

        self.label = QLabel(self.centralwidget)
        # noinspection PyArgumentList
        self.label.setGeometry(QtCore.QRect(437, 83, 150, 49))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # noinspection PyArgumentList
        self.url = QLineEdit(self.centralwidget)
        # noinspection PyArgumentList
        self.url.setGeometry(QtCore.QRect(182, 150, 660, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.url.setFont(font)
        self.url.setStyleSheet("border: 1px solid #e1e4ff")
        self.url.setText("")
        self.url.setObjectName("url")
        # noinspection PyArgumentList
        self.search = QPushButton(self.centralwidget)
        # noinspection PyArgumentList
        self.search.setGeometry(QtCore.QRect(847, 142, 53, 53))
        self.search.setStyleSheet("border-radius: 26px;\n"
                                  "border: 1px solid #000;\n"
                                  "image: url(:/search/src.png);\n"
                                  "")
        self.search.setText("")
        self.search.setObjectName("search")
        # noinspection PyArgumentList
        self.label = QLabel(self.centralwidget)
        # noinspection PyArgumentList
        self.label.setGeometry(QtCore.QRect(437, 83, 150, 49))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText('Input URL:')

        # noinspection PyArgumentList
        self.address = QLineEdit(self.centralwidget)
        self.view = QGraphicsView(self.centralwidget)
        self.address.setVisible(False)
        self.view.setVisible(False)

        self.count.setText(str(self.tabs))

        # noinspection PyUnresolvedReferences
        self.search.clicked.connect(self.searcher)
        self.settings_button.clicked.connect(self.settings)

        # animations
        self.anim_label = QtCore.QPropertyAnimation(self.label, b'pos')
        self.anim_settings = QtCore.QPropertyAnimation(self.settings_button, b'pos')

        self.show()

    def searcher(self):
        valid = ['http:', 'https:'] # допустимые значения в адресе
        url = self.url.toPlainText() # получение URL из строки ввода
        # проверка адреса на валидность
        for i in valid:
            if i in url:
                break
            elif i == 'https:':
                url = 'http://' + url


        we = WebEngine.QWebEngineView()
        we.load(url)

        response = requests.get(url)
        sc = response.status_code
        if sc == 200:
            pass
        elif sc == 404:
            pass

        self.view.setViewport(we)

        self.label.setVisible(False)
        self.url.setVisible(False)
        self.search.setVisible(False)

        # noinspection PyArgumentList
        self.address.setGeometry(QtCore.QRect(2, 53, 1024, 36))
        self.address.setStyleSheet("border-radius: 18px; border: 1px solid pink")
        self.address.setObjectName("address")
        # noinspection PyArgumentList
        self.view.setGeometry(QtCore.QRect(0, 90, 1024, 560))
        self.view.setStyleSheet("border: 1px rgb(235, 255, 252);")
        self.view.setObjectName("view")
        self.address.show()
        self.view.show()

    def new_tab(self):
        pass

    def settings(self):
        pass

    def resizeEvent(self, event):
        ratio = self.width() / self.height()
        # print(width / height)
        if self.width() == 1024 and self.height()== 650:
            # noinspection PyArgumentList
            self.anim_label.setStartValue(QtCore.QPoint(self.label.pos()))
            self.anim_label.setEndValue(QtCore.QPoint(437, 83))
            self.anim_label.setDuration(1000)
            self.anim_label.setEasingCurve(QtCore.QEasingCurve.Linear)
            self.anim_label.start()
            # noinspection PyArgumentList
            self.anim_settings.setStartValue(self.settings_button.pos())
            self.anim_settings.setEndValue(QtCore.QPoint(971, -1))
            self.anim_settings.setDuration(1000)
            self.anim_settings.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.anim_settings.start()
            # noinspection PyArgumentList
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 921, 51))
            # noinspection PyArgumentList
            self.url.setGeometry(QtCore.QRect(182, 150, 660, 40))
            # noinspection PyArgumentList
            self.search.setGeometry(QtCore.QRect(847, 142, 53, 53))
        elif 1.4 <= ratio <= 1.5:
            pass
        elif 1.3 <= ratio <= 1.35:
            # noinspection PyArgumentList
            self.anim_label.setStartValue(QtCore.QPoint(437, 83))
            self.anim_label.setEndValue(QtCore.QPoint(347, 83))
            self.anim_label.setDuration(1000)
            self.anim_label.setEasingCurve(QtCore.QEasingCurve.Linear)
            self.anim_label.start()
            # noinspection PyArgumentList
            self.anim_settings.setStartValue(QtCore.QPoint(971, -1))
            self.anim_settings.setEndValue(QtCore.QPoint(792, -1))
            self.anim_settings.setDuration(1000)
            self.anim_settings.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.anim_settings.start()
            # noinspection PyArgumentList
            self.horizontalLayout.setGeometry(QtCore.QRect(50, 0, 742, 51))
            # noinspection PyArgumentList
            self.url.setGeometry(QtCore.QRect(92.5, 150, 660, 40))
            # noinspection PyArgumentList
            self.search.setGeometry(QtCore.QRect(759, 142, 53, 53))
            # self.setGeometry(QtCore.QRect((QApplication.desktop().width() - 845) // 2, 40, 845, 650))

if __name__ == '__main__':
    app = QApplication()
    mw = MainWindow()
    e(app.exec_())
