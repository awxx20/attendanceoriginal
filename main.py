from models.student import Student
from models.course import Course
from models.attendance import Attendance

def main():
    print("--- Running MTU Attendance System ---")
    
    # 1. Create a student and a course
    student1 = Student(1, "Alice Smith", "alice@mtu.ie")
    course1 = Course(101, "Software Engineering", 5)

    # 2. Initialize an attendance record
    attendance_record = Attendance(
        attendance_id=1001,
        student=student1,
        course=course1,
        attend_date="2026-06-06"
    )

    # 3. Test marking Present and Absent
    print("\nTesting Present Status:")
    attendance_record.mark_present()

    print("\nTesting Absent Status:")
    attendance_record.mark_absent()

if __name__ == "__main__":
    main()