# Student data
mark = {
    "Quiz" : [70,66.2,80.5],
    "Homework": [90,88,72.6],
    "Recitation": [40.5,65.6],
    "Test": [85.4,63.4]
}
bill = {
    "Quiz" : [55.5,63.2,45.6],
    "Homework": [95,83.6,75.3],
    "Recitation": [33.6,50.2],
    "Test": [70.2,60.5]
}
jane = {
    "Quiz" : [86.6,89.6,95.6],
    "Homework": [86.3,82.3,80],
    "Recitation": [75.6,79.6],
    "Test": [92.6,90.4]
}

# Weights for each category
weights = {
    "Quiz": 0.2,
    "Homework": 0.1,
    "Recitation": 0.3,
    "Test": 0.4
}

def avg(scores):
    '''Calculates the average of each field'''
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def stud_average(student_data, category_weights):
    '''Returns the weighted average for each student'''
    total_score = 0
    for category, scores in student_data.items():
        category_avg = avg(scores)
        weight = category_weights.get(category, 0)
        total_score += category_avg * weight
    return round(total_score, 2)

def main():
    # List of students
    students = {
        "Mark": mark,
        "Bill": bill,
        "Jane": jane
    }

    # Calculate and print average scores for all students
    for student_name, student_data in students.items():
        score = stud_average(student_data, weights)
        print(f"The average score for {student_name} is: {score} %")

if __name__ == "__main__":
    main()
