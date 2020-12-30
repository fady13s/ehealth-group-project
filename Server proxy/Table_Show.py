from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import mysql.connector
from kivymd.uix.dialog import MDDialog

connection = mysql.connector.connect(host='127.0.0.1',
                             user='root',
                             password='gpuclpass!2',
                             db='gp_practice')

cursor=connection.cursor()

#building app and linking to relevant kv file
class MainApp(MDApp):
    def build(self):
        system = Builder.load_file("tableshow.kv")
        return system

    def words(self):
        cursor.execute('SELECT * from Patients')  # this lists all rows in a table (Patients) as a list of tuples
        rows = cursor.fetchall()
        print(rows)
        for row in rows:  # do this to print each row as a list - so more editable
            return (f"Firstname: {row[1]}")

    def show_table(self):
        dialog = MDDialog(text= self.words)
        dialog.open()

# run the app
MainApp().run()