import random
fivethings = [1,2,3,4,5]
print(fivethings)
del fivethings[2]
print(fivethings)
num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
num4 = random.randint(0,9)
num5 = random.randint(0,9)
num6 = random.randint(0,9)
randnums=[num1,num2,num3,num4,num5,num6,]
if num1%2==0:
    print("EVEN")
elif num1%2!=0:
    print("ODD")
if num2%2==0:
    print("EVEN")
elif num2%2!=0:
    print("ODD")
if num3%2==0:
    print("EVEN")
elif num3%2!=0:
    print("ODD")
if num4%2==0:
    print("EVEN")
elif num4%2!=0:
    print("ODD")
if num5%2==0:
    print("EVEN")
elif num5%2!=0:
    print("ODD")
if num6%2==0:
    print("EVEN")
elif num6%2!=0:
    print("ODD")
x = input("What word would you like? ")
for y in range(len(x)):
    print(x[y])
backwards = input("what word would you like to be backwards? ")
f = len(backwards)
for f in range(len(backwards)-1, 0, -1):
    print(backwards[f], end="")
print("")
sentence = "you're a wizard harry."

for t in range(len(sentence)):
    if sentence[t-1]=="e":
        sentence[t-1]="3"
    elif sentence[t-1]=="o":
        sentence[t-1]="0"
    if sentence[t-1]=="h":
        sentence[t-1]="4"
