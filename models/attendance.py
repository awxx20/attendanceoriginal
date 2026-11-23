from models.student import Student
from models.course import Course

class Attendance:
    def __init__(self, attendance_id: int, student: Student, course: Course, attend_date: str):
        self.attendance_id = attendance_id
        self.student = student
        self.course = course
        self.attend_date = attend_date
        self.status = "Not Marked"

    def mark_present(self):
        self.status = "Present"
        print(f"[Attendance] {self.attend_date}: {self.student.name} is marked **PRESENT** for {self.course.course_name}.")

    def mark_absent(self):
        self.status = "Absent"
        print(f"[Attendance] {self.attend_date}: {self.student.name} is marked **ABSENT** for {self.course.course_name}.")