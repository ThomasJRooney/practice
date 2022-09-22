# O(nlogn) time | O(n) space
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    l = array[:mid]
    r = array[mid:]
    return merge(mergeSort(l), mergeSort(r))

def merge(left, right):
    sortedArray = [None] * (len(left) + len(right))
    k = i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedArray[k] = left[i]
            i += 1
        else:
            sortedArray[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        sortedArray[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        sortedArray[k] = right[j]
        j += 1
        k += 1
    return sortedArray
