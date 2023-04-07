
# # 6*4
a = ["  *   ", " * *  ", " **** ", "*    *"]
o = [" **** ", "*    *", "*    *", " **** "]



alfa = [None] * 122
alfa[97]= a
alfa[111]= o


str = "aoao"
newSp = []
for i in range(len(str)):
    wr = alfa[ord(str[i])]
    newSp.append(wr)

for i in range(len(newSp)):
    for j in range(4):
        print(newSp[i][j])
