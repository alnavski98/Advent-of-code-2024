path = 'C:\\Users\\alnav\\Documents\\Projects\Advent of code 2024\\Input\\Input_day_1'

# Read all number strings from file and put in array
with open(path) as f:
    number_list = f.read().split()

# Split array into lists containing every other element
left_number_list = number_list[::2]
right_number_list = number_list[1::2]

# Convert elements to integers and sort them
integer_left_list = sorted(list(map(int, left_number_list)))
integer_right_list = sorted(list(map(int, right_number_list)))

# Part 1
# distance_apart = []

# for i in range(len(left_number_list)):
    # distance_apart.append(abs(integer_left_list[i] - integer_right_list[i]))

# print(sum(distance_apart))

# Part 2
similarity_score_list = []

for i in range(len(left_number_list)):
    similarity_score_list.append(integer_left_list[i] * integer_right_list.count(integer_left_list[i]))

print(sum(similarity_score_list))