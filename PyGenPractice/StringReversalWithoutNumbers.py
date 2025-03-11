'''
Created on Dec 2, 2024

@author: Sumeet Agrawal
'''

# Objective is to first just reverse the given string
# Then next objective is to  reverse the string in such a way that numbers remain as they are

test_str = "Volansys2024Technologies"

o_p_str = test_str[::-1]
print("First problem solved. Output: ", o_p_str)
# Part 1 completed here


final_op = ""
nums_str = ""

test_lst = [str(x) for x in range(0,9)]
# print(test_lst)

charc_indx = 1
#for charc_indx in range(1, len(test_str)+1):
while charc_indx <= len(test_str):
    # print(f"charc_indx: {charc_indx}")
    if test_str[-charc_indx] in test_lst:
        final_nums_str = ""
        while test_str[-charc_indx] in test_lst:
            nums_str += test_str[-charc_indx]
            # print(nums_str)
            charc_indx += 1
            # print(f"charc_indx: {charc_indx}")
        final_nums_str = nums_str[::-1]
        final_op += final_nums_str
    else:
        final_op += test_str[-charc_indx]
        charc_indx += 1
       

print("Second problem solved. Output: ", final_op)