from common import is_sorted, print_list

def bubble_sort(ls):
    n = len(ls)
    i = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
        #print_list(ls, "Sorted " + str(i+1) + " time: ")
    return ls


#a = [4,3,1,5,2]
n = 10000
a = []
for i in range(0, n):
    a.append(n-i)

#print_list(a, "Before: ")
bubble_sort(a)
is_sorted(a)
#print_list(a, "After: ")
