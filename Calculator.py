import sys
from PyQt5.QtWidgets import QApplication
from Backend.Action import Calculator 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())