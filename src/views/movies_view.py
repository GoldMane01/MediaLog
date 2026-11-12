from PySide6 import QtWidgets, QtCore, QtGui
from pathlib import Path

class MoviesView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_back = QtWidgets.QPushButton("Volver")
        self.button_godzilla = QtWidgets.QPushButton("Godzilla")

        title = QtWidgets.QLabel("Biblioteca de películas")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button_back)
        layout.addWidget(self.button_godzilla)
        layout.addWidget(title)


class MovieDetailView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_back = QtWidgets.QPushButton("Volver")

        self.poster = QtWidgets.QLabel()
        self.poster.setFixedSize(240, 360)
        self.poster.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.poster.setStyleSheet(
            "background-color: #252525; border: 1px solid #444;"
        )

        project_dir = Path(__file__).resolve().parents[2]
        poster_path = project_dir / "tests" / "godzilla.jpeg"

        pixmap = QtGui.QPixmap(str(poster_path))

        if not pixmap.isNull():
            self.poster.setPixmap(
                pixmap.scaled(
                    self.poster.size(),
                    QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                    QtCore.Qt.TransformationMode.SmoothTransformation
                )
            )
        else:
            self.poster.setText("Póster no encontrado")

        self.title = QtWidgets.QLabel("ゴジラ")

        self.alternative_titles = QtWidgets.QLabel(
            "<b>ES: Japón bajo el terror del monstruo</b> <br>"
            "<b>EN: Godzilla</b>"
        )

        self.year = QtWidgets.QLabel("<b>Año:</b> 1954")
        self.duration = QtWidgets.QLabel("<b>Duración:</b> 96 minutos")
        self.country = QtWidgets.QLabel("<b>País:</b> Japón")
        self.director = QtWidgets.QLabel("<b>Director:</b> Ishirō Honda")

        self.cast = QtWidgets.QLabel(
            "<b>Cast:</b> Akira Takarada, Momoko Kōchi, Akihiko Hirata"
        )
        self.cast.setWordWrap(True)

        self.genres = QtWidgets.QLabel(
            "<b>Género:</b> Ciencia ficción, Terror, Kaiju"
        )

        # Notas personales
        notes_title = QtWidgets.QLabel("<b>Notas personales</b>")

        self.notes = QtWidgets.QTextEdit()
        self.notes.setPlaceholderText(
            "Notas..."
        )
        self.notes.setMinimumHeight(120)

        self.title.setStyleSheet("font-size: 28px; font-weight: bold;")
        self.alternative_titles.setStyleSheet("font-size: 14px;")
        self.year.setStyleSheet("font-size: 18px;")
        self.duration.setStyleSheet("font-size: 18px;")
        self.country.setStyleSheet("font-size: 18px;")
        self.director.setStyleSheet("font-size: 18px;")
        self.cast.setStyleSheet("font-size: 18px;")
        self.genres.setStyleSheet("font-size: 18px;")

        # Seguimiento personal
        self.watched = QtWidgets.QCheckBox("Vista")

        self.rating = QtWidgets.QDoubleSpinBox()
        self.rating.setRange(0, 10)
        self.rating.setSingleStep(0.5)
        self.rating.setValue(0)

        # Distribución de la información
        info_layout = QtWidgets.QVBoxLayout()
        info_layout.addWidget(self.title)
        info_layout.addWidget(self.alternative_titles)
        info_layout.addSpacing(15)
        info_layout.addWidget(self.year)
        info_layout.addWidget(self.duration)
        info_layout.addWidget(self.country)
        info_layout.addWidget(self.director)
        info_layout.addWidget(self.cast)
        info_layout.addWidget(self.genres)
        info_layout.addSpacing(15)
        info_layout.addSpacing(15)
        info_layout.addWidget(self.watched)
        info_layout.addWidget(self.rating)
        info_layout.addWidget(self.notes)
        info_layout.addSpacing(15)
        info_layout.addStretch()

        # Póster + información
        content_layout = QtWidgets.QHBoxLayout()
        content_layout.addWidget(
            self.poster,
            alignment=QtCore.Qt.AlignmentFlag.AlignTop |
                    QtCore.Qt.AlignmentFlag.AlignLeft
        )
        content_layout.addSpacing(20)
        content_layout.addLayout(info_layout)
        content_layout.addStretch()

        # Layout principal
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.button_back)
        main_layout.addLayout(content_layout)