from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider

class MySlider:
    def __init__(self):
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(25)
    
    def value_changed(self, data):
       print("Wow! You moved a slider!", data) 
        