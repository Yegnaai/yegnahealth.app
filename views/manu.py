from kivymd.uix.screen import MDScreen

class ManuScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('food')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('tela')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('game')
    
 