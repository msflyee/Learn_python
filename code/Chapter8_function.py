# Chapter8_function.py

def greet_user(user_name):
    print("Hello, " + user_name.title() + "!");"""show simple greetings"""

greet_user('jesse');



"""    Types of parameters    """
'''---------------------------------------------------------
# 1. arguments according to positions
# 2. arguments according to key words
# 3. default value
---------------------------------------------------------'''
# type-1
    #pet.py
def describe_pet(animal_type,pet_name):
    """show info of pets"""
    print("\nI have a " + animal_type + ".");
    print("My " + animal_type + "'s name is " + pet_name.title() + ".");

describe_pet('hamster','harry');

# type-2
    #pet.py
def describe_pet(animal_type,pet_name):
    """show info of pets"""
    print("\nI have a " + animal_type + ".");
    print("My " + animal_type + "'s name is " + pet_name.title() + ".");

describe_pet(animal_type = 'hamster',pet_name = 'harry');  # key words

# type-3
    # pet.py
def describe_pet(pet_name,animal_type = 'dog'):  # NOTICE: default values should be put in the rightmos
    """show info of pets"""
    print("\nI have a " + animal_type + ".");
    print("My " + animal_type + "'s name is " + pet_name.title() + ".");

describe_pet(pet_name = 'willie');



"""    Combine function with while-recycle    """
    # greeter.py
def get_formatted_name(first_name,last_name):
    """return the full name"""
    full_name = first_name + ' ' + last_name;
    return full_name.title();

while True:
    print("\nPlease tell me your name:");
    print("\n(Enter 'q' at any time to quit)");
    f_name = input("First name: ");
    if f_name == 'q':
        break;
    l_name = input("Last name: ");
    if l_name == 'q':
        break;
    formatted_name = get_formatted_name(f_name,l_name);
    print("\nHello," + formatted_name + "!");



"""     Pass lists as actual parameters     """
    # greet_users.py
def greet_users(names):   # names is a formal parameter
    """send greetings to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + '!';
        print(msg);
usernames = ['hannah','ty','margot'];
greet_users(usernames);   # usernames is a actual parameter

    # printing_models.py
unprinted_designs = ['iphone case','robot pendant','dodecahedron'];
completed_models = [];
def print_models(unprinted_designs,completed_models):

    """ simulate printing every model until all models are printed
        after print every model, put it into completed_models"""
    while unprinted_designs[:]:
        current_design = unprinted_designs.pop();

        " simulate the process of 3D printing "
        print("Printing model: " + current_design);
        completed_models.append(current_design);
def show_completed_models(completed_models):
    " show all the models that have been printed "
    print("\nThe following models have been printed:");
    for completed_model in completed_models:
        print(completed_model);
print_models(unprinted_designs[:],completed_models);
# Improvement-->use replication of unprinted_designs to protect it from being modified-->unprinted_designs[:] instead unprinted_designs
show_completed_models(completed_models);

""" Pass many parameters """
    #pizza.py
def make_pizza(*toppings):  # *toppings-->toppings[]
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping);
make_pizza('pepperoni');
make_pizza('mushrooms','green pepper','extra cheese'); # no matter how many parameters



""" Combine position-parameters with many-parameters """
def make_pizza(size,*toppings):  # *toppings-->toppings[] / **info-->dictionary{}
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping);
make_pizza(16,'pepperoni');
make_pizza(12,'mushrooms','green pepper','extra cheese'); # no matter how many parameters



""" Combine many-parameters with key-words-parameters """
def build_profile(first ,last,**user_info):
    profile = {};
    profile['first_name'] = first;
    profile['last_name'] = last;
    for key,value in user_info.items():
        profile[key] = value;
    return profile;
user_profile = build_profile('albert','einstein',location = 'priceton',field = 'physics');
print(user_profile);
