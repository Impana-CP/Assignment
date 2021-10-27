no1=input("Enter the first num")
no2=input("Enter the second num")
no3=input("Enter the third num")

if(no1>no2) and (no1>no3):
    biggest=no1
elif(no2>no1) and (no2>no3):
    biggest=no2
else:
    biggest=no3

print("the biggest number is",biggest)