import random

num = "1234567890"
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


mini = int(input("min: "))
maxi = int(input("max: "))

    
def passgen():
    for i in range(mini, maxi):
        print (num + lowercase + uppercase)

passgen()