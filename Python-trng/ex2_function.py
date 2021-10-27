def big(no1,no2,no3):
    if(no1>no2) and (no1>no3):
        biggest=no1
    elif(no2>no1) and (no2>no3):
        biggest=no2
    else:
        biggest=no3
    return(biggest)

print(big(10,5,11))
print(big(12,20,18))
print(big(30,5,11))


