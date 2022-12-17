def vikt():
    que = ['1000 - 7 = ?', 'Висит груша, нельзя скушать', '']
    ans = ['993', 'Лампочка']
    kolvo = 0
    for i  in range(2):
        print(que[i])
        yans = str(input("Ответ:"))
        if yans == ans[i]:
            kolvo += 1
    print(f'Количество правильных ответов:{kolvo}')
    # return str(input(f' начать с начала?(yes/no){x}'))
vikt()
