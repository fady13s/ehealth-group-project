from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

import mysql.connector                 #must be installed already


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


screen_manager = ScreenManager()

email = ObjectProperty(None)
password = ObjectProperty(None)

class MainApp(MDApp):
    def build(self):
        system = Builder.load_file("start.kv")
        return system

    def login(self, instance):
        if email.text in gplogin:
            screen_manager.current = "gpscreen"


MainApp().run()
