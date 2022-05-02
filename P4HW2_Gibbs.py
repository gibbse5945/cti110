#Enter in the 4 exam scores
g1=int(input("Enter an exam score between 0 and 100 or -1 to end: "))
g2=int(input("Enter an exam score between 0 and 100 or -1 to end: "))
g3=int(input("Enter an exam score between 0 and 100 or -1 to end: "))
g4=int(input("Enter an exam score between 0 and 100 or -1 to end: "))

total =(g1 + g2 + g3 + g4)

while g1 is range(0,100):
    continue
# CTI-110
# P2HW2 - Score Avg
# Eli Gibbs
# 3/28/22

else:
    print("Sorry",g1,"is not in the range of 0 and 100 or -1.Please  Try again!")

while g2 is range(0,100):
    continue
else:
    print("Sorry",g2,"is not in the range of 0 and 100 or -1. Please Try again!")

while g3 is range(0,100):
    continue
else:
    print("Sorry",g3,"is not in the range of 0 and 100 or -1. Please Try again!")

while g4 is range(0,100):
    continue
else:
    print("Sorry",g4,"is not in the range of 0 and 100 or -1. Please Try again!")

#calculating Average
def calc_average(total):
    return total/4

def determine_letter_grade(grade):
    if 90 <= grade <= 100:
        1 + TotalA
    elif 80 <= grade <= 89:
        1 + TotalB
    elif 70 <= grade <= 79:
        1 + TotalC
    elif 60 <= grade <= 69:
        1 + TotalD
    else:
        1 + TotalF

grade=total
average=calc_average

# Calculate the grade average using every score.
print("You entered four valid exam scores with an average of: " + str(average))
print("------------------------------------------------------------------------")
print("Grade Distribution:")
print("Number of A's: ",TotalA)
print("Number of B's: ",TotalB)
print("Number of C's: ",TotalC)
print("Number of D's: ",TotalD)
print("Number of F's: ",TotalF)
