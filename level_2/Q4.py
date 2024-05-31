# Given an array of size N. The task is to rotate array by D elements towards right
# Sample Input: arr = [1, 2, 3, 4, 5], D = 2
# Sample Output: arr after rotation = [4, 5, 1, 2, 3]

def rotate_array(arr, D):
    D = D % len(arr)
    rotated_arr = arr[-D:] + arr[:-D]
    return rotated_arr

arr = input("Enter the elements of the array separated by spaces: ")
arr.split()
arr = [int(x) for x in arr]
D = int(input("Enter the number of rotations: "))
result = rotate_array(arr, D)
print("Array after rotation: {}".format(result))
