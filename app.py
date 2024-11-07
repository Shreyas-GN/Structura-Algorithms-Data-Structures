import streamlit as st

# Content dictionary for data structures and algorithms with expanded explanations
content = {
    "Data Structures": {
        "Arrays": {
            "definition": (
                "An array is a data structure that stores a collection of elements in contiguous memory locations. "
                "Each element in the array can be accessed via its index, which is its position in the array, starting from 0. "
                "Arrays store elements of the same type and are useful for managing data in a simple, sequential way."
            ),
            "usage": (
                "Arrays are commonly used when you need to store multiple values of the same type in a fixed-size collection. "
                "They allow fast access to elements by index, making them efficient for scenarios where data access is frequent. "
                "However, because arrays have a fixed size, they are less suited for situations where the number of items changes frequently. "
                "Example use cases include storing lists of scores, managing grids in games, or representing a series of readings."
            ),
            "example": (
                "Example: A list of test scores can be represented as an array of integers:\n\n"
                "scores = [85, 90, 78, 92, 88]\n"
                "print(scores[0])  # Output: 85\n"
            ),
            "code": """
# An array of integers representing scores
scores = [85, 90, 78, 92, 88]
print(scores[0])  # Output: 85
            """
        },
        "Linked Lists": {
            "definition": (
                "A linked list is a data structure where each element (called a node) contains data and a reference (or link) to the next node. "
                "Unlike arrays, linked lists do not require contiguous memory locations, allowing for dynamic memory allocation. "
                "This means you can add or remove nodes without needing to shift other elements around, making linked lists ideal for operations "
                "where data is frequently inserted or removed."
            ),
            "usage": (
                "Linked lists are useful when you need a data structure that supports frequent insertions and deletions. "
                "They allow easy expansion and contraction as nodes are added or removed. "
                "Linked lists are often used in scenarios like managing a playlist of songs, undo functionality in software, and implementing "
                "queues or stacks. There are several types of linked lists, including singly linked lists, doubly linked lists, and circular linked lists."
            ),
            "example": (
                "Example: A linked list storing the numbers 1, 2, 3, and 4:\n\n"
                "1 -> 2 -> 3 -> 4"
            ),
            "code": """
# Conceptual example of a linked list: 
# 1 -> 2 -> 3 -> 4

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating linked list nodes
head = Node(1)
second = Node(2)
head.next = second
# Adding a third node
third = Node(3)
second.next = third
            """
        },
        "Stacks": {
            "definition": (
                "A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. "
                "In a stack, you can only add (push) or remove (pop) items from the top of the stack. "
                "Stacks are often compared to a stack of plates where you can only add or remove a plate from the top."
            ),
            "usage": (
                "Stacks are useful for scenarios requiring temporary data storage, especially when data needs to be accessed in reverse order. "
                "They are widely used in implementing function calls in programming, managing undo actions in software, and for evaluating expressions. "
                "For example, when a function calls another function, it is added to the call stack, and once it finishes, it is removed from the stack."
            ),
            "example": (
                "Example Operations: Push items to the stack and pop the last item.\n\n"
                "stack = []\n"
                "stack.append(1)  # Push\n"
                "stack.append(2)\n"
                "print(stack.pop())  # Output: 2"
            ),
            "code": """
# Stack implementation in Python
stack = []
stack.append(1)  # Push 1 onto stack
stack.append(2)  # Push 2 onto stack
print(stack.pop())  # Pop from stack, output: 2
            """
        },
        "Queues": {
            "definition": (
                "A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. "
                "In a queue, elements are added at the back (enqueue) and removed from the front (dequeue). "
                "It is analogous to a line of people where the first person in line is the first to be served."
            ),
            "usage": (
                "Queues are ideal for scenarios that involve sequential processing. They are widely used in scheduling tasks, managing requests in web servers, and "
                "controlling print jobs in printers. In programming, queues are used to handle processes in a system, especially where processing order matters."
            ),
            "example": (
                "Example Operations: Enqueue items and dequeue from the front.\n\n"
                "queue = deque([1, 2, 3])\n"
                "queue.append(4)  # Enqueue\n"
                "print(queue.popleft())  # Output: 1 (Dequeue)"
            ),
            "code": """
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # Enqueue 4 to queue
print(queue.popleft())  # Output: 1 (Dequeues 1)
            """
        },
        "Trees": {
            "definition": (
                "A tree is a hierarchical data structure that consists of nodes connected by edges. "
                "The topmost node is called the root, and each node has zero or more child nodes. "
                "A tree with each node having at most two children is called a binary tree."
            ),
            "usage": (
                "Trees are used in scenarios that require hierarchical organization. They are common in file systems, database indexing, and in representing organizational structures. "
                "In computer science, binary trees are commonly used in binary search trees (BST) for fast data retrieval, while more complex trees like AVL and B-trees optimize data balancing and access speed."
            ),
            "example": (
                "Example of a Binary Tree:\n\n"
                "       1\n"
                "      / \\\n"
                "     2   3\n"
            ),
            "code": """
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
            """
        }
    },
    "Algorithms": {
        "Linear Search": {
            "definition": (
                "Linear search is a straightforward search algorithm that checks each element in a list one by one to find the target value. "
                "It works on both sorted and unsorted lists but is generally slower for large datasets compared to other algorithms."
            ),
            "usage": (
                "Linear search is used when dealing with unsorted data or when a list is small and other search algorithms may be unnecessary. "
                "Its simplicity makes it easy to implement but it has a linear time complexity (O(n)), which makes it less efficient for large datasets."
            ),
            "example": (
                "Example: Finding a value in a list\n\n"
                "def linear_search(arr, target):\n"
                "    for i in range(len(arr)):\n"
                "        if arr[i] == target:\n"
                "            return i\n"
                "    return -1\n\n"
                "print(linear_search([3, 1, 4, 2], 4))  # Output: 2"
            ),
            "code": """
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Using linear search to find an element
print(linear_search([3, 1, 4, 2], 4))  # Output: 2
            """
        },
        "Binary Search": {
            "definition": (
                "Binary search is an efficient algorithm for finding an item from a sorted list of items. "
                "It works by dividing the list in half, determining if the target is in the left or right half, and repeating this process until the target is found."
            ),
            "usage": (
                "Binary search is ideal for large, sorted datasets where you need to find elements quickly. "
                "It has a time complexity of O(log n), making it significantly faster than linear search for large lists. "
                "Binary search is commonly used in dictionaries, databases, and other applications that require fast lookups."
            ),
            "example": (
                "Example: Binary search on a sorted list\n\n"
                "def binary_search(arr, target):\n"
                "    low, high = 0, len(arr) - 1\n"
                "    while low <= high:\n"
                "        mid = (low + high) // 2\n"
                "        if arr[mid] == target:\n"
                "            return mid\n"
                "        elif arr[mid] < target:\n"
                "            low = mid + 1\n"
                "        else:\n"
                "            high = mid - 1\n"
                "    return -1\n\n"
                "print(binary_search([1, 2, 3, 4, 5], 4))  # Output: 3"
            ),
            "code": """
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 4))  # Output: 3
            """
        }
    }
}

# Streamlit app layout
st.title("Structura: Algorithms & Data Structures")

# Main menu for choosing Data Structures or Algorithms
category = st.selectbox("Select Category", list(content.keys()))

# Submenu to select specific data structure or algorithm
topic = st.selectbox("Select a Topic", list(content[category].keys()))

# Displaying content
st.subheader(f"{topic}")
st.write("**Definition:**", content[category][topic]["definition"])
st.write("**Usage:**", content[category][topic]["usage"])
st.write("**Example:**", content[category][topic]["example"])
st.code(content[category][topic]["code"], language="python")
