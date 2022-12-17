from PySide6.QtWidgets import QApplication
import sys
from my_button import MyButton
from my_slider import MySlider

app = QApplication(sys.argv)
window = MySlider()
# window = MyButton()
window.slider.valueChanged.connect(window.value_changed)
window.slider.show()
# window.button.setCheckable(True)
# window.button.clicked.connect(window.button_clicked)

app.exec()
