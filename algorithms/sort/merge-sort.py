'''
Merge Sort

merge sort = recursively divide array in 2, sort, re-combine

run-time complexity = O(n Log n)
space complexity    = O(n)

Sorts ascending in this example
'''

def merge(leftList, rightList, list):
    leftSize = len(list) // 2
    rightSize = len(list) - leftSize

    i, l, r = 0, 0 ,0

    while l < leftSize and r < rightSize:
        if leftList[l] < rightList[r]:
            list[i] = leftList[l]
            i += 1
            l += 1
        else:
            list[i] = rightList[r]
            i += 1
            r += 1

    while l < leftSize:
        list[i] = leftList[l]
        i += 1
        l += 1

    while r < rightSize:
        list[i] = rightList[r]
        i += 1
        r += 1

def mergeSort(list):
    length = len(list)
    if length <= 1:
        return # base case

    middle = length // 2
    leftList = list[:middle]
    rightList = list[middle:]

    i = 0 # left list
    j = 0 # right list

    for i in range(0, length):
        if i < middle:
            leftList[i] = list[i]
        else:
            rightList[j] = list[i]
            j += 1
    mergeSort(leftList)
    mergeSort(rightList)
    merge(leftList, rightList, list)

if __name__ == "__main__":
    
    list = [8,2,5,3,4,7,6,1]
    print(list)

    mergeSort(list)

    print(list)