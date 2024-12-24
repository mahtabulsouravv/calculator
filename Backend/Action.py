from Generated.Calculator import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load The Design
        self.addEvents()  # Call The Method To Connect Events
    
    def addEvents(self):
        # All Events
        self.percentB.clicked.connect(self.parcentClick)
        self.clearB.clicked.connect(self.clearClick)
        self.delB.clicked.connect(self.delClick)
        self.divB.clicked.connect(self.divClick)
        self.sevenB.clicked.connect(self.sevenClick)
        self.eightB.clicked.connect(self.eightClick)
        self.nineB.clicked.connect(self.nineClick)
        self.mulB.clicked.connect(self.mulClick)
        self.fourB.clicked.connect(self.fourClick)
        self.fiveB.clicked.connect(self.fiveClick)
        self.sixB.clicked.connect(self.sixClick)
        self.minusB.clicked.connect(self.minusClick)
        self.oneB.clicked.connect(self.oneClick)
        self.twoB.clicked.connect(self.twoClick)
        self.threeB.clicked.connect(self.threeClick)
        self.plusB.clicked.connect(self.plusClick)
        self.zeroB.clicked.connect(self.zeroClick)
        self.plusminusB.clicked.connect(self.plusminusClick)
        self.decB.clicked.connect(self.decClick)
        self.equalB.clicked.connect(self.equalClick)
    
    # All Methods For Click!
    def parcentClick(self):
        text = self.displayLabel.text()
        try:
            if text: 
                result = eval(text) / 100
                self.displayLabel.setText(str(result))
            else:
                self.displayLabel.setText("0")
        except Exception:  
            self.displayLabel.setText("Error")

    def clearClick(self):
        self.displayLabel.setText("")
    
    def delClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text[:len(text)-1])
    
    def divClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "/")
    
    def sevenClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "7")
    
    def eightClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "8")
    
    def nineClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "9")
    
    def mulClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "*")
    
    def fourClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "4")
    
    def fiveClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "5")
    
    def sixClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "6")
    
    def minusClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "-")
    
    def oneClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "1")
    
    def twoClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "2")
    
    def threeClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "3")

    def plusClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "+")

    def zeroClick(self):
        text = self.displayLabel.text()
        self.displayLabel.setText(text + "0")

    def plusminusClick(self):
        text = self.displayLabel.text()
        if text.startswith("-"):  
            self.displayLabel.setText(text[1:])
        elif text:  
            self.displayLabel.setText("-" + text)
        else:  
            self.displayLabel.setText("-")

    def decClick(self):
        text = self.displayLabel.text()
        if "." not in text: 
            self.displayLabel.setText(text + ".")

    def equalClick(self):
        text = self.displayLabel.text()
        try: 
            ans = eval(text)
            self.displayLabel.setText(str(ans))
        except Exception: 
            self.displayLabel.setText("Wrong Input")
