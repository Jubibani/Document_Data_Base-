# by: Christopher Jiovanni A. Orpilla
# create an application
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
class BoxLayoutExample(BoxLayout):

    pass

class MainWidget(Widget):

    pass
class ThelabApp(App):
    pass

ThelabApp().run()

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
