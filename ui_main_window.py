from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLayout,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
import res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 400)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(2, 3, 68, 1), stop:1 rgba(40, 184, 213, 1));"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(25, -1, 25, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 15)
        self.pushButton_git = QPushButton(self.centralwidget)
        self.pushButton_git.setObjectName("pushButton_git")
        self.pushButton_git.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 14pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(
            ":/icon/logo_icons/git-repository.svg",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pushButton_git.setIcon(icon)
        self.pushButton_git.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_git)

        self.pushButton_settings = QPushButton(self.centralwidget)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.pushButton_settings.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 14pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(
            ":/icon/logo_icons/setting.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.pushButton_settings.setIcon(icon1)
        self.pushButton_settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_settings)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 16pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile(
            ":/icon/logo_icons/snake_logo.svg",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pushButton_1.setIcon(icon2)
        self.pushButton_1.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 16pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon3 = QIcon()
        icon3.addFile(
            ":/icon/logo_icons/pong_logo.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 16pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon4 = QIcon()
        icon4.addFile(
            ":/icon/logo_icons/container.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 16pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon5 = QIcon()
        icon5.addFile(
            ":/icon/logo_icons/pacman.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 7px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "font-family: Tahoma, sans-serif;\n"
            "font-weight: bold;\n"
            "font-size: 16pt\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 40);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 70);\n"
            "}"
        )
        icon6 = QIcon()
        icon6.addFile(
            ":/icon/logo_icons/barrel.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "GameUniverse", None)
        )
        self.pushButton_git.setText(
            QCoreApplication.translate("MainWindow", "GiT", None)
        )
        self.pushButton_settings.setText(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
        self.pushButton_1.setText(
            QCoreApplication.translate("MainWindow", " SNAKE", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", " PONG", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", " CONTAINER LEAP", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", " PAC-MAN", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", " DONKEY KONG", None)
        )

    # retranslateUi
