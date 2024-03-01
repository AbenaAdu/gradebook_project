#Name of subjects
subjects = ["physics", "calculus", "poetry", "history"]

#Grades
grades = [98, 97, 85, 88]

#Combination of subjects and grades 
gradebook = [["physics", 98], 
             ["calculus", 97], 
             ["poetry", 85], 
             ["history", 88]]

last_semester_gradebook = [["politics", 80], 
                           ["latin", 96], 
                           ["dance", 97], 
                           ["architecture", 65]]

#Adding new subject and grade
gradebook.append(["computer science", 100])
print(gradebook)
#Adding new subject and grade
gradebook.append(["visual arts", 93])
print(gradebook)
#Added 5 points to the visual arts grade
gradebook[5][1] = 98
print(gradebook)
#Removed grade for poetry class
gradebook[2].remove(85)
print(gradebook)
#Added pass value to poetry class
gradebook[2].append("Pass")
print(gradebook)
#Combining last semester gradebook and gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
