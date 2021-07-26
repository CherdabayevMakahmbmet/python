
a=int(input("kon`1:  "))
b=int(input("kon`2:  "))
c=int(input("figura1:  "))
d=int(input("figura2:  "))
x=a - c
y= b-d

if x<0:
    x = -x
if y<0:
    y = -y

if (x == 1 and y ==2) or (x==2 and y ==1) :
    print("ok")
else:
    print("no")

