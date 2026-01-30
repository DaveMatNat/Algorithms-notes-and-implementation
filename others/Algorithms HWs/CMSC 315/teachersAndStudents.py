
s = {
    1: [1, 2],
    2: [2],
   
     }
out = []


def fewestTeachers():
    min = float('inf')
    studentInd = 0
    for key in s:
        list = s[key]
        # print(len(list))
        if (len(list)) < min:
            min = len(list)
            studentInd = key
    
    return studentInd


def inOut(teacherId):
    for id in out:
        if teacherId == id:
            return True
    return False

def generatingTeachersList():
    while s:
        for i in range(len(s)):
            studentId = fewestTeachers()
            print("student ", studentId )
            for teacherId in s[studentId]:
                flag = False
                if inOut(teacherId) == True:
                    print("Teacher", teacherId, "already in list")
                    flag = True
                    break
            
            if flag == False:
                out.append(teacherId)
                print("Teacher", teacherId, "added to list")
            
            s.pop(studentId)
        
    return out

print(generatingTeachersList())


    