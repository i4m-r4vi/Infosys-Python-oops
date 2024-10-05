class Instructor:
    def __init__(self):
        instructor_name=None
        experience=None
        avg_feedback=None
        technology_skill=None
        self.__instructor_name=instructor_name
        self.__experience=experience
        self.__avg_feedback=avg_feedback
        self.__technology_skill=technology_skill
    
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    
    def set_experience(self,experience):
        self.__experience=experience

    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
    
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
    
    def get_instructor_name(self):
        return self.__instructor_name
    
    def get_experience(self):
        return self.__experience
    
    def get_technology_skill(self):
        return self.__technology_skill
    
    def get_avg_feedback(self):
        return self.__avg_feedback
    
    def allocate_course(self,technology):
        skill=['C++','JAVA','PYTHON']
        for j in skill:
            if(j==technology):
                return True
            else:
                return False
    
    def check_eligibility(self):
        experience=self.get_experience()
        feedback=self.get_avg_feedback()
        if (experience > 3 and feedback >= 4.5):
            return True
        elif (experience <= 3 and feedback >= 4):
            return True
        else:
            return False
                
classes=Instructor()
classes.set_avg_feedback(4.5)
classes.set_experience(4)
print(classes.check_eligibility())
print(classes.allocate_course("cobol"))

    
