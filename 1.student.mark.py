def input_students():
    num_student=int(input("Enter number of students: "))
    students=[]
    
    for i in range(num_student):
        id_student=input("Enter the id of student: ")
        name_student=input("Enter the name of student: ")
        dob=input("Enter date of birth(DD/MM/YYYY): ")
        infor_student={'id':id_student,'name':name_student,'dob':dob}
        students.append(infor_student)
    return students

def input_courses():
    num_course=int(input("Enter number of courses: "))
    courses=[]
    
    for i in range(num_course):
        id_course=input("Enter the id of course: ")
        name_course=input("Enter the name of course: ")
        infor_course ={'id':id_course,'name':name_course}
        courses.append(infor_course)
    return courses

def list_student(students):
    print("The list of students: ")
    for i in students:
        print(f"Student ID:{i['id']},Student name:{i['name']},DOB:{i['dob']}")

def list_courses(courses):
    print("The list of courses: ")
    for j in courses:
        print("Course ID:%s, Course name:%s" % (j['id'],j['name']))


def input_marks(students, courses):
    id_course=input("Input course ID that you want input mark for: ")
    
    for a in courses:
        if a['id'] == id_course:
            for b in students:
                marks=int(input(f"Enter mark for {b['name']} in {a['name']}"))
                b.setdefault('marks',{})[id_course]=marks
            break
        else:
            print("No course ID ")
                
def show_student_marks(students,courses):
    id_student=input("Input student ID that you want to see mark for: ")
    
    for c in students:
        if c['id']== id_student:
            print(f"Student ID:{c['id']},Student name:{c['name']},DOB:{c['dob']}")
            if 'marks' in c:
                for d in courses:
                    marks= c['marks'].get(d['id'],'N/A')
                    print(f"Course ID:{d['id']}, Course name:{d['name']}, Mark:{marks}")
            else:
                print("No marks")
            break
        else:
            print("No student ID ")
        break
                
def main():
    while True:
        print('''
            Student mark management system: 
              0. Select course and input marks for students
              1. List students
              2. List courses
              3. Show student marks
              4. Exit
            ''')
        
        choice= int(input("Select number"))
        
        if choice == 0:
            input_marks(students, courses)
        elif choice ==1:
            list_student(students)
        elif choice ==2:
            list_courses(courses)
        elif choice ==3:
            show_student_marks(students,courses)
        elif choice ==4:
            break
        else:
            print("Enter again a number from 0->4: ")

if __name__ == "__main__":
    students=input_students()
    courses=input_courses()
    main()
    
    
            
            
        
            
            
        

    
    
                
            
        
        
    
    
        
        