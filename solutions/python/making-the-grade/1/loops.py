def round_scores(student_scores): 
    return [round(score) for score in student_scores]

print (round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))

def count_failed_students(student_scores):
    return len([score for score in student_scores if score <= 40])

print (count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))

def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]

print (above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))

def letter_grades(highest):
    return [i for i in range(41, highest, (highest - 40) // 4)]

print (letter_grades(highest=100))
print (letter_grades(highest=88))

def student_ranking(student_scores, student_names):
    rankink = []
    for i in range(len(student_scores)):
        rankink.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return rankink
print (student_ranking(student_scores=[100, 99, 90, 84, 66, 53, 47], student_names=['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']))

def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []

print (perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))

print (perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))