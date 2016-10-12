def find_missing(a,b):
    
    if a == [] and b == []:
        
        return 0
    elif a == b:
        return 0
    else:
        for i in b:
            if i not in a:
                return i
        
list1 = find_missing([1, 2], [1, 2, 5])
list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])

print [list1,list2,list3]