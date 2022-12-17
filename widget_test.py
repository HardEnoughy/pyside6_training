from PySide6.QtWidgets import QApplication, QWidget
from fire_widget import FireWidgets

import sys

app = QApplication(sys.argv)
window = FireWidgets()
window.show()

app.exec()
