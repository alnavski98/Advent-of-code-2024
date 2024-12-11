import re

path = 'C:\\Users\\alnav\\Documents\\Projects\Advent of code 2024\\Input\\test.txt'

def convert_file_to_2d_array(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Create a 2D array by converting each line into a list of characters and removing newlines
    array_2d = [list(line.strip()) for line in lines]
    return array_2d

# Example usage
result = convert_file_to_2d_array(path)

print(result)

# Print the 2D array
#for row in result:
    #print(row)
orientations = ["horizontal", "horizontal_r", "vertical", "vertical_r",
                "diagonally_dr", "diagonally_ul", "diagonally_dl", "diagonally_ur"]
xmas_strings = []

def extract_xmas(input_string):
    pattern = r"XMAS"
    return re.findall(pattern, input_string)
    

def count_xmas(input_list, orientation):
    i = 0
    j = 0
    temp_list = []
    if orientation == "horizontal":
        for i in range(len(input_list)):
            if(extract_xmas(''.join(input_list[i]))):
                xmas_strings.append(extract_xmas(''.join(input_list[i])))

    elif orientation == "horizontal_r":
        for i in range(len(input_list)): 
            input_list[i].reverse()
            if(extract_xmas(''.join(input_list[i]))):
                xmas_strings.append(extract_xmas(''.join(input_list[i])))
            input_list[i].reverse()

    elif orientation == "vertical":
        for i in range(len(input_list[0])):     # Column
            temp_list_row = []
            for j in range(len(input_list)):    # Row
                temp_list_row.append(input_list[j][i])
            temp_list.append(temp_list_row)

        i = 0
        j = 0

        for i in range(len(temp_list)):
            if(extract_xmas(''.join(temp_list[i]))):
                xmas_strings.append(extract_xmas(''.join(temp_list[i])))

    elif orientation == "vertical_r":
        for i in range(len(input_list[0])):     # Column
            temp_list_row = []
            for j in range(len(input_list)):    # Row
                temp_list_row.append(input_list[j][i])
            temp_list.append(temp_list_row)

        i = 0
        j = 0

        for i in range(len(temp_list)): 
            temp_list[i].reverse()
            if(extract_xmas(''.join(temp_list[i]))):
                xmas_strings.append(extract_xmas(''.join(temp_list[i])))
            temp_list[i].reverse()

    elif orientation == "diagonally_dr":
        for i in range(len(input_list)):
            for j in range(len(input_list[0])):
                temp_list_row = []
                if input_list[i][j] == "X":
                    temp_list_row.append("X")
                    if((input_list[i+1][j+1] == "M") and (i+1 < len(input_list)) and (j+1 < len(input_list[0]))):
                        temp_list_row.append("M")
                        if(input_list[i+2][j+2] == "A" and i+2 < len(input_list) and j+2 < len(input_list[0])):
                            temp_list_row.append("A")
                            if(input_list[i+3][j+3] == "S" and i+3 < len(input_list) and j+3 < len(input_list[0])):
                                temp_list_row.append("S")
                                temp_list.append(temp_list_row)

        #print(temp_list)
            

    elif orientation == "diagonally_ul":
        None
    elif orientation == "diagonally_dl":
        None
    elif orientation == "diagonally_ur":
        None

# Horizontal
# for i in range(len(result)):
#     if(extract_xmas(''.join(result[i]))):
#         xmas_strings.append(extract_xmas(''.join(result[i])))

# Horizontal backwards
# for j in range(len(result)): 
#     result[j].reverse()
#     if(extract_xmas(''.join(result[j]))):
#         xmas_strings.append(extract_xmas(''.join(result[j])))
#         result[j].reverse()
# print(len(xmas_strings))

for orientation in orientations:
    count_xmas(result, orientation)

print(len(xmas_strings))


# Vertical




# 1. Collect in each orientation
#   - Horizontal
#   - Horizontal reversed
#   - Vertical
#   - Vertical reversed
#   - Diagonally downwards right
#   - Diagonally upwards left
#   - Diagonally downwards left
#   - Diagonally upwards right