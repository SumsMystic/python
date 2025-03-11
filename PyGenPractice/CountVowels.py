'''
Created on Aug 18, 2024

@author: Sumeet Agrawal
'''

vowel = ['a', 'e', 'i', 'o', 'u']
word = "devilal"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)