from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David"]

    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')

        main_layout = self.root.ids.main

        for name in self.names:
            lbl = Label(text=name, font_size=24)
            main_layout.add_widget(lbl)
        return self.root

NameListApp().run()
