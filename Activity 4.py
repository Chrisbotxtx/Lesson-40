n=int(input("Enter a number"))
flag=False
for i in range(2,n):
    if n%i==0:
        flag=True
        break
    
if flag:
        print(n,"isn't prime")
else:
        print(n,"it's prime")