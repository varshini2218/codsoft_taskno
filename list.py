import os

def show_menu():
    print("Your To-Do List Menu:")
    print("1> View To-Do List")
    print("2> Add Item to To-Do List")
    print("3> Update Item in To-Do List")
    print("4> Exit")

def view_todo_list():
    with open("todo.txt", "r") as f:
        todo_items = f.readlines()
        if not todo_items:
            print("Your to-do list is empty!")
        else:
            print("Your To-Do List:")
            for idx, item in enumerate(todo_items, start=1):
                print(f"{idx}. {item.strip()}")

def add_to_todo_list():
    new_item = input("Enter new item: ")
    with open("todo.txt", "a") as f:
        f.write(new_item + "\n")
    print("Item added to your to-do list.")

def update_todo_list():
    view_todo_list()
    index = int(input("Enter the index of the item to update: "))
    updated_item = input("Enter updated item: ")
    with open("todo.txt", "r") as f:
        todo_items = f.readlines()
    todo_items[index - 1] = updated_item + "\n"
    with open("todo.txt", "w") as f:
        f.writelines(todo_items)
    print("To-Do list updated.")

def main():
    if not os.path.exists("todo.txt"):
        open("todo.txt", "w").close()  # Create todo.txt if it doesn't exist

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_to_todo_list()
        elif choice == "3":
            update_todo_list()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()