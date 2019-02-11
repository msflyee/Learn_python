#Chapter-3_list.py;
bicycles = ['trek','cannondale','redline','specialized'];
print(bicycles[0].title() + " " + bicycles[-1].title()+ " " + bicycles[-2].title());

message = "My first bicle was a" + bicycles[0].title() + ".";
print(message);

names = ['Yee','Liu','Nie','Yuan'];
print(names[-1] + " " + names[-2] + " " + names[-3] + " " + names[-4]);
print(names[-3] + "," + "I love you.");

transportations = ['bicycle','car','bus','subway','walk'];
print("I want to have a Cadillac as my " + transportations[1] + ".");

motorcycles =['honda','yamaha','suzuki'];
print(motorcycles);
motorcycles[2] = 'ducati';
print(motorcycles);
motorcycles.append('ducati');
print(motorcycles);
motorcycles.insert(2,'Cadillac');
print(motorcycles);
del motorcycles[2];
print(motorcycles);

second_owned = motorcycles.pop(1);
print(second_owned);
print(motorcycles);

motorcycles.remove('ducati');
print(motorcycles);

cars = ['Bmw','Toyota','Audi'];
#cars.sort(reverse = True);
#print(cars);


print(sorted(cars));
cars.reverse();
print(cars);

print(len(cars));
#copyright by Karry Yee in WuHan, Chin
