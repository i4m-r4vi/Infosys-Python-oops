#lex_auth_012736365493280768607
#Implement Student class here
class Student:
    def __init__(self):
        fees=None
        marks=None
        course_id=None
        student_id=None
        age=None
        self.__fees=fees
        self.__marks=marks
        self.__course_id=course_id
        self.__student_id=student_id
        self.__age=age
        
    def set_student_id(self,student_id):
        self.__student_id=student_id
        
    def set_age(self,age):
        self.__age=age
        
    def set_course_id(self,course_id):
        self.__course_id=course_id
        
    def set_fees(self,fees):
        self.__fees=fees
        
    def set_marks(self,marks):
        self.__marks=marks
        
    def get_student_id(self):
        return self.__student_id
        
    def get_age(self):
        return self.__age
    
    def get_course_id(self):
        return self.__course_id
        
    def get_fees(self):
        return self.__fees
        
    def get_marks(self):
        return self.__marks
        
    def validate_marks(self):
        marks=self.get_marks()
        if (0 <= marks) and (marks <= 100):
            return True
        else:
            return False
        
    def validate_age(self):
        age=self.get_age()
        if age>20:
            return True 
        else:
            return False
    
    def check_qualification(self):
        marks=self.get_marks()
        age=self.get_age()
        if age>20 and marks>=65:
            if marks>100:
                return False
            else:
                return True
        else:
            return False
            
    def choose_course(self,course_id):
        course={
            1001:25575,
            1002:15500
        }
        marks=self.get_marks()
        if course_id in course:
            self.set_course_id(course_id)
            self.set_fees(course[course_id])
            if marks > 85:
                fees=self.get_fees()
                amount=25/100*fees
                final_amount=fees-amount
                self.set_fees(final_amount)
            return True
        return False
        
maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if maddy.check_qualification():
    print("Student has qualified")
    if maddy.choose_course(1002):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")