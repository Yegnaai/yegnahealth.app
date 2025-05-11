from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class AsthmaeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('Asthma')