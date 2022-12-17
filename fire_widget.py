from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class FireWidgets(QWidget):
    def __init__(self):
        super().__init__()
        button1 = QPushButton("push me!")
        button2 = QPushButton("no, push me!")

        button1.clicked.connect(self.first_button)
        button2.clicked.connect(self.second_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)
        
    def first_button(self, f):
        print("Wow! You pushed first button")
    
    def second_button(self, f):
        print("No way! You pushed second button!")
    