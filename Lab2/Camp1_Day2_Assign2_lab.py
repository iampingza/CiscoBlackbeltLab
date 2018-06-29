from random import randint

RandInteger = randint(1, 10)

if __name__ == '__main__':
    while True:
        ##print("GBInteger = "+str(GBInteger))
        InputNumber = input("Guess the number: ")
        if(int(InputNumber) == int(RandInteger)):
            print("Correct! ")
            break
        else:
            print("Wrong, try again! ")