#lex_auth_012736358230835200606
#Start writing your code here
class Student:
    def __init__(self):
        student_id=None
        marks=0
        age=None
        self.__student_id=student_id
        self.__marks=marks
        self.__age=age
    
        
    def set_student_id(self,student_id):
        self.__student_id=student_id
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    
    def validate_marks(self):
        marks=self.get_marks()
        if(marks):
            if (marks>=65):
                if(marks>100):
                    return False
                return True
            elif(marks<0):
                return False
            
            return True
        else:
            return False

        
    def validate_age(self):
        age=self.get_age()
        if(age):
            if(age>=21):
                return True
            else:
                return False
        else:
            return False
            
    
    def check_qualification(self):
        if(self.__marks and self.__age):
            if(self.__marks>=65 and self.__age>10):
                if(self.__marks>100):
                    return False
                return True
            else:
                return False
        else:
            return False

stud1=Student()
stud1.set_marks(66)
stud1.set_age(10)
stud1.set_marks(0)
stud1.set_marks(101)
stud1.set_age(20)
stud1.set_age(19)
print(stud1.get_age())
print(stud1.check_qualification())