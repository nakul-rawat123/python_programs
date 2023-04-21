'''Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will 
become the final amount = total fare + 10% of the total fare.
Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.'''
# method-1:
class vehicles:
    def vehicle_fare(self, capacity):
        fare =  capacity*100
        return fare
class busses:
    def bus_fare(self, fare):
        new_fare = ((fare*10)/100)+fare
        return new_fare
bus1 = busses()
fare = bus1.vehicle_fare(50)
print('the total fare of the bus is: Rs.',bus1.bus_fare(fare), 'using method - 1')
# method_2
class busses_(vehicles):
    def bus_fare_(self):
        fare = super().vehicle_fare(50)
        new_fare = ((fare*10)/100)+fare
        return new_fare
bus2 = busses_()
print('the total fare of the bus is: Rs.',bus2.bus_fare_(), 'using method - 2')