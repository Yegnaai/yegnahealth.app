from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class AsthmaScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')

    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('Asthmaa')

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('Asthmab')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('Asthmac')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('Asthmad') 
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('Asthmae')