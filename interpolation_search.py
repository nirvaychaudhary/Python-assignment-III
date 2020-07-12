# Interpolation search

def interpolation(arr, x):
    low = 0
    high = len(arr)-1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + int(((x - arr[low])/(arr[high]-arr[low]))* (high-low))

        if arr[pos] == x:
            return pos

        elif arr[pos] < x:
            low = pos + 1

        else:
            low = pos-1

    return -1

arr = [1,3,5,7,9,13,15]
x = int(input("Enter any number to search: "))
index = interpolation(arr, x)

if index != -1:
    print("Found at", index)

else:
    print("Not found")

