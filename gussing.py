#NUMBER GUESSING GAME 
import random
num=random.randrange(1,250)
x=int(input("Enter the number: "))
print(num)
if(x>num):
    print('number is greater')
elif(x<num):
    print('number is lowest')
else:
    print('number is equal')  