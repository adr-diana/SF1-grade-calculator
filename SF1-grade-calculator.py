
numb_labs = int(input("Enter the number of labs completed between 0 and 6. If you did more than 6, just enter  6."))
numb_quiz = int(input("Enter the number of quizzes completed between 0 and 6. If you did more than 6, just enter 6."))
grade_a1 = float(input("Enter grade for assignment 1:"))
grade_a2 = float(input("Enter grade for assignment 2:"))
grade_a3 = float(input("Enter grade for assignment 3:"))
grade_a4 = float(input("Enter grade for assignment 4:"))
grade_m1 = float(input("Enter grade for midterm 1:"))
grade_m2 = float(input("Enter grade for midterm 2:"))
grade_final = float(input("Enter grade for final exam:"))
grade_prep = float(input("Enter grades for midterms and final preparation:"))

def grade_labs(numb_labs: int) -> float:
	return (numb_labs/6) * 20

def grade_quiz(numb_quiz: int) -> float:
	return (numb_quiz/6) * 15

def grade_assignments(grade_a1: float, grade_a2: float, grade_a3: float, grade_a4:float) -> float:
	return (grade_a1 * 0.04) + (grade_a2 * 0.04) + (grade_a3 * 0.04) + (grade_a4 * 0.04)

def grade_midterm(grade_m1: float, grade_m2: float) -> float:
	return (grade_m1 * 0.125) + (grade_m2 * 0.125)

def grade_f(grade_final: float) -> float:
	return grade_final * 0.18

def grade_preparation(grade_prep: float) -> float:
	return grade_prep * 0.06

course_total = 0
course_total += grade_labs(numb_labs)
course_total += grade_quiz(numb_quiz)
course_total += grade_assignments(grade_a1, grade_a2, grade_a3, grade_a4)
course_total += grade_midterm(grade_m1, grade_m2)
course_total += grade_f(grade_final)
course_total += grade_preparation(grade_prep)

print(f"Your grade is: {course_total}") 



