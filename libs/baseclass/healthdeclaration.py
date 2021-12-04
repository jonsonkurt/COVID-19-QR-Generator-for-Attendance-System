from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast import toast

Builder.load_file('./libs/kv/healthdeclaration.kv')

q1 = ['NO']
q2 = ['NO']
q3 = ['NO']
q4 = ['NO']

class HealthDeclarationScreen(Screen):

    def on_checkbox_active1(self, checkbox, value):
    
        if value:
            q1.append('YES')
        else:
            q1.append('NO')
        
        print(q1)

    def on_checkbox_active2(self, checkbox, value):
        
        if value:
            q2.append('YES')
        else:
            q2.append('NO')

        print(q2)

    def on_checkbox_active3(self, checkbox, value):
        
        if value:
            q3.append('YES')
        else:
            q3.append('NO')

        print(q3)

    def on_checkbox_active4(self, checkbox, value):
        
        if value:
            q4.append('YES')
        else:
            q4.append('NO')

        print(q4)