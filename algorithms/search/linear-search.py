'''
Linear Search

Iterate through a collection one element at a time
O(n) runtime complexity

Disadvantages:
Slow for large datasets

Advantages:
Fast for small to medium
Does not need to be sorted
Useful for structures with no random access like a linked list

'''

def linearSearch(list, value):

    # Return index if found
    for i in range(0, len(list)):
        if list[i] == value:
            return i

    # Return -1 if not found
    return -1

if __name__ == "__main__":

    list = [2,1,4,5,6,7,9,8]

    value = 1
    index = linearSearch(list, value)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
