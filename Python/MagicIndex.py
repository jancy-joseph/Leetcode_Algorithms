'''
2. A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i. 
Given a sorted array of distinct integers,  
write a method to find a magic index if one exists, in an array A. 
FOLLOW UP: What if the values are not distinct?

-1 1 7 8 9 10 11
0 1 2 3 4 5 6 7


brute force solution
go through each element and check which has a[i] equal to i

binary search

find mid (3) and check if value is 8 is > or < mid index (3)
if it is same then return mid
else
if it greater we need to look at left side so high is mid -1
if it lesser low becomes mid+1 


'''

def findMagicIndex(numarray, low, high):
    if len(numarray) == 0 :
        return -1
    if low == high  and numarray[low]!= low:
        return -1
    mid = (low +high)/2
    if numarray[mid] == mid :
        return mid
    elif numarray[mid] > mid :
        return findMagicIndex(numarray,0,mid -1)
    elif numarray[mid]< mid :
        return findMagicIndex(numarray,mid+1, high)


nums = [-1,1,7,8,9,10,11]
print (nums)
print(findMagicIndex(nums, 0, len(nums) - 1))