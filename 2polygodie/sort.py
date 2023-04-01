s = [100, 0, 1000, 10, 2, 4]
a = 1
while a == 1:
    if all(s[i] <= s[i + 1] for i in range(len(s)-1)):
        a = 2
    for i in range(len(s)-1):
        if(s[i] > s[i+1]):
            s[i], s[i+1] = s[i+1], s[i]
    for i in range(len(s)):
        print(s[i])
  
        
    
