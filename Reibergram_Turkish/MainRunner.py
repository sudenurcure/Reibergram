import sys
import os
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    # Create a directory to store all documents
    if not os.path.exists("Tüm Belgeler"):
        os.makedirs("Tüm Belgeler")

    data_entries = []
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
