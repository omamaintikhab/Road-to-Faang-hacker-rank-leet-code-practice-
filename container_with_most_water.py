# link: https://leetcode.com/problems/container-with-most-water/
# Notes
'''
* max_area jo he wo max_area = min_height*width aesa qk min wali height exceed kregi to water will overflow
* initiate min_height with 0 and max height with => lenght of array -1 
* take minimum of both the heights
* take area and compare with the max area
* MAIN STEP
* if left_height is less than right height so increment left
* if right_height is greater than left_height so decrement left
''' 
height = [1,8,6,2,5,4,8,3,7]
left_index = 0
right_index = len(height)-1
max_area = 0

while (left_index<right_index):
    left_height = height[left_index]
    right_height = height[right_index]
    minimum_height = min(left_height,right_height)
    max_area = max(max_area, minimum_height*(right_index-left_index))
    if left_height < right_height:
        left_index+= 1
    else:
        right_index-=1
print(max_area)
