path = 'C:\\Users\\alnav\\Documents\\Projects\Advent of code 2024\\Input\\Input_day_2'

report_list = []

with open(path) as f:
    for line in f.readlines():
        report_list.append(list(map(int, line.split())))

# Part 1
def is_safe(report):
    difference_list = []
    sorted_difference_list = []
    for i in range(len(report)-1):
        if(((abs(report[i+1]-report[i])) > 3) or (report[i+1]-report[i]) == 0):
            return False
        difference_list.append(report[i+1]-report[i])
    
    sorted_difference_list = sorted(difference_list)
    for j in range(len(difference_list)-1):
        if ((sorted_difference_list[j+1] > 0 and sorted_difference_list[j] < 0) or (sorted_difference_list[j+1] < 0 and sorted_difference_list[j] > 0)):
            return False
    
    return True

def truth_count(report_safety_list):
    truth_number = 0
    for j in range(len(report_safety_list)):
        if report_safety_list[j]:
            truth_number += 1
    return truth_number

report_safety_list = []

for i in range(len(report_list)):
    report_safety_list.append(is_safe(report_list[i]))

print(truth_count(report_safety_list))

# Part 2
# fault_count = 0
# false_state = False

# def difference(num1, num2):
#     return num2 - num1

# def new_is_safe(report):
#     global fault_count
#     #global false_state
#     negative_difference_count = 0
#     positive_difference_count = 0
#     zero_count = 0
#     current_difference = 0
#     for i in range(len(report)-1):
#         current_difference = difference(report[i], report[i+1])
#         if(current_difference < 0):
#             negative_difference_count += 1
#         elif(current_difference > 0):
#             positive_difference_count += 1
#         #elif(current_difference == 0):
#             #zero_count += 1

#         if((negative_difference_count > 0) and (positive_difference_count > 0)):
#             if fault_count == 0:
#                 fault_count += 1
#                 report.pop(i)
#                 return new_is_safe(report)
#             elif fault_count == 1:
#                 return False


#         if((abs(current_difference) == 0) or (abs(current_difference) > 3)):
#             if fault_count == 0:
#                 fault_count += 1
#                 report.pop(i+1)
#                 return new_is_safe(report)
#             elif fault_count == 1:
#                 return False

#         #if false_state and fault_count > 0:
#             # return False

#     return True

# new_report_safety_list = []

# for j in range(len(report_list)):
#     fault_count = 0
#     false_state = False
#     new_report_safety_list.append(new_is_safe(report_list[j]))

# print(truth_count(new_report_safety_list))

truth_list = []

for i in range(len(report_list)):
    is_it_safe = False
    popped_element = []
    new_report = list(report_list[i])
    for j in range(len(report_list[i])):
        if is_safe(new_report):
            is_it_safe = True
            break
        elif j == 0:
            popped_element.append(new_report.pop(0))
        else:
            new_report.insert(j-1, popped_element.pop())
            popped_element.append(new_report.pop(j))
    
    if is_safe(new_report):
            is_it_safe = True

    if not is_it_safe:
        truth_list.append(False)
    else:
        truth_list.append(True)

print(truth_count(truth_list))

        

