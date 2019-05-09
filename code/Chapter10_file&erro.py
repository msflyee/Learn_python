# Chapter_10_file&erro.py

filename = r'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

filename1 = r'pi_million_digits.txt'
with open(filename1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

"""birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi. ")
"""

""" How to creat a empty file and write messages into it """
# w ---> write mode
# r --->read mode
# a --->add mode

# write_message.py
filename = 'programing.txt'
with open(filename,'w') as file_object:     # creat a file called "programing.txt" and use '.write()' to write messages into it   'w' means using the way of writing
    file_object.write("I love programing.\n")
    file_object.write("I love creating new games.\n")

with open(filename,'a') as file_object1:
    file_object1.write("I love fighting.")

"""How to deal with exceptions"""
# division.py
print("\nGive me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

"""while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0! ")        # print messages you want to send to users when users come up with exceptions
    else:
        print(answer)"""        # print messages you want to send to users when no exceptions exsit

# alice.py
"""filename = 'alice.txt'
try:
    with open(filename) as file_object2:
        contents = f_obj2.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exsit."
    print(msg)
else:
    # caculate how many words in the file
    words = contents.split()
    num_words = len(words)"""

# we can pack these codes into a fuction so as to make them be used more easily
def count_words(filename):
    try:
        with open(filename) as f_obj3:
            contents = f_obj3.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + "dose not exist."
    else:
        words = contents.split()
        num_words = len(words)
        print("The file has " + str(num_words) + " words." )
count_words('programing.txt')
