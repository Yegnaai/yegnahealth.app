from kivymd.uix.screen import MDScreen
import webbrowser

class KdinyScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('kdinya')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('kdinyb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('kdinyc')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('kdinyd')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('kdinye')
    
    def switch_to_etho(self):
        # Open the URL in the default web browser
        webbrowser.open('https://www.ethiopiankidneyassociation.com/')
