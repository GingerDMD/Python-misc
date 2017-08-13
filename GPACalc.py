'''
Created on Feb 25, 2016

@author: preston wilson
'''

class GPACalc(object):
    
    def converter(self, initHours): #total hours before this semester, hours for this semester only
        prevGPA = float(raw_input("Enter your cumulative GPA, not including this semester:\n"))
        pointValues = {'A'  : 4.00,
                       'A-' : 3.67,
                       'B+' : 3.33,
                       'B'  : 3.00,
                       'B-' : 2.67,
                       'C+' : 2.33,
                       'C'  : 2.00,
                       'C-' : 1.67,
                       'D+' : 1.33,
                       'D'  : 1.00,
                       'D-' : 0.67,
                       'F+' : 0.33,
                       'F'  : 0.00}
        totalThis = 0
        grade = 'b'
        possibleThis = 0
        classes = int(raw_input("How many classes are you taking this semester?\n"))
        for i in range(0, classes):
            grade = raw_input("Enter estimated grade for a course\n")
            for x in pointValues:
                if grade == x:
                    value = float(pointValues[x])
                    break
            hours = float(raw_input("Hours for that course\n"))
            totalThis += float(hours * value)
            possibleThis += float(hours * 4)
        
        finalAnswer = ((initHours * prevGPA) + (totalThis)) / (possibleThis + (initHours * prevGPA))
        return round((finalAnswer * prevGPA), 2)
    
c = GPACalc()
hours = int(raw_input("How many hours of classes have you taken prior to this semester?\n"))
print "Estimated GPA: " + str(c.converter(hours))