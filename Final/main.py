from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import mysql.connector                 #must be installed already
from kivymd.uix.dialog import MDDialog

configuration ={
    'user': 'root',
    'password': 'gpuclpass!2',
    'host': '34.77.159.194',
    'db': 'gp_practice',
}

cnx = mysql.connector.connect(**configuration)

mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM Doctors")
gpinfo = mycursor.fetchall()
gplogin = {}
for i in gpinfo:
    gplogin[i[2]] = i[3]

mycursor.execute("SELECT * FROM Patients")
patientinfo = mycursor.fetchall()
patientlogin = {}
for i in patientinfo:
    patientlogin[i[3]] = i[4]

mycursor.execute("SELECT * FROM Admins")
admininfo = mycursor.fetchall()
adminlogin = {}
for i in admininfo:
    adminlogin[i[2]] = i[3]


class GPApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        GUI = Builder.load_file("kv files/main.kv")
        return GUI

    def change_screen(self, screen_name):
        screen_manager=self.root.ids["screen_manager"]
        screen_manager.current=screen_name
        screen_manager.transition.direction = "left"
        print(self.root.ids)

    def logout(self):
        screen_manager=self.root.ids["screen_manager"]
        screen_manager.current= "login_screen"
        screen_manager.transition.direction = "right"

    def login(self):
        screen_manager = self.root.ids["screen_manager"]
        username = self.root.ids["login_screen"].email.text
        password = self.root.ids["login_screen"].password.text
        wrongusernamedialog = MDDialog(title= "Incorrect Username")
        wrongpassworddialog = MDDialog(title= "Incorrect Password")

        print(username)
        print(password)

        if username in gplogin and password == gplogin[username]:
            screen_manager.current= "gp_screen"
            screen_manager.transition.direction = "left"
        elif username in gplogin and password != gplogin[username]:
            wrongpassworddialog.open()
        elif username in patientlogin and password == patientlogin[username]:
            screen_manager.current = "patient_screen"
            screen_manager.transition.direction = "left"
        elif username in patientlogin and password != patientlogin[username]:
            wrongpassworddialog.open()
        elif username in adminlogin and password == adminlogin[username]:
            screen_manager.current = "admin_screen"
            screen_manager.transition.direction = "left"
        elif username in adminlogin and password != adminlogin[username]:
            wrongpassworddialog.open()
        else:
            wrongusernamedialog.open()



GPApp().run()
