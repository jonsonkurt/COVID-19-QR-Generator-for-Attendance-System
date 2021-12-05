from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast import toast
import sqlite3
import re

Builder.load_file('./libs/kv/information.kv')

class InformationScreen(Screen):

    def on_enter(self):

        conn = sqlite3.connect("mybase.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM information")
        results = cur.fetchall()

        if len(results) == 0:
            self.ids['full_name_id'].text = ""
            self.ids['course_section_id'].text = ""
            self.ids['student_number_id'].text = ""
            self.ids['contact_number_id'].text = ""
        else:
            details = results[0]

            self.ids['full_name_id'].text = str(details[1])
            self.ids['course_section_id'].text = str(details[2])
            self.ids['student_number_id'].text = str(details[3])
            self.ids['contact_number_id'].text = str(details[4])

    def update_information(self, fullname, course_section, student_number, contact_number):

        fname = fullname.upper()
        course_sec = course_section.upper()
        stud_num = student_number.upper()
        contact_num = contact_number

        conn = sqlite3.connect("mybase.db")
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS information(id_num integer PRIMARY KEY, full_name VARCHAR(30), course_section VARCHAR(30), student_number VARCHAR(30), contact_number VARCHAR(30))")

        cur.execute("SELECT * FROM information")
        results1 = cur.fetchall()

        if len(results1) == 0:
            if(len(fname) > 0 and len(course_sec) > 0 and len(stud_num) > 0 and len(contact_num) > 0):
                    if fname == "":
                        return toast('Please enter your full name.')
                    elif course_sec == "":
                        return toast('Please enter your course and section.')
                    elif stud_num == "":
                        return toast('Please enter your student number.')
                    elif contact_num == "":
                        return toast('Please enter your contact number.')
                    else:
                        cur.execute("INSERT INTO information(full_name, course_section, student_number, contact_number) VALUES(?,?,?,?)",(fname, course_sec, stud_num, contact_num))
                        conn.commit()
                        self.manager.transition.direction = "right"
                        self.manager.transition.duration = 0.5
                        self.manager.current = "generate"
                        conn.close()
                        toast('Information saved.')
            else:
                return toast('Please enter your details.')

        else:
            find = ("SELECT * FROM information WHERE full_name = ? AND course_section = ? AND student_number = ? AND contact_number = ?")
            cur.execute(find,[(fname), (course_sec), (stud_num), (contact_num)])
            results2 = cur.fetchall()

            if(len(fname) > 0 and len(course_sec) > 0 and len(stud_num) > 0 and len(contact_num) > 0):
                if results2:
                    return toast('Information is already updated.')
                else:
                    cur.execute('UPDATE information SET full_name = ?, course_section = ?, student_number = ?, contact_number = ? WHERE id_num = ?', (fname, course_sec, stud_num, contact_num, 1))
                    conn.commit()
                    conn.close()
                    self.manager.current = "generate"
                    toast('Information updated.')