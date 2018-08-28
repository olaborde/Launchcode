# - course grader function that a list of test scores as its parameter
# - add test scores & calculate average
# -pass: if average_score > 70 & no single is below 50 
# -fai:' when average_score < 70 if at least one test score is less than 50


def course_grader(test_scores):
  average_score = sum(i for i in test_scores) / len(test_scores)
  # print(average_score)
  for score in test_scores:
    print(score)
  if average_score >= 70 and not score < 50:
    print(average_score, 'is a', 'PASS')
  else:
    print(average_score, 'is a', 'FAIL')



course_grader([100,75,45])     # "fail"
course_grader([100,70,85])     # "pass"
course_grader([80,60,60])      # "fail"
course_grader([80,80,90,30,80])  # "fail"
course_grader([70,70,70,70,70])  # "pass"  
