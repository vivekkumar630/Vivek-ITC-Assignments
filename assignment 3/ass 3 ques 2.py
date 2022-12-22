print("Enter date in following order")

d=int(input("enter date "))

m=int(input("enter month "))

y=int(input("enter year "))


mo=[1,3,5,7,8,10,12]
if m in mo:
        mod=31 
         
if m==2 and y%4!=0:
        mod=28
        print(d<28)
if m not in mo:
        mod=30
        print(d<30)
if m==2 and y%4== 0:
        mod=29
        print(d<29)
    

if d> 31 or d<1:
    print("invalid date")
elif m> 12 or m<1:
    print("invalid month")
elif y> 2025 or y<1880:
    print("year not available")
if d==31 and m==12:
    print("1 1 ",y+1)   
else:
    v=(d+1)%mod 
    w=(((d+1)//mod)+m)%12
    x=(v//12)+y
    print(v,w,x)
