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
