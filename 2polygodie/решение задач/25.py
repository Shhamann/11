from operator import itemgetter
def f25(chislo):
    if int(chislo)%2023==0:
        ost=int(chislo)//2023
        itog.append(chislo)
        itogost.append(ost)

itog=[]
itogost=[]
for i in range(10):
  for y in range(1000000):
      chislo='1'+str(i)+'21394'
      f25(chislo)

      chislo='1'+str(i)+'2139'+str(y)+'4'
      if int(chislo)>10**10: break
      f25(chislo)

itogo=list(zip(itog,itogost))
print(*itogo)
print(sorted(itogo, key=itemgetter(1)))
for i in range(2023,10**10,2023):
    num=str(i)
    if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
        print(i,i//2023)
