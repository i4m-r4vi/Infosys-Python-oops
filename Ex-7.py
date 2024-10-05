class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name =passenger_name
        self.__ticket_id=None
        self.__source=source
        self.__destination=destination

    def get_ticket_id(self):
        return self.__ticket_id
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def get_passenger_name(self):
        return self.__passenger_name

    def validate_source_destination(self):
        destinations='Mumbai','Chennai','Pune','Kolkata'
        sources='Delhi'
        passenger_name=self.get_passenger_name()
        source=self.get_source().lower().upper()
        destination=self.get_destination().lower().upper()
        if source in sources.lower().upper():
            for word in destinations:
                if destination in word.lower().upper():
                    return True
        return False

    def generate_ticket(self):
        destinations = self.get_destination()
        sources=self.get_source()
        valid_source=self.validate_source_destination()
        s = sources[0]
        d = destinations[0]
        Ticket.counter+=1
        if valid_source:
            if Ticket.counter<10:
                self.__ticket_id= str(s)+str(d)+'0'+str(Ticket.counter)
            else:
                self.__ticket_id= str(s) + str(d)+ str(Ticket.counter)

t=Ticket("Sudarshan","Delhi","Mumbai")
Ticket.counter=9
t.generate_ticket()
print(t.get_ticket_id())
print(t.get_passenger_name())
print(t.get_source())
print(t.get_destination())
t.generate_ticket()
print(t.get_ticket_id())










