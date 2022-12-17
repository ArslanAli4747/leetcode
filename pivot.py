
def pivotIndex(nums):
        leftsum = 0
        rightsum = 0
        left = None
        right = None
        if(len(nums)<1):
            return -1
        mid = len(nums)//2
        if mid>1:
            pass

print(pivotIndex([1,2,3]))
ls =[1,7,3,6,5,6]
leftsum = 0
rightsum = 0
left = []
right = []
index = 0
for i in range(len(ls)):
    if i==0:
        leftsum = 0
    if i == len(ls)-1:
        rightsum = 0
    if i>0:
        left = ls[:i]
        leftsum = sum(left)
    if i < len(ls)-1:
        right = ls[i+1:]
        rightsum = sum(right)
    if leftsum == rightsum:
        index = i
        break
    else:
        index = -1

    print("left : ",left)
    print("right , ",right)
    print("\n")
    print("leftsum : ",leftsum)
    print("rightsum : ",rightsum)
    print("\n")

print(index)