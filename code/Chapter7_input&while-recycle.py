# Chapter7_input&while-recycle.py
    # greeter.py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt);
print("\nHello, " + name + "!");



    # even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ");
number = int(number);

if number % 2 == 0:
    print("\nThe number " + str(number) + "is even.");
else:
    print("\nThe number " + str(number) + " is odd.");



'''---------------------------------------------------------------
# all ways of using "while"
# 1- while number < 4:
# 2- while s != True:   s--->bool
# 3- while a in b:   'a' can be string or int or other types
# 4- while a:        a-->bool
--------------------------------------------------------------'''
    # parrot.py
prompt = "\nTell me something, and I will repeat it back to you:";
prompt += "\nEnter 'quit' to end the program.";
message = " ";
while message != 'quit':
    message = input(prompt);
    print(message);

#using signs to signify and simplify the condition to choose the next step
prompt = "\nTell me something, and I will repeat it back to you:";
prompt += "\nEnter 'quit' to end the program.";

active = True;  # the sign-->active

while active:
    message = input(prompt);

    if message == 'quit':
        active = False;
    else:
        print(message);



    # cities.py
prompt = "\nTell me something, and I will repeat it back to you:";
prompt += "\nEnter 'quit' to end the program.";

while True:
    city = input(prompt);
    if city == 'quit':
        break;          #using break to end the whole recycle
    else:
        print("I'd love to go to " + city.title() + "!");



        #counting.py
current_number = 0;
while current_number <10:
    current_number += 1;
    if current_number % 2 == 0:
        continue;
    print(current_number);



    # confirmed_users.py
'''First, creat a list of users waiting for being verified and a list to save users who have been verified'''
unconfirmed_users = ['alice','brain','candace'];
confirmed_users = [];

'''verify every user and then put them into confirmed_users'''
'''--------------------------------------------------------------
# how to use "while" when traversing lists
--------------------------------------------------------------'''
while unconfirmed_users:               # this expression traverses the elements in "unconfirmed_users"
    current_user = unconfirmed_users.pop();
    print("Verifying user:" + current_user.title());
    confirmed_users.append(current_user);

''' show all users who have been verufied'''
print("\nThe following users have been confirmed:");
for confirmed_user in confirmed_users:
    print(confirmed_user.title());



# mountain_poll.py
response = {};

polling_active = True;  # set a sign to indicate whether the survey to continue
while polling_active:
    # hint to input the answers and the names of people being surveied
    name = input("\nWhat is your name?");
    response = input("Which mountain would you like to climb someday?");

    responses[name] = respnse;      # put the answers into the dictionary
    # to find whether there is anayone else to take part in this survey
    repeat = input("Would you like to let another person respond? (yse/no)");
    if repeat == 'no':
        polling_active = False;

    # end the survey and show the outcome
print("\n---Poll Results---")
for name in response.items():
    print(name + "would like to climb " + response + ".");
