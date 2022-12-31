"""Module that manage the database"""
import sys
from time import sleep

from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QMessageBox


class Database:
    """Database"""
    def __init__(self, database_driver: str, database_name: str) -> None:
        """
        Database's constructor
        :param database_driver: The database's name for the connnection
        :param database_name: The database's driver for the connection
        """
        self.database_connection: QSqlDatabase = QSqlDatabase(database_driver)
        self.database_connection.setDatabaseName(database_name)

    def open_connection(self) -> None:
        """Open the connection to the database"""
        if not self.database_connection.open():
            QMessageBox.warning(None, "Failed Connection", f"The connection to the database fialed : {self.database_connection.lastError().text()}")
            sleep(5000)
            sys.exit(1)
