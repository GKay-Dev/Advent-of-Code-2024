with open("input.txt", "r") as f:
    memory = [l for l in f.readlines()]

import re

# Part One
text_pattern = r'mul\(\d{1,3},\d{1,3}\)'
sum_of_mul = 0
for m in memory:
    instruction = re.findall(text_pattern, m)
    for text in instruction:
        nums = list(map(int, re.findall(r'\d+', text)))
        sum_of_mul += nums[0] * nums[1]

print('Sum of all of the results of the multiplications:', sum_of_mul)

# Part Two
condition_pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
sum_of_mul = 0
flag = True
for m in memory:
    instruction = re.findall(condition_pattern, m)
    for text in instruction:
        if text == "don't()":
            flag = False
        elif text == 'do()':
            flag = True
        elif flag and 'mul' in text:
            nums = list(map(int, re.findall(r'\d+', text)))
            sum_of_mul += nums[0] * nums[1]
            
print('Sum of all of the results of just the enabled multiplications:', sum_of_mul)
