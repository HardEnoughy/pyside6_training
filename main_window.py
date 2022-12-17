from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("My own app!")

        #menu bar
        menu_bar = self.menuBar()

        #file menu
        file_menu = menu_bar.addMenu("&File")

        #file menu actions
        quit_action = file_menu.addAction("Exit")
        quit_action.triggered.connect(self.quit_app)
    
    def quit_app(self):
        self.app.quit()
        