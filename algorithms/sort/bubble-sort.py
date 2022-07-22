'''
Bubble Sort

Pairs of adjacent elements are compared
Elements are swapped of they are not in order

O(n^2)
Small data set is alright
Large data set is bad
'''

def bubbleSort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - i - 1):
            # > for ascending, < for descending sort
            if (list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


if __name__ == "__main__":

    list = [9,1,8,2,7,3,6,4,5]
    print("Original list")
    print(list)

    bubbleSort(list)
    print("Sorted List")
    print(list)