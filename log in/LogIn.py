from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class LogIn(MDApp):
    def build(self):
        return WindowManager()


class WindowManager(ScreenManager):
    pass


class LogInScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)


class MainScreen(Screen):
    pass


LogIn().run()
