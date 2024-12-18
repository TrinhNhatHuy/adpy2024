class student:
    def __init__(self, id_student, name_student,dob):
        self.id_student=id_student
        self.name_student=name_student
        self.dob=dob
        self.marks={}
        
    def add_mark(self,course_id,mark):
        self.marks[course_id]=mark
        
    def get_mark(self, id_course):
        return self.marks.get(id_course,"N/A")
    

class course:
    def __init__(self,id_course,name_course):
        self.id_course=id_course
        self.name_course=name_course


class studentmanagement:
    def __init__(self):
        self.students=[]
        self.courses=[]
    
    def input_students(self):
        num_student=int(input("Enter number of students: "))
    
        for _ in range(num_student):
            id_student=input("Enter the id of student: ")
            name_student=input("Enter the name of student: ")
            dob=input("Enter date of birth(DD/MM/YYYY): ")
            infor_student=student(id_student,name_student,dob)
            self.students.append(infor_student)

    def input_courses(self):
        num_course=int(input("Enter number of courses: "))
    
        for _ in range(num_course):
            id_course=input("Enter the id of course: ")
            name_course=input("Enter the name of course: ")
            infor_course =course(id_course, name_course )
            self.courses.append(infor_course)
    

    def list_student(self):
        print("The list of students: ")
        for student in self.students:
            print(f"Student ID:{student.id_student},Student name:{student.name_student},DOB:{student.dob}")

    def list_courses(self):
        print("The list of courses: ")
        for course in self.courses:
            print(f"Course ID:{course.id_course}, Course name:{course.name_course}" )


    def input_marks(self):
        id_course=input("Input course ID that you want input mark for: ")
        course =next((a for a in self.courses if a.id_course ==id_course),None)
        if not course:
            print("No course found")
            return
        for student in self.students:
            mark=int(input(f"Enter mark for {student.name_student}in {course.name_course}:"))
            student.add_mark(id_course,mark) 
             
    def show_student_marks(self):
        id_student=input("Input student ID that you want to see mark for: ")
        student = next((b for b in self.students if b.id_student==id_student),None)
        
        if not student:
            print("No student found")
            return
        
        print(f"Student ID:{student.id_student}, Name:{student.name_student}, DOB: {student.dob}")
        if student.marks:
            for course in self.courses:
                mark=student.get_mark(course.id_course)
                print(f"Course ID: {course.id_course}, Name: {course.name_course}, Mark: {mark}")
        else:
            print("No marks available")
                
    def run(self):
        while True:
            print('''
                Student mark management system: 
                0. Select course and input marks for students
                1. List students
                2. List courses
                3. Show student marks
                4. Exit
                ''')
        
            choice= int(input("Select number: "))
        
            if choice == 0:
                self.input_marks()
            elif choice ==1:
                self.list_student()
            elif choice ==2:
                self.list_courses()
            elif choice ==3:
                self.show_student_marks()
            elif choice ==4:
                break
            else:
                print("Enter again a number from 0->4: ")

if __name__ == "__main__":
    sm = studentmanagement()
    sm.input_students()
    sm.input_courses()
    sm.run()