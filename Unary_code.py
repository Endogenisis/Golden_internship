s=input("")
a=1
for i in range(len(s[:-1])):
    if s[i]==s[i+1]:
        a+=1
    elif s[i]!=s[i+1]:
        if s[i]=="1":
            print("0"+" "+str("0"*a), end=" ")
        else: print("00"+" "+str("0"*a), end=" ")
        a=1
if s[-1] == "1":
    print("0"+" "+str("0"*a),end=' ')
else: print("00"+" "+str("0"*a),end=' ')