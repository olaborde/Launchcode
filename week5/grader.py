def course_grader(test_scores):
    
  sorted_grades = sorted(test_scores)
  if sorted_grades[0] < 50:
    return 'fail'
  if sum( test_scores) / len( test_scores) < 70:
    return 'fail'
  return 'pass'  

print(course_grader([100,75,45]))  

print(course_grader([100,70,85]))  

print(course_grader([80,60,60]))
print(course_grader([80,80,90,30,80])) 
print(course_grader([70,70,70,70,70]))  