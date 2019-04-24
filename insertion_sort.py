def insertion_sort(ls):
    # show before
    #print("Before: " + ",".join([str(n) for n in ls]))

    for i in range(0, len(ls)):
        v = ls[i]
        j = i
        while j > 0:
            if ls[j-1] > v:
                #print("swapping")
                ls[j] = ls[j-1]
                j -= 1
            else:
                break
        ls[j] = v
        # show intermediate result
        #print(str(i+1) + " times sorted: " + ",".join([str(n) for n in ls]))

    #print("After: " + ",".join([str(n) for n in ls]))
    return ls

def is_sorted(ls):
    for i in range(0, len(ls)-1):
        if ls[i] > ls[i+1]:
            print("Not sorted!")
            return False
    print("Sorted!")
    return True

#a = [4,3,1,5,2]
#insertion_sort(a)

#a = [9,8,7,6,5,4,3,2,1,0]
n = 10000
a = []
for i in range(0, n):
    a.append(n-i)
is_sorted(insertion_sort(a))
