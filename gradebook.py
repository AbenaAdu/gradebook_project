#Name of subjects
subjects = ["physics", "calculus", "poetry", "history"]

#Grades
grades = [98, 97, 85, 88]

#Combination of subjects and grades 
gradebook = [["physics", 98], 
             ["calculus", 97], 
             ["poetry", 85], 
             ["history", 88]]

#Adding new subject and grade
gradebook.append(["computer science", 100])
#Adding new subject and grade
gradebook.append(["visual arts", 93])
#Added 5 points to the visual arts grade
gradebook[5][1] = 98
#Removed grade for poetry class
gradebook[2].remove(85)
