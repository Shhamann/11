def sistch():
    p = int(input("Ввидите основание системы счисления данного числа: "))
    np = int(input('Введите число: '))
    k = int(1)
    N10 = int(0)
    while not np == 0:
        N10 = N10 + (np % 10) * k
        k = k * p
        np = np // 10
    print(f"N10 = {N10}")
    print('Готово!')
def sistchh():
    N10 = int(input('Введите исходное 10-тичное число: '))
    p = 1
    while ((p<2) or (p>9)):
        p = int(input('Введите основание системы счисления в диапазоне [2; 9]: '))
    k = int(1)
    Np = int(0)
    while not (N10 == 0):
        Np = Np + (N10 % p)*k
        k = k*10
        N10 = N10 // p
    print('N' + str(p) + ' = ' + str(Np))
def morz():
    A = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    a = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')  
    Morze = list([".-","-...",".--","--.","-..",".","...-","--..","..",".---","-.-",".-..","--","-","---",".--.",".-.","...","-","..-","..-.","....","-.-.","---.","----","--.-",".--.-","-.--","-..-","..-..","..--",".-.-"])
    InpS = input('Введите исходную строку: ')
    OutS = str('')
    for i in range(1, (len(InpS)+1)):
        for j in range (1, 32):
            if (InpS[i-1] == str(A[j-1])) or (InpS[i-1] == str(a[j-1])):
                OutS = OutS + str(Morze[j-1]) + ' '
    print('Ваша строка, перекодированная на азбуку Морзе: ' +OutS)
def hemm():
    nums=list(range(10))
    print(nums)
    b='0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem=list(map(int, b.split()))
    print(hem)
    def distance(x,y):
        k=7
        for i in range(7):
            if x%10==y%10:
                k=k-1
                x=x//10
                y=y//10
        return k
    cod=int(input("код="))
    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
        D=distance(cod,hem[i])
    if D<min:
        min=D
        imin=i
    if min==0:
        print(f"Код верный: символ {nums[imin]}")
    elif min==1:
        print(f"Код исправлен: символ {nums[imin]}")
    else:print(f"Код неверный")

def tabl():
    p = int(input('Введите р (2<p,=10): '))
    print(f'{p} - ичная таблица умножения')
    for i in range(1, p):
        for j in range(1, p):
            z = (i*j//p)*10 + (i*j)%p
            print(z, end = ' ')
        print()
vchod = int(input('Задачи: \n 1) перевод в 10-ую систему счиления \n 2) перевод из 10-ой системы счисления \n 3) перевод слова с помощью азбуки морзе \n 4) код хемминга \n 5) таблица умножения чисел в различных системах счисления'))
if vchod == 1:
    sistch()
if vchod == 2:
    sistchh()
if vchod == 3:
    morz()
if vchod == 4:
    hemm()
if vchod == 5:
    tabl()