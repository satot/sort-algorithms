from common import is_sorted, print_list

def merge_sort(aList):
    if len(aList) <= 1:
        return aList

    mid = len(aList) // 2
    left = aList[:mid]
    right = aList[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])

    return sorted_list


n = 100000
a = []
for i in range(0, n):
    a.append(n-i)

is_sorted(merge_sort(a))
