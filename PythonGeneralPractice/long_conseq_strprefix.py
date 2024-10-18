'''
Created on Sep 23, 2024

@author: Sumeet
'''
# Write a program to find LONGEST common prefix from an array of strings
# E.g., ["tree", "trunk", "trust"]
#    Here, 'tr' appears in all 3 strings but 'tru' has 3 chars and appears in 2 strs and...
#    ... no other '3-char-subs' is present in 2 or more strs so 'tru' is the answer

# test_lst = ["tree", "trunk", "trust"]
test_lst = ["tree", "trunk", "trust", "truth", "triumph", "trump", "trumpet", "abc12312", "abc1223423", "abc1223423", "abc1288434"]
dicti = {}
longest_prefix = ""
longest_prefix_len = 0
longest_prefix_cnt = 0

# {t:3, tr:2, tre:1, tree:1, tru:2}

for stri in test_lst:
    subst = ""
    for chara in stri:
        subst += chara
        if subst not in dicti.keys():
            dicti[subst] = 1
        else:
            dicti[subst] += 1

print(dicti)
# {'t': 3, 'tr': 3, 'tre': 1, 'tree': 1, 'tru': 2, 'trun': 1, 'trunk': 1, 'trus': 1, 'trust': 1}

# For each key in this dict --> meaning for each prefix in the list of strings input...
for ks in dicti.keys():
    # If number of chars of the prefix is more than or same as highest so far...
    if len(ks) > longest_prefix_len:
        # To find COMMON prefix meaning it has to exist in AT LEAST 2 strings in the list...
        # ... so if count of a prefix is 1, then it has to be ignored. 
        if dicti[ks] == 1:
            continue
        # It comes here meaning current prefix has length longer than all prefixes so far - this length of prefix has appeared 1st time 
        longest_prefix_cnt = dicti[ks]
        longest_prefix = ks
        longest_prefix_len = len(ks)
    
    # If current prefix has length SAME as some other prefix so far -->
    # ... meaning this LENGTH of prefix has NOT appeared 1st time (e.g., tre and tru) - appearing 1 and 2 times respectively.. so.... 
    if len(ks) == longest_prefix_len:
        # If value of this key (highest num of chars in the prefixes) is more than or same as the highest -->
        # ... meaning if this prefix has appeared more than or same number of times as highest prefix count so far... 
        if dicti[ks] >= longest_prefix_cnt:
            longest_prefix_cnt = dicti[ks]
            longest_prefix = ks
            longest_prefix_len = len(ks)
            
print("longest_prefix: ", longest_prefix)
print("longest_prefix_len: ", longest_prefix_len)
print("longest_prefix_cnt: ", longest_prefix_cnt)