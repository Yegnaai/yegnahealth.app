from kivymd.uix.screen import MDScreen
import webbrowser

class HeartScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('hearta')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('heartb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('heartc')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('heartd')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('hearte')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('heartf')
    
    def switch_to_etho(self):
        # Open the URL in the default web browser
        webbrowser.open('https://ethiopianheart.org/')