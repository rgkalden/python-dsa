'''
Selection Sort

Search through a list and keep track of the minimum value during eachc iteration
at the end of each iteration, swap variables

O(n^2)
BAD for large datasets
'''

def selectionSort(list):

    for i in range(0, len(list) - 1):
        min = i
        for j in range(i+1, len(list)):
            # > for ascending, < for descending sort
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

if __name__ == "__main__":
    list = [8,7,9,2,3,1,5,4,6]
    print(list)

    selectionSort(list)

    print(list)