# by: Christopher Jiovanni A. Orpilla
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

# define the kivy version
kivy.require('2.2.1')


# define the screens
class FirstWindow(Screen):
    # Instantiating some variables
    # these variables should also be in the kv.file to build (should be identical)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    re_password = ObjectProperty(None)

    # the popup
    # def PopupWindow(self):
    #     popup = PopupWindow(
    #         title="Warning!", size_hint=(None, None), size=(400, 400)
    #     )
    #     popup.open()

    # button for logging in
    def log_in(self):
        # If the input is not empty
        # strip() method returns a non-empty string if there is input,
        # and an empty string if there is no input,
        # the condition will evaluate to True only if all fields have input.
        if self.username.text.strip() and self.password.text.strip() == self.re_password.text.strip():
            print("Greetings! ", self.username.text)
            print("your password is: ", self.password.text)
            self.manager.current = "second"
            # to check if the passwords are the same
        if self.password.text.strip() != self.re_password.text.strip():
            print("please check your inputs: ")
            print("your input for password: ", self.password.text)
            print("your input for re_password: ", self.re_password.text)
            self.Popup.open()
        else:
            # to check if required fields are inputted by the user
            if not self.username.text.strip():
                print("Username is required!")
            if not self.password.text.strip():
                print("Password is required!")
            if not self.re_password.text.strip():
                print("Re-password is required!")
                self.Popup.open()

    # button for clearing inputs
    def clear_input(self):
        self.username.text = ""
        self.password.text = ""
        self.re_password.text = ""
        print("cleared!")

    pass


class SecondWindow(Screen):
    def back_button(self):
        self.manager.current = "create"


class ThirdWindow(Screen):
    pass


class PopupWindow(Popup):
    pass


class WindowManager(ScreenManager):
    pass


# instantiate your app [an object just means to create it]
class MainApp(App):
    def build(self):
        # define kv.file
        kv = Builder.load_file("my.kv")
        return kv


if __name__ == '__main__':
    MainApp().run()
