from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast import toast
import sqlite3

Builder.load_file('./libs/kv/generate.kv')

class GenerateScreen(Screen):

    def check_information(self):

        conn = sqlite3.connect("mybase.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS information(id_num integer PRIMARY KEY, full_name VARCHAR(30), course_section VARCHAR(30), student_number VARCHAR(30), contact_number VARCHAR(30))")
        cur.execute("SELECT id_num FROM information")
        results = cur.fetchall()
        if len(results) == 0:
            conn.close()
            return toast('Please update your information.')
        else:
            self.manager.current = "health_declaration"
