'''
Binary Search

Half of data is eliminated after each iteration
O(log n) runtime complexity

Disadvantages:
Slow for small datasets
Data needs to be sorted

Advantages:
Fast for large datasets

'''

def binarySearch(list, value):

    # Return index if found, -1 if not found
    # assume list is sorted in increasing order

    left = 0
    right = len(list)

    while left <= right:
        mid = (left + right) // 2
        #print(mid)
        midValue = list[mid]
        if midValue == value:
            return mid
        elif midValue < value:
            left = mid - 1
        elif midValue > value:
            right = mid + 1

    return -1

if __name__ == "__main__":

    list = [i for i in range(0, 100)]

    value = 34
    index = binarySearch(list, value)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")


