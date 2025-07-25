from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main application class for dynamically adding labels."""
    def __init__(self, **kwargs):
        """Initialise the app and define the data model."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI and add a Label for each name."""
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()