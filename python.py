# create library class
# display book
# add book
# borrow book 
# return book
# def main()
# display all choices
# conditions
# call the function

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def display_books(self):
        if not self.books:
            print("\nNo books currently available.")    
        else:
            print("\nAvailable Books: ")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")
    
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"\n' {book_name} has been added to the library. ")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"\nYou have borrowed '{book_name}'. Please return it on time. ")
        else:
            print(f"\nSorry, '{book_name}' is not availabel right now. ")    

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"\nThank you for returning '{book_name}'.")

def main():
    library = Library("City Library")

    while True:
        print("\n===== Library Menu =====")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")   

        choice = input("Enter your choice(1-5): ")    

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_name = input("Enter the name of book to add: ")         
            library.add_book(book_name)
        elif choice == "3":
            book_name = input("Enter the name of the book to borrow: ")    
            library.borrow_book(book_name)
        elif choice == "4":
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
        elif choice == "5":
            print("\nThank you for using the library system. Goodbye!")    
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()             