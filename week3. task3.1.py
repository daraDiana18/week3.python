import math
def cPow(lst):
    x1 = math.sqrt(math.pow(lst[0],2)+math.pow(lst[1],2))
    x2 = math.sqrt(math.pow(lst[2],2)+math.pow(lst[3],2))
    print("hypotenuses of 1 triangle =",x1)
    print("hypotenuses of 2 triangle =",x2)
    if x1 > x2:
        print("the hypotenus or 1st triangle largest:",x2)
    elif x1 == x2:
        print("they are equal")
    else:
        print("the hypotenus or 2nd triangle largest:",x2)

tr=[]
print("enter the sides of triangle")
for i in range(2):
    print("for",i+1,"triangle")
    tr.append(float(input("the 1st side: ")))
    tr.append(float(input("the 2st side: ")))

cPow(tr)
