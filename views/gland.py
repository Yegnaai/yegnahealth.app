from kivymd.uix.screen import MDScreen

class GlandScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('glanda')

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('glandb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('glandc')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('glandd')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('glande')
    
