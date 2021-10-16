from common import is_sorted
import unittest

# --- out ------------------------------------------------------------------ #

def find_pivot(array):
    left, right = 0, len(array)-1
    mid = (left + right)//2
    candidates = [array[left], array[mid], array[right]]
    for i in range(2):
        for j in range(2-i):
            if candidates[j] > candidates[j+1]:
                candidates[j], candidates[j+1] = candidates[j+1], candidates[j]
    return candidates[1]

def quick_sort_out(array):
    if len(array) <= 1:
        return array
    less, pivot, greater = [], [], []
    for i in array:
        p = find_pivot(array)
        if i > p:
            greater.append(i)
        elif i < p:
            less.append(i)
        else:
            pivot.append(i)
    return quick_sort_out(less) + pivot + quick_sort_out(greater)

# --- in ------------------------------------------------------------------ #

def partition(arr, low, high):
    i = low-1 # boundary (smaller than pivot)
    pivot = arr[high]
    #print(arr, low, high)

    for j in range(low, high):
        # move an element smaller than pivot to front
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    # move pivot to the boundary
    arr[i+1], arr[high] = arr[high], arr[i+1]
    # index of pivot
    return i+1


def quick_sort_in(arr, low, high):
    if len(arr) <= 1:
        return arr
    if low < high:
        p = partition(arr, low, high)

        quick_sort_in(arr, low, p-1)  # all arr[low:p-1] < arr[p] (pivot)
        quick_sort_in(arr, p+1, high) # all arr[p+1:high] > arr[p] (pivot)

# ------------------------------------------------------------------------- #


class TestFunc(unittest.TestCase):
    def test_in_1(self):
        arr = [9,6,8,2,5,10,3,7,1]
        quick_sort_in(arr, 0, len(arr)-1)
        self.assertTrue(is_sorted(arr))

    def test_out_1(self):
        arr = [9,6,8,2,5,10,3,7,1]
        self.assertTrue(is_sorted(quick_sort_out(arr)))

if __name__ == "__main__":
    unittest.main()
