
def process_exam_scores(filename):
    subject_totals = {}
    failing_students = []
    with open(filename,"r") as file1:
        for info in file1:
            parts = info.split(",")
            if len(parts) !=4:
                continue
            student,subject,part1,part2 = parts
            try:
                part1 = int(part1)
                part2 = int(part2)
            except ValueError:
                continue
            total_score = part1 + part2
            if subject not in subject_totals:
                subject_totals[subject] = total_score
            else:
                subject_totals[subject] = subject_totals[subject] + total_score
            if total_score<100:
                failing_students.append((student, total_score))
    return subject_totals,failing_students
def save_grade_report(subject_totals, failing_students):
    with open("grade_report.txt", "w") as file2:
        file2.write("SUBJECT TOTAL POINTS\n")
        file2.write("--------------------\n")
        for subject,total in subject_totals.items():
            file2.write(f"{subject} : {total}\n")
        file2.write("\nAT RISK STUDENTS (< 100 pts)\n") 
        file2.write("--------------------\n")
        for student,total_score in failing_students:
            file2.write(f"{student} ({total_score} pts)\n")
subject_totals, failing_students = process_exam_scores("exam_scores.txt")
save_grade_report(subject_totals, failing_students) 








    


    
    

            