"""This module all the views of the application"""
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """The Main Window of the application"""
    def __init__(self):
        """Main Window's constructor"""
        super().__init__()
        self.setWindowTitle("Contacts")
        self.setFixedSize(QSize(600, 300))
        self.show()