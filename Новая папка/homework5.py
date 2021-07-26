
a=int(input("FERZ1:  "))
b=int(input("FERZ2:  "))
c=int(input("figura1:  "))
d=int(input("figura2:  "))
diffx=a - c
diffy= b-d

if diffx<0:
    diffx = -diffx
if diffy<0:
    diffy = -diffy

if (diffx == diffy) or (a==c or b==d):
    print("ok")
else:
    print("no")

