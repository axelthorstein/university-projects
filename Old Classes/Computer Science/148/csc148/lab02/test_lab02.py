if __name__ == ’__main__’:
    grades = [NumericGradeEntry(’csc148’, 87, 1.0), NumericGradeEntry(’bio150, 76, 2.0), LetterGradeEntry(’his450’, 1.0, ’B+’)]
    for g in grades:
# Use appropriate ??? methods or attributes of g in format
        print("Weight: {}, grade: {}, points: {}".format(g.?, g.??, g.???)
# Use methods or attributes of g to compute weight times points
total = sum( # sum of the list of...
             [g.? * g.?? # ? and ?? are methods or attributes of g
              for g in grades]) # using each g in grades
print("GPA = {}".format(total / len(grades))