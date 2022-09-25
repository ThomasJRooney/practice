#O(nlog(n)) time | O(log(n)) space
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start, end):
    if start >= end:
        return
    pivot = start
    l = start + 1
    r = end
    while r >= l:
        if array[l] > array[pivot] and array[r] < array[pivot]:
            swap(l, r, array)
        if array[l] <= array[pivot]:
            l += 1
        if array[r] >= array[pivot]:
            r -= 1
    swap(pivot, r, array)
    leftSmaller = r - 1 - start < end - (r + 1)
    if leftSmaller:
        quickSortHelper(array, start, r - 1)
        quickSortHelper(array, r + 1, end)
    else:
        quickSortHelper(array, r + 1, end)
        quickSortHelper(array, start, r - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
