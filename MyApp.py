# by: Christopher Jiovanni A. Orpilla
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# create an application
class MyApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        # add widgets to window

        self.greet_user = Label(
            text="hello!"
            + "  " + "let's create your account"
        )

        self.window.add_widget(self.greet_user)
        self.user_name = TextInput(multiline=False)
        self.window.add_widget(self.user_name)

        self.button = Button(text="Greet")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window
    def callback(self, instance):
        self.greet_user.text = "You are " + self.user_name.text + "!"


if __name__ == '__main__':
    MyApp().run()

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
