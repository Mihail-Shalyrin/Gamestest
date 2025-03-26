import random as r


print("Welcome to Brain Games!")
s = input("May i have your name? ")
print("Hello " + s + "!")

while True:

    a1 =(r.randint(1,100),r.randint(1,100),r.randint(1,100))
    print("Question",a1[0],a1[1],a1[2],sep=' ')
    max1 = max(a1)

    while True:
        if (max1 % a1[0]  == 0 and max1 % a1[1] % max1 == 0 and max1 %  a1[2] % max1 ==0 ):
            break

        max1+=1
    s1 = int(input("Your answer: "))
    if s1==max1:
        print(f"Correct! \nCongratulations, {s}!")
    else:
        print(f"\'{s1}\' is wrong answer ;(, Correct answer was \'{max1}\' \nLet's try again, {s}!")


