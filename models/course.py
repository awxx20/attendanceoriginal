class Course:
    def __init__(self, course_id: int, course_name: str, credits: int):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def add_student(self, student):
        print(f"Student {student.name} added to course {self.course_name}")

    def assign_instructor(self, instructor):
        print(f"Instructor {instructor.name} assigned to {self.course_name}")