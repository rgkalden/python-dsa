'''
Interpolation Search

Improves over binary search
Best used for uniformly distributed data

Guesses where a value mimght be based on calculated probe results
If probe is incorrect, search area is narrowed, and a new probe is calculated
Assume sorted in increasing order

Average case O(log(log(n)))
Worst case O(n)

'''

def interpolationSearch(list, value):
    low = 0
    high = len(list) - 1

    while (value >= list[low] and value <= list[high] and low <= high):
        probe = int(low + (high - low) * (value - list[low]) / (list[high] - list[low]))
        print("Probe:", probe)
        if list[probe] == value:
            return probe
        elif list[probe] < value:
            low = probe + 1
        else:
            high = probe - 1

    return -1

if __name__ == "__main__":

    list = [1,2,3,4,5,6,7,8,9]
    list2 = [1,2,4,8,16,32,64,128,256,512,1024]
    value = 1
    value2 = 256
    index = interpolationSearch(list2, value2)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")

