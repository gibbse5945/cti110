# CTI-110
# P2HW2 - Score Avg
# Eli Gibbs
# 3/28/22

d = {
    'StudentName':['Score1','Score 2','Score 3','Score 4',
                   'Score5','Score6','Score7'],
    'Score':[78,99.9,86.7,56,75.9,95,80.5]}

def determine_grade(scores): 
 if scores >= 90 and scores <= 100:
    return 'A'
 elif scores >= 80 and scores <= 89:
    return 'B'
 elif scores >= 70 and scores <= 79:
    return 'C'
 elif scores >= 60 and scores <= 69:
    return 'D'
 elif scores >= 50 and scores <= 59:
    return 'E'
 else:
    return 'F'

    
    


# Calculate the grade average using every score.
