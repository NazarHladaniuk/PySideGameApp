import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QMainWindow

from games.pong import PongWidget
from games.snake import SnakeWindow
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.snake_window = None
        self.pong_window = None

        self.ui.pushButton_git.clicked.connect(self.openGitHubPage)
        self.ui.pushButton_1.clicked.connect(self.openSnakeWindow)
        self.ui.pushButton_2.clicked.connect(self.openPongWindow)

    def openGitHubPage(self):
        url = QUrl("https://github.com/NazarHladaniuk")
        QDesktopServices.openUrl(url)

    def openSnakeWindow(self):
        if self.snake_window is None:
            self.snake_window = SnakeWindow()
        self.snake_window.show()

    def openPongWindow(self):
        if self.pong_window is None:
            self.pong_window = PongWidget()
        self.pong_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
