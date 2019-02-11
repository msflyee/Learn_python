# Chapter4-operations on a list
magicians = ['Alice','David','Liuqian'];
for magician in magicians:  #define 'magician'
    print(magician + '\t');

for value in range(1,5):  #define value
  print(value);

numbers = list(range(1,6));
print(numbers);

even_numbers = list(range(2,11,2));  #打印偶数，函数range()的第三个参数为 步数
print(even_numbers);

squares = [];
for value in range(1,6):
    squares.append(value ** 2);
    print(squares);

list = [4,3,2,1];
for value in list:
    squares.pop(value);
    print(squares);

squares = [value ** 2 for value in range(1,11)];
print(squares);

list = [];
for value in range(1,1000001):
    list.append(value);
print(min(list));
print(max(list));
print(sum(list));

players = ['Charles','Martina','Florence','Eli'];
print(players[0:3]);
print(players[:3]);
print(players[2:]);
print(players[-3:]);

for player in players[-3:]:
    print(player);

_players = players[:];
print(_players);
print(players);
players.append('Karry');
print(_players);
print(players);

#copyright by Karry Yee in WuHan,China.
