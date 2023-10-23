from math import modf
m=374.3453
a,b=modf(m)
print(a,int(b)) #a will contain decimal value

print(round(m,2)) #for rounding off decimal upto 2 decimal place