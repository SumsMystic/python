'''
Created on Sep 19, 2024

@author: Sumeet Agrawal
'''

#Implement a Function to Find Missing Numbers in a Sequence.
#[1,2,4,6,8,10,13] - sequence of all integers

# test_lst = [1,2,4,6,8,10,13]
test_lst = [1,4,9,25]
final_lst = list()

for cntr in range(len(test_lst)-1):
    start_num = test_lst[cntr]
    next_num = test_lst[cntr+1]
    new_num = start_num + 1

    while new_num != next_num:
        final_lst.append(new_num)
        new_num += 1

print(final_lst)