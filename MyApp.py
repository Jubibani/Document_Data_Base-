# by: Christopher Jiovanni A. Orpilla
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# create an application (login_screen)
kivy.require('2.2.1')

# functionality for user input
class MyApp(GridLayout):
    # create initialization
    def __init__(self, **kwargs):
        # calling the MyApp Constructor
        super(MyApp, self).__init__(**kwargs)
        self.cols = 2
        # add_widgets
        # creating account
        self.greet = Label(
            text=
            "   ---- Personal Data Base ----"
            "\n Hello! What should we call you?")
        self.add_widget(self.greet)
        # it will default the program to have multiple lines, but we only want one
        self.user = TextInput(multiline=False )
        self.add_widget(self.user)
        # creating_password
        self.password_txt = Label(text="Enter Password: ")   # method_1: for display
        self.add_widget(self.password_txt)
        self.enter_password = TextInput(multiline=False)
        self.add_widget(self.enter_password)
        # and_re-entering_password
        self.add_widget(Label(text="Re-enter Password: "))  # method_2: for display
        self.re_enter = TextInput(multiline=False)
        self.add_widget(self.re_enter)
        # submit input
        self.enter = Button(text="submit")
        self.add_widget(self.enter)
class MainApp(App):
    def build(self):
        return MyApp()

if __name__ == "__main__":
    MainApp().run()

# def create():
#     print("-- create an Account --")
#     user_name = input("Enter username: ")
#     password = input("password: ")
#     print("one line added")
#     print(" --- Account created ---  ")
#     print("Hello " + user_name + "!")
#     print(" [Please don't share your password] ")
#     print("password: " + password)
#     # verifying the account
#     print("-- -log in your account - -- ")
#     def log_in():
#         print("-------------------------------")
#         print("Welcome Back " + user_name + "!")
#         print()
#         print("[q] to quit")
#         print("[+] to add")
#         print("[-] to delete")
#         print("--------------------------------")
#         search = input("Search or type a keyword: ")
#         print("--------------------------------")
#         print()
#         print("--------------------------------")
#         print("you searched " + "'" + search + "'")
#     while True:
#         enter_password = input("Enter password: ")
#         if enter_password == password:
#             log_in()
#             break
#         elif enter_password == 'q':
#             create()
#         else:
#             print("try again")
#
#     data()
#
# create()
