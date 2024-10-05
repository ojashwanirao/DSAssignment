class ArrayQueue:
    def __init__(self, capacity=10):
        """Initialize the queue with a specific capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity  # Initialize array with None
        self.front = -1  # Indicates the front of the queue
        self.rear = -1   # Indicates the rear of the queue
        self.size = 0    # Current size of the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity

    def enqueue(self, item):
        """Insert an element at the rear of the queue."""
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item}. Queue size is now {self.size}.")

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed_item = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the spot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued {removed_item}. Queue size is now {self.size}.")
        return removed_item

    def display(self):
        """Display the current elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements are:")
            index = self.front
            for i in range(self.size):
                print(self.queue[index], end=" ")
                index = (index + 1) % self.capacity
            print()

    def exit(self):
        """Exit the program (Dummy method for now)."""
        print("Exiting the queue program.")
        exit()

# Example usage
if __name__ == "__main__":
    queue = ArrayQueue(5)  # Queue with capacity of 5

    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Display elements
    queue.display()

    # Dequeue elements
    queue.dequeue()
    queue.display()

    # More enqueue and display
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)  # Queue is now full
    queue.display()

    # Try to enqueue when full
    queue.enqueue(70)

    # Dequeue and exit
    queue.dequeue()
    queue.display()
    queue.exit()
