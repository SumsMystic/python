'''
Created on Sep 18, 2024

@author: Sumeet Agrawal
'''


test_str = "This is a simple TEST"

sliced_reversed_str = test_str[::-1]
sliced_str = test_str[:4:-1]
sliced_str_2 = test_str[:4]
sliced_str_3 = test_str[:]

# Loop for reversing - without using slicing and without built-in reverse()
reversed_3 = ""
for i in range(1, len(test_str)+1):
    reversed_3 += test_str[-i]
    
print(sliced_reversed_str)
print(sliced_str)
print(sliced_str_2)
print(sliced_str_3)
print(reversed_3)