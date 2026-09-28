import requests

URL = "https://jsonplaceholder.typicode.com/users"


def get_users():

    try:
        response = requests.get(URL, timeout=5)

        # Check HTTP status
        response.raise_for_status()

        # Convert response to JSON
        users = response.json()

        return users

    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)

    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON response.")

    except requests.exceptions.RequestException as e:
        print("Request error:", e)

    return []


def display_users(users):

    for user in users:

        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("Company:", user["company"]["name"])
        print("-" * 30)


def search_user(name):

    users = get_users()

    for user in users:

        if user["name"].lower() == name.lower():
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            print("Company:", user["company"]["name"])
            return

    print("User not found.")


# Main program

users = get_users()

if users:
    display_users(users)

    name = input("\nEnter user name to search: ")
    search_user(name)