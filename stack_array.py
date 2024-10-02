# Array Stack Implementation
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the stack
        self.stack = []  # Initialize an empty list to hold stack elements

    def push(self, value):
        """Insert an element onto the top of the stack."""
        if len(self.stack) < self.capacity:
            self.stack.append(value)
            print(f"Pushed {value} onto the stack.")
        else:
            print("Stack overflow. Cannot push value.")

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            value = self.stack.pop()
            print(f"Popped {value} from the stack.")
            return value
        else:
            print("Stack underflow. Cannot pop value.")
            return None

    def display(self):
        """Display the elements in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the current size of the stack."""
        return len(self.stack)

# Example usage
if __name__ == "__main__":
    stack = ArrayStack(5) 
    stack.push(10) 
    stack.push(20) 
    stack.display() 
    stack.pop() 
    stack.display()  