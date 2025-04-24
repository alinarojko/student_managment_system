import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, \
            QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create Widgets, line 1
        distance_label = QLabel("Distance: ")
        self.distance_edit = QLineEdit()
        self.metric = QComboBox()
        self.metric.addItems(['Metric (km)', 'Imperial (miles)'])

        # Create Widgets, line 2
        time_label = QLabel("Time (hours): ")
        self.time_edit = QLineEdit()

        # Create Button, line 3
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to the layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit, 0, 1)
        grid.addWidget(self.metric, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 1)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_edit.text())
        time = float(self.time_edit.text())

        speed = distance / time

        if self.metric.currentText() == "Metric (km)":
            unit = "km/h"
            self.output_label.setText(f"The average speed is {speed} {unit}")
        if self.metric.currentText() == "Imperial (miles)":
            unit = "miles/hour"
            self.output_label.setText(f"The average speed is {speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())

