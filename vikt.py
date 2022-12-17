def vikt(x):
    que = ['1000 - 7 = ?', 'Висит груша, нельзя скушать', 'Зимой и летом одним цветом', '3^2 = ', '2 + 3 = ']
    ans = ['993', 'лампочка', 'ёлка', '9', '5']
    kolvo = 0
    for i  in range(5):
        print(que[i])
        yans = str(input("Ответ:"))
        if yans == ans[i]:
            kolvo += 1
    print(f'Количество правильных ответов:{kolvo}')
    return str(input(f' начать с начала?(yes/no)'))
a = str('yes')
while a == 'yes':
    x = str(a)
    a = vikt(x)
