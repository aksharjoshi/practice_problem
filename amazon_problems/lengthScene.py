def lengthEachScene(inputList):
    # WRITE YOUR CODE HERE
    dict_map = {}
    
    for i in range(0, len(inputList)):
        dict_map[inputList[i]] = i 
    
    final_res = []
    
    left = right = 0
    
    for i in range(0, len(inputList)):
        right = max(right, dict_map[inputList[i]])
        if right == i:
            final_res.append(1 + right - left)
            left = right + 1
    return final_res