import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PPT")

        delete_button = QtWidgets.QPushButton("Delete", self)
        delete_button.move(0, 0)
        delete_button.clicked.connect(self.close)
        
        language_button = QtWidgets.QPushButton("Language", self)
        language_button.move(0, 30)
        language_button.clicked.connect(self.close)
        
        celendar_button = QtWidgets.QPushButton("Celendar", self)
        celendar_button.move(0, 60)
        celendar_button.clicked.connect(self.close)

        cancel_button = QtWidgets.QPushButton("Cancel", self)
        cancel_button.move(100, 0)
        cancel_button.clicked.connect(self.close)
        
        report_button = QtWidgets.QPushButton("Report", self)
        report_button.move(100, 30)
        report_button.clicked.connect(self.close)
        
        teleport_button = QtWidgets.QPushButton("Visit our website", self)
        teleport_button.move(100, 60)
        teleport_button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
