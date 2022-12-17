
s ="abc"
t = "ahbgdc"
j = 0
i = 0
dic = {}
while i<len(s) and j<len(t):
    if s[i] == t[j]:
        i+=1
    j+=1
if i==len(s):
    print("true")
else:
    print(False)