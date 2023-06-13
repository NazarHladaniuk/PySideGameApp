import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QPainter
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class SnakeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snake")
        self.setGeometry(300, 300, 400, 400)
        self.setFocusPolicy(Qt.StrongFocus)

        self.timer_interval = 100
        self.board_size = 20
        self.snake_size = 20
        self.score = 0

        self.snake = [(2, 2), (3, 2), (4, 2)]
        self.food = self.generate_food()

        self.direction = Direction.RIGHT

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(self.timer_interval)

        # Add restart button
        self.restart_button = QPushButton("Restart", self)
        self.restart_button.setGeometry(160, 180, 80, 30)
        self.restart_button.hide()
        self.restart_button.clicked.connect(self.restart_game)

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw the snake
        painter.setBrush(Qt.green)
        for segment in self.snake:
            x, y = segment
            painter.drawRect(
                x * self.snake_size,
                y * self.snake_size,
                self.snake_size,
                self.snake_size,
            )

        # Draw the food
        painter.setBrush(Qt.red)
        x, y = self.food
        painter.drawRect(
            x * self.snake_size,
            y * self.snake_size,
            self.snake_size,
            self.snake_size,
        )

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif key == Qt.Key_Down and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif key == Qt.Key_Left and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif key == Qt.Key_Right and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def update_game(self):
        head = self.snake[-1]
        x, y = head

        if self.direction == Direction.UP:
            y -= 1
        elif self.direction == Direction.DOWN:
            y += 1
        elif self.direction == Direction.LEFT:
            x -= 1
        elif self.direction == Direction.RIGHT:
            x += 1

        # Check collision with the snake's body
        if (x, y) in self.snake[:-1]:
            self.game_over()

        # Check collision with the walls
        if x < 0 or x >= self.board_size or y < 0 or y >= self.board_size:
            self.game_over()

        # Check collision with food
        if (x, y) == self.food:
            self.snake.append(self.food)
            self.food = self.generate_food()
            self.score += 1
            self.update_score()

            # Increase the speed of the snake
            self.timer_interval -= 1
            self.timer.start(self.timer_interval)

        else:
            # Move the snake
            self.snake.pop(0)
            self.snake.append((x, y))

        self.update()

    def generate_food(self):
        while True:
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            if (x, y) not in self.snake:
                return x, y

    def update_score(self):
        self.statusBar().showMessage("Score: {}".format(self.score))

    def game_over(self):
        self.timer.stop()
        self.statusBar().showMessage(
            "Game Over. Final Score: {}".format(self.score)
        )
        self.restart_button.show()

    def restart_game(self):
        self.timer_interval = 100
        self.score = 0
        self.snake = [(2, 2), (3, 2), (4, 2)]
        self.food = self.generate_food()
        self.direction = Direction.RIGHT
        self.restart_button.hide()
        self.timer.start(self.timer_interval)
        self.update_score()

        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SnakeWindow()
    sys.exit(app.exec())
