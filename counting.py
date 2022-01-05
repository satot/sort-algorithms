import random
def counting_sort(array, k):
    result_array = [-1 for _ in array]
    # Array to count each element
    counting_array = [0 for _ in range(k)]
    
    # counting_array[i]: number of elements which is equal to i in the array
    # e.g. array [1, 4, 0, 2, 0] => counting_array [2, 1, 1, 0, 1]
    for i in range(len(array)):
        counting_array[array[i]] += 1
    print(counting_array)
    
    # counting_array[i]: number of elements which is less than i in the array
    # e.g. array [1, 4, 0, 2, 0] 
    #  => counting_array [2, 1, 1, 0, 1]
    #  => counting_array [2, 3, 4, 4, 5]
    for i in range(1, k):
        counting_array[i] += counting_array[i-1]
    print(counting_array)
    
    # Stable sort by populating the array from last element
    # e.g. array [1, 4, 0, 2, 0], counting_array [2, 3, 4, 4, 5]
    # number of 0 in array: 2 => result_array[-1, 0, -1, -1, -1]
    # next 0 would be populated before this index, hence this sort would be stable
    for i in range(len(array), 0, -1):
        cur = array[i-1]
        result_array[counting_array[cur]-1] = cur
        counting_array[cur] -= 1
        print(counting_array, result_array)
    
    return result_array

if __name__ == '__main__':
    random.seed(1)
    array = [random.randrange(10) for _ in range(20)]
    #array = [1,1,1,4,0,2,2,0]
    print("before", array)
    sorted_array = counting_sort(array, max(array)+1)
    print('after', sorted_array) 
