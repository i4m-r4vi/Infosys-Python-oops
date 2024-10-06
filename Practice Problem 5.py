#lex_auth_012752531983671296301
#Start writing you code here
import time
from datetime import timedelta, date


class GarmentOrder:
    garment_dict= {"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}
    def __init__(self,cloth_type,no_of_piece):
        self.__cloth_type=cloth_type
        self.__no_of_piece=no_of_piece
        self.__order_date=time.strftime("%d/%m/%Y")
        self.__delivery_date=0

    def get_cloth_type(self):
        return self.__cloth_type

    def get_no_of_piece(self):
        return self.__no_of_piece

    def get_order_date(self):
        return self.__order_date

    def get_delivery_date(self):
        return self.__delivery_date

    def calculate_amount(self):
        cloth_type=self.__cloth_type
        for garment in GarmentOrder.garment_dict:
            if garment == cloth_type:
                values=GarmentOrder.garment_dict[garment]
                return values[1]*self.__no_of_piece

    def update_stock(self):
        """
            Update stock based on details given below.
            Set the attribute, delivery_date to order_date + number of days required to deliver the ordered item. Hint: d = date.today() + timedelta(days=n) will give the resultant date which is the sum of today's date and 'n' number of days. Convert it to string using time.strftime("%d/%m/%Y") where time is the datetime variable to be converted to string.
            Update the number of pieces available for the ordered cloth type based on number of pieces ordered
        """
        cloth_details=GarmentOrder.garment_dict[self.__cloth_type]
        delivery_days=cloth_details[2]
        self.__delivery_date=(date.today()+timedelta(days=delivery_days)).strftime("%d/%m/%Y")
        cloth_details[0]=cloth_details[0]-self.__no_of_piece

    def take_order(self):
        if self.__cloth_type in GarmentOrder.garment_dict.keys():
            no_of_pieces=GarmentOrder.garment_dict[self.__cloth_type]
            if self.__no_of_piece <= no_of_pieces[0]:
                amount=self.calculate_amount()
                self.update_stock()
                return amount
            else:
                return -1
        else:
            return -1

G=GarmentOrder("saree",15)
G.update_stock()
print(G.get_delivery_date())
print(G.get_no_of_piece())
print(G.calculate_amount())
print(GarmentOrder.garment_dict)
