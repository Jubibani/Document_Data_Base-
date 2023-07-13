# by: Christopher Jiovanni A. Orpilla
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

# define the kivy version
kivy.require('2.2.1')
# define the screens
class FirstWindow(Screen):
    # Instantiating some variables
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    re_password = ObjectProperty(None)
    # the buttons
    def log_in(self):
        print("You entered: ", self.username.text)
        print("You entered: ", self.password.text)
        print("You entered: ", self.re_password.text)

class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
# define kv.file
kv = Builder.load_file("my.kv")
# instantiate your app [an object just means to create it]
class MainApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MainApp().run()

