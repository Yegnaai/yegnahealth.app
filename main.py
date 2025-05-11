from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from controllers.main_controller import LazyScreenManager
import views

class MainApp(MDApp):
    dark_theme = BooleanProperty(False)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.screen_manager = LazyScreenManager()
        self.screen_manager.switch_to_screen('splash')
        self.navigation_history = ['splash']  # Initialize navigation history
        Window.bind(on_keyboard=self.on_back_button)
        return self.screen_manager

    def on_start(self):
        Clock.schedule_once(self.switch_to_main, 25)  # Ensure fallback transition after 2 minutes

    def switch_to_main(self, *args):
        pass
        self.screen_manager.switch_to_screen('main')
        self.navigation_history.append('main')  # Add to navigation history

    def toggle_theme(self):
        if not hasattr(self, 'dark_theme'):
            self.dark_theme = False

        if self.dark_theme:
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
        self.dark_theme = not self.dark_theme

    def on_back_button(self, window, key, *args):
        if key == 27:  # 27 is the code for the back button on Android
            if len(self.navigation_history) > 1:
                self.navigation_history.pop()  # Remove current screen
                previous_screen = self.navigation_history[-1]
                self.screen_manager.switch_to_screen(previous_screen)
                return True
            else:
                return False  # Allow the app to close if no history
        return False

    def switch_to_screen(self, screen_name):
        self.screen_manager.switch_to_screen(screen_name)
        self.navigation_history.append(screen_name)  # Add to navigation history

if __name__ == '__main__':
    MainApp().run()
