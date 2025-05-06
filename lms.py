class Library:
    def __init__(self, book_list, library_name):
        self.books = book_list
        self.name = library_name
        self.lend_data = {} # tracks who borrowed what 

    def display_books(self):
        print(f"\n Books available in {self.name}:")
        for book in self.books:
            print(" -",book)    

    def lend_book(self,book,user):
        if book not in self.books:
            print("this book is not in library")

        elif book in self.lend_data:
            printf(f"Book is already borrowed by {self.lend_data[book]}") 

        else:
            self.lend_data[book] = user
            print(f"{user} borrowed {book}")

    def return_book(self, book):
        if book in self.lend_data:
            print(f"{book} returned by {self.lend_data[book]}")
            del self.lend_data[book]

        else:
            print("this book was not borrowed") 


    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added to the library")

# interface for the user interaction
def main():
    my_library = Library(["python Basics", "data Structures", "c++ fundamentals"],"Code library") 

    while True:
        print("\n=======Library menau==========")    
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return book" )
        print("4. Add Book")
        print("5. Exit")


        choice = input("enter your choice").strip()

        if choice =="1":
            my_library.display_books()

        elif choice=="2":
            book = input("enter the name of the book you want to borrow:").strip()
            user = input("enter your name:").strip()
            my_library.lend_book(book,user)    

        elif choice == "3":
            book = input("enter the name of the book you want to return").strip()
            my_library.return_book(book)

        elif choice == "4":
            book = input("enter the name of  the book to add:").strip()
            my_library.add_book(book)

        elif choice == "5":
            print("Exiting... Thank you for using the library system")
            break

        else:
            print("invalid choice. Try again")

if __name__ == "__main__":
    main()



