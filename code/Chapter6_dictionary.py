# alien.py
alien_0 = {'color':'green','points': 5 };
print(alien_0['color']);
print(alien_0['points']);
alien_0['x_position'] = 0;
alien_0['y_position'] = 25;
print(alien_0);

alien_1 = {'x_position':0,'y_position':25,'speed':'medium'};
print("Original x_position:" + str(alien_1['x_position']));

# move towards right
# the distance depends on the speed of the alien
if alien_1['speed'] == 'slow':
    x_increment = 1;
elif alien_1['speed'] == 'medium':
    x_increment = 2;
else:
    # this alien must move very quickly
    x_increment = 3;

# the new position = old position + increment
alien_1['x_position'] = alien_1['x_position'] + x_increment;
print('New x_position:' + str(alien_1['x_position']));

# favorite_languages.py
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    };
print("\nSarah's favorite language is " + favorite_languages['sarah'].title() + ".\n")
friends = ['phil','sarah'];
for name in favorite_languages.keys():
    print(name.title());
    if name in friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!");

print("\nThe following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title());

print("\nThe following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title());

languages = set(favorite_languages.values());
print(languages)

# user.py
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    };
for key,value in user_0.items():
    print("\nKey: " + key);
    print("Value: " + value + "\n");

# aliens.py 1.0
alien_0 = {'color':'green','points': 5};
alien_1 = {'color':'yellow','points': 10};
alien_2 = {'color':'red','points': 15};

aliens = [alien_0,alien_1,alien_2];
for alien in aliens:
    print(alien);

print("\n")

# aliens.py 2.0
      # create a empty list to save aliens
aliens = []

      # create 30 aliens
for alien_number in range(30):
      new_alien = {'color':'green','point':5,'speed':'slow'};
      aliens.append(new_alien)

      # show the first 5 aliens
for alien in aliens[:5]:
      print(alien);
print("...");

      # show the amount of aliens that have been created
print("Total number of aliens: " + str(len(aliens)));

# pizza.py
  # save all the information aof the pizza
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    };
  # show the information of the pizza
print("\nYou ordered a " + pizza['crust'] + "-crust pizza" +
" with the following toppings:");
for  toppings in pizza['toppings']:
    print("\t" + toppings);

# many_user.py
users = {
'einstein':{
    'first':'albert',
    'last':'einstein',
    'location':'princeton',
    },
'curie':{
    'first':'marie',
    'last':'curie',
    'location':'paris',
    },
}

for username,user_info in users.items():
    print("\nUsername: " + username);
    full_name = user_info['first'] + " " + user_info['last'];

    print("\tFull name: " + full_name.title());
    print("\tLocation: " + user_info['location']);
