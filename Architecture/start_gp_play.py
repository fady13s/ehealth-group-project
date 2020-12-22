from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

# creating overall screenmanager to separate  different user apps
screen_manager = ScreenManager()


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


#building app and linking to relevant kv file
class MainApp(MDApp):
    def build(self):
        system = Builder.load_file("start_gp_play.kv")
        return system

# run the app
MainApp().run()
