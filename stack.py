stack = []

def push():
    item = input("Enter the item to push: ")
    stack.append(item)
    print(f"{item} has been pushed onto the stack.")
    def pop():
    if not stack:
        print("Stack is empty. Nothing to pop.")
    else:
        item = stack.pop()
        print(f"Popped item: {item}")

        def peek():
    if not stack:
        print("Stack is empty. Nothing to peek.")
    else:
        print(f"Top of the stack: {stack[-1]}")
        def is_empty():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack is not empty.")

        def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack elements (bottom to top):")
        for item in stack:
            print(item)
while True:
    print("\nStack Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Stack is Empty")
    print("5. Display Stack")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        is_empty()
    elif choice == '5':
        display()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
