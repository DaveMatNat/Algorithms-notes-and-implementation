def calmStudents (S, T):
    # sort list of teachers
    teacherList = []
    sortedT = sorted(T, key=len, reverse=True) 
        
    # # allocate teachers
    # to students based on the order of the list
    # until there are no more students
        
    i = 0
    while S: # 0(T)
        students = sortedT[i][1:]
        teacherName = sortedT[i][0]
        teacherList.append(teacherName)
        for student in students: 
            
            try:    
                S.remove(student)
            except:
                pass
        i += 1
    
    return teacherList
    
    
    #==== test cases 三三=
    # good example


T = ["Alice", 1, 21, ["Bob", 2], ["Chris", 3], ["Dawn", 3, 4]]


calmStudents(S)
