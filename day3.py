import re

path = 'C:\\Users\\alnav\\Documents\\Projects\Advent of code 2024\\Input\\Input_day_3'
invalid_text = ""

with open(path) as f:
    invalid_text = f.read()

# Part 1
multiplication_sum = 0

def extract_mul_expressions(input_string):
    # Regular expression pattern to match "mul(X,Y)" where X and Y are 1-3 digit numbers
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, input_string)

def extract_multiplication_numbers(input_string):
    pattern = r"\d{1,3}"
    return re.findall(pattern, input_string)

result = extract_mul_expressions(invalid_text)

print(result)

for i in range(len(result)):
    products = extract_multiplication_numbers(result[i])
    multiplication_sum += int(products[0]) * int(products[1])

print(multiplication_sum)

# Part 2
def extract_mul_and_instruction_expressions(input_string):
    # Regular expression pattern to match "mul(X,Y)" where X and Y are 1-3 digit numbers
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    #pattern_2 = r"do\(\)"
    #pattern_3 = r"don\'t\(\)"
    return re.findall(pattern, input_string)

new_multiplication_sum = 0

new_result = extract_mul_and_instruction_expressions(invalid_text)

print(new_result)

do = True

for j in range(len(new_result)):
    if new_result[j] == "do()":
        do = True 
        continue

    if new_result[j] == "don't()":
        do = False
        continue

    if do:
        products = extract_multiplication_numbers(new_result[j])
        new_multiplication_sum += int(products[0]) * int(products[1])
    else:
        do = False
    
print(new_multiplication_sum)

