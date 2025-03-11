'''
Created on Sep 19, 2024

@author: Sumeet Agrawal
'''

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


# nums = [100,4,200,1,3,2]
# nums = [0,3,4,5,5,9,8,6,7]
nums = [0,3,7,2,5,8,4,6,0,1]
nums.sort()
print('Sorted list of numbers: ', nums)

max_con_seq = 0
cur_con_seq = 1

for i in range(len(nums)):
    # print(nums[i])
    if max_con_seq > (len(nums)/2):
        # If the max. consecutive numbers list length is already more than half the length of the list, we are not going to find any longer list, so we can break.
        break
    # Earlier if condition was this:  {{nums[i] == nums[i+1]}} and therefore loop was for this:   {{for i in range(len(nums)-1)}}
    if ((i != len(nums)-1) and (nums[i] == nums[i+1])):
        # And now since we are specifically checking if the loop is now in last iteration, first condition fails and hence no out of bounds error and this if 
        # ... will not get executed.
        cur_con_seq = 1
        continue
    elif nums[i]+1 in nums:
        # print('inside first elif')
        cur_con_seq += 1
        continue
    if max_con_seq < cur_con_seq:
        max_con_seq = cur_con_seq
        cur_con_seq = 1
        print('max_con_seq: ', max_con_seq)
    
'''
# If in sorted list, last number is part of the longest sequence, then last number iteration of the loop is not done
# Therefore the following if condition part never gets completed there and hence needs to be repeated once.  

if max_con_seq < cur_con_seq:
    max_con_seq = cur_con_seq
    cur_con_seq = 1
    print('max_con_seq: ', max_con_seq)

'''

print("Final maximum length of consecutive numbers is: ", max_con_seq)