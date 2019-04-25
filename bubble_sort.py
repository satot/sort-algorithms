def bubble_sort(ls):
    n = len(ls)
    i = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if ls[j] > ls[j+1]:
                tmp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = tmp
        #print_list(ls, "Sorted " + str(i+1) + " time: ")
    return ls

def print_list(ls, prefix=""):
    print(prefix + "[" + ",".join([str(n) for n in ls]) + "]")
    return

def is_sorted(ls):
    for i in range(0, len(ls)-1):
        if ls[i] > ls[i+1]:
            print("Not sorted!")
            return False
    print("Sorted!")
    return True

#a = [4,3,1,5,2]
n = 10000
a = []
for i in range(0, n):
    a.append(n-i)

#print_list(a, "Before: ")
bubble_sort(a)
is_sorted(a)
#print_list(a, "After: ")
