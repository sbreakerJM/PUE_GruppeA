import numpy as np

def bubble_sort(the_array_to_sort):
    temp_array = the_array_to_sort.copy()
    n = len(temp_array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_array[j] > temp_array[j + 1]:
                temp_array[j], temp_array[j + 1] = temp_array[j + 1], temp_array[j]
    
    return temp_array


if __name__ == "__main__":
    test_array = np.array([5, 2, 9, 1, 5, 6])
    print(bubble_sort(test_array))
 