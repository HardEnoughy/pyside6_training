from PySide6.QtWidgets import QMainWindow, QPushButton

class MyButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push me!")
        self.setCentralWidget(self.button)
    
    def button_clicked(self, data):
       print("You have succesfully clicked the button! Congrats!", data) 
