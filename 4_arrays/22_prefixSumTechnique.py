"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NjQxMg%3D%3D
Use prefixSumTechnique to efficiently print sum of ranges without having to iterate over array multiple times
"""


def prefixSumTechnique(arr,q):
    prefix=[0] #Always a good idea to create a prefix sum array for length +1 since arr references become easier
    for i in range(len(arr)):
        prefix.append(arr[i]+prefix[i])
    for arr1 in q:
        print(prefix[arr1[1]]-prefix[arr1[0]])

q =[ [ 2, 3 ],[ 4, 6 ],[ 1, 5 ],[ 3, 6 ]]
prefixSumTechnique([ 3, 6, 2, 8, 9, 2 ],q)
