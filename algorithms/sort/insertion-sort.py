'''
Insertion Sort

Compare elements to the left, then shift elements to the right
to insert a value

O(n^2)
BAD for large data set

Less steps than Bubble Sort, best case is O(n) compared to
Selection Sort O(n^2)
'''

def insertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1

        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp


if __name__ == "__main__":
    list = [9,1,8,2,7,3,6,5,4]
    print(list)

    insertionSort(list)

    print(list)