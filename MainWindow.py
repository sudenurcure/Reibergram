from DataWord import DataEntryWindow
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer
from reportlab.lib.pagesizes import letter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("REIBERGRAM")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        label = QLabel("REIBERGRAM\nPrepared by: Sude Nur Cüre")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Create a timer to close the main window and show the data entry window
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_and_show_data_entry)
        self.timer.start(4000)  # Close after 4 seconds

    def close_and_show_data_entry(self):
        self.timer.stop()  # Stop the timer
        self.close()  # Close the main window
        self.data_entry_window = DataEntryWindow()
        self.data_entry_window.show()
