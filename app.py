"""The main module of the application"""
from PySide6.QtWidgets import QApplication

from views import MainWindow

if __name__ == '__main__':
    app: QApplication = QApplication()
    main_window: MainWindow = MainWindow()
    app.exec()
