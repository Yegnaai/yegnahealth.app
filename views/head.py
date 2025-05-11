from kivymd.uix.screen import MDScreen

class HeadScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('heada')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('headb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('headc')

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('headd')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('heade')