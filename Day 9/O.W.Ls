student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades
for i in student_scores:
  if 91<= student_scores[i]<= 100:
    student_grades[i] = "Outstanding"
  elif 81<= student_scores[i]<= 90:
    student_grades[i] = "Exceeds Expectations"
  elif 71<= student_scores[i]<= 80:
    student_grades[i] = "Acceptable"
  elif student_scores[i]<=70:
    student_grades[i] = "Fail"
    

print(student_grades)
