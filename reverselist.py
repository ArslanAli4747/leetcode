ls = [2,3,4,5,1,10]
new = ls[:]
j = 0
for i in range(len(ls)-1,0,-1):
    new.insert(j,ls[i])
    new.pop(-1)
    j+=1

print(ls)
print(new)