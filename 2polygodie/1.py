word = 'ao' 
alf = ['a', 'o']
a = ["  *   ", " * *  ", " **** ", "*    *", "*    *"] 
o = [" **** ", "*    *", "*    *", "*    *", " **** "]

mat = [a, o]
ch = [alf.index(x) for x in list(word)]
for i in range(len(mat[0])):
    for j in range(len(ch)):
        print(mat[ch[j]][i], end = '  ')
    print()
