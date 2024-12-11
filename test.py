test_list = [[1,2,3], [4,5,6]]

for i in range(len(test_list)):
    for j in range(len(test_list[0])):
        print(test_list[i][j])
        if(((i+1) < len(test_list)) and ((j+1) < len(test_list[0]))):
            print(test_list[i+1][j+1])
            if(((i+2) < len(test_list)) and ((j+2) < len(test_list[0]))):
                print(test_list[i+2][j+2])
