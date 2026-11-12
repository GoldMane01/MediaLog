from PySide6 import QtWidgets


class HomeView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_games = QtWidgets.QPushButton("Videojuegos")
        self.button_movies = QtWidgets.QPushButton("Películas")
        self.button_shows = QtWidgets.QPushButton("Series")
        self.button_books = QtWidgets.QPushButton("Libros")

        layout = QtWidgets.QGridLayout(self)

        layout.addWidget(self.button_games, 0, 0)
        layout.addWidget(self.button_movies, 0, 1)
        layout.addWidget(self.button_shows, 1, 0)
        layout.addWidget(self.button_books, 1, 1)