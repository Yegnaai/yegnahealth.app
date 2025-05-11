from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.app import MDApp

LABEL_IDS = ['label_1', 'label_2', 'label_3', 'label_4']

class SplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.labels = [self.ids[label_id] for label_id in LABEL_IDS]

    def on_enter(self, *args):
        self.animate_labels()

    def animate_labels(self):
        for index, label in enumerate(self.labels):
            self.animate_label(label, delay=index * 1.5)

    def animate_label(self, label, delay):
        initial_pos_hint = {'center_y': 0.2}
        final_pos_hint = {'center_y': 0.5}

        label.pos_hint = initial_pos_hint
        label.opacity = 0
        label.y -= 100

        animation = Animation(opacity=1, pos_hint=final_pos_hint, duration=1, t='out_bounce')
        animation += Animation(opacity=1, duration=2)
        Clock.schedule_once(lambda dt: animation.start(label), delay)

    def start_fade_out(self, *args):
        fade_out = Animation(opacity=0, duration=1)
        fade_out.bind(on_complete=self.switch_to_main)
        fade_out.start(self)

    def switch_to_main(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen('main')
