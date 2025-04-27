print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation: Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item {item} enqueued to the queue.")

    # Dequeue operation: Remove an element from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Item {item} dequeued from the queue.")
        else:
            print("Queue is empty. Cannot dequeue.")

    # Get the front element
    def front(self):
        if not self.is_empty():
            print(f"Front item in the queue is {self.queue[0]}")
        else:
            print("Queue is empty. No front item.")

    # Get the rear element
    def rear(self):
        if not self.is_empty():
            print(f"Rear item in the queue is {self.queue[-1]}")
        else:
            print("Queue is empty. No rear item.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        if not self.is_empty():
            print("Queue:", self.queue)
        else:
            print("Queue is empty.")

# Main program
def main():
    queue = Queue()

    while True:
        # Menu-driven options
        print("\nMenu:")
        print("1. Enqueue an element to the queue")
        print("2. Dequeue an element from the queue")
        print("3. Get front element")
        print("4. Get rear element")
        print("5. Display the queue")
        print("6. Exit")

        # User input for operation
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = int(input("Enter an item to enqueue: "))
            queue.enqueue(item)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.front()
        elif choice == '4':
            queue.rear()
        elif choice == '5':
            queue.display()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
