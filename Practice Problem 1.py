# lex_auth_0127390120635678722716
# Start writing you code here
class Purchase:
    list_of_items = ['Cake', 'Soap', 'Jam', 'Cereal', 'Hand Sanitizer', 'Biscuits', 'Bread','Chocolates']
    list_of_count_of_each_item_sold = [0] * len(list_of_items)

    def __init__(self):
        self.__items_purchased=[]
        self.__item_on_offer=None

    def provide_offer(self):
        index=-1
        for i in range(len(Purchase.list_of_items)):
            if Purchase.list_of_items[i].lower()=="hand sanitizer":
                index=i

            if index==-1:
                pass
            else:
                Purchase.list_of_count_of_each_item_sold[index]+=1
                self.__item_on_offer=Purchase.list_of_items[index]

    def sell_items(self,list_of_items_to_be_purchased):
        """"
            Accept the list of items that are to be purchased by the customer
            For every item in list_of_items_to_be_purchased
            Increment count of the item in the static list, list_of_count_of_each_item_sold by 1
            Add the item to attribute, items_purchased list
            If soap is purchased by the customer, then provide the offer by invoking the appropriate method
        """
        for item in list_of_items_to_be_purchased:
            item_index=-1
            for i in range(len(Purchase.list_of_items)):
                if str(item).lower()==str(Purchase.list_of_items[i]).lower():
                    item_index=i
                    Purchase.list_of_count_of_each_item_sold[item_index] += 1
                    self.__items_purchased.append(str(item))
            if str(item).lower() == "soap":
                self.provide_offer()

    @staticmethod
    def find_total_items_sold():
        total_items=0
        for purchase_items in Purchase.list_of_count_of_each_item_sold:
            total_items=total_items+purchase_items
        return total_items

    def get_items_purchased(self):
        return self.__items_purchased

    def get_item_on_offer(self):
        return self.__item_on_offer


c=Purchase()
c.sell_items(['JAM', 'CHOcolates', 'Ghee', 'Soap'])
c.find_total_items_sold()
print(c.get_items_purchased())
print(c.find_total_items_sold())
print(Purchase.list_of_count_of_each_item_sold)




