import requests
import design
from sys import exit as e
from PySide2.QtWidgets import (QMainWindow,
                               QLineEdit,
                               QApplication,
                               QLabel,
                               QPushButton,
                               QGraphicsView)
from PySide2 import QtWebEngineWidgets as WebEngine
from PySide2 import QtGui, QtCore
from threading import Thread as Th
from time import sleep as sl
import keyboard

class MainWindow(QMainWindow, design.Ui_MainWindow):
    tabs = {}
    ID = 0
    x_last = 53

    width = 0
    height = 0

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

        # BUTTONS
        # noinspection PyUnresolvedReferences
        self.search.clicked.connect(self.searcher)
        self.settings_button.clicked.connect(self.settings)
        self.addTab.clicked.connect(self.new_tab)

        # ANIMATIONS
        self.anim_label = QtCore.QPropertyAnimation(self.label, b'pos')
        self.anim_settings = QtCore.QPropertyAnimation(self.settings_button, b'pos')

        keyboard.on_press(lambda i: self.on_press(e))

        self.new_tab()

    def searcher(self):
        valid = ['http:', 'https:'] # допустимые значения в адресе
        url = self.url.text() # получение URL из строки ввода
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

    # noinspection PyAttributeOutsideInit
    def new_tab(self):
        tab = QLabel(self.centralwidget)
        if self.tabs.__len__() == 0:
            tab.setText('Welcome!')
        else:
            tab.setText('')
        tab.setStyleSheet('border: 1px solid #289591; border-top-right-radius: 30')
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(15)
        tab.setFont(font)

        # кнопка закрытия вкладки
        # noinspection PyArgumentList,PyAttributeOutsideInit
        self.btn_cls_tab = QPushButton(self.centralwidget)
        # noinspection PyArgumentList
        self.btn_cls_tab.setGeometry(QtCore.QRect(self.x_last + 93, 24, 18, 18))
        self.btn_cls_tab.setStyleSheet(
        'border-radius: 9px;\n'
        'border: 1px solid #000;\n'
        'image: url(:/btnClsTab/btnClsTab.png);\n'
        )
        self.btn_cls_tab.hide()

        # анимация новых вкладок
        # позиция вкладки
        # self.tabs_anim_pos = QtCore.QPropertyAnimation(tab, b'pos')
        # # noinspection PyArgumentList
        # self.tabs_anim_pos.setStartValue(QtCore.QPoint(53, 14))
        # # noinspection PyArgumentList
        # self.tabs_anim_pos.setEndValue(QtCore.QPoint(self.x_last, 14))
        # self.tabs_anim_pos.setDuration(800)
        # self.tabs_anim_pos.setEasingCurve(QtCore.QEasingCurve.InOutQuad)

        tab.setGeometry(QtCore.QRect(self.x_last, 14, 0, 0))

        # размер вкладки
        self.tabs_anim_size = QtCore.QPropertyAnimation(tab, b'size')
        # noinspection PyArgumentList
        self.tabs_anim_size.setStartValue(QtCore.QSize(2, 33))
        # noinspection PyArgumentList
        self.tabs_anim_size.setEndValue(QtCore.QSize(120, 33))
        self.tabs_anim_size.setDuration(800)
        self.tabs_anim_size.setEasingCurve(QtCore.QEasingCurve.InOutQuad)

        # позиция кнопки новой вкладки
        self.addTab_anim = QtCore.QPropertyAnimation(self.addTab, b'pos')
        self.addTab_anim.setStartValue(self.addTab.pos())
        # noinspection PyArgumentList
        self.addTab_anim.setEndValue(QtCore.QPoint(
            self.x_last + 123,
            self.addTab.pos().y())
        )
        self.addTab_anim.setDuration(800)
        self.addTab_anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)

        # self.tabs_anim_pos.start()
        self.tabs_anim_size.start()
        self.addTab_anim.start()

        # укоротим текст, если он длиннее, чем нужно
        if tab.text().__len__() > 8:
            tab.setText(self.tab.text()[:6])

        def btn():
            sl(2)
            self.btn_cls_tab.show()

        th = Th(target = btn, args = ())
        th.start()

        # добавим новую вкладку в список вкладок
        self.tabs[self.ID] = (tab, self.btn_cls_tab)

        self.count.setText(str(self.tabs.__len__()))

        self.show()

        self.x_last += 120

        del th

    def settings(self):
        pass

    # noinspection PyArgumentList
    def resizeEvent(self, event):

        # settings button animation
        self.anim_settings.setStartValue(self.settings_button.pos())
        self.anim_settings.setEndValue(QtCore.QPoint(
            self.geometry().width() - 53,
            self.settings_button.pos().y())
        )
        self.anim_settings.setDuration(0.1)
        self.anim_settings.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.anim_settings.start()

        # label animation
        self.anim_label.setStartValue(self.label.pos())
        self.anim_label.setEndValue(QtCore.QPoint(
            (self.geometry().width() - 150) // 2,
            self.label.pos().y())
        )
        self.anim_label.setDuration(0.1)
        self.anim_label.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.anim_label.start()

        # search string move
        self.url.setGeometry(
            QtCore.QRect(
                (self.geometry().width() - 660) // 2 - 20,
                self.url.pos().y(),
                self.url.geometry().width(),
                self.url.geometry().height()
            )
        )

        # search button move
        self.search.setGeometry(
            QtCore.QRect(
                self.url.pos().x() + self.url.geometry().width() + 5,
                self.search.pos().y(),
                self.search.size().width(),
                self.search.size().height()
            )
        )

    # noinspection PyUnusedLocal
    def on_press(self, event):
        if keyboard.is_pressed('enter'):
            self.searcher()


if __name__ == '__main__':
    app = QApplication()
    mw = MainWindow()
    e(app.exec_())
