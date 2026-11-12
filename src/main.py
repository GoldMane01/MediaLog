import sys
from PySide6 import QtWidgets
from views.main_view import MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainView()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
