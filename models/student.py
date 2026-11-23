class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def register_course(self, course):
        print(f"Student {self.name} registered for course {course.course_name}")