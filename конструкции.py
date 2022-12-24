f = 0
while True:
    print(f)
    f = f + 1
    if f % 4 == 0:
        break
print("Готово!\n\n")

for x in range(2):
    for y in range(2):
        print(x, y)
print('Готово!\n')


w = int(input("Введите число "))
s = int(input("Введите число "))
if (w > s and w < 20):
    e = True
else:
    e = False

if e == True:
    print("готово!ура")
else:
    print("готово!лол")

a = int(input("Введите число "))
if a % 7 == 0:
    print("число делится на 7 \n")
elif a//10 != 0:
    print(f"число десятков в числе: {a // 10} \n")
else:
    print("lol")
num=(bin(a)[2:]) 
print(f"число в двоичной системе: {num}")

nnn = a.count('1')
print(f"количество единиц в числе: {nnn}")

mmm = a.index('1')
print(f"индекс единицы в строке : {mmm}")

b = str(input("введите слово"))
c = b.count('а')
print(f'количество буквы а в слове: {c}')


print("функции для файла, в котороом числа записаны в одну строчку:")
with open('1111.txt') as zz:       
    mm = zz.readline()
    print(f"функция redline: {mm}")
with open('1111.txt') as zz:   
    aa = zz.readlines()
    print(f"функция redlines: {aa}")
with open('1111.txt') as zz:       
    qq=[int(x) for x in zz]
    print(f"[x for x in f]: {qq}")
print("функции для файла, в котороом числа записаны на разных строчках:")
with open('2222.txt') as zz:       
    mm = zz.readline()
    print(f"функция redline: {mm}")
with open('2222.txt') as zz:   
    aa = zz.readlines()
    print(f"функция redlines: {aa}")
with open('2222.txt') as zz:       
    qq=[int(x) for x in zz]
    print(f"[x for x in f]: {qq}")