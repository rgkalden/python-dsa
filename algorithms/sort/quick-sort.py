'''
Quick Sort

quick sort = moves smaller elements to left of a pivot.

recursively divide array in 2 partitions

run-time complexity = Best case O(n log(n))
Average case O(n log(n))
Worst case O(n^2) if already sorted

space complexity    = O(log(n)) due to recursion

Pivot begins at the end
Sort ascending
'''


def partition(list, start, end):

    pivot = list[end]
    i = start - 1

    for j in range(start, end):
        if list[j] < pivot:
            i += 1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    i += 1
    temp = list[i]
    list[i] = list[end]
    list[end] = temp

    return i # location of pivot

def quickSort(list, start, end):
    if end <= start:
        return # base case

    pivot = partition(list, start, end)

    quickSort(list, start, pivot - 1)
    quickSort(list, pivot + 1, end)



if __name__ == "__main__":

    list = [8,2,5,3,9,4,7,6,1]
    print(list)

    quickSort(list, 0, len(list) - 1)

    print(list)