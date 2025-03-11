'''
Created on Nov 8, 2024

@author: Sumeet Agrawal
'''

# Given a list of integers - order qty for customers, provide ranking based on highest order qty. 
# If same qty, then ranking will be on 1st come 1st served-basis

# E.g., [6, 7, 4, 4, 7]                                 --- Output should be - 3 1 4 5 2 
# E.g., [6, 7, 4, 5, 8]                                 --- Output should be - 3 2 5 4 1 
# E.g., [6, 7, 4, 4, 7, 4, 6, 7, 4, 8, 9, 4 ]           --- Output should be - 6 3 8 9 4 10 7 5 11 2 1 12

import random
import time
import psutil


time_start = time.perf_counter()


# First we'll see below a few test input lists
small_test_inps_with_dups = [6, 7, 4, 4, 7]
small_test_inps_wtht_dups = [6, 7, 4, 5, 8]
medm_test_inps_with_dups = [6, 7, 4, 4, 7, 4, 6, 7, 4, 8, 9, 4 ] 
large_test_inps_with_dups = [random.randrange(10000000) for i in range(1000)]

final_test_lst_app1 = large_test_inps_with_dups[::]
final_test_lst_app2 = large_test_inps_with_dups[::]

# Approach 1
# Here we will create a 'custPriorityLst' assigning '0' priority to all customers to start with...
time_start_apprch1 = time.perf_counter()
py_own_process = psutil.Process()
custPriorityLst = [0 for j in range(len(final_test_lst_app1))]

highestCustOrderQty = 0
for indx in range(len(final_test_lst_app1)):
    # First find the highest order qty from the list. 
    highestCustOrderQty = max(final_test_lst_app1)
    
    # We will break from the loop once highest order qty is 0.
    if (highestCustOrderQty != 0):
        # Next we find the 1st instance (index of the int in the list) of the highest order qty customer
        highestOrderIndex = final_test_lst_app1.index(highestCustOrderQty)
        
        # The 'custPriorityLst' for that index will then get assigned the highest priority... 
        # ... (Loop starts with index 0, hence need to increment by 1. 
        # So basically the priority 1 will be assigned to 1st instance of highest qty customer
        custPriorityLst[highestOrderIndex] = indx + 1
        
        # And now we'll update the element of the original list to 0 at the index that was found earlier. 
        # This way, eventually we'll have original list with all order qty as 0 at the end. 
        # And secondly, if there are multiple instances of same order qty, the one that appears later in the 1st list...
        # ... is the one that gets lower priority .. Hence this logic works.  
        final_test_lst_app1[highestOrderIndex] = 0
    else:
        break

final_op = " ".join(str(x) for x in custPriorityLst)       
# print(f"custPriorityLst: {custPriorityLst}")
print(f"Output of Approach 1 is: {final_op}")
time_elapsed_apprch1 = (time.perf_counter() - time_start)
memMb_apprch1 = (py_own_process.memory_info().rss)/1024.0**2
print (f" Time taken by Approach 1: {time_elapsed_apprch1}, And Memory Consumed was: {memMb_apprch1}")




time_start_apprch2 = time.perf_counter()
# Approach 2

# 'custPriorityLst' is to contain the final customer priority list - similar to approach 1
# 'newCustomerOrdersList' will contain the customer order qty that has already been parsed
# The main logic in Approach 2 is that if there are duplicates in the list, meaning...
# ... If there are multiple customers with same order qty, then "first come first served" is the motto...
# ... Hence basically that order qty customer will therefore be treated similar to a customer with lower order qty. So...

 
custPriorityLst = list()
newCustomerOrdersList = list()

highestCustOrderQty = 0
for eachNum in final_test_lst_app2:
    # To optimize if test input list is of len 1 and also for other cases, this is for first element parsing...
    if ((len(final_test_lst_app2) >= 1) and (len(newCustomerOrdersList) == 0)):
        # This will happen just once for EACH TEST INPUT.. Hence 1st customer will get priority 1 for now.
        custPriorityLst.append(1)
        
        # And also update the 'newCustomerOrdersList' so that it contains 1st customer order qty from input list meaning it has been parsed!
        newCustomerOrdersList.append(final_test_lst_app2[0])
    else:
        # For rest of the list, initialize current customer priority as 1. And then...
        # ... Loop through the list of customer order qty (COQ) that has already been parsed and ... 
        # ... If current COQ is higher that current inner loop qty, then change that customer's priority and increment it by 1
        # ... and if current COQ is lower or equal than the current inner loop customer order qty, then current COQ gets incremented by 1.
        currCustomrPriority = 1
        for eachParsedNumIndx in range(len(newCustomerOrdersList)):
            eachParsedNum = newCustomerOrdersList[eachParsedNumIndx]
            if eachNum > eachParsedNum:
                custPriorityLst[eachParsedNumIndx] += 1
            else:
                # Basically --> eachNum <= eachParsedNum:
                currCustomrPriority += 1
                        
        custPriorityLst.append(currCustomrPriority)
        newCustomerOrdersList.append(eachNum)
        
# print(f"newCustomerOrdersList is: {newCustomerOrdersList}")
final_op_app2 = " ".join(str(x) for x in custPriorityLst)
print(f"Output of Approach 2 is: {final_op_app2}")

time_elapsed_apprch2 = (time.perf_counter() - time_start_apprch2)
memMb_apprch2 = (py_own_process.memory_info().rss)/1024.0**2
print (f" Time taken by Approach 2: {time_elapsed_apprch2}, And Memory Consumed was: {memMb_apprch2}")


# Approach 3 - Initialize each customer priority to be same as the index of that customer in the array ...
# ... then keep doing -1 and +1 based on whether that num is smaller or equal to the current customers lst 
                
            