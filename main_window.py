from PySide6.QtWidgets import QMainWindow, QToolBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("My own app!")

        #menu bar
        menu_bar = self.menuBar()

        #file menu
        file_menu = menu_bar.addMenu("&File")
        instruments_menu = menu_bar.addMenu("Instruments")

        #file menu actions
        quit_action = file_menu.addAction("Exit")
        quit_action.triggered.connect(self.quit_app)

        back_action = instruments_menu.addAction("Back")

        #toolbar
        toolbar = QToolBar("Some toolbar")
        self.addToolBar(toolbar) 

        #add actions on toolbar
        toolbar.addAction(quit_action)
    
    def quit_app(self):
        self.app.quit()
        