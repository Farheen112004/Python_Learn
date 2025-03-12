gpa = float(input('enter ur gpa: '))
lowest_score = float(input('enter ur lowest score: '))
if gpa>= 8.5 and lowest_score >= 7.0: #and comment can be used both statememts should be true
    internship = True
else:
    internship = False
if internship:
    print("yes you are eligible to apply")
else:
    print("no you are not eligible to apply")
