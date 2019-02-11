#cars.py
cars = ['audi','bmw','subara','toyota'];
for car in cars:
    if car =='bmw':
        print(car.upper());
    else:
        print(car.title());

age_0 = 22;age_1 = 18;
if age_0 >= 21 and age_1>=21:
    print('Great!');

age_0 = 22;age_1 = 18;
if age_0 >= 21 or age_1>=21:
    print('Great!');

#toppings.py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#amusement-park.py
age = 12;
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#and & or.py
age_0 = 22;
age_1 = 18;
age_0 >= 21 or age_1 >= 21;
age_0 >= 21 and age_1 >=21;

#banned_users.py
banned_users = ['andrew','carolina','david'];
user = 'marie';
if user not in banned_users:
    print(user.title()+",you can post a response if you wish.");

#color_of_alien.py 1.0
alien_color_1 = ['green','yellow','red'];
if 'green' in alien_color_1:
    print("You've got 5 points.");

#color_of_alien.py 2.0
alien_color_2 = ['yellow','red'];
if 'green' in alien_color_2 :
    print("You've got 5 points.")
else:
    print("You've got 10 points.")

#stages_of_life.py
age = 19;
if age <2:
    print("He is a baby.");
elif age < 4:
    print("He is learning how to wal.k");
elif age < 13:
    print("He is a boy.");
elif age < 20:
    print("He is a teenager.");
elif age < 65:
    print("He is a adult.");
else:
    print("He is a old man.");

#toppings.py 1.0
requested_toppings = ['mushrooms','green pepper','extra'];

for requested_topping in requested_toppings:
    if requested_topping =='green pepper':
        print("Sorry,we are out of green right now.");
    else : print("Adding " + requested_topping + ".");
print("\nFinished making your pizza.");

#toppings.py 1.01
requested_toppings = [ ];

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".");
    print("\nFinished making your pizza.");
else:
    print("Are you sure you want a plain pizza?")

#toppings.py 2.0
requested_toppings = ['mushrooms','green pepper','extra cheese'];
avaliable_toppings = ['mushrooms','olives','green peppers','pepperoni','pinapple','etra cheese'];

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in requested_toppings:
            print("Adding " + requested_topping + ".");
        else:
            print("Sorry, we don't have " + requested_topping + ".");
    print("\nFinished making your pizza.\n");
else:
    print("Are you sure you want a plain pizza?")

#log_in_plus_register.py
current_users = ["Eric","Karry","Stark","Rogers","Jack"];
new_users = ["Eric","Hank","Smith","Jhon","Tom"];

#register
for user in new_users:
    if user in current_users:
        print("Sorry,this account name has been used by someone,please change your account name!")
    else:
        if user == "admin":
            print("Hello admin,would you like to see a status report?");
        else:
            print("Hello " + user + ",thank you for registering!")
#log in
for user in current_users:
    print("Hello " + user + ",welcome to a unique world!")
