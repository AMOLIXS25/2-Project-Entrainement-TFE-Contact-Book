"""This module all the views of the application"""
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QTableView, QAbstractItemView, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """The Main Window of the application"""

    def __init__(self):
        """Main Window's constructor"""
        super().__init__()
        self.setWindowTitle("Contacts")
        self.setFixedSize(QSize(600, 300))
        self.setup_ui()
        self.show()

    def setup_ui(self):
        """Method that setup all widgets and layout of the application"""
        # Create the table view widget
        self.table: QTableView = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows) # Cela nous assure que lorsqu'un utilisateur clique sur une donnée de la table cela sélectionne la ligne entière.
        # Create Buttons
        self.add_contact_button: QPushButton = QPushButton("Add...")
        self.delete_contact_button: QPushButton = QPushButton("Delete")
        self.clear_all_contact_button: QPushButton = QPushButton("Clear All")
        self.setup_layouts()

    def setup_layouts(self):
        """Method that setup all layouts of the application"""
        self.main_layout_container: QWidget = QWidget()
        main_layout: QHBoxLayout = QHBoxLayout()
        main_layout.addWidget(self.table)
        buttons_layout: QVBoxLayout = QVBoxLayout()
        buttons_layout.addWidget(self.add_contact_button)
        buttons_layout.addWidget(self.delete_contact_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.clear_all_contact_button)
        main_layout.addLayout(buttons_layout)
        self.main_layout_container.setLayout(main_layout)
        self.setCentralWidget(self.main_layout_container)
