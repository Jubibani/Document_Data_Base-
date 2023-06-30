# by: Christopher Jiovanni A. Orpilla
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
# create an application (login_screen)
kivy.require('2.2.1')
    # main application
class FirstPage(Screen):
    text = StringProperty("----")
    # from the button submit
    def Pressed(self):
        self.text = "Logged In!"



class ErrorPage(Screen):
    pass
class WindowManager(ScreenManager):
    pass
# functionality for user input
# class MyApp(GridLayout):
    # create initialization
#     def __init__(self, **kwargs):
#         # calling the MyApp Constructor
#         super(MyApp, self).__init__(**kwargs)
#         self.cols = 1
#         # add_widgets
#
#         self.inside = GridLayout()  # This will act as a container
#         self.inside.cols = 2
#         # creating account
#         self.greet = Label(
#             text=
#             "   ---- [Personal Data Base] ----"
#             "\n Hello! What should we call you?", font_size=25)
#         self.inside.add_widget(self.greet)
#         # it will default the program to have multiple lines, but we only want one
#         self.user = TextInput(multiline=False, font_size=40)
#         self.inside.add_widget(self.user)
#         # creating_password
#         self.password_txt = Label(text="<Enter Password: >")   # method_1: for display
#         self.inside.add_widget(self.password_txt)
#         self.enter_password = TextInput(multiline=False, font_size=40)
#         self.inside.add_widget(self.enter_password)
#         # and_re-entering_password
#         self.inside.add_widget(Label(text="<Re-enter Password: >"))  # method_2: for display
#         self.re_enter = TextInput(multiline=False, font_size=40)
#         self.inside.add_widget(self.re_enter)
#
#         self.add_widget(self.inside)    # call the container
#         # submit input
#         self.enter = Button(text="submit", font_size=40)
#         self.clear = Button(text="clear", font_size=40)
#         # button bind
#         self.enter.bind(on_press=self.Pressed)
#         self.clear.bind(on_press=self.Cleared)
#         self.add_widget(self.enter)
#         self.add_widget(self.clear)
#
#         # from the button submit
#     def Pressed(self, instance):
#         user = self.user.text
#         enter_password = self.enter_password.text
#         re_enter = self.re_enter.text
#         # print from the button w/ control statement
#         if enter_password == re_enter:
#             print("Hello " + user)
#             print("-------Thank you for using our application-------")
#             print("Your password: " + enter_password)
#         else:
#             print("Password Incorrect! Let's see your input: ")
#             print("entered_password: " + enter_password)
#             print("re-entered_password: " + re_enter)
#
#         # from the button clear
#     def Cleared(self, instance):
#         self.user.text = ""
#         self.enter_password.text = ""
#         self.re_enter.text = ""
# # another class for screen window
class MainApp(App):
    def build(self):
        return kv

kv = Builder.load_file("my.kv")

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
