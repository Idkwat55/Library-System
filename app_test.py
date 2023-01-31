import sys
import random
import PyQt6
from PySide6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import*  

 

app =  QApplication(sys.argv)

widget =QWidget()
widget.setWindowTitle("Library Manager Beta v1.00.0")
widget.resize(700, 300)
layout = QFormLayout()
name = layout.addRow("Name:", QLineEdit())
age = layout.addRow("Age:", QLineEdit())

str_1 = "Your Name is ",name ,"\n","Your age is ",age


button = QPushButton("button eh?")
button.show()
abc = QLabel(str_1)

abc.resize(100,80)
abc.show()
widget.setLayout(layout)
widget.show()

sys.exit(app.exec())

