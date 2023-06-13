from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class PongWidget(QWidget):
    def __init__(self, parent=None):
        super(PongWidget, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)

        self.WIDTH, self.HEIGHT = 800, 600
        self.PADDLE_WIDTH, self.PADDLE_HEIGHT = 20, 100
        self.BALL_RADIUS = 7
        self.WINNING_SCORE = 3

        self.paddle_speed = 8
        self.ball_speed = 5

        self.left_paddle_y = self.HEIGHT // 2 - self.PADDLE_HEIGHT // 2
        self.right_paddle_y = self.HEIGHT // 2 - self.PADDLE_HEIGHT // 2
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2
        self.ball_x_vel = self.ball_speed
        self.ball_y_vel = 0
        self.left_score = 0
        self.right_score = 0
        self.winner = None

        self.keys_pressed = set()

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGame)
        self.timer.start(16)

        self.restart_button = QPushButton("Restart")
        self.restart_button.clicked.connect(self.restartGame)
        self.restart_button.hide()

        layout = QVBoxLayout()
        layout.addWidget(self.restart_button)
        self.setLayout(layout)

        self.setFixedSize(self.WIDTH, self.HEIGHT)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), Qt.black)
        painter.setPen(Qt.white)

        # Draw paddles
        painter.drawRect(
            10, self.left_paddle_y, self.PADDLE_WIDTH, self.PADDLE_HEIGHT
        )
        painter.drawRect(
            self.WIDTH - 10 - self.PADDLE_WIDTH,
            self.right_paddle_y,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT,
        )

        # Draw center line
        for i in range(10, self.HEIGHT, self.HEIGHT // 20):
            if i % 2 == 1:
                continue
            painter.drawRect(self.WIDTH // 2 - 5, i, 10, self.HEIGHT // 20)

        # Draw ball
        painter.drawEllipse(
            self.ball_x - self.BALL_RADIUS,
            self.ball_y - self.BALL_RADIUS,
            self.BALL_RADIUS * 2,
            self.BALL_RADIUS * 2,
        )

        # Draw scores
        font = QFont("Arial", 50)
        painter.setFont(font)
        painter.drawText(self.WIDTH // 4 - 50, 50, str(self.left_score))
        painter.drawText(self.WIDTH * 3 // 4 - 50, 50, str(self.right_score))

        # Draw winner message
        if self.winner is not None:
            painter.setFont(QFont("Arial", 30))
            painter.drawText(
                self.WIDTH // 2 - 150, self.HEIGHT // 2 - 50, self.winner
            )
            self.restart_button.show()  # Show restart button when there is a winner
        else:
            self.restart_button.hide()  # Hide restart button if there is no winner

    def updateGame(self):
        # Check if a player has already won
        if self.winner is not None:
            return

        self.ball_x += self.ball_x_vel
        self.ball_y += self.ball_y_vel

        # Check collision with paddles
        if self.ball_x_vel < 0:
            if (
                self.ball_y >= self.left_paddle_y
                and self.ball_y <= self.left_paddle_y + self.PADDLE_HEIGHT
            ):
                if self.ball_x - self.BALL_RADIUS <= 10 + self.PADDLE_WIDTH:
                    self.ball_x_vel *= -1
                    middle_y = self.left_paddle_y + self.PADDLE_HEIGHT // 2
                    difference_in_y = middle_y - self.ball_y
                    reduction_factor = (
                        self.PADDLE_HEIGHT // 2
                    ) / self.ball_speed
                    y_vel = difference_in_y / reduction_factor
                    self.ball_y_vel = -y_vel
        else:
            if (
                self.ball_y >= self.right_paddle_y
                and self.ball_y <= self.right_paddle_y + self.PADDLE_HEIGHT
            ):
                if (
                    self.ball_x + self.BALL_RADIUS
                    >= self.WIDTH - 10 - self.PADDLE_WIDTH
                ):
                    self.ball_x_vel *= -1
                    middle_y = self.right_paddle_y + self.PADDLE_HEIGHT // 2
                    difference_in_y = middle_y - self.ball_y
                    reduction_factor = (
                        self.PADDLE_HEIGHT // 2
                    ) / self.ball_speed
                    y_vel = difference_in_y / reduction_factor
                    self.ball_y_vel = -y_vel

        # Check collision with top/bottom walls
        if (
            self.ball_y - self.BALL_RADIUS <= 0
            or self.ball_y + self.BALL_RADIUS >= self.HEIGHT
        ):
            self.ball_y_vel *= -1

        # Check if ball goes out of bounds
        if self.ball_x < 0:
            self.right_score += 1
            if self.right_score >= self.WINNING_SCORE:
                self.winner = "Right Player Won!"
            else:
                self.resetGame()
        elif self.ball_x > self.WIDTH:
            self.left_score += 1
            if self.left_score >= self.WINNING_SCORE:
                self.winner = "Left Player Won!"
            else:
                self.resetGame()

        self.update()

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())
        self.handleKeyPresses()

    def keyReleaseEvent(self, event):
        self.keys_pressed.discard(event.key())
        self.handleKeyPresses()

    def handleKeyPresses(self):
        if Qt.Key_W in self.keys_pressed and self.left_paddle_y > 0:
            self.left_paddle_y -= self.paddle_speed
        if (
            Qt.Key_S in self.keys_pressed
            and self.left_paddle_y + self.PADDLE_HEIGHT < self.HEIGHT
        ):
            self.left_paddle_y += self.paddle_speed
        if Qt.Key_Up in self.keys_pressed and self.right_paddle_y > 0:
            self.right_paddle_y -= self.paddle_speed
        if (
            Qt.Key_Down in self.keys_pressed
            and self.right_paddle_y + self.PADDLE_HEIGHT < self.HEIGHT
        ):
            self.right_paddle_y += self.paddle_speed

    def resetGame(self):
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2
        self.ball_x_vel = self.ball_speed
        self.ball_y_vel = 0
        self.winner = None

    def restartGame(self):
        self.left_score = 0
        self.right_score = 0
        self.resetGame()
        self.update()


if __name__ == "__main__":
    app = QApplication([])
    window = PongWidget()
    window.show()
    app.exec()
