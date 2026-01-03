import json
import os

DATA_FILE = "books.json"


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = file.read().strip()
                if not data:
                    return []
                return json.loads(data)
        except json.JSONDecodeError:
            return []
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')



# -------------------- Book Management --------------------

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    for b in books:
        if b["id"] == book_id:
            print("⚠️ A book with this ID already exists!\n")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available",
        "borrower": None,
        "borrow_days": None
    }

    books.append(book)
    save_data(books)
    print("✅ Book added successfully!\n")




def view_books():
    print("-" * 90)
    print(f"{' ' * 40}All Books")
    if not books:
        print("No books found.\n")
        return
    print("-" * 90)
    print(f"{'Book ID':<10}{'Title':<25}{'Author':<20}{'Status':<12}{'Borrower':<15}{'Days':<6}")
    print("-" * 90)
    for b in books:
        borrower = b["borrower"] if b["borrower"] else "-"
        days = b["borrow_days"] if b["borrow_days"] else "-"
        print(f"{b['id']:<10}{b['title']:<25}{b['author']:<20}{b['status']:<12}{borrower:<15}{days:<6}")

    print("-" * 90)
    print()




def search_book():
    print("\n--- Search Book ---")
    title = input("Enter Book Title to search: ").strip().lower()

    found_books = [b for b in books
                   if title in b["title"].lower()]

    if found_books:
        print(f"\n📚 Found {len(found_books)} book(s):\n")
        print("-" * 90)
        print(f"{'Book ID':<10}{'Title':<25}{'Author':<20}{'Status':<12}{'Borrower':<15}{'Days':<6}")
        print("-" * 90)
        for b in found_books:
            borrower = b["borrower"] if b["borrower"] else "-"
            days = b["borrow_days"] if b["borrow_days"] else "-"


            print(f"{b['id']:<10}{b['title']:<25}{b['author']:<20}{b['status']:<12}{borrower:<15}{days:<6}")
        print("-" * 90)
        print()
    else:
        print("❌ No book found with that title.\n")



def borrow_book():
    print("\n--- Borrow Book ---")
    book_id = input("Enter Book ID to borrow: ")

    for b in books:
        if b["id"] == book_id:
            if b["status"] == "Available":
                borrower_name = input("Enter Borrower Name: ")
                borrow_days = input("Enter Number of Days: ")

                b["status"] = "Borrowed"
                b["borrower"] = borrower_name
                b["borrow_days"] = borrow_days

                save_data(books)
                print(f"📘 {borrower_name} borrowed '{b['title']}' for {borrow_days} days!\n")
                return
            else:
                print(f"⚠️ Book is already borrowed by {b['borrower']}.\n")
                return

    print("❌ Book not found.\n")



def return_book():
    print("\n--- Return Book ---")
    book_id = input("Enter Book ID to return: ")

    for b in books:
        if b["id"] == book_id:
            if b["status"] == "Borrowed":
                print(f"Returning '{b['title']}' borrowed by {b['borrower']}.")
                b["status"] = "Available"
                b["borrower"] = None
                b["borrow_days"] = None

                save_data(books)
                print("✅ Book returned successfully!\n")
                return
            else:
                print("⚠️ This book was not borrowed!\n")
                return

    print("❌ Book not found.\n")



def delete_book():
    print("\n--- Delete Book ---")
    book_id = input("Enter Book ID to delete: ")

    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            save_data(books)
            print("🗑️ Book deleted successfully!\n")
            return

    print("❌ Book not found.\n")
       
    
    

def admin_menu():
    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Logout")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            print("👋 Logging out...")
            break
        else:
            print("Invalid choice! Try again.\n")

def user_menu():
    while True:
        print("\n========== USER MENU ==========")
        print("1. View All Books")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Logout")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_books()
        elif choice == '2':
            search_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("👋 Logging out...")
            break
        else:
            print("Invalid choice! Try again.\n")


def login():
    print("\n===============================================")
    print("     📚 LIBRARY MANAGEMENT SYSTEM     ")
    print("===============================================")
    print("\nLogin as:")
    print("1. Admin")
    print("2. User")

    role = input("Enter choice (1-2): ")

    if role == '1':
        password = input("Enter admin password: ")
        if password == "admin123":
            print("\n✅ Login successful! Welcome, Admin.")
            admin_menu()
        else:
            print("❌ Incorrect password! Access denied.\n")
            login()
    elif role == '2':
        print("\n👋 Welcome, User.")
        user_menu()
    else:
        print("Invalid choice! Try again.\n")
        login()

books = load_data()
login()
input("\nPress Enter to exit...")
