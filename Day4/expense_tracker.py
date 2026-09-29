import json
from datetime import datetime

expenses = []

def load_expense():
    global expenses

    with open('Day4/expenses.json', 'r') as file:
        expenses = json.load(file)

def add_expense():    
    try:
        id = int(input("Enter id: "))
        title = input("Enter title: ")
        amount = int(input("Enter amount: "))
        category = input("Enter Category: ")
        date_input = input("Enter date (DD-MM-YYYY): ")
        
        # date = datetime.strptime(date_input, "%d-%m-%Y").date()
        
        expense = {
            "id": id,
            "title": title,
            "amount":amount,
            "category": category,
            "date":date_input
        }
        
        expenses.append(expense)
    except Exception as e:
        print(e)
    

def view_expense():
    for expense in expenses:
        print(expense)
    
        
def delete_expense(): 
    id = int(input("Enter id to delete expense: "))
    
    for expense in expenses:
        if(expense["id"] == id):
            expenses.remove(expense)
            return
    print("No such expense")
    
    
def save_expense():
    try:
        with open('Day4/expenses.json', 'r') as file:
            json.dump(file, expenses, indent=5)
    
    except Exception as e:
        print(e)
        
def search_by_category():
    category = input("Enter category to search: ")
    
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense)
            
def total_expense():
    amount = 0
    
    for expense in expenses:
        amount+=expense["amount"]
    
    print(f"Total expense: {amount}")

def monthly_summary():
    monthly = {}
    
    for expense in expenses:
            expense["date"] = datetime.strptime(
                expense["date"],
                "%Y-%m-%d").date()
            
    for expense in expenses:

        month = expense["date"].month
        category = expense["category"]
        amount = expense["amount"]

        # If month is not present, create an empty dictionary
        if month not in monthly:
            monthly[month] = {}

        # Add amount to the category
        monthly[month][category] = (
            monthly[month].get(category, 0) + amount
        )
    
    print(monthly)


load_expense()