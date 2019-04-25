from common import is_sorted, print_list

def insertion_sort(ls):
    for i in range(len(ls)):
        v = ls[i]
        j = i
        while j > 0:
            if ls[j-1] > v:
                ls[j] = ls[j-1]
                j -= 1
            else:
                break
        ls[j] = v
        #print_list(ls, "Sorted " + str(i+1) + " time: ")
    return ls

#a = [4,3,1,5,2]
#insertion_sort(a)

#a = [9,8,7,6,5,4,3,2,1,0]
n = 10000
a = []
for i in range(0, n):
    a.append(n-i)
#print_list(a, "Before: ")
is_sorted(insertion_sort(a))
#print_list(a, "After: ")
