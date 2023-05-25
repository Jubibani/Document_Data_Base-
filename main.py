# by: Christopher Jiovanni A. Orpilla
# # creating an account
from pymongo import MongoClient

# my mongo object
client = MongoClient("mongodb+srv://Jubibani:<Jubibi'sstrawbibi>@cluster0.fdzmcqq.mongodb.net/")

# access my_data_base
db = client["doc_files"]

# Access a collection
collection = db["documents"]

# Insert a document
document = {"name": "John", "age": 30}
collection.insert_one(document)
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
#     print("-- - L"
#           "log in your account - -- ")
#     def log_in():
#         print("-------------------------------")
#         print("Welcome Back " + user_name + "!")
#         print()
#         print("[q] to quit")
#         # print("[+] to add")
#         # print("[-] to delete")
#         # pri   nt("--------------------------------")
#         # search = input("Search or type a keyword: ")
#         # print("--------------------------------")
#         # print()
#         # print("--------------------------------")
#         # print("you searched " + "'" + search + "'"
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
