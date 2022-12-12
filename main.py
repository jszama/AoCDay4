file = open("input4.txt","r")
assignmentPairs1 = 0
assignmentPairs2 = 0

for line in file:
    assignment1, assignment2 = line.split(",")
    
    assignment1 = [int(number) for number in assignment1.split("-")]
    assignment2 = [int(number) for number in assignment2.split("-")]
    
    if assignment1[0] <=  assignment2[0] and assignment1[1] >=  assignment2[1]:
        assignmentPairs1+= 1
    elif assignment2[0] <=  assignment1[0] and assignment2[1] >=  assignment1[1]:
        assignmentPairs1 += 1
        
    if assignment1[0] in range(assignment2[0], assignment2[1]+1) or assignment1[1] in range(assignment2[0], assignment2[1]+1):
        assignmentPairs2 += 1
    elif assignment2[0] in range(assignment1[0], assignment1[1]+1) or assignment2[1] in range(assignment1[0], assignment1[1]+1):
        assignmentPairs2 += 1
        
print(assignmentPairs1, assignmentPairs2)