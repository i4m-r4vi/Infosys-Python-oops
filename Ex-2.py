#lex_auth_01275045546160947226
class Athlete:
    def _init_(self,name,gender):
        self.__name=name
        self.__gender=gender
        self.get_name()
        self.get_gender()
        
    def set_name(self,name):
        self.__name=name

    def set_gender(self,gender):
        self.__gender=gender
        
    def get_name(self):
        return self.__name
        
    def get_gender(self):
        return self.__gender
        
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
            
girl=Athlete("Maria","girl")
girl.running()
girl.set_name("Ravi")
girl.set_gender("male")
girl.running()