"""
PLAIN ENGLISH
open file in read
capture variable (test scores) from list of grades (float)
calculate number of grades
append grade scores to avg lis
calculate average class grade score from avg list of grades 
calculate number of above average scores
out grade information to user
end
"""

"""
Pseudo Code
initialize total to 0
initialize counter to 0
get list of grades from txt. file (open in read (r))
input first grade
add this grade to total
add one to the grade counter
input the next grade
if counter is not = 0
set the average to the total divided by the counter
print the number of grades
print the average
print the percent above the average
"""


def calculate_percent_above_average(grades,avg):
    count = 0
    for grade in grades:
        if grade > avg:
            count += 1
    return(count * 100) / len(grades)

def main():
    f = open("Final.txt",'r')
    grades =[]
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:",len(grades))
    avg = 0
    for grade in grades:
        avg += grade
    avg /= len(grades)
    print("Average grade:",avg)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades,avg)))
    f.close()

main()