"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty()
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.output_text = "0.0"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root