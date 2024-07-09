from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime


class TaskTimerApp(App):
    def build(self):
        self.start_time = None
        self.running = False
        self.time = 0

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.task_input = TextInput(
            hint_text='Enter task name', font_size='20sp', size_hint=(1, 0.1))
        self.layout.add_widget(self.task_input)

        self.time_label = Label(text="00:00:00", font_size='40sp')
        self.layout.add_widget(self.time_label)

        self.start_button = Button(
            text="Start", font_size='20sp', size_hint=(1, 0.2))
        self.start_button.bind(on_press=self.start_timer)
        self.layout.add_widget(self.start_button)

        self.stop_button = Button(
            text="Stop", font_size='20sp', size_hint=(1, 0.2), disabled=True)
        self.stop_button.bind(on_press=self.stop_timer)
        self.layout.add_widget(self.stop_button)

        return self.layout

    def start_timer(self, instance):
        self.task_name = self.task_input.text
        if self.task_name:
            self.start_time = datetime.now()
            self.running = True
            self.time = 0
            self.start_button.disabled = True
            self.stop_button.disabled = False
            self.task_input.disabled = True
            Clock.schedule_interval(self.update_time, 1)

    def stop_timer(self, instance):
        self.running = False
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.task_input.disabled = False
        Clock.unschedule(self.update_time)

    def update_time(self, dt):
        if self.running:
            self.time += 1
            hours, remainder = divmod(self.time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.time_label.text = f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == '__main__':
    TaskTimerApp().run()
