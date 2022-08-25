'''
Time complexity
O(1) => 2+3
O(log(n)) => includes for example divide function
O(n) => iterating over a loop of n
O(n^2) => 2 for loops with n number of inputs
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
    return min_sum, max_sum

print(min_max_sum([1,3,5,7,9]))