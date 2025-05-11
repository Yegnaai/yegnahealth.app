from kivymd.uix.screen import MDScreen

class FoodScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('manu')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('fooda')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('foodb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('foodc')
    
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('foode')