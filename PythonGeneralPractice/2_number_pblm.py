'''
Created on Sep 19, 2024

@author: Sumeet Agrawal
'''


#Given a list of integers, write a Python function to return the sum of the two largest numbers in the list. -- Without using sort()

# num_list = input()
# new_num_lst = [int(x) for x in num_list]
#new_num_lst = [1,4,7,9]
new_num_lst = [5,2,12,1,8,3,2]

max_num = 0
max_num2 = 0

for i in new_num_lst:
    if i > max_num:
        max_num2 = max_num
        max_num = i
    if i < max_num and i > max_num2:
        max_num2 = i

print(max_num + max_num2)
