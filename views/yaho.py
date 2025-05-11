from kivymd.uix.screen import MDScreen

class YahoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('manu')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('yahoa')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('yahob')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('yahoc')
    
    def switch_to_health(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('yahod')