from kivymd.app import MDApp
from kivy.lang.builder import Builder

from libs.baseclass import generate, help, information, healthdeclaration

# this class serves as the main class that runs the system
class MyApp(MDApp):

    title = "QR Code Generator for Attendance"

    def build(self):
        
        self.icon = 'qr_attendance.ico'
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_file("main.kv")
        return screen

if __name__ == '__main__':
    MyApp().run()