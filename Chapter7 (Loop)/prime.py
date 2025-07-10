n=int(input("enter a no :"))
for i in range (2,n):
    if n%i==0:
        print("the no. is not prime")
        break
    else:
        print("the no. is prime")
        break