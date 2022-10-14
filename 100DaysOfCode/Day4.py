import random 


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

x = random.randint(0,1)

if x == 0:
    y = "Tails"
elif x == 1:
    y = "Heads"
else:
    pass

print(x)
print(y)