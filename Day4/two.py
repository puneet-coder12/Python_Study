import json

users = []


def load_users():

    global users

    try:
        with open("Day4/users.json", "r") as file:
            users = json.load(file)

    except Exception as e:
        print(e)

    else:
        print("Users loaded successfully")

    finally:
        print("Loading process done")


def add_user():

    name = input("Enter a name: ")
    user_id = int(input("Enter id: "))
    email = input("Enter email: ")
    skills = input("Enter skills separated with comma: ")

    try:
        skills = skills.split(",")

        user = {
            "name": name,
            "id": user_id,
            "email": email,
            "skills": skills
        }

        users.append(user)

        print("User added successfully")

    except Exception as e:
        print(e)


def get_user():

    user_id = int(input("Enter id of user you want: "))

    for user in users:

        if user["id"] == user_id:
            print(user)
            return

    print("User Not Found")


def update_user():

    user_id = int(input("Enter id of user you want to update: "))

    for user in users:

        if user["id"] == user_id:

            user["name"] = input("Enter new name: ")
            user["email"] = input("Enter new email: ")

            user["skills"] = input(
                "Enter new skills separated by commas: "
            ).split(",")

            print("User updated successfully")
            return

    print("User not found")


def delete_user():

    user_id = int(input("Enter id of user you want to delete: "))

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            print("User deleted successfully")
            return

    print("User not found")


def save_users():

    try:

        with open("Day4/users.json", "w") as file:
            json.dump(users, file, indent=4)

    except Exception as e:
        print(e)

    else:
        print("Users saved successfully")

    finally:
        print("Saving process done")
        
load_users()

while True:

    print("\n1. Add User")
    print("2. Get User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Save Users")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        get_user()

    elif choice == "3":
        update_user()

    elif choice == "4":
        delete_user()

    elif choice == "5":
        save_users()

    elif choice == "6":
        save_users()
        print("Program ended")
        break

    else:
        print("Invalid choice")