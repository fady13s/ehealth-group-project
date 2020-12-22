from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.lang.builder import Builder


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
