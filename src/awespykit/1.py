import random
x = 40
for i in range(1,7200):
    j = random.randint(0,332)
    if j == 50:
        x += 1
x = str(x)      
print("出现次数："+x)
#88,91,114
#84,91,