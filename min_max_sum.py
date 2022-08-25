'''
Time complexity
O(1) => 2+3
O(log(n)) => includes for example divide function
O(n) => iterating over a loop of n
O(n^2) => 2 for loops with n number of inputs
'''

'''
My Approach:
since we need to tell the minimum and maximum sum that could be made from the given array of five
1. sort the array
2. initiat min and max sum to 0
3. run a loop for a range five 
4. for minimum skip the last index
5. for max skip the first index
'''
def min_max_sum(arr):
    arr.sort()
    min_sum = 0
    max_sum = 0
    for i in range(5):
        if i != 4:
            min_sum+=arr[i]
        if i !=0:
            max_sum+=arr[i]
    print(str(min_sum)+" "+str(max_sum))

print(min_max_sum([1,3,5,7,9]))