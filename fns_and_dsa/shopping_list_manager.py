def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            items = input("Enter Your Item You Want To Add To The List: ")
            shopping_list.append(items)
            for item in shopping_list:
                print(shopping_list)
            pass
        elif choice == '2':
            items = input("Enter Your Item You Want To Remove From The List: ")
            shopping_list.remove(items)
            for item in shopping_list:
                print(shopping_list)
            pass
        elif choice == '3':
            for items in shopping_list:
                print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()