"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/rearrange-an-array-with-o1-extra-space3142

Principle here is that in order to store 2 values a and b in a cell with value a, modify a as :

a = a + bn

a%n yields a and a/n yields b

Note: the %n tricks works iff max(arr) <= n. Or better instead of %n use %max(arr). It just needs largest item in arr
"""


def rearrangeWithO1ExtraSpace(arr, n):
    # First step: Increase all values
    # by (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n #Note u need the %n here since you are modifying arr[i] as you go. %n will make
        # this seemless for modified and unmodified arr[i]

    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)

# A utility function to print
# an array of size n


def printArr(arr, n):

    for i in range(0, n):
        print(arr[i], end=" ")
    print("")


# Driver program
arr = [3, 2, 0, 1]
n = len(arr)

print("Given array is")
printArr(arr, n)

rearrangeWithO1ExtraSpace(arr, n)
print("Modified array is")
printArr(arr, n)

