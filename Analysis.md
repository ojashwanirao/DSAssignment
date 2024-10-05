# Algorithm Analysis for Static Arrays

## Overview
This document provides an analysis of the time and space complexities associated with the operations implemented in the static array data structure. The analysis is categorized based on each operation performed.

## 1. Static Array (1-Dimensional)

### Operations:
1. Insertion
   - Description: Adds an element at a specified index in the array.
   - Time Complexity: O(n) in the worst case (if shifting elements is required).
   - Space Complexity: O(1) as no additional space is used apart from the existing array.

2. Deletion
   - Description: Removes an element from a specified index and shifts subsequent elements left.
   - Time Complexity: O(n) in the worst case (if shifting elements is required).
   - Space Complexity: O(1) as it uses the existing array space.

3. Traversal
   - Description: Visits each element in the array to display or process them.
   - Time Complexity: O(n) as it requires iterating through all elements.
   - Space Complexity: O(1) since it does not use additional space apart from a variable for iteration.

4. Addition (Row-wise)**
   - Description: Sums up all elements in the array.
   - Time Complexity: O(n) as it requires visiting each element.
   - Space Complexity: O(1) as it uses a constant amount of space for storing the sum.

5. **Cumulative Addition**
   - **Description**: Computes cumulative sums for each element in the array.
   - **Time Complexity**: O(n) as it requires visiting each element.
   - **Space Complexity**: O(1) if cumulative sums are stored back in the same array; O(n) if a separate array is used.

6. **Subtraction**
   - **Description**: Subtracts a value from each element in the array.
   - **Time Complexity**: O(n) as it requires visiting each element.
   - **Space Complexity**: O(1) as it operates in-place.

## 2. Static Array (2-Dimensional)

### Operations:
1. **Insertion**
   - **Description**: Adds an element at a specified index in a 2D array (row, column).
   - **Time Complexity**: O(1) if the position is directly accessed; O(n*m) if shifting is required for maintaining the structure.
   - **Space Complexity**: O(1) as it uses the existing array space.

2. **Deletion**
   - **Description**: Removes an element from a specified position and shifts elements accordingly.
   - **Time Complexity**: O(n*m) in the worst case (if shifting is required).
   - **Space Complexity**: O(1) as it uses the existing array space.

3. **Traversal**
   - **Description**: Visits each element in the 2D array.
   - **Time Complexity**: O(n*m) where n is the number of rows and m is the number of columns.
   - **Space Complexity**: O(1) as it uses a constant amount of space for iteration.

4. **Addition (Row-wise)**
   - **Description**: Sums up all elements in each row.
   - **Time Complexity**: O(n*m) as it requires visiting each element.
   - **Space Complexity**: O(1) if results are stored in a single variable.

5. **Cumulative Addition**
   - **Description**: Computes cumulative sums for each row in the 2D array.
   - **Time Complexity**: O(n*m) as it requires visiting each element.
   - **Space Complexity**: O(1) if cumulative sums are stored back in the same structure.

6. **Subtraction**
   - Description: Subtracts a value from each element in the 2D array.
   - Time Complexity: O(n*m) as it requires visiting each element.
   - Space Complexity: O(1) as it operates in-place.

## Conclusion
The analysis shows that most operations on static arrays have a time complexity of O(n) or O(n*m) depending on whether they are one-dimensional or two-dimensional. Space complexity for all operations remains optimal at O(1), utilizing existing memory without requiring additional space. 

Understanding these complexities is crucial for optimizing performance in applications using static arrays.



# Algorithm Analysis for stack 

## Time Complexity:
1. Push Operation: O(1)
   - The push operation takes constant time since we simply append an element to the end of the list.

2. Pop Operation: O(1)
   - The pop operation also takes constant time because we remove the last element of the list.

3. Display Operation: O(n)
   - Displaying the elements requires iterating through the list, resulting in linear time complexity.

4. Size Operation**: O(1)
   - Retrieving the current size of the stack is done in constant time.

## Space Complexity:
- The space complexity of the stack is O(n) where n is the capacity of the stack, as we may need to store up to 'n' elements in the stack.

# Algorithm analysis for  Array Queue
## Time and Space Complexity Analysis

1. Insertion (enqueue):
Time Complexity: O(1) (Inserting at the rear using modular arithmetic to handle the circular nature)
Space Complexity: O(1) for the operation, O(n) for the array storage

2. Deletion (dequeue):
Time Complexity: O(1) (Removing from the front using modular arithmetic)
Space Complexity: O(1) for the operation, O(n) for the array storage

3.Display:
Time Complexity: O(n) (where n is the number of elements in the queue)
Space Complexity: O(1) for the operation, O(n) for the array storage

4.Exit:
Time Complexity: O(1)
Space Complexity: O(1)