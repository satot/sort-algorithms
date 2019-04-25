def is_sorted(ls):
    for i in range(0, len(ls)-1):
        if ls[i] > ls[i+1]:
            print("Not sorted!")
            return False
    print("Sorted!")
    return True

def print_list(ls, prefix=""):
    print(prefix + "[" + ",".join([str(n) for n in ls]) + "]")
    return
