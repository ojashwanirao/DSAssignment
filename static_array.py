class StaticArray1D:
    def __init__(self, size):
        # Initialize the array with zeros and store the size
        self.array = [0] * size
        self.size = size

    def insert(self, index, value):
        # Insert value at the given index if index is within bounds
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            print("Index out of bounds.")

    def delete(self, index):
        # Set the value at the given index to 0
        if 0 <= index < self.size:
            self.array[index] = 0
        else:
            print("Index out of bounds.")

    def traverse(self):
        # Traverse and display all elements of the array
        for i in self.array:
            print(i, end=" ")
        print()

    def row_wise_addition(self):
        # Calculate and return the sum of all elements
        return sum(self.array)

    def cumulative_addition(self):
        # Calculate and return the cumulative sum of elements
        total = 0
        cumulative_sum = []
        for i in self.array:
            total += i
            cumulative_sum.append(total)
        return cumulative_sum

class StaticArray2D:
    def __init__(self, rows, cols):
        # Initialize a 2D array of size rows x cols with zeros
        self.array = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def insert(self, row, col, value):
        # Insert value at the specified row and column
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[row][col] = value
        else:
            print("Index out of bounds.")

    def delete(self, row, col):
        # Set the value at the specified row and column to 0
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[row][col] = 0
        else:
            print("Index out of bounds.")

    def traverse(self):
        # Traverse and display all elements of the 2D array
        for row in self.array:
            for col in row:
                print(col, end=" ")
            print()

    def row_wise_addition(self):
        # Calculate and return the sum of elements for each row
        row_sums = []
        for row in self.array:
            row_sums.append(sum(row))
        return row_sums

    def cumulative_addition(self):
        # Calculate and return the cumulative sum of all elements across rows
        total = 0
        cumulative_sum = []
        for row in self.array:
            for col in row:
                total += col
                cumulative_sum.append(total)
        return cumulative_sum

def main():
    print("Testing Static 1-D Array:")
    arr_1d = StaticArray1D(5)
    arr_1d.insert(0, 10)
    arr_1d.insert(1, 20)
    arr_1d.insert(2, 30)
    arr_1d.traverse()
    print("Row-wise addition:", arr_1d.row_wise_addition())
    print("Cumulative addition:", arr_1d.cumulative_addition())

    print("\nTesting Static 2-D Array (4x4):")
    arr_2d = StaticArray2D(4, 4)
    arr_2d.insert(0, 0, 5)
    arr_2d.insert(1, 1, 10)
    arr_2d.insert(2, 2, 15)
    arr_2d.traverse()
    print("Row-wise addition:", arr_2d.row_wise_addition())
    print("Cumulative addition:", arr_2d.cumulative_addition())

if __name__ == "__main__":
    main()
