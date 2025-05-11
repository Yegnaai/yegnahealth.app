from kivymd.uix.screen import MDScreen
import webbrowser


class CancerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('cancera')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('cancerb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('cancerc')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('cancerd')

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('cancere')

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('cancerf')

    def switch_to_etho(self):
        # Open the URL in the default web browser
        webbrowser.open('https://yeeca.org/')
    
