# by: Christopher Jiovanni A. Orpilla
# # creating an account
def create():
    print("-- create an Account --")
    user_name = input("Enter username: ")
    password = input("password: ")

    print(" --- Account created ---  ")
    print("Hello " + user_name + "!")
    print(" [Please don't share your password] ")
    print("password: " + password)
    # verifying the account
    print("-- - Log in your account - -- ")
    def data():
        from pymongo import MongoClient

        # Connect to the MongoDB server
        client = MongoClient('mongodb://localhost:27017/')

        # Create a new database
        database = client['mydatabase']

        # Create a new collection
        collection = database['mycollection']

        # Insert a document into the collection
        document = {
            'name': 'John Doe',
            'age': 30,
            'email': 'johndoe@example.com'
        }
        result = collection.insert_one(document)
        print(f"Inserted document id: {result.inserted_id}")

        # Retrieve documents from the collection
        documents = collection.find()
        for document in documents:
            print(document)

        # Update a document in the collection
        query = {'name': 'John Doe'}
        new_values = {'$set': {'age': 35}}
        result = collection.update_one(query, new_values)
        print(f"Modified {result.modified_count} document(s)")

        # Delete a document from the collection
        query = {'name': 'John Doe'}
        result = collection.delete_one(query)
        print(f"Deleted {result.deleted_count} document(s)")

        # Drop the collection
        collection.drop()

        # Disconnect from the MongoDB server
        client.close()

    def log_in():
        print("-------------------------------")
        print("Welcome Back " + user_name + "!")
        print()
        print("[q] to quit")
        # print("[+] to add")
        # print("[-] to delete")
        # pri   nt("--------------------------------")
        # search = input("Search or type a keyword: ")
        # print("--------------------------------")
        # print()
        # print("--------------------------------")
        # print("you searched " + "'" + search + "'"
    while True:
        enter_password = input("Enter password: ")
        if enter_password == password:
            log_in()
            break
        elif enter_password == 'q':
            create()
        else:
            print("try again")

    data()

create()
