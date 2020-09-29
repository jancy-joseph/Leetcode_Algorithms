'''
1. Find the element that appears once in a sorted array where all other elements appear twice one after another. 
Find that element in 0(logn) complexity.
Input: arr[]={1,1,3,3,4,5,5,7,7,8,8} 
             0 1 2 3 4 5 6 7 8 9 10
Output: 4


Solution 1:
1. Check first element and second elment if they are same 
 if they are same skip one element and test 3 rd and 4 th element
 if they are not same then return the element compared.
 Do the same steps  1-3  till we reach end of array
 if no different element found say we have nounique element

 solution 2: Xor the elements
 
 


'''

class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        
        sum = arr[0]
        for i in range(1, len(arr)):
            sum = sum ^ arr[i]
        return sum
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends

########

#### c Sharp solution
################
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        int lowIndex=0;
        int highIndex = nums.Length -1;
        
        while(lowIndex < highIndex){
            //check if index is odd or even
            int midIndex = (lowIndex+highIndex)/2;
            if (midIndex % 2 == 1) midIndex--;

            // We didn't find a pair. The single element must be on the left.
            // (pipes mean start & end)
            // Example: |0 1 1 3 3 6 6|
            //               ^ ^
            // Next:    |0 1 1|3 3 6 6
            if (nums[midIndex] != nums[midIndex + 1]) highIndex = midIndex;

            // We found a pair. The single element must be on the right.
            // Example: |1 1 3 3 5 6 6|
            //               ^ ^
            // Next:     1 1 3 3|5 6 6|
            else lowIndex = midIndex + 2;
        }
        return nums[lowIndex];
    }
}

################################
#####c Sharp solution
##########################
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        
        int res = nums[0];
        for(int i = 1; i< nums.Length; i++){
            res = res ^ nums[i];
        }
        return res;
        
    }
}