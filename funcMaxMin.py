def find_max_min(numList):
    for i in numList:
        max_num = max(numList)
        min_num = min(numList)
        maxmin = [min_num, max_num]
        if max_num == min_num:
            num_element = [numList.count(i)]
            return num_element
    return maxmin