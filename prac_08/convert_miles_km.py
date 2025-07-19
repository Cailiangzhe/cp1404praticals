from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """Main application class for the Miles to Kilometres converter"""
    output_km = StringProperty("0.0")

    def build(self):
        """ Build and return the root widget of the app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert(self, text):
        """ Convert miles to kilometres and update the output label"""
        self.output_km = self.miles_to_km(text)

    def handle_increment(self, text, change):
        """Increase or decrease the miles value by a specified amount"""
        try:
            value = int(text)
        except ValueError:
            value = 0
        value += change
        self.root.ids.input_miles.text = str(value)
        self.output_km = self.miles_to_km(str(value))

    def miles_to_km(self, text):
        """ Convert a string number in miles to a formatted kilometre string"""
        try:
            miles = float(text)
            km = miles * MILES_TO_KM
            return f"{km:.5f}"
        except ValueError:
            return "0.0"

if __name__ == '__main__':
    MilesConverterApp().run()

