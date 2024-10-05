# class shoppingCart:
#     __counter=0
#     def __init__(self,cart_items):
#         self.__cart_items=cart_items
#         shoppingCart.__counter+=1
#
#     @staticmethod
#     def getCounter():
#         return shoppingCart.__counter
#
#     def get_cart_items(self):
#         return self.__cart_items
#
#     def set_cart_items(self,new_cart_items):
#         self.__cart_items=new_cart_items
#
#     def remove_items(self,removeItems):
#         self.__cart_items.remove(removeItems)
#         return self.__cart_items
#
#     def add_newCart(self,addcart):
#         self.__cart_items.append(addcart)
#         return self.__cart_items
#
#     def no_of_cartItems(self):
#         return "The Length of Cart is "+str(len(self.__cart_items))
#
# def testShopping():
#     print(shoppingCart.getCounter())
#     shoppingClass1=shoppingCart(['Uniform'])
#     print(shoppingClass1.getCounter())
#     shoppingClass2=shoppingCart(['Umbrella','Raincoat','Tie'])
#     print(shoppingClass2.getCounter())
#
# testShopping()

list_of_items=['Apple','Orange','Grapes']
list_of_count_of_each_item_sold = [0] * len(list_of_items)
for i in range(len(list_of_items)):
    if list_of_items[i]=="Orange":
        list_of_count_of_each_item_sold[i]+=1
        print(True)
    else:
        print(False)
print(list_of_count_of_each_item_sold)