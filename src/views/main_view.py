from PySide6 import QtWidgets
from views.movies_view import MoviesView, MovieDetailView
from views.home_view import HomeView

class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MediaLog")

        self.home_view = HomeView()
        self.movies_view = MoviesView()
        self.movie_detail_view = MovieDetailView()

        self.stack = QtWidgets.QStackedWidget()
        self.stack.addWidget(self.home_view)
        self.stack.addWidget(self.movies_view)
        self.stack.addWidget(self.movie_detail_view)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.stack)

        self.home_view.button_movies.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.movies_view)
        )

        self.movies_view.button_back.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.home_view)
        )

        self.movie_detail_view.button_back.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.movies_view)
        )

        self.movies_view.button_godzilla.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.movie_detail_view)
        )