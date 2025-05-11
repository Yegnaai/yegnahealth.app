from kivymd.uix.screen import MDScreen

class TelaScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('manu')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('telaa')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('telab')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('telac')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('telad')