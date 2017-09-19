# Initialize variables to keep track of the highest scorer and highest score.
max_score = 0   # This is the lowest score possible
max_scorer = '' # Null, no names are known initially

numOfStudents = int(input("Enter number of students: "))

count = 1
while count <= numOfStudents:
    name = input("Enter student #" + str(count) + " name: ")
    score = int(input("Enter student #" + str(count) + " score: ")) 

    # Equals to check is also needed to update the name
    # if there is only one student and his score is 0.
    if score >= max_score:
        max_score = score
        max_scorer = name

    count = count + 1
    
print("\nTop student:", max_scorer, "\nScore:", max_score)
