from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
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


class MyLayout(BoxLayout):

    screen_manager = ObjectProperty(None)

    def login(self):
        username = self.screen_manager.startscreen.email.text
        password = self.screen_manager.startscreen.password.text
        wrongusernamedialog = MDDialog(title= "Incorrect Username")
        wrongpassworddialog = MDDialog(title= "Incorrect Password")

        print(username)
        print(password)

        if username in gplogin and password == gplogin[username]:
            self.screen_manager.current= "gpscreen"
            self.screen_manager.transition.direction = "left"
        elif username in gplogin and password != gplogin[username]:
            wrongpassworddialog.open()
        elif username in patientlogin and password == patientlogin[username]:
            self.screen_manager.current = "patientscreen"
            self.screen_manager.transition.direction = "left"
        elif username in patientlogin and password != patientlogin[username]:
            wrongpassworddialog.open()
        elif username in adminlogin and password == adminlogin[username]:
            self.screen_manager.current = "adminscreen"
            self.screen_manager.transition.direction = "left"
        elif username in adminlogin and password != adminlogin[username]:
            wrongpassworddialog.open()
        else:
            wrongusernamedialog.open()

    def logout(self):
        self.screen_manager.current = "startscreen"
        self.screen_manager.transition.direction = "right"

# creating navigation drawer class for GP
class GPContentNavigationDrawer(BoxLayout):
    gp_screen_manager = ObjectProperty()
    gp_nav_drawer = ObjectProperty()

# creating navigation drawer class for Admin
class AdminContentNavigationDrawer(BoxLayout):
    admin_screen_manager = ObjectProperty()
    admin_nav_drawer = ObjectProperty()

# creating navigation drawer class for Patient
class PatientContentNavigationDrawer(BoxLayout):
    patient_screen_manager = ObjectProperty()
    patient_nav_drawer = ObjectProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        system = Builder.load_file("start2.kv")
        return system


MainApp().run()
