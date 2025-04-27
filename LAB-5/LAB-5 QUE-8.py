print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

class Stack:
    def __init__(self):
        self.stack = []
    
    # Push operation: Add an item to the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Item {item} pushed to the stack.")

    # Pop operation: Remove an item from the stack
    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Item {item} popped from the stack.")
        else:
            print("Stack is empty. Cannot pop.")

    # Peek operation: View the top item of the stack
    def peek(self):
        if not self.is_empty():
            print(f"Top item of the stack is {self.stack[-1]}")
        else:
            print("Stack is empty. No top item.")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack
    def display(self):
        if not self.is_empty():
            print("Stack:", self.stack)
        else:
            print("Stack is empty.")

# Main program
def main():
    stack = Stack()
    
    while True:
        # Menu-driven options
        print("\nMenu:")
        print("1. Push an element to the stack")
        print("2. Pop an element from the stack")
        print("3. Peek at the top element")
        print("4. Display the stack")
        print("5. Exit")
        
        # User input for operation
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item = int(input("Enter an item to push: "))
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
