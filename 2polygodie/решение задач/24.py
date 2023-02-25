with open('24.txt') as f:
   let=f.readline()
   c,maxi=0,0
   #text=''
   delt=0
   for i in range(len(let)-1):
      if (let[i]=='C' or let[i]=='D' or let[i]=='F') and (let[i+1]=='A' or let[i+1]=='O'):
         delt=0
         #text=text+let[i]+let[i+1]
         c+=1
         maxi=max(c,max)
      else: delt+=1
      if delt==2:
         c=0
         #text=''
print(maxi)

with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*'
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)
