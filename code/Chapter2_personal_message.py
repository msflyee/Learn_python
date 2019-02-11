first_name = " Eric   ";
"""等学到循环再将这一部分优化，能够识别用户的姓和名并将用户的名显示在用户界面上"""
last_name = " Hufee  ";
full_name =first_name + last_name;
message = "Hello" + " " + first_name.strip() + "," + "would you like to learn some Python today?  "
print(message.strip())

name = input("Please input your name:"); #input names

name = name.strip();
names = [];
for letter in name:
    names.append(letter);
    if letter == ' ':
        del names[-1];
        first_name = ''.join(names);
        print('Hello'+' '+first_name.title() +','+'would you like to learn some Python today?'); #waiting for improvement  --->complete improvement
