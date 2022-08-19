'''
Linear Search Alghotithm
'''

#iterative approach
def linear_search(arr, n, target):
    """
    It searches for a target value in a list of numbers.
    
    :param arr: the array to search
    :param n: the length of the array
    :param target: the value we're looking for
    """
    for i in range(0,n):
        if arr[i] == target:
            print("Found at index: ", i)
            return i
    print("Array is exhuausted")
    return -1

# Creating an array of numbers.
arr = [1,2,3,4,5,6,7,8,9,11,23,45,67,33,89,32,44,65,234,256,990,100]

# Asking the user to input a number.
target = int(input("Enter the target number: "))

# Getting the length of the array.
n = len(arr)

# Printing the result of the function.
print(linear_search(arr, n, target))

# Recursive approach
def linear_search2(arr, index, target):
    if index == -1:
        print("The array is exhausted")
        return -1
    if arr[index] == target:
        print("Key Found", index)
        return index
    return linear_search2(arr, index - 1, target)

# Creating an array of numbers.
arr = [1,2,3,4,5,6,7,8,9,11,23,45,67,33,89,32,44,65,234,256,990,100]

# Asking the user to input a number.
target = int(input("Enter the target number: "))

index = len(arr) - 1

linear_search2(arr, index, target)