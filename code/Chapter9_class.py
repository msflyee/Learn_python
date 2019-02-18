# Chapter9_class.py

"""How to creat a brand new class!"""
    #dog.py
class Dog():
    """First try of simulating a dog"""
    def __init__(self,name,age):        #NOTICE:Here are two underlined lines!!!  "" _"_init_"_""  It is kind of like the constructor funciton in C++.
        """initialize name and age"""   #All parameters which will be used in this class will be defined and assigned in the "__init__" function.
        self.name = name;
        self.age = age;
    def sit(self):
        """simulate dog's sitting"""
        print(self.name.title() + "is now sitting.");
    def roll_over(self):
        """simulate dog's rolling"""
        print(self.name.title() + "rolled over!");
my_dog = Dog('whillie', 6);
my_dog.sit();
my_dog.roll_over();



    #car.py
class Car():
    """First try of simulating a car"""
    def __init__(self,make,model,year):
        """initialize the car"""
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0;
    def read_odometer(self):
        """print a message to indicate the odometer"""
        print("This car has " + str(self.odometer_reading) + "miles on it.")
    def update_odometer(self,mileage):
        """protect odometer_reading from being rolled back"""
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage;
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """add increments to odometer"""
        if miles >=0:
            self.odometer_reading += miles;
        else:
            print("You can't roll back an odometer!")
    def get_descriptive_name(self):
        """return simple and clean discriptive infomation"""
        long_name = str(self.year) + ' ' + self.make  + ' ' + self.model;   #long_name is a string made up of three strings and two spaces
        return long_name.title();
my_new_car = Car('Audi','a4',2016);
print(my_new_car.get_descriptive_name());

my_new_car.update_odometer(23500);
my_new_car.read_odometer();

my_new_car.increment_odometer(100);
my_new_car.read_odometer();
my_new_car.increment_odometer(-100);



"""How to inherit a parent class!"""
class ElectricCar(Car):
    " special points of electric car "
    def __init__(self,make,model,year):
        " initialize the attributes of the parent class "
        super().__init__(make,model,year)       #fuction "super()" connect the parent class with the subclass--->make the subclass contain all attributes of the parent class
        # equal to:Car.__init__(self,make,model,year)
        self.battery_size = 70
    def describe_battery(self):
        """ print a message to describe the battery """
        print("This car has a " + str(self.battery_size) + "-kwh battery")
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
ElectricCar.battery_size = 100
my_tesla.describe_battery()     # why the message shows that battery_size hasn't been changed?

""" How to transfer a class to a module and import it """
#Example: here is a module named car.py and the class "Car" is in it.
# We can import it like this: from car import Car.
# Meanwhile, a module can include classes not only one classes.
# And in this case, we can do like this: from car import Car,ElectricCar

""" Come to see the stadard modules in Python """
    # favorite_languages.py
from collections import OrdereDict
favorite_languages = OrdereDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c++'

for name,langauge in favorite_languages.items():
    print(name.title() + "'s' favorite language is " + langauge.title() + "." )
