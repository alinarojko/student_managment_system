from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout,\
                            QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem

from PyQt6.QtGui import QAction
import sqlite3
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        # Create Widgets
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        # Add dropdow items for Help and File menu
        add_student_action = QAction("Add Student")
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About")
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        # Add table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)



    # Add data to the table using SQLite from db file
    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM student")
        self.table.setRowCount(0)
        for row_number , row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        connection.close()





app = QApplication(sys.argv)
main_window = MainWindow()
MainWindow.show()
sys.exit(app.exec())