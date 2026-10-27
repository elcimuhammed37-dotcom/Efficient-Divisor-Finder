# def find_divisor(number):
#     divisor=[]
#     for item in range(1,number+1):
#         if  number % item==0:
#             divisor.append(item)
#     return divisor


# def find_divisor(number):
#     divisor=[ item for item in range(1,number+1) if number%item==0]
#     return divisor

import math
def find_divisor_mod(number):
    waste=0
    divisor= set(())
    for item in range(1,int(math.sqrt(number)+1)):
        if number%item==0:
            waste=number//item
            divisor.add(item)
            divisor.add(waste)
    
    itdivisor = sorted(divisor)
    return divisor

number=int(input("enter a possitive number : " ))
if number<=0:
    print("enter a possitive number : ")
else:
    result=find_divisor_mod(number)
    print(f" the divisor of {number} are: {result}")

