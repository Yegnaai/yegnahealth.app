from kivymd.uix.screen import MDScreen


class StomachScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('stomacha')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('stomachb')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('stomachc')
        
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('stomachd')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('stomache')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('stomachf')
    
    