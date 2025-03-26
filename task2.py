import random as r


print("Welcome to Brain Games!")
s = input("May i have your name? ")
print("Hello ",s,"!",'\nWhat number is missing in the progression?',sep='')

while True:
    a=[]
    a.append(r.randint(1,5))
    g = r.randint(2,9)
    len1 = r.randint(5, 10)
    for i in range (1,len1):
       a.append(a[i-1]*g)
    index = r.randint(3,len1-1)
    print("Question ",end='')
    for i in range(0,len(a)):
        if i == index:
            print(".. ",sep=' ',end='')
            i+=1
        else:

            print(str(a[i]) + " ",sep=' ',end='')
    else:
        print()
    s1 = int(input("Your answer: "))
    if s1==a[index]:
        print(f"Correct! \nCongratulations, {s}!")
    else:
        print(f"\'{s1}\' is wrong answer ;(, Correct answer was \'{a[index]}\' \nLet's try again, {s}!")

