import csv 
import os
from datetime import date
FILENAME = 'expenses.csv'

#make sure the file exist with the headers

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Description"])



#add a new expense
def add_expense():
    today=str(date.today())
    category = input("enter category(e.g. food, transport)")
    amount = input("enter amount")
    description = input("enter description")

    with open(FILENAME,mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today,category,amount,description])   


    print("enpense added")


#view all expenses

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found")
        return


    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))


#main menu
def main():
    initialize_csv()
    while True:
        print("\n Expense tracker menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("choose an option 1/2/3: ")
        if choice =='1':
            add_expense()

        elif choice=='2':
            view_expenses()

        elif choice=='3':
            print("exiting.goodbye!")
            break

        else:
            print("invalid choice.try again")


if __name__ == "__main__":
    main()                                        


