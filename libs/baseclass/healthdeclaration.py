from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import qrcode
import sqlite3

Builder.load_file('./libs/kv/healthdeclaration.kv')

q1 = ['NO']
q2 = ['NO']
q3 = ['NO']
q4 = ['NO']
ans = ['Y','y','yes','YES']
qr_name = []

class Content(BoxLayout):
    
    def source_name(self):
        if len(qr_name) != 0:
            image_name = qr_name[-1]
            final_name = f"{image_name}.jpg"
            return(final_name)
        else:
            return 'Media/QR_Attendance_Logo.png'

class HealthDeclarationScreen(Screen):

    def on_leave(self):
        self.ids['temp'].text = ""
        qr_name.clear()
        Content.source_name(self)

    def on_checkbox_active1(self, checkbox, value):
    
        if value:
            q1.append('YES')
        else:
            q1.append('NO')

    def on_checkbox_active2(self, checkbox, value):
        
        if value:
            q2.append('YES')
        else:
            q2.append('NO')

    def on_checkbox_active3(self, checkbox, value):
        
        if value:
            q3.append('YES')
        else:
            q3.append('NO')

    def on_checkbox_active4(self, checkbox, value):
        
        if value:
            q4.append('YES')
        else:
            q4.append('NO')

    def generate(self, temperature):

        stud_temp = temperature
        now = datetime.now()

        conn = sqlite3.connect("mybase.db")
        cur = conn.cursor()
        find = ("SELECT * FROM information WHERE id_num = ?")
        cur.execute(find, [(1)])
        results = cur.fetchall()

        info = results[0]

        if stud_temp == "":
            toast("Please enter your temperature.")
        elif float(stud_temp) >= 38:
            toast('Your temperature exceeded normal range.') 
        elif (q1[-1] in ans) or (q2[-1] in ans) or (q3[-1] in ans) or (q4[-1] in ans):
            toast("You have not meet the requirement to enter this facility") 
        else:
            img = qrcode.make(str(info[3]) + ";" + str(info[1])+ ";" + str(q1[-1])+ ";" + str(q2[-1])+ ";" + \
                str(q3[-1])+ ";" + str(q4[-1])+ ";"  + str(stud_temp) + ";" + now.strftime('%Y/%m/%d')+ ";" + now.strftime('%I:%M:%S'))
            img.save(str(info[3]) + "-" + str(info[1]) + '.jpg')
            file_name = str(info[3]) + "-" + str(info[1])
            qr_name.append(file_name)
            conn.close()

            self.manager.current = "generate"
            self.show_alert_dialog()

    dialog = None

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Your QR Code",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color="#07575B",
                        on_release=self.dialog_close,
                    ),
                ],
            )
        self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)