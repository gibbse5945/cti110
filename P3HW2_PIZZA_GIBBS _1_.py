# I was supposed to put a comment here
# Gibbs

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores

    
    score = input('Enter grade: ')

    if score >= A_score:
    print('Your grade is: A')
    else:
    if score > B_score:
     print('Your grade is: B')
    else:
    if score > C_score:
     print('Your grade is: C')
    else:
    if score > D_score:
     print('Your grade is: D')
    else:
   

    else:
    print('Your grade is: F') # TO DO: finish this

    if score > 100:
        print("Error: Score cannot be higher than 100")
    elif score < 0:
        print("Error: Score cannot be lower than 0")







# program start
main()
