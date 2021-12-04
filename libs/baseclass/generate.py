from libs.baseclass import information
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('./libs/kv/generate.kv')

class GenerateScreen(Screen):

    def generate(self):

        pass
