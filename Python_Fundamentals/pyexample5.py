#function scoresAndGrades that generate random scores between 60 and 100 and display the letter grade
import random
import math

def scoresAndGrades():
    randomScores = []
    for idx in range(0,10):
        randomScores.append(math.floor(random.random()*40 + 60))

    for element in randomScores:
        if element >= 60 and element <=69:
            print "Score:", element, "; Your Graded is D"
        elif element >= 70 and element <=79:
            print "Score:", element, "; Your Graded is C"
        elif element >= 80 and element <=89:
            print "Score:", element, "; Your Graded is B"
        else:
            print "Score:", element, "; Your Graded is A"

scoresAndGrades()

