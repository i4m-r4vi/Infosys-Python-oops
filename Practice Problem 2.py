#lex_auth_0127390295941775362719
#Start writing you code here
class Dog:
    counter=100
    dog_breed_dict={"Labrador Retriever":5,"German Shepherd":12,"Beagle":10}
    def __init__(self,breed_list,accessories_required):
        self.__breed_list=breed_list
        self.__dog_id_list=[]
        self.__price=0
        self.__accessories_required=accessories_required
    def get_dog_id_list(self):
        return self.__dog_id_list
    def get_breed_list(self):
        return self.__breed_list
    def get_price(self):
        return self.__price
    def get_accessories_required(self):
        return self.__accessories_required

    def validate_breed(self):
        for breed in self.__breed_list:
            if breed not in Dog.dog_breed_dict:
                return False
        return True

    def validate_quantity(self):
        for breed in self.__breed_list:
            quantity=Dog.dog_breed_dict[breed]
            if quantity == None or quantity == 0:
                    return False
        return True

    def calculate_total_price(self):
        if self.validate_breed():
            if self.validate_quantity():
                for breed in self.__breed_list:
                    Dog.dog_breed_dict[breed]+=1
                    gen_id=self.generate_dog_id(breed)
                    self.__dog_id_list.append(gen_id)
                    price=self.get_dog_price(breed)
                    self.__price+=price
                if self.__accessories_required:
                    self.__price+=350
                if self.__price>1500:
                    discount=self.__price*5/100
                    discount_price=self.__price-discount
                    self.__price=discount_price
            else:
                return -2
        else:
            return -1

    def generate_dog_id(self,breed):
        Dog.counter+=1
        gen_id=breed[0]+str(Dog.counter)
        return gen_id

    def get_dog_price(self,breed):
        if breed == "Labrador Retriever":
            return 800
        elif breed =="German Shepherd":
            return 1230
        elif breed == "Beagle":
            return 650
        else:
            return 0


c = Dog(['Labrador Retriever', 'Beagle'],True)
print(c.validate_breed())
print(c.validate_quantity())
print(c.generate_dog_id('Labrador Retrieve'))
print(c.calculate_total_price())

