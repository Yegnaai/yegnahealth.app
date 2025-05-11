from kivymd.uix.screen import MDScreen

class SkinScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('skina')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('skinb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('skinc')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('skind')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('skine')
    
    
