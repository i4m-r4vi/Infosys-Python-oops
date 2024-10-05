# lex_auth_012727119215337472135
# Start writing your code here
class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name

    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg

    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available

    def get_flower_name(self):
        return self.__flower_name

    def get_price_per_kg(self):
        return self.__price_per_kg

    def get_stock_available(self):
        return self.__stock_available

    def validate_flower(self):
        flower_name=[
            'Orchid','Rose','Jasmine'
        ]
        flower1=str(self.get_flower_name()).casefold()
        if flower1 in str(flower_name).casefold():
            return True
        else:
            return False

    def check_level(self):
        flower_name={
                    'Orchid':15,'Rose':25,'Jasmine':40
                }
        flower1=self.get_flower_name()
        flowers_stock=int(self.__stock_available)
        for  flower1 in str(flower_name):
            if flower1:
                if flowers_stock > flower_name[flower1]:
                    return True
                else:
                    return False


flower=Flower()
flower.set_flower_name('rOSE')
flower.set_stock_available(14)
print(flower.validate_flower())
print(flower.check_level())




